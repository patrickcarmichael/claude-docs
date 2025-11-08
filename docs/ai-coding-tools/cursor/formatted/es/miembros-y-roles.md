---
title: "Miembros y roles"
source: "https://docs.cursor.com/es/account/teams/members"
language: "es"
language_name: "Spanish"
---

# Miembros y roles
Source: https://docs.cursor.com/es/account/teams/members

Administra los miembros y roles del equipo

Los equipos de Cursor tienen tres roles:

<div id="roles">
  ## Roles
</div>

**Miembros** es el rol predeterminado con acceso a las funciones Pro de Cursor.

* Acceso completo a las funciones Pro de Cursor
* Sin acceso a la configuración de facturación ni al panel de administración
* Pueden ver su propio uso y el presupuesto restante según el uso

**Admins** controlan la gestión del equipo y la configuración de seguridad.

* Acceso completo a las funciones Pro
* Agregar/quitar miembros, modificar roles, configurar SSO
* Configurar precios basados en uso y límites de gasto
* Acceso a analíticas del equipo

**Admins no pagados** gestionan equipos sin ocupar un asiento de pago; ideal para personal de TI o finanzas que no necesita acceso a Cursor.

* No facturables, sin funciones Pro
* Las mismas capacidades administrativas que los Admins

<Info>Los Admins no pagados requieren al menos un usuario de pago en el equipo.</Info>

<div id="role-comparison">
  ## Comparación de roles
</div>

<div className="full-width-table">
  | Capacidades                 | Miembro | Admin | Admin sin pago |
  | --------------------------- | :-----: | :---: | :------------: |
  | Usar funciones de Cursor    |    ✓    |   ✓   |                |
  | Invitar miembros            |    ✓    |   ✓   |        ✓       |
  | Quitar miembros             |         |   ✓   |        ✓       |
  | Cambiar rol de usuario      |         |   ✓   |        ✓       |
  | Panel de administración     |         |   ✓   |        ✓       |
  | Configurar SSO/seguridad    |         |   ✓   |        ✓       |
  | Gestionar facturación       |         |   ✓   |        ✓       |
  | Ver analíticas              |         |   ✓   |        ✓       |
  | Gestionar acceso            |         |   ✓   |        ✓       |
  | Establecer controles de uso |         |   ✓   |        ✓       |
  | Requiere asiento de pago    |    ✓    |   ✓   |                |
</div>

<div id="managing-members">
  ## Gestión de miembros
</div>

Todos los miembros del equipo pueden invitar a otras personas. Actualmente no controlamos las invitaciones.

<div id="add-member">
  ### Agregar miembro
</div>

Podés agregar miembros de tres maneras:

1. **Invitación por email**

   * Hacé clic en `Invite Members`
   * Ingresá direcciones de email
   * Les usuaries reciben invitaciones por email

2. **Enlace de invitación**

   * Hacé clic en `Invite Members`
   * Copiá `Invite Link`
   * Compartilo con miembros del equipo

3. **SSO**
   * Configurá SSO en el [admin dashboard](/es/account/teams/sso)
   * Les usuaries se unen automáticamente al iniciar sesión con el email de SSO

<Warning>
  Los enlaces de invitación tienen una fecha de vencimiento larga: cualquiera con el enlace puede unirse.
  Revocalos o usá [SSO](/es/account/teams/sso)
</Warning>

<div id="remove-member">
  ### Eliminar miembro
</div>

Les admins pueden eliminar miembros en cualquier momento mediante el menú contextual → "Remove". Si un miembro usó créditos, su asiento permanece ocupado hasta el final del ciclo de facturación.

<div id="change-role">
  ### Cambiar rol
</div>

Les admins pueden cambiar los roles de otres miembros haciendo clic en el menú contextual y luego usando la opción "Change role".<br />

Debe haber al menos un admin y un miembro de pago en el equipo en todo momento.

<div id="security-sso">
  ## Seguridad y SSO
</div>

El inicio de sesión único (SSO) con SAML 2.0 está disponible en los planes Team. Las funciones clave incluyen:

* Configurar conexiones de SSO ([más info](/es/account/teams/sso))
* Configurar la verificación de dominio
* Alta automática de usuarios
* Opciones para exigir SSO
* Integración con el proveedor de identidad (Okta, etc.)

<Note>
  <p className="!mb-0">La verificación de dominio es necesaria para habilitar SSO.</p>
</Note>

<Frame>
  <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=76608c26daf1f9ab2bbc2c4ccb156c0e" style={{ padding: `32px 64px`, backgroundColor: "#0c0c0c" }} data-og-width="802" width="802" data-og-height="440" height="440" data-path="images/account/sso-settings.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=334dc1fc107338d19ec7b0052e7ea0e4 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=543b3d868c19960a5fb4c526d9895bd3 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=a06655178ba10f6a72919e9f7d598191 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=e280fc911306fe8d3b8e90b7221b0c11 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=ffd8f2c0168e2ac4f95431062b226021 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=1c17e4eac666b663d676ce874f1c4ba5 2500w" />
</Frame>

<div id="usage-controls">
  ## Controles de uso
</div>

Accede a la configuración de uso para:

* Habilitar la facturación basada en el uso
* Habilitar para modelos premium
* Permitir modificaciones solo para administradores
* Establecer límites de gasto mensuales
* Supervisar el uso de todo el equipo

<Frame>
  <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/usage-based-pricing.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=e8149f830c27308af1bcc329c25e38b5" style={{ backgroundColor: "#0c0c0c" }} data-og-width="1668" width="1668" data-og-height="1160" height="1160" data-path="images/account/usage-based-pricing.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/usage-based-pricing.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=bc308a967251694ad7b03189c1083c61 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/usage-based-pricing.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=ddc293e19fa993e65be8c09ced649b4f 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/usage-based-pricing.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=3a4df7d48d75c6166ab215550a641ca6 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/usage-based-pricing.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=f9051947c802ae54fd964196c50a3701 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/usage-based-pricing.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=ed775e3e98611ead1b938aedaf917f11 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/usage-based-pricing.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=b26f86bce94dc981d3cf71853a965374 2500w" />
</Frame>

<div id="billing">
  ## Facturación
</div>

Al agregar miembros al equipo:

* Cada miembro o admin suma un asiento facturable (ver [pricing](https://cursor.com/pricing))
* A los nuevos miembros se les cobra de forma prorrateada por el tiempo restante del período de facturación
* Los asientos de admin no pago no se cuentan

Las altas a mitad de mes solo cobran por los días usados. Al quitar miembros que ya usaron créditos, su asiento queda ocupado hasta el final del ciclo de facturación: no hay reembolsos prorrateados.

Los cambios de rol (p. ej., de Admin a Admin no pago) ajustan la facturación desde la fecha del cambio. Elegí facturación mensual o anual.

La renovación mensual/anual ocurre en tu fecha original de registro, sin importar los cambios de miembros.

<div id="switch-to-yearly-billing">
  ### Cambiar a facturación anual
</div>

Ahorrá un **20%** al pasar de mensual a anual:

1. Andá al [Dashboard](https://cursor.com/dashboard)
2. En la sección de cuenta, hacé clic en "Advanced" y luego en "Upgrade to yearly billing"

<Note>
  Solo podés cambiar de mensual a anual desde el dashboard. Para cambiar de
  anual a mensual, escribí a [hi@cursor.com](mailto:hi@cursor.com).
</Note>

---

← Previous: [Ajustes de empresa](./ajustes-de-empresa.md) | [Index](./index.md) | Next: [SCIM](./scim.md) →