---
title: "Analytics"
source: "https://docs.cursor.com/es/account/teams/analytics"
language: "es"
language_name: "Spanish"
---

# Analytics
Source: https://docs.cursor.com/es/account/teams/analytics

Haz seguimiento del uso del equipo y las métrricas de actividad

Los admins del equipo pueden ver métricas desde el [dashboard](/es/account/teams/dashboard).

<Frame>
  <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/analytics.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=a8a4a0ca334e5f5acac55307b2ebeadf" data-og-width="3456" width="3456" data-og-height="1944" height="1944" data-path="images/account/team/analytics.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/analytics.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=73c11df8fcb2862e5c1fd551e6399159 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/analytics.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=c3eaa0d4faa7d6fdf5e3c79dfd11fb5a 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/analytics.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=e9ee5fc554ae46e9d0e2cf53c19e652d 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/analytics.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=5f0afded72e0b02142c5a85e448f2d4e 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/analytics.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=3a6dec2a182ac88d7de75f7a42b1f5ff 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/analytics.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=7a8ac7dafe559da435f3f4974b04df52 2500w" />
</Frame>

<div id="total-usage">
  ### Uso total
</div>

Consulta métricas agregadas de tu equipo, incluidas pestañas totales y solicitudes premium. En equipos con menos de 30 días, las métricas muestran el uso desde la creación, incluida la actividad previa al ingreso de los miembros del equipo.

<div id="per-active-user">
  ### Por usuario activo
</div>

Mira los promedios por usuario activo: pestañas aceptadas, líneas de código y solicitudes premium.

<div id="user-activity">
  ### Actividad de usuarios
</div>

Haz seguimiento de usuarios activos semanales y mensuales.

<div id="analytics-report-headers">
  ## Encabezados del informe de analíticas
</div>

Cuando exportas datos de analíticas desde el panel, el informe incluye métricas detalladas sobre el comportamiento de los usuarios y el uso de funcionalidades. Esto es lo que significa cada encabezado:

<div id="user-information">
  ### Información del usuario
</div>

<ResponseField name="Date" type="ISO 8601 timestamp">
  La fecha en que se registraron los datos de analíticas (p. ej., 2024-01-15T04:30:00.000Z)
</ResponseField>

<ResponseField name="User ID" type="string">
  Identificador único de cada usuario en el sistema
</ResponseField>

<ResponseField name="Email" type="string">
  Dirección de correo del usuario asociada a su cuenta
</ResponseField>

<ResponseField name="Is Active" type="boolean">
  Indica si el usuario estuvo activo en esta fecha
</ResponseField>

<div id="ai-generated-code-metrics">
  ### Métricas de código generado por IA
</div>

<ResponseField name="Chat Suggested Lines Added" type="number">
  Total de líneas de código sugeridas por la función de chat con IA
</ResponseField>

<ResponseField name="Chat Suggested Lines Deleted" type="number">
  Total de líneas de código sugeridas para eliminación por el chat con IA
</ResponseField>

<ResponseField name="Chat Accepted Lines Added" type="number">
  Líneas sugeridas por IA que el usuario aceptó y añadió a su código
</ResponseField>

<ResponseField name="Chat Accepted Lines Deleted" type="number">
  Eliminaciones sugeridas por IA que el usuario aceptó
</ResponseField>

<div id="feature-usage-metrics">
  ### Métricas de uso de funcionalidades
</div>

<ResponseField name="Chat Total Applies" type="number">
  Veces que un usuario aplicó cambios generados por IA desde el chat
</ResponseField>

<ResponseField name="Chat Total Accepts" type="number">
  Veces que un usuario aceptó sugerencias de IA
</ResponseField>

<ResponseField name="Chat Total Rejects" type="number">
  Veces que un usuario rechazó sugerencias de IA
</ResponseField>

<ResponseField name="Chat Tabs Shown" type="number">
  Veces que se mostraron al usuario pestañas de sugerencias de IA
</ResponseField>

<ResponseField name="Tabs Accepted" type="number">
  Pestañas de sugerencias de IA aceptadas por el usuario
</ResponseField>

<div id="request-type-metrics">
  ### Métricas por tipo de solicitud
</div>

<ResponseField name="Edit Requests" type="number">
  Solicitudes realizadas a través de la función de composer/edición (Cmd+K ediciones en línea)
</ResponseField>

<ResponseField name="Ask Requests" type="number">
  Solicitudes de chat donde los usuarios hicieron preguntas a la IA
</ResponseField>

<ResponseField name="Agent Requests" type="number">
  Solicitudes realizadas a agentes de IA (asistentes de IA especializados)
</ResponseField>

<ResponseField name="Cmd+K Usages" type="number">
  Veces que se usó la paleta de comandos Cmd+K (o Ctrl+K)
</ResponseField>

<div id="subscription-and-api-metrics">
  ### Métricas de suscripción y API
</div>

<ResponseField name="Subscription Included Reqs" type="number">
  Solicitudes a la IA cubiertas por el plan de suscripción del usuario
</ResponseField>

<ResponseField name="API Key Reqs" type="number">
  Solicitudes realizadas usando claves de API para acceso programático
</ResponseField>

<ResponseField name="Usage-Based Reqs" type="number">
  Solicitudes que computan para la facturación basada en uso
</ResponseField>

<div id="additional-features">
  ### Funcionalidades adicionales
</div>

<ResponseField name="Bugbot Usages" type="number">
  Veces que se usó la función de detección/corrección de errores con IA
</ResponseField>

<div id="configuration-information">
  ### Información de configuración
</div>

<ResponseField name="Most Used Model" type="string">
  El modelo de IA que el usuario usó con mayor frecuencia (p. ej., GPT-4, Claude)
</ResponseField>

<ResponseField name="Most Used Apply Extension" type="string">
  Extensión de archivo más usada al aplicar sugerencias de IA (p. ej., .ts,
  .py, .java)
</ResponseField>

<ResponseField name="Most Used Tab Extension" type="string">
  Extensión de archivo más usada con las funciones de autocompletado por pestañas
</ResponseField>

<ResponseField name="Client Version" type="string">
  Versión del editor Cursor en uso
</ResponseField>

<div id="calculated-metrics">
  ### Métricas calculadas
</div>

El informe también incluye datos procesados que ayudan a entender la contribución de código de la IA:

* Total de líneas agregadas/eliminadas: conteo bruto de todos los cambios de código
* Líneas aceptadas agregadas/eliminadas: líneas que se originaron en sugerencias de IA y fueron aceptadas
* Solicitudes del compositor: solicitudes realizadas a través de la función de compositor en línea
* Solicitudes de chat: solicitudes realizadas a través de la interfaz de chat

<Note>
  Todos los valores numéricos por defecto son 0 si no están presentes, los valores booleanos por defecto son false y los valores de cadena por defecto son cadenas vacías. Las métricas se agregan a nivel diario por usuario.
</Note>

---

← Previous: [API de seguimiento de código con IA](./api-de-seguimiento-de-cdigo-con-ia.md) | [Index](./index.md) | Next: [Analytics V2](./analytics-v2.md) →