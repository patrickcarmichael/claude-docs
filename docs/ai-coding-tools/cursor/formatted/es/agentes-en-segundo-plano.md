---
title: "Agentes en segundo plano"
source: "https://docs.cursor.com/es/background-agent"
language: "es"
language_name: "Spanish"
---

# Agentes en segundo plano
Source: https://docs.cursor.com/es/background-agent

Agentes remotos asíncronos en Cursor

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

Con los agentes en segundo plano, podés lanzar agentes asíncronos que editen y ejecuten código en un entorno remoto. Mirá su estado, mandá seguimientos o tomá el control en cualquier momento.

<div id="how-to-use">
  ## Cómo usar
</div>

Podés acceder a los agentes en segundo plano de dos maneras:

1. **Barra lateral de agentes en segundo plano**: Usá la pestaña de agentes en segundo plano en la barra lateral nativa de Cursor para ver todos los agentes en segundo plano asociados con tu cuenta, buscar agentes existentes y arrancar nuevos.
2. **Modo de agente en segundo plano**: Presioná <Kbd tooltip="Trigger background agent mode">Cmd E</Kbd> para activar el modo de agente en segundo plano en la UI.

Después de enviar un prompt, seleccioná tu agente de la lista para ver el estado y entrar a la máquina.

<Note>
  <p className="!mb-0">
    Los agentes en segundo plano requieren retener datos por unos pocos días.
  </p>
</Note>

<div id="setup">
  ## Configuración
</div>

Por defecto, los agentes en segundo plano se ejecutan en una máquina aislada basada en Ubuntu. Tienen acceso a Internet y pueden instalar paquetes.

<div id="github-connection">
  #### Conexión con GitHub
</div>

Los agentes en segundo plano clonan tu repositorio desde GitHub y trabajan en una rama aparte, haciendo push a tu repositorio para facilitar la entrega.

Concede permisos de lectura y escritura a tu repositorio (y a cualquier repositorio dependiente o submódulo). En el futuro, admitiremos otros proveedores (GitLab, Bitbucket, etc.).

<div id="ip-allow-list-configuration">
  ##### Configuración de la lista de IP permitidas
</div>

