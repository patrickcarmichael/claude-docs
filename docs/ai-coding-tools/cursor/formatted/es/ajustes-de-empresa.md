---
title: "Ajustes de empresa"
source: "https://docs.cursor.com/es/account/teams/enterprise-settings"
language: "es"
language_name: "Spanish"
---

# Ajustes de empresa
Source: https://docs.cursor.com/es/account/teams/enterprise-settings

Administra centralmente los ajustes de Cursor para tu organización

<div id="enterprise-settings">
  # Configuración para empresas
</div>

Podés gestionar de forma centralizada funciones específicas de Cursor mediante soluciones de administración de dispositivos para asegurarte de que cumpla con las necesidades de tu organización. Cuando especificás una política de Cursor, su valor reemplaza la configuración correspondiente de Cursor en los dispositivos de los usuarios.

Editor de configuración que muestra que la opción 'Extensions: Allowed' está gestionada por la organización.

Actualmente, Cursor ofrece políticas para controlar las siguientes funciones administradas por el equipo de TI:

| Policy            | Description                                                                                                                         | Cursor setting           | Available since |
| ----------------- | ----------------------------------------------------------------------------------------------------------------------------------- | ------------------------ | --------------- |
| AllowedExtensions | Controla qué extensiones se pueden instalar.                                                                                        | extensions.allowed       | 1.2             |
| AllowedTeamId     | Controla qué IDs de equipo pueden iniciar sesión. Los usuarios con IDs de equipo no autorizados se cierran sesión de forma forzosa. | cursorAuth.allowedTeamId | 1.3             |

<div id="configure-allowed-extensions">
  ## Configurar extensiones permitidas
</div>

La configuración de Cursor `extensions.allowed` controla qué extensiones se pueden instalar. Esta configuración acepta un objeto JSON donde las claves son nombres de publishers y los valores son booleanos que indican si se permiten las extensiones de ese publisher.

Por ejemplo, establecer `extensions.allowed` en `{"anysphere": true, "github": true}` permite extensiones de los publishers Anysphere y GitHub, mientras que configurarlo en `{"anysphere": false}` bloquea las extensiones de Anysphere.

Para gestionar de forma centralizada las extensiones permitidas para tu organización, configura la política `AllowedExtensions` usando tu solución de administración de dispositivos. Esta política reemplaza la configuración `extensions.allowed` en los dispositivos de los usuarios. El valor de esta política es una cadena JSON que define los publishers permitidos.

Si quieres saber más sobre las extensiones en Cursor, consulta la documentación de extensiones.

<div id="configure-allowed-team-ids">
  ## Configurar IDs de equipo permitidos
</div>

La configuración de Cursor `cursorAuth.allowedTeamId` controla qué IDs de equipo pueden iniciar sesión en Cursor. Esta configuración acepta una lista de IDs de equipo autorizados separada por comas.

Por ejemplo, establecer `cursorAuth.allowedTeamId` en "1,3,7" permite que usuarios de esos IDs de equipo específicos inicien sesión.

Cuando un usuario intenta iniciar sesión con un ID de equipo que no está en la lista permitida:

* Se cierra su sesión de forma inmediata
* Se muestra un mensaje de error
* La aplicación bloquea más intentos de autenticación hasta que se use un ID de equipo válido

Para gestionar de forma centralizada los IDs de equipo permitidos de tu organización, configura la directiva `AllowedTeamId` usando tu solución de gestión de dispositivos. Esta directiva reemplaza la configuración `cursorAuth.allowedTeamId` en los dispositivos de los usuarios. El valor de esta directiva es una cadena que contiene la lista de IDs de equipo autorizados separada por comas.

<div id="group-policy-on-windows">
  ## Directiva de grupo en Windows
</div>

Cursor es compatible con la Directiva de grupo basada en el Registro de Windows. Cuando se instalan las definiciones de directiva, los administradores pueden usar el Editor de directivas de grupo local para gestionar los valores de las directivas.

Para agregar una directiva:

