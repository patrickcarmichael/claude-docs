---
title: "Problemas comunes"
source: "https://docs.cursor.com/es/troubleshooting/common-issues"
language: "es"
language_name: "Spanish"
---

# Problemas comunes
Source: https://docs.cursor.com/es/troubleshooting/common-issues

Soluciones para problemas habituales y preguntas frecuentes

A continuación encontrarás problemas comunes y sus soluciones.

<div id="networking-issues">
  ### Problemas de red
</div>

Primero, verifica tu conectividad de red. Ve a `Cursor Settings` > `Network` y haz clic en `Run Diagnostics`. Esto probará tu conexión con los servidores de Cursor y ayudará a identificar cualquier problema de red que pueda estar afectando las funciones de IA, las actualizaciones u otras funcionalidades en línea.

Cursor depende de HTTP/2 para las funciones de IA porque maneja las respuestas en streaming de forma eficiente. Si tu red no admite HTTP/2, podrías experimentar fallos de indexación y problemas con las funciones de IA.

Esto puede ocurrir en redes corporativas, VPN o al usar proxies como Zscaler.

Para solucionarlo, habilita la conmutación a HTTP/1.1 en la configuración de la app (no en la configuración de Cursor): presiona `CMD/CTRL + ,`, busca `HTTP/2` y activa `Disable HTTP/2`. Esto fuerza el uso de HTTP/1.1 y resuelve el problema.

Planeamos añadir detección y conmutación automáticas.

<div id="resource-issues-cpu-ram-etc">
  ### Problemas de recursos (CPU, RAM, etc.)
</div>

Un uso elevado de CPU o RAM puede ralentizar tu equipo o activar advertencias de recursos.

Aunque los repos grandes requieren más recursos, el consumo alto normalmente se debe a extensiones o a problemas de configuración.

<Note>
  Si ves una advertencia de poca RAM en **macOS**, ten en cuenta que hay un bug para algunos usuarios que puede mostrar valores totalmente incorrectos. Si te pasa, abre Activity Monitor y mira la pestaña "Memory" para ver el uso correcto de memoria.
</Note>

Si estás experimentando un uso alto de CPU o RAM, prueba estos pasos:

<AccordionGroup>
  <Accordion title="Check Your Extensions">
    Las extensiones pueden afectar el rendimiento.

    El Extension Monitor muestra el consumo de recursos de todas tus extensiones instaladas y las integradas.

    Activa el monitor de extensiones desde `Settings` > `Application` > `Experimental` y habilita `Extension Monitor: Enabled`. Se te pedirá reiniciar Cursor.

    Ábrelo: `Cmd/Ctrl + Shift + P` → `Developer: Open Extension Monitor`.

    Cursor ejecuta tus extensiones en uno o más **extension hosts**. Por lo general, la mayoría de tus extensiones se ejecutan en el mismo extension host, lo que significa que una extensión que consuma mucho tiempo de CPU puede asfixiar a sus extensiones vecinas.

    El Extension Monitor muestra:

    * Cada proceso de larga duración lanzado por una extensión (solo macOS y Linux).
    * **% Ext Host**: El porcentaje del tiempo total del extension host consumido por esa extensión. Ayuda a identificar qué extensiones usan más tiempo en relación con las demás.
    * **Max Blocking**: El bloqueo continuo más largo de ejecución de una extensión, por intervalo de monitoreo.
    * **% CPU**:
      * Para extensiones: El porcentaje del uso total de CPU atribuido al código de la extensión.
      * Para procesos: El porcentaje del uso total de CPU atribuido al proceso lanzado (solo macOS y Linux).
    * **Memory**:
      * Para extensiones: La cantidad de memoria de heap de JS utilizada por el código de la extensión (no incluye asignaciones externas).
      * Para procesos: La cantidad de memoria del sistema utilizada por el proceso lanzado (solo macOS y Linux).

    También puedes probar ejecutando `cursor --disable-extensions` desde la línea de comandos. Si el rendimiento mejora, vuelve a habilitar las extensiones una por una para identificar las problemáticas.

    Prueba Extension Bisect para identificar extensiones problemáticas. Lee más [aquí](https://code.visualstudio.com/blogs/2021/02/16/extension-bisect#_welcome-extension-bisect). Nota: esto funciona mejor para problemas inmediatos, no para degradación gradual del rendimiento.
  </Accordion>

  <Accordion title="Use the Process Explorer">
    El Process Explorer muestra qué procesos consumen recursos.

    Ábrelo: Command Palette (`Cmd/Ctrl + Shift + P`) → `Developer: Open Process Explorer`.

    Revisa los procesos:

    * **`extensionHost`**: Problemas relacionados con extensiones
    * **`ptyHost`**: Consumo de recursos del terminal

    El Process Explorer muestra cada terminal y sus comandos en ejecución para diagnóstico.

    Para otros procesos con alto uso, repórtalo en el [foro](https://forum.cursor.com/).
  </Accordion>

  <Accordion title="Monitor System Resources">
    Usa las herramientas de monitoreo de tu sistema operativo para determinar si el problema es específico de Cursor o de todo el sistema.
  </Accordion>

  <Accordion title="Testing a Minimal Installation">
    Si los problemas persisten, prueba una instalación mínima de Cursor.
  </Accordion>
</AccordionGroup>

<div id="general-faqs">
  ## Preguntas frecuentes generales
</div>

<AccordionGroup>
  <Accordion title="Veo una actualización en el changelog pero Cursor no se actualiza">
    Las actualizaciones se lanzan de forma escalonada: a algunos usuarios aleatorios les llegan primero. Deberías recibirla en unos días.
  </Accordion>

  <Accordion title="Tengo problemas con mi inicio de sesión de GitHub en Cursor / ¿Cómo cierro sesión de GitHub en Cursor?">
    Usa `Sign Out of GitHub` desde la paleta de comandos `Ctrl/⌘ + Shift + P`.
  </Accordion>

  <Accordion title="No puedo usar GitHub Codespaces">
    GitHub Codespaces todavía no es compatible.
  </Accordion>

  <Accordion title="Tengo errores al conectarme a Remote SSH">
    No se admite SSH a máquinas Mac o Windows. Para otros problemas, repórtalo en el [foro](https://forum.cursor.com/) con logs.
  </Accordion>

  <Accordion title="Problemas de conexión SSH en Windows">
    Si ves "SSH is only supported in Microsoft versions of VS Code":

    1. Desinstala Remote-SSH:
       * Abre la vista de Extensiones (`Ctrl + Shift + X`)
       * Busca "Remote-SSH"
       * Haz clic en el ícono de engranaje → "Uninstall"

    2. Instala Anysphere Remote SSH:
       * Abre el marketplace de Cursor
       * Busca "SSH"
       * Instala la extensión Anysphere Remote SSH

    3. Después de la instalación:
       * Cierra todas las instancias de VS Code con conexiones SSH activas
       * Reinicia Cursor
       * Vuelve a conectarte por SSH

    Verifica que tu configuración y claves SSH estén configuradas correctamente.
  </Accordion>

  <Accordion title="Cursor Tab e Inline Edit no funcionan detrás de mi proxy corporativo">
    Cursor Tab e Inline Edit usan HTTP/2 para menor latencia y uso de recursos. Algunos proxys corporativos (p. ej., Zscaler) bloquean HTTP/2. Solución: establece `"cursor.general.disableHttp2": true` en Ajustes (`Cmd/Ctrl + ,`, busca `http2`).
  </Accordion>

  <Accordion title="Acabo de suscribirme a Pro pero aún estoy en el plan gratuito en la app">
    Cierra sesión y vuelve a iniciarla desde Cursor Settings.
  </Accordion>

  <Accordion title="¿Cuándo se restablecerá mi uso otra vez?">
    Suscriptores Pro: haz clic en `Manage Subscription` en el [Dashboard](https://cursor.com/dashboard) para ver tu fecha de renovación.

    Usuarios gratuitos: revisa la fecha de tu primer correo de Cursor. El uso se restablece mensualmente a partir de esa fecha.
  </Accordion>

  <Accordion title="Mi historial de Chat/Composer desapareció después de una actualización">
    El poco espacio en disco puede hacer que Cursor borre datos históricos durante las actualizaciones. Para evitarlo:

    1. Mantén suficiente espacio libre en disco antes de actualizar
    2. Limpia regularmente archivos del sistema que no necesites
    3. Haz una copia de seguridad de conversaciones importantes antes de actualizar
  </Accordion>

  <Accordion title="¿Cómo desinstalo Cursor?">
    Sigue [esta guía](https://code.visualstudio.com/docs/setup/uninstall). Reemplaza "VS Code" o "Code" por "Cursor", y ".vscode" por ".cursor".
  </Accordion>

  <Accordion title="¿Cómo elimino mi cuenta?">
    Haz clic en `Delete Account` en el [Dashboard](https://cursor.com/dashboard). Esto elimina permanentemente tu cuenta y todos los datos asociados.
  </Accordion>

  <Accordion title="¿Cómo abro Cursor desde la línea de comandos?">
    Ejecuta `cursor` en tu terminal. Si falta el comando:

    1. Abre la paleta de comandos `⌘⇧P`
    2. Escribe `install command`
    3. Selecciona `Install 'cursor' command` (opcionalmente instala el comando `code` para reemplazar el de VS Code)
  </Accordion>

  <Accordion title="No puedo iniciar sesión en Cursor">
    Si al hacer clic en Sign In te redirige a cursor.com pero no inicia sesión, desactiva tu firewall o antivirus; pueden estar bloqueando el proceso de inicio de sesión.
  </Accordion>

  <Accordion title="Mensaje de actividad sospechosa">
    Debido al aumento reciente de uso indebido de nuestro sistema, es posible que tu solicitud haya sido bloqueada como medida de seguridad. Así puedes resolverlo:

    Primero, revisa tu VPN. Si estás usando una, intenta apagarla, ya que las VPN a veces activan nuestros sistemas de seguridad.

    Si eso no lo resuelve, puedes probar:

    * Crear un nuevo chat
    * Esperar un poco e intentarlo más tarde
    * Crear una cuenta nueva usando autenticación con Google o GitHub
    * Pasarte a Cursor Pro
  </Accordion>
</AccordionGroup>

---

← Previous: [Servidores MCP](./servidores-mcp.md) | [Index](./index.md) | Next: [Obtener un ID de solicitud](./obtener-un-id-de-solicitud.md) →