Si tu organización usa la función de lista de IP permitidas de GitHub, vas a tener que configurar el acceso para los agentes en segundo plano. Consulta la [documentación de la integración con GitHub](/es/integrations/github#ip-allow-list-configuration) para ver las instrucciones completas de configuración, incluida la información de contacto y las direcciones IP.

<div id="base-environment-setup">
  #### Configuración base del entorno
</div>

Para casos avanzados, configura el entorno por tu cuenta. Consigue una instancia del IDE conectada a la máquina remota. Prepara tu máquina, instala herramientas y paquetes, y luego toma un snapshot. Configura los ajustes de runtime:

* El comando de instalación se ejecuta antes de que arranque un agente e instala las dependencias de runtime. Esto puede implicar ejecutar `npm install` o `bazel build`.
* Los terminales ejecutan procesos en segundo plano mientras el agente trabaja, como iniciar un servidor web o compilar archivos protobuf.

Para los casos más avanzados, usa un Dockerfile para configurar la máquina. El Dockerfile te permite configurar dependencias a nivel del sistema: instalar versiones específicas de compiladores, depuradores o cambiar la imagen base del SO. No hagas `COPY` de todo el proyecto: nosotros gestionamos el workspace y hacemos checkout del commit correcto. Aun así, gestiona la instalación de dependencias en el script de instalación.

Ingresa cualquier secreto requerido para tu entorno de desarrollo: se almacenan cifrados en reposo (usando KMS) en nuestra base de datos y se proporcionan en el entorno del agente en segundo plano.

La configuración de la máquina vive en `.cursor/environment.json`, que puedes commitear en tu repo (recomendado) o almacenar de forma privada. El flujo de configuración te guía para crear `environment.json`.

<div id="maintenance-commands">
  #### Comandos de mantenimiento
</div>

Al configurar una máquina nueva, empezamos desde el entorno base y luego ejecutamos el comando `install` de tu `environment.json`. Este comando es el que ejecutaría un desarrollador al cambiar de rama: instalar cualquier dependencia nueva.

Para la mayoría, el comando `install` es `npm install` o `bazel build`.

Para asegurar un arranque rápido de la máquina, almacenamos en caché el estado del disco después de que se ejecute el comando `install`. Diseñalo para que pueda ejecutarse varias veces. Solo persiste el estado del disco desde el comando `install`: los procesos iniciados aquí no seguirán en ejecución cuando el agente arranque.

<div id="startup-commands">
  #### Comandos de inicio
</div>

Después de ejecutar `install`, la máquina arranca y ejecutamos el comando `start`, seguido de iniciar cualquier `terminals`. Esto levanta procesos que deberían estar en ejecución cuando se ejecute el agente.

El comando `start` a menudo se puede omitir. Úsalo si tu entorno de dev depende de Docker: pon `sudo service docker start` en el comando `start`.

Los `terminals` son para código de la app. Estos terminales se ejecutan en una sesión de `tmux` disponible para ti y para el agente. Por ejemplo, muchos repos de sitios web ponen `npm run watch` como un terminal.

<div id="the-environmentjson-spec">
  #### La especificación de `environment.json`
</div>

El archivo `environment.json` puede tener este aspecto:

```json  theme={null}
{
  "snapshot": "POPULATED_FROM_SETTINGS",
  "install": "npm install",
  "terminals": [
    {
      "name": "Iniciar Next.js",
      "command": "npm run dev"
    }
  ]
}
```

Formalmente, la especificación se [define aquí](https://www.cursor.com/schemas/environment.schema.json).

<div id="models">
  ## Modelos
</div>

Solo los modelos compatibles con [Max Mode](/es/context/max-mode) están disponibles para los agentes en segundo plano.

<div id="pricing">
  ## Precios
</div>

Conocé más sobre los [precios de Background Agent](/es/account/pricing#background-agent).

<div id="security">
  ## Seguridad
</div>

Los Background Agents están disponibles en Privacy Mode. Nunca entrenamos con tu código y solo lo conservamos para ejecutar el agente. [Más información sobre Privacy Mode](https://www.cursor.com/privacy-overview).

Lo que deberías saber:

1. Concede privilegios de lectura y escritura a nuestra app de GitHub en los repos que quieras editar. Usamos esto para clonar el repo y hacer cambios.
2. Tu código se ejecuta dentro de nuestra infraestructura en AWS, en VMs aisladas, y se almacena en discos de VM mientras el agente está activo.
3. El agente tiene acceso a Internet.
4. El agente ejecuta automáticamente todos los comandos de terminal, lo que le permite iterar en las pruebas. Esto difiere del foreground agent, que requiere tu aprobación para cada comando. La ejecución automática introduce riesgo de exfiltración de datos: atacantes podrían lanzar ataques de prompt injection, engañando al agente para que suba código a sitios web maliciosos. Consulta la [explicación de OpenAI sobre los riesgos de prompt injection para background agents](https://platform.openai.com/docs/codex/agent-network#risks-of-agent-internet-access).
5. Si Privacy Mode está deshabilitado, recopilamos prompts y entornos de desarrollo para mejorar el producto.
6. Si deshabilitas Privacy Mode al iniciar un background agent y luego lo habilitas durante la ejecución, el agente sigue con Privacy Mode deshabilitado hasta que termine.

<div id="dashboard-settings">
  ## Configuración del dashboard
</div>

Los admins del workspace pueden configurar opciones adicionales desde la pestaña Background Agents en el dashboard.

<div id="defaults-settings">
  ### Configuración predeterminada
</div>

* **Modelo predeterminado** – el modelo que se usa cuando una ejecución no especifica ninguno. Elige cualquier modelo compatible con Max Mode.
* **Repositorio predeterminado** – si está vacío, los agentes te piden que elijas un repo. Indicar un repo aquí te permite saltarte ese paso.
* **Rama base** – la rama desde la que los agentes crean un fork al abrir pull requests. Déjala en blanco para usar la rama predeterminada del repositorio.

<div id="security-settings">
  ### Configuración de seguridad
</div>

Todas las opciones de seguridad requieren privilegios de admin.

* **Restricciones de usuario** – elige *Ninguna* (todos los miembros pueden iniciar agentes en segundo plano) o *Lista de permitidos*. Cuando está en *Lista de permitidos*, especificas exactamente qué compas de equipo pueden crear agentes.
* **Seguimientos del equipo** – cuando está activado, cualquiera en el espacio de trabajo puede añadir mensajes de seguimiento a un agente que inició otra persona. Apágalo para restringir los seguimientos al propietario del agente y a los admins.
* **Mostrar resumen del agente** – controla si Cursor muestra las imágenes de diferencias de archivos del agente y los fragmentos de código. Desactívalo si prefieres no exponer rutas de archivo o código en la barra lateral.
* **Mostrar resumen del agente en canales externos** – extiende la opción anterior a Slack o cualquier canal externo que tengas conectado.

Los cambios se guardan al instante y se aplican de inmediato a los nuevos agentes.

---

← Previous: [Herramientas](./herramientas.md) | [Index](./index.md) | Next: [Agregar seguimiento](./agregar-seguimiento.md) →