---
title: "SCIM"
source: "https://docs.cursor.com/es/account/teams/scim"
language: "es"
language_name: "Spanish"
---

# SCIM
Source: https://docs.cursor.com/es/account/teams/scim

Configurá el aprovisionamiento de SCIM para la gestión automatizada de usuarios y grupos

<div id="overview">
  ## Descripción general
</div>

El aprovisionamiento con SCIM 2.0 gestiona automáticamente los miembros de tu equipo y los grupos del directorio a través de tu proveedor de identidad. Disponible en planes Enterprise con SSO activado.

<product_visual type="screenshot">
  Panel de SCIM que muestra la configuración de Active Directory Management
</product_visual>

<div id="prerequisites">
  ## Requisitos previos
</div>

* Plan de Cursor Enterprise
* Primero debe configurarse el SSO: **SCIM requiere una conexión SSO activa**
* Acceso de administrador a tu proveedor de identidad (Okta, Azure AD, etc.)
* Acceso de administrador a tu organización de Cursor

<div id="how-it-works">
  ## Cómo funciona
</div>

<div id="user-provisioning">
  ### Aprovisionamiento de usuarios
</div>

Los usuarios se añaden automáticamente a Cursor cuando los asignas a la aplicación SCIM en tu proveedor de identidad. Al desasignarlos, se eliminan. Los cambios se sincronizan en tiempo real.

<div id="directory-groups">
  ### Grupos de directorio
</div>

Los grupos de directorio y su pertenencia se sincronizan desde tu proveedor de identidad. La gestión de grupos y usuarios debe hacerse a través de tu proveedor de identidad; Cursor muestra esta información como de solo lectura.

<div id="spend-management">
  ### Gestión del gasto
</div>

Configura distintos límites de gasto por usuario para cada grupo de directorio. Los límites de los grupos de directorio tienen prioridad sobre los límites a nivel de equipo. Los usuarios que pertenezcan a varios grupos reciben el límite de gasto más alto aplicable.

<div id="setup">
  ## Configuración
</div>

<Steps>
  <Step title="Asegurate de tener SSO configurado">
    SCIM requiere que primero configures SSO. Si aún no lo hiciste,
    seguí la [guía de configuración de SSO](/es/account/teams/sso) antes de continuar.
  </Step>

  <Step title="Accedé a Active Directory Management">
    Navegá a
    [cursor.com/dashboard?tab=active-directory](https://www.cursor.com/dashboard?tab=active-directory)
    con una cuenta de admin, o andá a la configuración de tu dashboard y seleccioná la
    "Active Directory Management" tab.
  </Step>

  <Step title="Iniciá la configuración de SCIM">
    Una vez verificado SSO, vas a ver un enlace para la configuración de SCIM paso a paso. Hacé clic
    para iniciar el asistente de configuración.
  </Step>

  <Step title="Configurá SCIM en tu proveedor de identidad">
    En tu proveedor de identidad: Creá o configurá tu aplicación SCIM. Usá
    el endpoint y el token de SCIM provistos por Cursor. Activá el aprovisionamiento de usuarios y el envío de grupos.
    Probá la conexión.
  </Step>

  <Step title="Configurá límites de gasto (opcional)">
    De vuelta en la página de Active Directory Management de Cursor: Mirá tus grupos de directorio sincronizados.
    Configurá límites de gasto por usuario para grupos específicos según sea necesario.
    Revisá qué límites aplican a usuarios en múltiples grupos.
  </Step>
</Steps>

<div id="identity-provider-setup">
  ### Configuración del proveedor de identidad
</div>

Para instrucciones específicas del proveedor:

<Card title="Guías del proveedor de identidad" icon="book" href="https://workos.com/docs/integrations">
  Instrucciones de configuración para Okta, Azure AD, Google Workspace y más.
</Card>

<div id="managing-users-and-groups">
  ## Gestión de usuarios y grupos
</div>

<Warning>
  Toda la gestión de usuarios y grupos debe hacerse a través de tu proveedor de identidad.
  Los cambios que realices en tu proveedor de identidad se sincronizan automáticamente con Cursor, pero
  no puedes modificar usuarios ni grupos directamente en Cursor.
</Warning>

<div id="user-management">
  ### Gestión de usuarios
</div>

* Agrega usuarios asignándolos a tu aplicación SCIM en tu proveedor de identidad
* Elimina usuarios quitándolos de la asignación de la aplicación SCIM
* Los cambios en el perfil del usuario (nombre, correo) se sincronizan automáticamente desde tu proveedor de identidad

<div id="group-management">
  ### Gestión de grupos
</div>

* Los grupos del directorio se sincronizan automáticamente desde tu proveedor de identidad
* Los cambios en la pertenencia a grupos se reflejan en tiempo real
* Usa grupos para organizar usuarios y establecer distintos límites de gasto

<div id="spend-limits">
  ### Límites de gasto
</div>

* Establece distintos límites por usuario para cada grupo del directorio
* Los usuarios heredan el límite de gasto más alto de sus grupos
* Los límites de grupo reemplazan el límite predeterminado por usuario del equipo

<div id="faq">
  ## Preguntas frecuentes
</div>

<div id="why-isnt-scim-management-showing-up-in-my-dashboard">
  ### ¿Por qué la administración de SCIM no aparece en mi panel?
</div>

Asegurate de que SSO esté configurado correctamente y funcionando antes de configurar SCIM. SCIM requiere una conexión de SSO activa para funcionar.

<div id="why-arent-users-syncing">
  ### ¿Por qué los usuarios no se están sincronizando?
</div>

Verificá que los usuarios estén asignados a la aplicación de SCIM en tu proveedor de identidad. Los usuarios tienen que estar asignados explícitamente para aparecer en Cursor.

<div id="why-arent-groups-appearing">
  ### ¿Por qué los grupos no aparecen?
</div>

Comprobá que el aprovisionamiento de grupos por push esté habilitado en la configuración de SCIM de tu proveedor de identidad. La sincronización de grupos se configura por separado de la sincronización de usuarios.

<div id="why-arent-spend-limits-applying">
  ### ¿Por qué no se aplican los límites de gasto?
</div>

Confirmá que los usuarios estén correctamente asignados a los grupos correspondientes en tu proveedor de identidad. La pertenencia a grupos determina qué límites de gasto se aplican.

<div id="can-i-manage-scim-users-and-groups-directly-in-cursor">
  ### ¿Puedo administrar usuarios y grupos de SCIM directamente en Cursor?
</div>

No. Toda la administración de usuarios y grupos se tiene que hacer a través de tu proveedor de identidad. Cursor muestra esta información como de solo lectura.

<div id="how-quickly-do-changes-sync">
  ### ¿Qué tan rápido se sincronizan los cambios?
</div>

Los cambios realizados en tu proveedor de identidad se sincronizan con Cursor en tiempo real. Puede haber una breve demora en operaciones masivas.

---

← Previous: [Miembros y roles](./miembros-y-roles.md) | [Index](./index.md) | Next: [Primeros pasos](./primeros-pasos.md) →