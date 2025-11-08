---
title: "Bugbot"
source: "https://docs.cursor.com/es/bugbot"
language: "es"
language_name: "Spanish"
---

# Bugbot
Source: https://docs.cursor.com/es/bugbot

Revisión de código con IA para pull requests

Bugbot revisa pull requests e identifica bugs, problemas de seguridad y de calidad de código.

<Tip>
  Bugbot incluye un plan gratuito: cada usuario recibe una cantidad limitada de revisiones de PR gratis cada mes. Cuando alcanzas el límite, las revisiones se pausan hasta tu próximo ciclo de facturación. Podés actualizar en cualquier momento a una prueba Pro gratuita de 14 días para revisiones ilimitadas (sujeto a controles estándar contra abusos).
</Tip>

<Frame>
  <video src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/bugbot/bugbot-report-cropped.mp4?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=013060fbd22f397ac81f2c32bb8b6b14" alt="Bugbot dejando comentarios en un PR" autoPlay loop muted playsInline controls data-path="images/bugbot/bugbot-report-cropped.mp4" />
</Frame>

<div id="how-it-works">
  ## Cómo funciona
</div>

Bugbot analiza los diffs de los PR y deja comentarios con explicaciones y sugerencias de corrección. Se ejecuta automáticamente en cada actualización del PR o manualmente cuando se activa.

