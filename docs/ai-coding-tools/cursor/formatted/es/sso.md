---
title: "SSO"
source: "https://docs.cursor.com/es/account/teams/sso"
language: "es"
language_name: "Spanish"
---

# SSO
Source: https://docs.cursor.com/es/account/teams/sso

Configura el inicio de sesión único para tu equipo

<div id="overview">
  ## Descripción general
</div>

El SSO con SAML 2.0 está disponible sin costo adicional en los planes Business. Usa tu proveedor de identidad (IdP) existente para autenticar a los miembros del equipo sin que necesiten cuentas independientes de Cursor.

<Frame>
  <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=76608c26daf1f9ab2bbc2c4ccb156c0e" style={{ padding: 32, backgroundColor: "#0c0c0c" }} data-og-width="802" width="802" data-og-height="440" height="440" data-path="images/account/sso-settings.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=334dc1fc107338d19ec7b0052e7ea0e4 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=543b3d868c19960a5fb4c526d9895bd3 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=a06655178ba10f6a72919e9f7d598191 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=e280fc911306fe8d3b8e90b7221b0c11 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=ffd8f2c0168e2ac4f95431062b226021 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=1c17e4eac666b663d676ce874f1c4ba5 2500w" />
</Frame>

<div id="prerequisites">
  ## Requisitos previos
</div>

* Plan Cursor Team
* Acceso de admin a tu proveedor de identidad (p. ej., Okta)
* Acceso de admin a tu organización de Cursor

<div id="configuration-steps">
  ## Pasos de configuración
</div>

<Steps>
  <Step title="Inicia sesión en tu cuenta de Cursor">
    Ve a [cursor.com/dashboard?tab=settings](https://www.cursor.com/dashboard?tab=settings) con una cuenta de admin.
  </Step>

  <Step title="Ubica la configuración de SSO">
    Busca la sección "Single Sign-On (SSO)" y ábrela.
  </Step>

  <Step title="Comienza el proceso de configuración">
    Haz clic en el botón "SSO Provider Connection settings" para iniciar la configuración de SSO y sigue el asistente.
  </Step>

  <Step title="Configura tu proveedor de identidad">
    En tu proveedor de identidad (p. ej., Okta):

    * Crea una nueva aplicación SAML
    * Configura los parámetros de SAML usando la información de Cursor
    * Configura el aprovisionamiento Just‑in‑Time (JIT)
  </Step>

  <Step title="Verifica el dominio">
    Verifica el dominio de tus usuarios en Cursor haciendo clic en el botón "Domain verification settings".
  </Step>
</Steps>

<div id="identity-provider-setup-guides">
  ### Guías de configuración del proveedor de identidad
</div>

Para instrucciones de configuración específicas por proveedor:

<Card title="Guías del proveedor de identidad" icon="book" href="https://workos.com/docs/integrations">
  Instrucciones de configuración para Okta, Azure AD, Google Workspace y más.
</Card>

<div id="additional-settings">
  ## Configuraciones adicionales
</div>

* Controla la aplicación forzosa de SSO desde el panel de administración
* Los nuevos usuarios se registran automáticamente al iniciar sesión con SSO
* Administra a los usuarios a través de tu proveedor de identidad

<div id="troubleshooting">
  ## Solución de problemas
</div>

Si tienes problemas:

* Verifica que el dominio esté validado en Cursor
* Asegúrate de que los atributos SAML estén asignados correctamente
* Comprueba que el SSO esté habilitado en el panel de administración
* Asegúrate de que nombre y apellido coincidan entre el proveedor de identidad y Cursor
* Revisa las guías específicas del proveedor de más arriba
* Escríbenos a [hi@cursor.com](mailto:hi@cursor.com) si el problema persiste

---

← Previous: [Primeros pasos](./primeros-pasos.md) | [Index](./index.md) | Next: [Acceso a actualizaciones](./acceso-a-actualizaciones.md) →