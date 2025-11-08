---
title: "Guía de solución de problemas"
source: "https://docs.cursor.com/es/troubleshooting/troubleshooting-guide"
language: "es"
language_name: "Spanish"
---

# Guía de solución de problemas
Source: https://docs.cursor.com/es/troubleshooting/troubleshooting-guide

Pasos para solucionar problemas y reportar errores

Los problemas de Cursor pueden deberse a extensiones, datos de la app o fallas del sistema. Prueba estos pasos de solución de problemas.

<CardGroup cols={1}>
  <Card horizontal title="Reportar un problema" icon="bug" href="#reporting-an-issue">
    Pasos para reportar un problema al equipo de Cursor
  </Card>
</CardGroup>

<div id="troubleshooting">
  ## Solución de problemas
</div>

<Steps>
  <Step title="Check network connectivity">
    Primero verifica si Cursor puede conectarse a sus servicios.

    **Ejecuta diagnósticos de red:** Ve a `Cursor Settings` > `Network` y haz clic en `Run Diagnostics`. Esto prueba tu conexión con los servidores de Cursor e identifica problemas de red que afecten las funciones de IA, las actualizaciones u otras funcionalidades en línea.

    Si los diagnósticos detectan problemas de conectividad, revisa la configuración del firewall, el proxy o las restricciones de red que puedan estar bloqueando el acceso de Cursor.
  </Step>

  <Step title="Clearing extension data">
    Para problemas con extensiones:

    **Desactiva temporalmente todas las extensiones:** Ejecuta `cursor --disable-extensions` desde la línea de comandos. Si el problema se resuelve, vuelve a habilitarlas una por una para identificar cuál causa el fallo.

    **Restablece los datos de la extensión:** Desinstala y vuelve a instalar las extensiones problemáticas para restablecer sus datos almacenados. Revisa si hay configuración de la extensión que persista tras la reinstalación.
  </Step>

  <Step title="Clearing app data">
    <Warning>
      Esto elimina tus datos de la app, incluidas extensiones, temas, snippets y datos relacionados con la instalación. Exporta tu perfil primero para conservarlos.
    </Warning>

    Cursor guarda datos de la app fuera de la aplicación para poder restaurarlos entre actualizaciones y reinstalaciones.

    Para borrar los datos de la app:

    **Windows:** Ejecuta estos comandos en el Símbolo del sistema:

    ```txt  theme={null}
    rd /s /q "%USERPROFILE%\AppData\Local\Programs\Cursor"
    rd /s /q "%USERPROFILE%\AppData\Local\Cursor"
    rd /s /q "%USERPROFILE%\AppData\Roaming\Cursor"
    del /f /q "%USERPROFILE%\.cursor*"
    rd /s /q "%USERPROFILE%\.cursor"
    ```

    **MacOS:** Ejecuta `sudo rm -rf ~/Library/Application\ Support/Cursor` y `rm -f ~/.cursor.json` en Terminal.

    **Linux:** Ejecuta `rm -rf ~/.cursor ~/.config/Cursor/` en Terminal.
  </Step>

  <Step title="Uninstalling Cursor">
    Para desinstalar Cursor:

    <CardGroup cols={1}>
      <Card horizontal title="Windows" icon="windows">
        Busca "Add or Remove Programs" en el menú Inicio, encuentra "Cursor" y haz clic en "Uninstall".
      </Card>

      <Card horizontal title="MacOS" icon="apple">
        Abre la carpeta Applications, haz clic derecho en "Cursor" y selecciona "Move to Trash".
      </Card>

      <Card horizontal title="Linux" icon="linux">
        **Para paquetes .deb:** `sudo apt remove cursor`

        **Para paquetes .rpm:** `sudo dnf remove cursor` o `sudo yum remove cursor`

        **Para AppImage:** Elimina el archivo Cursor.appimage de su ubicación.
      </Card>
    </CardGroup>
  </Step>

  <Step title="Reinstalling Cursor">
    Reinstala desde la [página de descargas](https://www.cursor.com/downloads). Si no borras los datos de la app, Cursor se restaurará a su estado anterior. De lo contrario, obtendrás una instalación limpia.
  </Step>
</Steps>

<div id="reporting-an-issue">
  ## Reportar un problema
</div>

Si estos pasos no te ayudan, repórtalo en el [foro](https://forum.cursor.com/).

<Card horizontal title="Cursor Forum" icon="message" href="https://forum.cursor.com/">
  Reporta un bug o problema en el foro de Cursor
</Card>

Para resolverlo más rápido, proporciona:

<CardGroup cols={2}>
  <Card title="Screenshot of Issue" icon="image">
    Toma una captura de pantalla y oculta la información sensible.
  </Card>

  <Card title="Steps to Reproduce" icon="list-check">
    Documenta los pasos exactos para reproducir el problema.
  </Card>

  <Card title="System Information" icon="computer">
    Obtén la información del sistema desde:

    <br />

    `Cursor` > `Help` > `About`
  </Card>

  <Card title="Request IDs" icon="shield-halved" href="/es/troubleshooting/request-reporting">
    Haz clic para ver nuestra guía sobre cómo recopilar IDs de solicitud
  </Card>

  <Card title="Console Errors" icon="bug">
    Revisa la consola de desarrollador: <br />
    `Developer: Toggle Developer Tools`
  </Card>

  <Card title="Logs" icon="file-lines">
    Accede a los registros: <br />
    `Developer: Open Logs Folder`
  </Card>
</CardGroup>

---

← Previous: [Obtener un ID de solicitud](./obtener-un-id-de-solicitud.md) | [Index](./index.md) | Next: [Bienvenido](./bienvenido.md) →