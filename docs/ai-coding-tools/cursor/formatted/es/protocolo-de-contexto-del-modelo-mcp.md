---
title: "Protocolo de Contexto del Modelo (MCP)"
source: "https://docs.cursor.com/es/context/mcp"
language: "es"
language_name: "Spanish"
---

# Protocolo de Contexto del Modelo (MCP)
Source: https://docs.cursor.com/es/context/mcp

Conecta herramientas externas y fuentes de datos a Cursor con MCP

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

<div id="what-is-mcp">
  ## ¿Qué es MCP?
</div>

[Model Context Protocol (MCP)](https://modelcontextprotocol.io/introduction) permite que Cursor se conecte con herramientas externas y fuentes de datos.

<Frame>
  <video src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/mcp/simple-mcp-call.mp4?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=08c642babc501c939ecbec9ef5124ce7" autoPlay loop muted playsInline controls data-path="images/context/mcp/simple-mcp-call.mp4" />
</Frame>

<div id="why-use-mcp">
  ### ¿Por qué usar MCP?
</div>

MCP conecta Cursor con sistemas y datos externos. En lugar de explicar la estructura de tu proyecto una y otra vez, intégrate directamente con tus herramientas.

Escribe servidores MCP en cualquier lenguaje que pueda imprimir en `stdout` o exponer un endpoint HTTP: Python, JavaScript, Go, etc.

<div id="how-it-works">
  ### Cómo funciona
</div>

Los servidores MCP exponen capacidades a través del protocolo, conectando Cursor con herramientas externas y fuentes de datos.

Cursor admite tres métodos de transporte:

<div className="full-width-table">
  | Transporte                                                       | Entorno de ejecución | Implementación            | Usuarios        | Entrada                | Autenticación |
  | :--------------------------------------------------------------- | :------------------- | :------------------------ | :-------------- | :--------------------- | :------------ |
  | **<span className="whitespace-nowrap">`stdio`</span>**           | Local                | Gestionado por Cursor     | Un solo usuario | Comando de shell       | Manual        |
  | **<span className="whitespace-nowrap">`SSE`</span>**             | Local/Remoto         | Implementar como servidor | Varios usuarios | URL a un endpoint SSE  | OAuth         |
  | **<span className="whitespace-nowrap">`Streamable HTTP`</span>** | Local/Remoto         | Implementar como servidor | Varios usuarios | URL a un endpoint HTTP | OAuth         |
</div>

<div id="protocol-support">
  ### Compatibilidad con el protocolo
</div>

Cursor admite estas capacidades del protocolo MCP:

<div className="full-width-table">
  | Función         | Compatibilidad | Descripción                                                                                              |
  | :-------------- | :------------- | :------------------------------------------------------------------------------------------------------- |
  | **Tools**       | Compatible     | Funciones que el modelo de IA puede ejecutar                                                             |
  | **Prompts**     | Compatible     | Mensajes y flujos de trabajo con plantillas para usuaries                                                |
  | **Resources**   | Compatible     | Fuentes de datos estructuradas que se pueden leer y consultar                                            |
  | **Roots**       | Compatible     | Consultas iniciadas por el servidor sobre los límites de URI o del sistema de archivos en los que operar |
  | **Elicitation** | Compatible     | Solicitudes iniciadas por el servidor para obtener información adicional de les usuaries                 |
</div>

<div id="installing-mcp-servers">
  ## Instalación de servidores MCP
</div>

<div id="one-click-installation">
  ### Instalación con un clic
</div>

Instala servidores MCP de nuestra colección y autentícate con OAuth.

<Columns cols={2}>
  <Card title="Browse MCP Tools" icon="table" horizontal href="/es/tools">
    Explora los servidores MCP disponibles
  </Card>

  <Card title="Add to Cursor Button" icon="plus" horizontal href="/es/deeplinks">
    Crea un botón “Add to Cursor”
  </Card>
</Columns>

<div id="using-mcpjson">
  ### Uso de `mcp.json`
</div>

Configura servidores MCP personalizados con un archivo JSON:

<CodeGroup>
  ```json CLI Server - Node.js theme={null}
  {
    "mcpServers": {
      "server-name": {
        "command": "npx",
        "args": ["-y", "mcp-server"],
        "env": {
          "API_KEY": "value"
        }
      }
    }
  }
  ```

  ```json CLI Server - Python theme={null}
  {
    "mcpServers": {
      "server-name": {
        "command": "python",
        "args": ["mcp-server.py"],
        "env": {
          "API_KEY": "value"
        }
      }
    }
  }
  ```

  ```json Remote Server theme={null}
  // Servidor MCP vía HTTP o SSE: se ejecuta de forma remota
  {
    "mcpServers": {
      "server-name": {
        "url": "http://localhost:3000/mcp",
        "headers": {
          "API_KEY": "value"
        }
      }
    }
  }
  ```
</CodeGroup>

<div id="stdio-server-configuration">
  ### Configuración del servidor STDIO
</div>

Para servidores STDIO (servidores locales de línea de comandos), configura estos campos en tu `mcp.json`:

<div className="full-width-table">
  | Campo       | Requerido | Descripción                                                                                                                          | Ejemplos                                  |
  | :---------- | :-------- | :----------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------- |
  | **type**    | Sí        | Tipo de conexión del servidor                                                                                                        | `"stdio"`                                 |
  | **command** | Sí        | Comando para iniciar el ejecutable del servidor. Debe estar disponible en la variable PATH de tu sistema o incluir su ruta completa. | `"npx"`, `"node"`, `"python"`, `"docker"` |
  | **args**    | No        | Lista de argumentos pasados al comando                                                                                               | `["server.py", "--port", "3000"]`         |
  | **env**     | No        | Variables de entorno para el servidor                                                                                                | `{"API_KEY": "${input:api-key}"}`         |
  | **envFile** | No        | Ruta a un archivo de entorno para cargar más variables                                                                               | `".env"`, `"${workspaceFolder}/.env"`     |
</div>

<div id="using-the-extension-api">
  ### Uso de la API de extensión
</div>

Para registrar servidores MCP de forma programática, Cursor ofrece una API de extensión que permite una configuración dinámica sin modificar archivos `mcp.json`. Esto es especialmente útil en entornos empresariales y en flujos de configuración automatizados.

<Card title="Referencia de la API de extensión de MCP" icon="code" href="/es/context/mcp-extension-api">
  Aprende a registrar servidores MCP de forma programática usando `vscode.cursor.mcp.registerServer()`
</Card>

<div id="configuration-locations">
  ### Ubicaciones de configuración
</div>

<CardGroup cols={2}>
  <Card title="Configuración del proyecto" icon="folder-tree">
    Crea `.cursor/mcp.json` en tu proyecto para herramientas específicas del proyecto.
  </Card>

  <Card title="Configuración global" icon="globe">
    Crea `~/.cursor/mcp.json` en tu directorio personal para tener las herramientas disponibles en cualquier lugar.
  </Card>
</CardGroup>

<div id="config-interpolation">
  ### Interpolación de configuración
</div>

Usa variables en los valores de `mcp.json`. Cursor resuelve variables en estos campos: `command`, `args`, `env`, `url` y `headers`.

Sintaxis admitida:

* `${env:NAME}` variables de entorno
* `${userHome}` ruta a tu carpeta personal
* `${workspaceFolder}` raíz del proyecto (la carpeta que contiene `.cursor/mcp.json`)
* `${workspaceFolderBasename}` nombre de la carpeta raíz del proyecto
* `${pathSeparator}` y `${/}` separador de rutas del sistema operativo

Ejemplos

```json  theme={null}
{
  "mcpServers": {
    "local-server": {
      "command": "python",
      "args": ["${workspaceFolder}/tools/mcp_server.py"],
      "env": {
        "API_KEY": "${env:API_KEY}"
      }
    }
  }
}
```

```json  theme={null}
{
  "mcpServers": {
    "remote-server": {
      "url": "https://api.example.com/mcp",
      "headers": {
        "Authorization": "Bearer ${env:MY_SERVICE_TOKEN}"
      }
    }
  }
}
```

<div id="authentication">
  ### Autenticación
</div>

Los servidores MCP usan variables de entorno para la autenticación. Pasa las claves de API y los tokens a través de la configuración.

Cursor admite OAuth para los servidores que lo requieran.

<div id="using-mcp-in-chat">
  ## Usar MCP en el chat
</div>

El Composer Agent utiliza automáticamente las herramientas MCP que aparecen en `Available Tools` cuando corresponde. Pide una herramienta específica por su nombre o describe lo que necesitas. Activa o desactiva herramientas desde Settings.

<div id="toggling-tools">
  ### Activar o desactivar herramientas
</div>

Activa o desactiva herramientas MCP directamente desde la interfaz del chat. Haz clic en el nombre de una herramienta en la lista para activarla o desactivarla. Las herramientas desactivadas no se cargarán en el contexto ni estarán disponibles para Agent.

<Frame>
  <video src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/mcp/tool-toggle.mp4?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=0fa3060f593cae3e5fb7c7d2f041a715" autoPlay loop muted playsInline controls data-path="images/context/mcp/tool-toggle.mp4" />
</Frame>

<div id="tool-approval">
  ### Aprobación de herramientas
</div>

De forma predeterminada, el agente solicita aprobación antes de usar herramientas MCP. Haz clic en la flecha junto al nombre de la herramienta para ver los argumentos.

<Frame><img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/mcp/tool-confirm.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=bf9b19d5f23abc65914f712185b3ec72" alt="" data-og-width="1212" width="1212" data-og-height="902" height="902" data-path="images/context/mcp/tool-confirm.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/mcp/tool-confirm.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=e3f900fad0b8f2a469460c70fa1dd1dc 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/mcp/tool-confirm.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=de2f90138de39d75d70c5800f13be93a 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/mcp/tool-confirm.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=b9c616ce7a4080ea4088a0fdd0050c7c 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/mcp/tool-confirm.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=3f783e62a7a31957b8988edb97c139f9 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/mcp/tool-confirm.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=10bf2c1dbfd5c2a03aa95334f53cd571 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/mcp/tool-confirm.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=231c0e3cd60df5ad12455d5e8ef308d2 2500w" /></Frame>

<div id="auto-run">
  #### Auto-run
</div>

Activa Auto-run para que Agent use las herramientas MCP sin pedir confirmación. Funciona como comandos de terminal. Lee más sobre la configuración de Auto-run [aquí](/es/agent/tools#auto-run).

<div id="tool-response">
  ### Respuesta de la herramienta
</div>

Cursor muestra la respuesta en el chat con vistas desplegables de los argumentos y las respuestas:

<Frame><img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/mcp/tool-call.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=30af3f35869e9a78781f455bdbc0e3b5" alt="" data-og-width="1212" width="1212" data-og-height="952" height="952" data-path="images/context/mcp/tool-call.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/mcp/tool-call.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=8821ac7bad00ad54a18abc614c2e3d5c 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/mcp/tool-call.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=d9d55f089ad53a89da99b8ddd524f6de 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/mcp/tool-call.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=a107d68a1fb05ed43851548b34fb4496 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/mcp/tool-call.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=b409b4941c2fd783043770fad0bd6390 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/mcp/tool-call.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=2a331b5e2bb9be0b9659393157454c2e 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/mcp/tool-call.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=585b769dfa2a5114b111eb901a969845 2500w" /></Frame>

<div id="images-as-context">
  ### Imágenes como contexto
</div>

Los servidores MCP pueden devolver imágenes —capturas de pantalla, diagramas, etc.—. Devuélvelas como cadenas codificadas en base64:

```js  theme={null}
const RED_CIRCLE_BASE64 = "/9j/4AAQSkZJRgABAgEASABIAAD/2w...";
// ^ base64 completo omitido para mejorar la legibilidad

server.tool("generate_image", async (params) => {
  return {
    content: [
      {
        type: "image",
        data: RED_CIRCLE_BASE64,
        mimeType: "image/jpeg",
      },
    ],
  };
});
```

Consulta este [servidor de ejemplo](https://github.com/msfeldstein/mcp-test-servers/blob/main/src/image-server.js) para ver los detalles de implementación. Cursor adjunta las imágenes devueltas al chat. Si el modelo admite imágenes, las analiza.

<div id="security-considerations">
  ## Consideraciones de seguridad
</div>

Al instalar servidores MCP, ten en cuenta estas prácticas de seguridad:

* **Verifica el origen**: Instala servidores MCP solo de desarrolladores y repositorios de confianza
* **Revisa los permisos**: Comprueba a qué datos y APIs tendrá acceso el servidor
* **Limita las claves de API**: Usa claves de API restringidas con los permisos mínimos necesarios
* **Audita el código**: Para integraciones críticas, revisa el código fuente del servidor

Recuerda que los servidores MCP pueden acceder a servicios externos y ejecutar código en tu nombre. Asegúrate de entender qué hace un servidor antes de instalarlo.

<div id="real-world-examples">
  ## Ejemplos del mundo real
</div>

Para ver ejemplos prácticos de MCP en acción, consulta nuestra [guía de desarrollo web](/es/guides/tutorials/web-development), donde mostramos cómo integrar Linear, Figma y herramientas del navegador en tu flujo de trabajo de desarrollo.

<div id="faq">
  ## Preguntas frecuentes
</div>

<AccordionGroup>
  <Accordion title="¿Para qué sirven los servidores MCP?">
    Los servidores MCP conectan Cursor con herramientas externas como Google Drive, Notion y
    otros servicios para incorporar documentos y requisitos a tu flujo de trabajo de código.
  </Accordion>

  {" "}

  <Accordion title="¿Cómo depuro problemas con servidores MCP?">
    Revisa los logs de MCP así: 1. Abre el panel Output en Cursor (<Kbd>Cmd+Shift+U</Kbd>) 2. Selecciona "MCP Logs" en el menú desplegable 3. Busca errores de conexión, problemas de autenticación o caídas del servidor. Los logs muestran la inicialización del servidor, llamadas a herramientas y mensajes de error.
  </Accordion>

  {" "}

  <Accordion title="¿Puedo desactivar temporalmente un servidor MCP?">
    ¡Sí! Activa o desactiva servidores sin quitarlos: 1. Abre Settings (<Kbd>Cmd+Shift+J</Kbd>) 2. Ve a Features → Model Context Protocol 3. Haz clic en el interruptor junto a cualquier servidor para habilitar o deshabilitar. Los servidores deshabilitados no se cargan ni aparecen en el chat. Esto es útil para depurar o reducir el ruido de herramientas.
  </Accordion>

  {" "}

  <Accordion title="¿Qué pasa si un servidor MCP se bloquea o supera el tiempo de espera?">
    Si un servidor MCP falla: - Cursor muestra un mensaje de error en el chat - La llamada a la herramienta se marca como fallida - Puedes reintentar la operación o revisar los logs para ver detalles - Otros servidores MCP siguen funcionando con normalidad. Cursor aísla las fallas de servidores para evitar que uno afecte a los demás.
  </Accordion>

  {" "}

  <Accordion title="¿Cómo actualizo un servidor MCP?">
    Para servidores basados en npm: 1. Quita el servidor desde Settings 2. Limpia la caché de npm: `npm cache clean --force` 3. Vuelve a agregar el servidor para obtener la versión más reciente. Para servidores personalizados, actualiza tus archivos locales y reinicia Cursor.
  </Accordion>

  <Accordion title="¿Puedo usar servidores MCP con datos sensibles?">
    Sí, pero sigue las mejores prácticas de seguridad: - Usa variables de entorno para secretos; nunca los hardcodees - Ejecuta servidores sensibles localmente con transporte `stdio` - Limita los permisos de las API keys al mínimo necesario - Revisa el código del servidor antes de conectarlo a sistemas sensibles - Considera ejecutar los servidores en entornos aislados
  </Accordion>
</AccordionGroup>

---

← Previous: [Ignorar archivos](./ignorar-archivos.md) | [Index](./index.md) | Next: [Memories](./memories.md) →