1. Copia los archivos ADMX y ADML de `AppData\Local\Programs\cursor\policies`.
2. Pega el archivo ADMX en `C:\Windows\PolicyDefinitions` y el archivo ADML en `C:\Windows\PolicyDefinitions\<your-locale>\`.
3. Reinicia el Editor de directivas de grupo local.
4. Establece los valores de directiva correspondientes (p. ej., `{"anysphere": true, "github": true}` para la directiva `AllowedExtensions`) en el Editor de directivas de grupo local.

Las directivas se pueden establecer tanto a nivel de equipo como a nivel de usuario. Si ambos están configurados, el nivel de equipo tendrá prioridad. Cuando se establece un valor de directiva, ese valor reemplaza el valor de configuración de Cursor establecido en cualquier nivel (predeterminado, usuario, espacio de trabajo, etc.).

<div id="configuration-profiles-on-macos">
  ## Perfiles de configuración en macOS
</div>

Los perfiles de configuración administran ajustes en dispositivos macOS. Un perfil es un archivo XML con pares clave/valor que corresponden a las políticas disponibles. Estos perfiles pueden desplegarse con soluciones de Mobile Device Management (MDM) o instalarse manualmente.

<Accordion title="Archivo .mobileconfig de ejemplo">
  A continuación se muestra un archivo `.mobileconfig` de ejemplo para macOS:

  ```
  <?xml version="1.0" encoding="UTF-8"?>
  <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
  <plist version="1.0">
  	<dict>
  		<key>PayloadContent</key>
  		<array>
  			<dict>
  				<key>PayloadDisplayName</key>
  				<string>Cursor</string>
  				<key>PayloadIdentifier</key>
  				<string>com.todesktop.230313mzl4w4u92.J6B5723A-6539-4F31-8A4E-3CC96E51F48C</string>
  				<key>PayloadType</key>
  				<string>com.todesktop.230313mzl4w4u92</string>
  				<key>PayloadUUID</key>
  				<string>J6B5723A-6539-4F31-8A4E-3CC96E51F48C</string>
  				<key>PayloadVersion</key>
  				<integer>1</integer>
  				<key>AllowedExtensions</key>
  				<string>{"anysphere":true}</string>
  				<key>AllowedTeamId</key>
  				<string>1,2</string>
  			</dict>
  		</array>
  		<key>PayloadDescription</key>
  		<string>This profile manages Cursor.</string>
  		<key>PayloadDisplayName</key>
  		<string>Cursor</string>
  		<key>PayloadIdentifier</key>
  		<string>com.todesktop.230313mzl4w4u92</string>
  		<key>PayloadOrganization</key>
  		<string>Anysphere</string>
  		<key>PayloadType</key>
  		<string>Configuration</string>
  		<key>PayloadUUID</key>
  		<string>F2C1A7B3-9D4E-4B2C-8E1F-7A6C5D4B3E2F</string>
  		<key>PayloadVersion</key>
  		<integer>1</integer>
  		<key>TargetDeviceType</key>
  		<integer>5</integer>
  	</dict>
  </plist>
  ```
</Accordion>

<div id="string-policies">
  ### Políticas de tipo string
</div>

El ejemplo de abajo muestra cómo configurar la política `AllowedExtensions`. El valor de la política comienza vacío en el archivo de ejemplo (no se permite ninguna extensión).

```
<key>AllowedExtensions</key>
<string></string>
```

Agrega la cadena JSON adecuada que defina tu policy entre las etiquetas `<string>`.

```
<key>AllowedExtensions</key>
<string>{"anysphere": true, "github": true}</string>
```

Para la directiva `AllowedTeamId`, agrega la lista de IDs de equipo separadas por comas:

```
<key>AllowedTeamId</key>
<string>1,3,7</string>
```

**Importante:** El archivo `.mobileconfig` proporcionado inicializa **todas** las políticas disponibles en esa versión de Cursor. Elimina cualquier política que no necesites.

Si no editas o eliminas una política del `.mobileconfig` de muestra, esa política se aplicará con su valor predeterminado (restrictivo).

Instala manualmente un perfil de configuración haciendo doble clic en el perfil `.mobileconfig` en Finder y luego habilitándolo en Preferencias del Sistema en **General** > **Administración de dispositivos**. Al quitar el perfil desde Preferencias del Sistema, se eliminarán las políticas de Cursor.

Para obtener más información sobre los perfiles de configuración, consulta la documentación de Apple.

<div id="additional-policies">
  ## Políticas adicionales
</div>

La idea es promover las configuraciones actuales de Cursor como políticas y ceñirse de cerca a las existentes, para que la nomenclatura y el comportamiento sean consistentes. Si querés proponer más políticas, abrí un issue en el repositorio de GitHub de Cursor. El equipo va a determinar si ya existe una configuración correspondiente para ese comportamiento o si se debería crear una nueva para controlar el comportamiento deseado.

<div id="frequently-asked-questions">
  ## Preguntas frecuentes
</div>

<div id="does-cursor-support-configuration-profiles-on-linux">
  ### ¿Cursor admite perfiles de configuración en Linux?
</div>

El soporte para Linux no está en la hoja de ruta. Si te interesan los perfiles de configuración en Linux, abre un issue en el repositorio de GitHub de Cursor y comparte detalles sobre tu caso.

---

← Previous: [Panel](./panel.md) | [Index](./index.md) | Next: [Miembros y roles](./miembros-y-roles.md) →