* Ejecuta **revisiones automáticas** en cada actualización del PR
* **Disparo manual** comentando `cursor review` o `bugbot run` en cualquier PR
* Los enlaces **Fix in Cursor** abren issues directamente en Cursor
* Los enlaces **Fix in Web** abren issues directamente en [cursor.com/agents](https://cursor.com/agents)

<div id="setup">
  ## Configuración
</div>

Requiere acceso de admin en Cursor y acceso de admin en la organización de GitHub.

1. Ve a [cursor.com/dashboard](https://cursor.com/dashboard?tab=bugbot)
2. Entra a la pestaña Bugbot
3. Haz clic en `Connect GitHub` (o en `Manage Connections` si ya está conectado)
4. Sigue el flujo de instalación de GitHub
5. Vuelve al dashboard para habilitar Bugbot en repositorios específicos

<Frame>
  <video src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/bugbot/bugbot-install.mp4?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=75745d4464b183c306a44571db86a0c4" alt="Configuración de Bugbot en GitHub" autoPlay loop muted playsInline controls data-path="images/bugbot/bugbot-install.mp4" />
</Frame>

<div id="setup">
  ## Configuración
</div>

<Tabs defaultValue="Team">
  <Tab title="Individual">
    ### Configuración del repositorio

    Activa o desactiva Bugbot por repositorio desde tu lista de instalaciones. Bugbot solo se ejecuta en PR que tú crees.

    ### Configuración personal

    * Ejecutar **solo cuando se le mencione** comentando `cursor review` o `bugbot run`
    * Ejecutar **solo una vez** por PR, omitiendo commits posteriores
  </Tab>

  <Tab title="Team">
    ### Configuración del repositorio

    Los administradores del equipo pueden activar Bugbot por repositorio, configurar listas de permitidos/denegados para revisores y definir:

    * Ejecutar **solo una vez** por PR y por instalación, omitiendo commits posteriores
    * **Desactivar las revisiones en línea** para evitar que Bugbot deje comentarios directamente en las líneas de código

    Bugbot se ejecuta para todas las personas que contribuyan en los repositorios habilitados, sin importar la pertenencia al equipo.

    ### Configuración personal

    Los miembros del equipo pueden anular la configuración para sus propios PR:

    * Ejecutar **solo cuando se le mencione** comentando `cursor review` o `bugbot run`
    * Ejecutar **solo una vez** por PR, omitiendo commits posteriores
    * **Habilitar revisiones en PR en borrador** para incluir pull requests en borrador en las revisiones automáticas
  </Tab>
</Tabs>

<div id="analytics">
  ### Analítica
</div>

<Frame>
  <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/bugbot/bugbot-dashboard.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=0b09bc0e61d1c92017c3ca42957c70e1" alt="Panel de Bugbot" data-og-width="1832" width="1832" data-og-height="2022" height="2022" data-path="images/bugbot/bugbot-dashboard.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/bugbot/bugbot-dashboard.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=fe3c6151118fa404a0a5a100968649cf 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/bugbot/bugbot-dashboard.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=7a602dfdaa6f737dc6d5010ea90a74b8 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/bugbot/bugbot-dashboard.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=6a21a6cb4b32248fb2b8cbea9afb8bcc 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/bugbot/bugbot-dashboard.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=27df9beda1ee9efc84e6f2c339ff1076 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/bugbot/bugbot-dashboard.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=80cb6507ca96d1c2aa74bcc30170b517 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/bugbot/bugbot-dashboard.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=ce35818f10c462b16b2d697519557019 2500w" />
</Frame>

<div id="rules">
  ## Reglas
</div>

Crea archivos `.cursor/BUGBOT.md` para aportar contexto específico del proyecto en las revisiones. Bugbot siempre incluye el archivo raíz `.cursor/BUGBOT.md` y cualquier archivo adicional que encuentre al recorrer hacia arriba desde los archivos modificados.

```
project/
  .cursor/BUGBOT.md          # Siempre incluido (reglas a nivel de proyecto)
  backend/
    .cursor/BUGBOT.md        # Incluido al revisar archivos del backend
    api/
      .cursor/BUGBOT.md      # Incluido al revisar archivos del API
  frontend/
    .cursor/BUGBOT.md        # Incluido al revisar archivos del frontend
```

<AccordionGroup>
  <Accordion title="Ejemplo .cursor/BUGBOT.md">
    ```markdown  theme={null}
    # Guías para la revisión del proyecto

    ## Enfoques de seguridad

    - Validar la entrada del usuario en los endpoints de la API
    - Revisar vulnerabilidades de inyección SQL en las consultas a la base de datos
    - Garantizar una autenticación adecuada en las rutas protegidas

    ## Patrones de arquitectura

    - Usar inyección de dependencias para los servicios
    - Seguir el patrón de repositorio para el acceso a datos
    - Implementar un manejo de errores adecuado con clases de error personalizadas

    ## Problemas comunes

    - Fugas de memoria en componentes de React (revisa la limpieza de useEffect)
    - Falta de límites de error (error boundaries) en componentes de UI
    - Convenciones de nombres inconsistentes (usa camelCase para las funciones)

    ```
  </Accordion>
</AccordionGroup>

<div id="pricing">
  ## Precios
</div>

Bugbot ofrece dos planes: **Gratis** y **Pro**.

<div id="free-tier">
  ### Free tier
</div>

Cada usuario obtiene una cantidad limitada de revisiones de PR gratis cada mes. En equipos, cada miembro del equipo recibe sus propias revisiones gratis. Cuando llegás al límite, las revisiones se pausan hasta tu próximo ciclo de facturación. Podés pasar en cualquier momento a la prueba Pro gratuita de 14 días para tener revisiones ilimitadas.

<div id="pro-tier">
  ### Plan Pro
</div>

<Tabs defaultValue="Teams">
  <Tab title="Individuals">
    ### Tarifa fija

    USD 40 al mes por revisiones ilimitadas de Bugbot en hasta 200 PR al mes en todos los repositorios.

    ### Primeros pasos

    Suscribite desde la configuración de tu cuenta.
  </Tab>

  <Tab title="Teams">
    ### Facturación por usuario

    Los equipos pagan USD 40 por usuario por mes por revisiones ilimitadas.

    Consideramos usuario a quien haya sido autor de PR revisados por Bugbot en un mes.

    Todas las licencias se liberan al inicio de cada ciclo de facturación y se asignan por orden de llegada. Si un usuario no autoriza ningún PR revisado por Bugbot en un mes, el cupo puede ser usado por otra persona.

    ### Límites de cupos

    Los admins del equipo pueden establecer un máximo de cupos de Bugbot por mes para controlar los costos.

    ### Primeros pasos

    Suscribite desde el panel de tu equipo para habilitar la facturación.

    ### Medidas contra abusos

    Para evitar abusos, tenemos un tope conjunto de 200 pull requests por mes por cada licencia de Bugbot. Si necesitás más de 200 pull requests por mes, contactanos en [hi@cursor.com](mailto:hi@cursor.com) y con gusto te ayudamos.

    Por ejemplo, si tu equipo tiene 100 usuarios, tu organización inicialmente podrá revisar 20.000 pull requests por mes. Si alcanzan ese límite de forma natural, por favor escribinos y con gusto aumentamos el límite.
  </Tab>
</Tabs>

<div id="troubleshooting">
  ## Solución de problemas
</div>

Si Bugbot no está funcionando:

1. **Activa el modo detallado** añadiendo un comentario `cursor review verbose=true` o `bugbot run verbose=true` para obtener logs detallados y el ID de la solicitud
2. **Revisa los permisos** para verificar que Bugbot tenga acceso al repositorio
3. **Verifica la instalación** para confirmar que la app de GitHub esté instalada y habilitada

Incluye el ID de la solicitud del modo detallado al reportar problemas.

<div id="faq">
  ## Preguntas frecuentes
</div>

<AccordionGroup>
  <Accordion title="¿Bugbot es compatible con el modo de privacidad?">
    Sí, Bugbot cumple las mismas normas de privacidad que Cursor y procesa los datos de la misma forma que otras solicitudes de Cursor.
  </Accordion>

  <Accordion title="¿Qué pasa cuando alcanzó el límite del plan gratuito?">
    Cuando llegas a tu límite mensual del plan gratuito, las revisiones de Bugbot se pausan hasta tu siguiente ciclo de facturación. Puedes pasar a la prueba Pro gratuita de 14 días para obtener revisiones ilimitadas (sujetas a las protecciones estándar contra abuso).
  </Accordion>
</AccordionGroup>

```
```

---

← Previous: [Web y móvil](./web-y-mvil.md) | [Index](./index.md) | Next: [Code Review](./code-review.md) →