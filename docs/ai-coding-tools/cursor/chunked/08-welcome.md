# Welcome

**Navigation:** [← Previous](./07-slack.md) | [Index](./index.md) | [Next →](./09-code-review.md)

---

# Welcome
Source: https://docs.cursor.com/en/welcome

Learn about Cursor and how to get started

Cursor is an AI-powered code editor that understands your codebase and helps you code faster through natural language. Just describe what you want to build or change and Cursor will generate the code for you.

<Frame>
  <img src="https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/welcome.png?fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=bf7bbe430ee044eea33a0ca66edf910d" className="rounded-lg" data-og-width="2000" width="2000" data-og-height="1275" height="1275" data-path="images/welcome.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/welcome.png?w=280&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=fa28a55e9896b15cbec778edf8597b5f 280w, https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/welcome.png?w=560&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=701e61d65b8f296aba427b3fe79d5360 560w, https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/welcome.png?w=840&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=8cf10e0727ab76689bc983e9d69d002f 840w, https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/welcome.png?w=1100&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=cddcb51dd8ccf60c6fc0b4135f3e6933 1100w, https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/welcome.png?w=1650&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=e2e9068dc6b3e9b81c4124e7736ecd8f 1650w, https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/welcome.png?w=2500&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=2bd03fc2dc3a340795c5bfa868b7d30b 2500w" />
</Frame>

<CardGroup cols={3}>
  <Card title="Get started" icon="rocket" href="/en/get-started/installation">
    <div>
      Download, install, and start building with Cursor in minutes
    </div>
  </Card>

  <Card title="Changelog" icon="sparkles" href="https://www.cursor.com/changelog">
    <div>
      Stay up to date with the latest features and improvements
    </div>
  </Card>

  <Card title="CLI" icon="terminal" href="/en/cli/overview">
    <div>
      Use Cursor in your terminal
    </div>
  </Card>

  <Card title="Concepts" icon="lightbulb" href="/en/get-started/concepts">
    <div>
      Understand core concepts and features that power Cursor
    </div>
  </Card>

  <Card title="Models" icon="brain" href="/en/models">
    <div>
      Explore AI models available and how to select the right one
    </div>
  </Card>

  <Card title="Guides" icon="book" href="/en/guides/working-with-context">
    <div>
      Learn best practices and workflows for different use cases
    </div>
  </Card>

  <Card title="Downloads" icon="download" href="https://cursor.com/downloads" arrow>
    <div>
      Get Cursor for your computer
    </div>
  </Card>

  <Card title="Forum" icon="message" href="https://forum.cursor.com">
    <div>
      For technical queries and to share experiences, visit our forum
    </div>
  </Card>

  <Card title="Support" icon="headset" href="mailto:hi@cursor.com">
    <div>
      For account and billing questions, email our support team
    </div>
  </Card>
</CardGroup>



# Seguridad del Agente
Source: https://docs.cursor.com/es/account/agent-security

Consideraciones de seguridad para usar Cursor Agent

La inyección de prompts, las alucinaciones de IA y otros problemas pueden hacer que la IA se comporte de formas inesperadas y potencialmente maliciosas. Mientras seguimos trabajando para resolver la inyección de prompts a un nivel más fundamental, nuestra protección principal en los productos de Cursor son los rieles de seguridad sobre lo que un agente puede hacer, incluyendo exigir aprobación manual para acciones sensibles de forma predeterminada. El objetivo de este documento es explicar estos rieles de seguridad y qué pueden esperar los usuarios de ellos.

Todos los controles y comportamientos a continuación son nuestra configuración predeterminada y recomendada.

<div id="first-party-tool-calls">
  ## Llamadas a herramientas nativas
</div>

Cursor viene con herramientas integradas que le permiten al agente ayudarte a escribir código. Estas incluyen lectura de archivos, edición, ejecución de comandos de terminal, búsqueda de documentación en la web y otras.

Las herramientas de lectura no requieren aprobación (p. ej., leer archivos, buscar en el código). Puedes usar [.cursorignore](/es/context/ignore-files) para bloquear por completo el acceso del agente a archivos específicos, pero en caso contrario las lecturas generalmente están permitidas sin aprobación. Para acciones que conllevan riesgo de exfiltración de datos sensibles, requerimos aprobación explícita.

Modificar archivos dentro del espacio de trabajo actual no requiere aprobación explícita con algunas excepciones. Cuando un agente realiza cambios en archivos, estos se guardan inmediatamente en disco. Recomendamos ejecutar Cursor en espacios de trabajo con control de versiones, de modo que el contenido de los archivos pueda revertirse en cualquier momento. Requerimos aprobación explícita antes de cambiar archivos que modifiquen la configuración de nuestro IDE/CLI, como el archivo de configuración del espacio de trabajo del editor. Sin embargo, si tienes recarga automática al detectar cambios en archivos, ten en cuenta que los cambios del agente pueden activar ejecuciones automáticas antes de que hayas tenido oportunidad de revisarlos.

Cualquier comando de terminal sugerido por los agentes requiere aprobación de forma predeterminada. Recomendamos revisar cada comando antes de que el agente lo ejecute. Quienes acepten el riesgo pueden habilitar que el agente ejecute todos los comandos sin aprobación. Incluimos una [allowlist](/es/agent/tools) en Cursor, pero no la consideramos un control de seguridad. Algunas personas eligen permitir comandos específicos, pero es un sistema de mejor esfuerzo y pueden existir formas de eludirlo. No recomendamos "Run Everything", que omite cualquier allowlist configurada.

<div id="third-party-tool-calls">
  ## Llamadas a herramientas de terceros
</div>

Cursor permite conectar herramientas externas a través de [MCP](/es/context/mcp). Todas las conexiones MCP de terceros deben ser aprobadas explícitamente por el usuario. Una vez que el usuario aprueba un MCP, de forma predeterminada cada llamada de herramienta sugerida en Agent Mode para cualquier integración MCP externa debe ser aprobada explícitamente antes de su ejecución.

<div id="network-requests">
  ## Solicitudes de red
</div>

Un atacante podría usar las solicitudes de red para exfiltrar datos. Actualmente no admitimos que herramientas propias realicen solicitudes de red fuera de un conjunto muy selecto de hosts (p. ej., GitHub), la recuperación explícita de enlaces ni el uso de la búsqueda web más que con un conjunto selecto de proveedores. Con la configuración predeterminada se impiden las solicitudes de red arbitrarias por parte de agentes.

<div id="workspace-trust">
  ## Confianza del espacio de trabajo
</div>

El IDE de Cursor admite la función estándar de [workspace trust](https://code.visualstudio.com/docs/editing/workspaces/workspace-trust), que está *desactivada* de forma predeterminada. Workspace trust te muestra un aviso al abrir un nuevo espacio de trabajo para elegir entre modo normal o restringido. El modo restringido inutiliza la IA y otras funciones por las que normalmente usas Cursor. Te recomendamos usar otras herramientas, como un editor de texto básico, para trabajar con repos en los que no confíes.

Puedes habilitar workspace trust en la configuración de usuario siguiendo estos pasos:

1. Abre tu archivo de usuario settings.json
2. Agrega la siguiente configuración:
   ```json  theme={null}
   "security.workspace.trust.enabled": true
   ```

Esta configuración también puede aplicarse a nivel de organización mediante soluciones de Mobile Device Management (MDM).

<div id="responsible-disclosure">
  ## Divulgación responsable
</div>

Si crees que has encontrado una vulnerabilidad en Cursor, sigue la guía en nuestra página de seguridad de GitHub y envía el informe ahí. Si no puedes usar GitHub, también puedes escribirnos a [security@cursor.com](mailto:security@cursor.com).

Nos comprometemos a acusar recibo de los informes de vulnerabilidades en un plazo de 5 días hábiles y a resolverlos tan pronto como podamos. Publicaremos los resultados en forma de avisos de seguridad en nuestra página de seguridad de GitHub. Los incidentes críticos se comunicarán tanto en la página de seguridad de GitHub como por correo electrónico a todos los usuarios.



# Facturación
Source: https://docs.cursor.com/es/account/billing

Gestión de suscripciones, reembolsos y facturas de Cursor

<div id="how-do-i-access-billing-settings">
  ### How do I access billing settings?
</div>

Accede al portal de facturación desde el [Dashboard](https://cursor.com/dashboard) haciendo clic en "Billing" en tu dashboard. Se abrirá un portal seguro para todas las tareas de facturación.

<div id="what-are-cursors-billing-cycles">
  ### What are Cursor's billing cycles?
</div>

Los ciclos de facturación pueden ser mensuales o anuales y comienzan en la fecha de tu suscripción. Las cuentas de Teams se cobran por asiento, con prorrateo para miembros nuevos.

<div id="how-do-seats-work-for-teams-accounts">
  ### How do seats work for Teams accounts?
</div>

Las cuentas de Teams cobran por asiento (uno por cada miembro del equipo). Si agregas miembros a mitad de ciclo, solo se te cobra por el tiempo restante. Si un miembro ha usado créditos y lo quitas, su asiento permanece ocupado hasta el final del ciclo de facturación; no hay reembolsos prorrateados. Los administradores del equipo pueden gestionar los asientos desde el dashboard.

<div id="can-i-switch-between-monthly-and-annual-billing">
  ### Can I switch between monthly and annual billing?
</div>

¡Sí! Así es cómo:

**Pro plan**

1. Ve al [dashboard](https://cursor.com/dashboard) de Cursor
2. Haz clic en "Billing and Invoices" en la barra lateral izquierda para ir a la página de facturación
3. Haz clic en "Manage subscription"
4. Haz clic en "Update subscription"
5. Selecciona "Yearly" o "Monthly" y luego haz clic en "Continue"

**Teams plan**

1. Ve al [dashboard](https://cursor.com/dashboard) de Cursor
2. Haz clic en "Billing and Invoices" en la barra lateral izquierda para ir a la página de facturación
3. Haz clic en el botón "Upgrade Now" para cambiar a facturación anual

<Note>
  Solo puedes cambiar de facturación mensual a anual por tu cuenta. Para cambiar de anual a mensual, contáctanos en
  [hi@cursor.com](mailto:hi@cursor.com).
</Note>

<div id="where-can-i-find-my-invoices">
  ### Where can I find my invoices?
</div>

Encuentra todo tu historial de facturación en el portal de facturación. Puedes ver y descargar facturas actuales y pasadas.

<div id="can-i-get-invoices-automatically-emailed-to-me">
  ### Can I get invoices automatically emailed to me?
</div>

Las facturas deben descargarse manualmente desde el portal de facturación. Estamos desarrollando el envío automático por email. Podrás activar la opción cuando esté disponible.

<div id="how-do-i-update-my-billing-information">
  ### How do I update my billing information?
</div>

Actualiza el método de pago, el nombre de la empresa, la dirección y la información fiscal desde el portal de facturación. Usamos Stripe para transacciones seguras. Los cambios solo afectan a facturas futuras; no podemos modificar facturas anteriores.

<div id="how-do-i-cancel-my-subscription">
  ### How do I cancel my subscription?
</div>

Cancela tu suscripción desde la página "Billing and Invoices" haciendo clic en "Manage Subscription" y luego en el botón "Cancel subscription". Seguirás teniendo acceso hasta el final de tu período de facturación actual.

<div id="im-having-other-billing-issues-how-can-i-get-help">
  ### I'm having other billing issues. How can I get help?
</div>

Para consultas de facturación no cubiertas aquí, envía un email a [hi@cursor.com](mailto:hi@cursor.com) desde el email asociado a tu cuenta. Incluye los detalles de tu cuenta y tus inquietudes.



# Precios
Source: https://docs.cursor.com/es/account/pricing

Los planes de Cursor y sus precios

Podés probar Cursor gratis o comprar un plan individual o de equipo.

<div id="individual">
  ## Individual
</div>

Todos los planes individuales incluyen:

* Autocompletados en pestañas ilimitados
* Límites ampliados de uso de agentes en todos los modelos
* Acceso a Bugbot
* Acceso a Background Agents

Cada plan incluye uso facturado según los precios de inferencia del modelo [API prices](/es/models#model-pricing):

* Pro incluye \$20 de uso de API de agentes + uso adicional de bonificación
* Pro Plus incluye \$70 de uso de API de agentes + uso adicional de bonificación
* Ultra incluye \$400 de uso de API de agentes + uso adicional de bonificación

Trabajamos mucho para otorgar capacidad de bonificación adicional más allá del uso incluido garantizado. Como distintos modelos tienen diferentes costos de API, la selección de modelo afecta la salida de tokens y qué tan rápido se consume tu uso incluido. Puedes ver el uso y los desgloses de tokens en [tu panel](https://cursor.com/dashboard?tab=usage). Las notificaciones de límite se muestran de forma habitual en el editor.

<img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/usage-limits.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=c42b8ad6347f6fe9d075647dfece934c" alt="Límites de uso" style={{ borderRadius: 16 }} data-og-width="666" width="666" data-og-height="394" height="394" data-path="images/account/usage-limits.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/usage-limits.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=e1ca3b5ab64a6ba6f3ad7d75b1ee72e2 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/usage-limits.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=d39dc254e7d059ac24310f26ea47dd5d 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/usage-limits.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=153472f14b4c10ec9a096b7a9db59888 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/usage-limits.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=0dc8b0cdb5c0677e45c1a082d0002880 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/usage-limits.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=cf4ac9875f5e587d16d4c6f1e7fdc057 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/usage-limits.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=13f21676cda8e4c2973bc3371892f4aa 2500w" />

<div id="how-much-usage-do-i-need">
  ### ¿Cuánto uso necesito?
</div>

Según nuestros datos de uso, puedes esperar los siguientes niveles:

* **Usuarios que usan Tab a diario**: Siempre se mantienen dentro de \$20
* **Usuarios con uso limitado de Agent**: A menudo se mantienen dentro de los \$20 incluidos
* **Usuarios que usan Agent a diario**: Normalmente $60–$100/mes de uso total
* **Usuarios avanzados (varios agents/automatización)**: A menudo \$200+/mes de uso total

Según nuestros datos de uso, los límites son aproximadamente equivalentes a lo siguiente para un *usuario mediano*:

* Pro: \~225 solicitudes de Sonnet 4, \~550 solicitudes de Gemini o \~500 solicitudes de GPT 5
* Pro+: \~675 solicitudes de Sonnet 4, \~1,650 solicitudes de Gemini o \~1,500 solicitudes de GPT 5
* Ultra: \~4,500 solicitudes de Sonnet 4, \~11,000 solicitudes de Gemini o \~10,000 solicitudes de GPT 5

<div id="what-happens-when-i-reach-my-limit">
  ### ¿Qué pasa cuando llego a mi límite?
</div>

Cuando superes tu uso mensual incluido, vas a recibir una notificación en el editor y podés elegir:

* **Agregar uso bajo demanda**: Seguí usando Cursor a las mismas tarifas de API con facturación por consumo
* **Actualizar tu plan**: Pasá a un nivel superior para tener más uso incluido

El uso bajo demanda se factura mensualmente a las mismas tarifas que tu uso incluido. Las solicitudes nunca se degradan en calidad ni velocidad.

<div id="teams">
  ## Teams
</div>

Hay dos planes para equipos: Teams (\$40/usuario/mes) y Enterprise (Personalizado).

Los planes de Teams incluyen funciones adicionales como:

* Aplicación del Privacy Mode
* Panel de administración con estadísticas de uso
* Facturación centralizada del equipo
* SSO con SAML/OIDC

Recomendamos Teams para cualquier cliente que esté cómodo autoatendiéndose. Recomendamos [Enterprise](/es/contact-sales) para clientes que necesiten soporte prioritario, uso compartido, facturación, SCIM o controles de seguridad avanzados.

Obtén más información sobre los [precios de Teams](/es/account/teams/pricing).

<div id="auto">
  ## Auto
</div>

Activar Auto permite que Cursor elija el modelo premium más adecuado para la tarea inmediata y con la mayor fiabilidad según la demanda actual. Esta función puede detectar una degradación en el rendimiento de salida y cambiar de modelo automáticamente para solucionarlo.

<Frame>
  <img src="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/models/model-picker.png?fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=9f039569ed0dc2ad7e02bb1b2e9cea71" data-og-width="2256" width="2256" data-og-height="1248" height="1248" data-path="images/models/model-picker.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/models/model-picker.png?w=280&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=49c6a091945972253eb6e819593e45f0 280w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/models/model-picker.png?w=560&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=f9bddfb2e130789d8d51a3d1a4eeba94 560w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/models/model-picker.png?w=840&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=db7273f399bb5decfed9d1b06f389df4 840w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/models/model-picker.png?w=1100&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=920fe98d4f99b5d7fddd47a14fb45699 1100w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/models/model-picker.png?w=1650&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=3b049686e5826263800b63299f4c19ca 1650w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/models/model-picker.png?w=2500&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=72ddd56b4d3ea9b2efa4001a155566fd 2500w" />
</Frame>

<Note>Hemos invertido mucho en la calidad y el rendimiento general de Auto. A partir de tu próxima renovación de facturación después del 15 de septiembre, Auto consumirá a las siguientes tarifas de API.</Note>

* **Input + Cache Write**: \$1.25 por 1M de tokens
* **Output**: \$6.00 por 1M de tokens
* **Cache Read**: \$0.25 por 1M de tokens

Tanto el editor como el panel mostrarán tu consumo, que incluye Auto. Si prefieres seleccionar un modelo directamente, el consumo se cobrará al precio de lista de la API de ese modelo.

<div id="max-mode">
  ## Modo Max
</div>

Algunos modelos pueden usar [Max Mode](/es/models#max-mode), lo que permite razonamientos más extensos y ventanas de contexto más grandes, de hasta 1M tokens. Aunque la mayoría de las tareas de programación no necesitan usar Max Mode, puede ser útil para consultas más complejas, especialmente con archivos o codebases grandes. Usar Max Mode consumirá más cuota. Puedes ver todas las solicitudes y el desglose de tokens en [tu panel](https://cursor.com/dashboard?tab=usage).

<div id="bugbot">
  ## Bugbot
</div>

Bugbot es un producto independiente de las suscripciones de Cursor y tiene su propio plan de precios.

* **Pro** (40 \$/mes): Revisiones ilimitadas en hasta 200 PR/mes, acceso ilimitado a Cursor Ask, integración con Cursor para corregir bugs y acceso a Bugbot Rules
* **Teams** (40 \$/usuario/mes): Revisiones de código ilimitadas en todos los PR, acceso ilimitado a Cursor Ask, uso compartido entre tu equipo y reglas y configuraciones avanzadas
* **Enterprise** (Personalizado): Todo lo de Teams, más analíticas y reportes avanzados, soporte prioritario y gestión de cuentas

Más información sobre los [precios de Bugbot](https://cursor.com/bugbot#pricing).

<div id="background-agent">
  ## Agente en segundo plano
</div>

Los agentes en segundo plano se cobran según los precios de la API para el [modelo](/es/models) seleccionado. Cuando empieces a usarlos por primera vez, se te pedirá que establezcas un límite de gasto para los agentes en segundo plano.

<Info>
  El cómputo de la máquina virtual (VM) para agentes en segundo plano se tarificará en el futuro.
</Info>



# Admin API
Source: https://docs.cursor.com/es/account/teams/admin-api

Accedé a métricas del equipo, datos de uso e información de gastos vía API

La Admin API te permite acceder de forma programática a los datos de tu equipo, incluyendo información de miembros, métricas de uso y detalles de gastos. Creá dashboards personalizados, herramientas de monitoreo o integrá con tus workflows existentes.

<Note>
  La API está en su primera versión. Estamos ampliando capacidades según el feedback: ¡contanos qué endpoints necesitás!
</Note>

<div id="authentication">
  ## Autenticación
</div>

Todas las solicitudes a la API requieren autenticación con una clave de API. Solo los administradores del equipo pueden crear y gestionar claves de API.

Las claves de API están vinculadas a la organización, son visibles para todos los administradores y no se ven afectadas por el estado de la cuenta de quien las creó originalmente.

<div id="creating-an-api-key">
  ### Crear una clave de API
</div>

1. Ve a **cursor.com/dashboard** → pestaña **Settings** → **Cursor Admin API Keys**
2. Haz clic en **Create New API Key**
3. Dale a tu clave un nombre descriptivo (p. ej., "Integración del panel de uso")
4. Copia la clave generada de inmediato: no la volverás a ver

Formato: `key_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`

<div id="using-your-api-key">
  ### Usar tu clave de API
</div>

Usa tu clave de API como nombre de usuario en la autenticación básica:

**Usar curl con autenticación básica:**

```bash  theme={null}
curl https://api.cursor.com/{route} -u API_KEY:
```

**O bien establece directamente el encabezado Authorization:**

```bash  theme={null}
Authorization: Basic {base64_encode('API_KEY:')}
```

<div id="base-url">
  ## URL base
</div>

Todos los endpoints de la API utilizan:

```
https://api.cursor.com
```

<div id="endpoints">
  ## Endpoints
</div>

<div id="get-team-members">
  ### Obtener miembros del equipo
</div>

Obtén todos los miembros del equipo y sus detalles.

```
GET /teams/members
```

#### Respuesta

Devuelve un array de objetos de miembros del equipo:

```typescript  theme={null}
{
  teamMembers: {
    name: string;
    email: string;
    role: 'owner' | 'member' | 'free-owner';
  }[];
}
```

#### Respuesta de ejemplo

```json  theme={null}
{
  "teamMembers": [
    {
      "name": "Alex",
      "email": "developer@company.com",
      "role": "miembro"
    },
    {
      "name": "Sam",
      "email": "admin@company.com",
      "role": "dueño"
    }
  ]
}

```

#### Ejemplo de solicitud

```bash  theme={null}
curl -X GET https://api.cursor.com/teams/members \
  -u TU_CLAVE_API:
```

<div id="get-daily-usage-data">
  ### Obtener datos de uso diario
</div>

Obtén métricas diarias detalladas para tu equipo en un rango de fechas. Ofrece información sobre ediciones de código, uso de la IA de asistencia y tasas de aceptación.

```
POST /teams/uso-diario
```

#### Cuerpo de la solicitud

<div className="full-width-table">
  | Parámetro   | Tipo   | Requerido | Descripción                              |
  | :---------- | :----- | :-------- | :--------------------------------------- |
  | `startDate` | number | Sí        | Fecha de inicio en milisegundos de época |
  | `endDate`   | number | Sí        | Fecha de fin en milisegundos de época    |
</div>

<Note>
  El rango de fechas no puede superar los 90 días. Haz varias solicitudes para periodos más largos.
</Note>

#### Respuesta

```typescript  theme={null}
{
  data: {
    date: number;
    isActive: boolean;
    totalLinesAdded: number;
    totalLinesDeleted: number;
    acceptedLinesAdded: number;
    acceptedLinesDeleted: number;
    totalApplies: number;
    totalAccepts: number;
    totalRejects: number;
    totalTabsShown: number;
    totalTabsAccepted: number;
    composerRequests: number;
    chatRequests: number;
    agentRequests: number;
    cmdkUsages: number;
    subscriptionIncludedReqs: number;
    apiKeyReqs: number;
    usageBasedReqs: number;
    bugbotUsages: number;
    mostUsedModel: string;
    applyMostUsedExtension?: string;
    tabMostUsedExtension?: string;
    clientVersion?: string;
    email?: string;
  }[];
  period: {
    startDate: number;
    endDate: number;
  };
}
```

<div id="response-fields">
  #### Campos de respuesta
</div>

<div className="full-width-table">
  | Field                      | Description                                      |
  | :------------------------- | :----------------------------------------------- |
  | `date`                     | Fecha en milisegundos desde la época (epoch)     |
  | `isActive`                 | Usuario activo ese día                           |
  | `totalLinesAdded`          | Líneas de código añadidas                        |
  | `totalLinesDeleted`        | Líneas de código eliminadas                      |
  | `acceptedLinesAdded`       | Líneas añadidas de sugerencias de IA aceptadas   |
  | `acceptedLinesDeleted`     | Líneas eliminadas de sugerencias de IA aceptadas |
  | `totalApplies`             | Operaciones de apply                             |
  | `totalAccepts`             | Sugerencias aceptadas                            |
  | `totalRejects`             | Sugerencias rechazadas                           |
  | `totalTabsShown`           | Autocompletados por tab mostrados                |
  | `totalTabsAccepted`        | Autocompletados por tab aceptados                |
  | `composerRequests`         | Solicitudes del Composer                         |
  | `chatRequests`             | Solicitudes de chat                              |
  | `agentRequests`            | Solicitudes del agente                           |
  | `cmdkUsages`               | Usos de la paleta de comandos (Cmd+K)            |
  | `subscriptionIncludedReqs` | Solicitudes incluidas en la suscripción          |
  | `apiKeyReqs`               | Solicitudes con clave de API                     |
  | `usageBasedReqs`           | Solicitudes de pago por uso                      |
  | `bugbotUsages`             | Usos del detector de bugs                        |
  | `mostUsedModel`            | Modelo de IA más usado                           |
  | `applyMostUsedExtension`   | Extensión de archivo más usada en applies        |
  | `tabMostUsedExtension`     | Extensión de archivo más usada en tabs           |
  | `clientVersion`            | Versión de Cursor                                |
  | `email`                    | Correo electrónico del usuario                   |
</div>

#### Ejemplo de respuesta

```json  theme={null}
{
  "data": [
    {
      "date": 1710720000000,
      "isActive": true,
      "totalLinesAdded": 1543,
      "totalLinesDeleted": 892,
      "acceptedLinesAdded": 1102,
      "acceptedLinesDeleted": 645,
      "totalApplies": 87,
      "totalAccepts": 73,
      "totalRejects": 14,
      "totalTabsShown": 342,
      "totalTabsAccepted": 289,
      "composerRequests": 45,
      "chatRequests": 128,
      "agentRequests": 12,
      "cmdkUsages": 67,
      "subscriptionIncludedReqs": 180,
      "apiKeyReqs": 0,
      "usageBasedReqs": 5,
      "bugbotUsages": 3,
      "mostUsedModel": "gpt-4",
      "applyMostUsedExtension": ".tsx",
      "tabMostUsedExtension": ".ts",
      "clientVersion": "0.25.1",
      "email": "developer@company.com"
    },
    {
      "date": 1710806400000,
      "isActive": true,
      "totalLinesAdded": 2104,
      "totalLinesDeleted": 1203,
      "acceptedLinesAdded": 1876,
      "acceptedLinesDeleted": 987,
      "totalApplies": 102,
      "totalAccepts": 91,
      "totalRejects": 11,
      "totalTabsShown": 456,
      "totalTabsAccepted": 398,
      "composerRequests": 67,
      "chatRequests": 156,
      "agentRequests": 23,
      "cmdkUsages": 89,
      "subscriptionIncludedReqs": 320,
      "apiKeyReqs": 15,
      "usageBasedReqs": 0,
      "bugbotUsages": 5,
      "mostUsedModel": "claude-3-opus",
      "applyMostUsedExtension": ".py",
      "tabMostUsedExtension": ".py",
      "clientVersion": "0.25.1",
      "email": "developer@company.com"
    }
  ],
  "period": {
    "startDate": 1710720000000,
    "endDate": 1710892800000
  }
}
```

#### Ejemplo de petición

```bash  theme={null}
curl -X POST https://api.cursor.com/teams/daily-usage-data \
  -u YOUR_API_KEY: \
  -H "Content-Type: application/json" \
  -d '{
    "startDate": 1710720000000,
    "endDate": 1710892800000
  }'
```

<div id="get-spending-data">
  ### Obtener datos de gastos
</div>

Obtén la información de gastos del mes calendario actual con búsqueda, ordenación y paginación.

```
POST /teams/spend
```

#### Cuerpo de la solicitud

<div className="full-width-table">
  | Parámetro       | Tipo   | Requerido | Descripción                                                  |
  | :-------------- | :----- | :-------- | :----------------------------------------------------------- |
  | `searchTerm`    | string | No        | Busca en nombres de usuario y direcciones de correo          |
  | `sortBy`        | string | No        | Ordena por: `amount`, `date`, `user`. Predeterminado: `date` |
  | `sortDirection` | string | No        | Dirección de orden: `asc`, `desc`. Predeterminado: `desc`    |
  | `page`          | number | No        | Número de página (indexado desde 1). Predeterminado: `1`     |
  | `pageSize`      | number | No        | Resultados por página                                        |
</div>

#### Respuesta

```typescript  theme={null}
{
  teamMemberSpend: {
    spendCents: number;
    fastPremiumRequests: number;
    name: string;
    email: string;
    role: 'owner' | 'member' | 'free-owner';
    hardLimitOverrideDollars: number;
  }[];
  subscriptionCycleStart: number;
  totalMembers: number;
  totalPages: number;
}
```

<div id="response-fields">
  #### Campos de respuesta
</div>

<div className="full-width-table">
  | Campo                      | Descripción                                                   |
  | :------------------------- | :------------------------------------------------------------ |
  | `spendCents`               | Gasto total en centavos                                       |
  | `fastPremiumRequests`      | Solicitudes al modelo premium rápido                          |
  | `name`                     | Nombre del miembro                                            |
  | `email`                    | Correo electrónico del miembro                                |
  | `role`                     | Rol en el equipo                                              |
  | `hardLimitOverrideDollars` | Anulación del límite de gasto personalizado                   |
  | `subscriptionCycleStart`   | Inicio del ciclo de suscripción (milisegundos desde la época) |
  | `totalMembers`             | Total de miembros del equipo                                  |
  | `totalPages`               | Total de páginas                                              |
</div>

#### Ejemplo de respuesta

```json  theme={null}
{
  "teamMemberSpend": [
    {
      "spendCents": 2450,
      "fastPremiumRequests": 1250,
      "name": "Alex",
      "email": "developer@company.com",
      "role": "miembro",
      "hardLimitOverrideDollars": 100
    },
    {
      "spendCents": 1875,
      "fastPremiumRequests": 980,
      "name": "Sam",
      "email": "admin@company.com",
      "role": "propietario",
      "hardLimitOverrideDollars": 0
    },
  ],
  "subscriptionCycleStart": 1708992000000,
  "totalMembers": 15,
  "totalPages": 1
}
```

#### Solicitudes de ejemplo

**Datos básicos de gastos:**

```bash  theme={null}
curl -X POST https://api.cursor.com/teams/spend \
  -u YOUR_API_KEY: \
  -H "Content-Type: application/json" \
  -d '{}'
```

**Buscar a un usuario específico con paginación:**

```bash  theme={null}
curl -X POST https://api.cursor.com/teams/spend \
  -u YOUR_API_KEY: \
  -H "Content-Type: application/json" \
  -d '{
    "searchTerm": "alex@company.com",
    "page": 2,
    "pageSize": 25
  }'
```

<div id="get-usage-events-data">
  ### Obtener datos de eventos de uso
</div>

Obtén eventos de uso detallados para tu equipo con opciones completas de filtrado, búsqueda y paginación. Este endpoint ofrece información granular sobre llamadas individuales a la API, uso de modelos, consumo de tokens y costos.

```
POST /teams/filtered-usage-events
```

#### Cuerpo de la solicitud

<div className="full-width-table">
  | Parámetro   | Tipo   | Requerido | Descripción                                                |
  | :---------- | :----- | :-------- | :--------------------------------------------------------- |
  | `startDate` | number | No        | Fecha de inicio en milisegundos de época (epoch)           |
  | `endDate`   | number | No        | Fecha de fin en milisegundos de época (epoch)              |
  | `userId`    | number | No        | Filtrar por ID de usuario específico                       |
  | `page`      | number | No        | Número de página (con índice desde 1). Predeterminado: `1` |
  | `pageSize`  | number | No        | Cantidad de resultados por página. Predeterminado: `10`    |
  | `email`     | string | No        | Filtrar por correo electrónico del usuario                 |
</div>

#### Respuesta

```typescript  theme={null}
{
  totalUsageEventsCount: number;
  pagination: {
    numPages: number;
    currentPage: number;
    pageSize: number;
    hasNextPage: boolean;
    hasPreviousPage: boolean;
  };
  usageEvents: {
    timestamp: string;
    model: string;
    kind: string;
    maxMode: boolean;
    requestsCosts: number;
    isTokenBasedCall: boolean;
    tokenUsage?: {
      inputTokens: number;
      outputTokens: number;
      cacheWriteTokens: number;
      cacheReadTokens: number;
      totalCents: number;
    };
    isFreeBugbot: boolean;
    userEmail: string;
  }[];
  period: {
    startDate: number;
    endDate: number;
  };
}
```

<div id="response-fields">
  #### Campos de respuesta
</div>

<div className="full-width-table">
  | Campo                   | Descripción                                                              |
  | :---------------------- | :----------------------------------------------------------------------- |
  | `totalUsageEventsCount` | Número total de eventos de uso que coinciden con la consulta             |
  | `pagination`            | Metadatos de paginación para navegar los resultados                      |
  | `timestamp`             | Marca de tiempo del evento en milisegundos desde el epoch                |
  | `model`                 | Modelo de IA usado para la solicitud                                     |
  | `kind`                  | Categoría de uso (p. ej., "Usage-based", "Included in Business")         |
  | `maxMode`               | Si el modo máximo estaba habilitado                                      |
  | `requestsCosts`         | Costo en unidades de solicitud                                           |
  | `isTokenBasedCall`      | True cuando el evento se cobra como evento basado en uso                 |
  | `tokenUsage`            | Consumo detallado de tokens (disponible cuando isTokenBasedCall es true) |
  | `isFreeBugbot`          | Si fue un uso gratuito de bugbot                                         |
  | `userEmail`             | Correo del usuario que hizo la solicitud                                 |
  | `period`                | Rango de fechas de los datos consultados                                 |
</div>

#### Ejemplo de respuesta

```json  theme={null}
{
  "totalUsageEventsCount": 113,
  "pagination": {
    "numPages": 12,
    "currentPage": 1,
    "pageSize": 10,
    "hasNextPage": true,
    "hasPreviousPage": false
  },
  "usageEvents": [
    {
      "timestamp": "1750979225854",
      "model": "claude-4-opus",
      "kind": "Según uso",
      "maxMode": true,
      "requestsCosts": 5,
      "isTokenBasedCall": true,
      "tokenUsage": {
        "inputTokens": 126,
        "outputTokens": 450,
        "cacheWriteTokens": 6112,
        "cacheReadTokens": 11964,
        "totalCents": 20.18232
      },
      "isFreeBugbot": false,
      "userEmail": "developer@company.com"
    },
    {
      "timestamp": "1750979173824",
      "model": "claude-4-opus",
      "kind": "Según uso",
      "maxMode": true,
      "requestsCosts": 10,
      "isTokenBasedCall": true,
      "tokenUsage": {
        "inputTokens": 5805,
        "outputTokens": 311,
        "cacheWriteTokens": 11964,
        "cacheReadTokens": 0,
        "totalCents": 40.16699999999999
      },
      "isFreeBugbot": false,
      "userEmail": "developer@company.com"
    },
    {
      "timestamp": "1750978339901",
      "model": "claude-4-sonnet-thinking",
      "kind": "Incluido en Business"
      "maxMode": true,
      "requestsCosts": 1.4,
      "isTokenBasedCall": false,
      "isFreeBugbot": false,
      "userEmail": "admin@company.com"
    }
  ],
  "period": {
    "startDate": 1748411762359,
    "endDate": 1751003762359
  }
}
```

<div id="example-requests">
  #### Ejemplos de solicitudes
</div>

**Obtener todos los eventos de uso con la paginación por defecto:**

```bash  theme={null}
curl -X POST https://api.cursor.com/teams/filtered-usage-events \
  -u YOUR_API_KEY: \
  -H "Content-Type: application/json" \
  -d '{}'
```

**Filtrar por intervalo de fechas y usuario específico:**

```bash  theme={null}
curl -X POST https://api.cursor.com/teams/filtered-usage-events \
  -u YOUR_API_KEY: \
  -H "Content-Type: application/json" \
  -d '{
    "startDate": 1748411762359,
    "endDate": 1751003762359,
    "email": "developer@company.com",
    "page": 1,
    "pageSize": 25
  }'
```

**Obtén eventos de uso de un usuario específico con paginación personalizada:**

```bash  theme={null}
curl -X POST https://api.cursor.com/teams/filtered-usage-events \
  -u YOUR_API_KEY: \
  -H "Content-Type: application/json" \
  -d '{
    "userId": 12345,
    "page": 2,
    "pageSize": 50
  }'
```

<div id="set-user-spend-limit">
  ### Establecer límite de gasto por usuario
</div>

Establece límites de gasto para miembros específicos del equipo. Esto te permite controlar cuánto puede gastar cada usuario en uso de IA dentro de tu equipo.

```
POST /teams/user-spend-limit
```

<Note>
  **Limitación de frecuencia:** 60 solicitudes por minuto por equipo
</Note>

#### Cuerpo de la solicitud

<div className="full-width-table">
  | Parámetro           | Tipo   | Obligatorio | Descripción                                                       |
  | :------------------ | :----- | :---------- | :---------------------------------------------------------------- |
  | `userEmail`         | string | Sí          | Dirección de correo del miembro del equipo                        |
  | `spendLimitDollars` | number | Sí          | Límite de gasto en dólares (solo números enteros, sin decimales). |
</div>

<Note>
  * El usuario ya debe ser miembro de tu equipo
  * Solo se aceptan valores enteros (sin decimales)
  * Establecer `spendLimitDollars` en 0 fija el límite en \$0
</Note>

#### Respuesta

Devuelve una respuesta estandarizada que indica si hubo éxito o error:

```typescript  theme={null}
{
  outcome: 'success' | 'error';
  message: string;
}
```

<div id="example-responses">
  #### Respuestas de ejemplo
</div>

**Límite establecido correctamente:**

```json  theme={null}
{
  "outcome": "success",
  "message": "Límite de gasto configurado en $100 para el usuario developer@company.com"
}
```

**Respuesta de error:**

```json  theme={null}
{
  "outcome": "error",
  "message": "Formato de correo electrónico inválido"
}
```

<div id="example-requests">
  #### Ejemplos de solicitudes
</div>

**Configurar un límite de gasto:**

```bash  theme={null}
curl -X POST https://api.cursor.com/teams/user-spend-limit \
  -u TU_API_KEY: \
  -H "Content-Type: application/json" \
  -d '{
    "userEmail": "developer@company.com",
    "spendLimitDollars": 100
  }'
```

<div id="repo-blocklists-api">
  ### API de listas de bloqueo de repos
</div>

Agrega repos y usa patrones para evitar que archivos o directorios se indexen o se usen como contexto para tu equipo.

<div id="get-team-repo-blocklists">
  #### Obtener las blocklists de repos del equipo
</div>

Obtén todas las blocklists de repos configuradas para tu equipo.

```
GET /settings/repo-blocklists/repos
```

<div id="response">
  ##### Respuesta
</div>

Devuelve un array de objetos de lista de bloqueo del repositorio:

```typescript  theme={null}
{
  repos: {
    id: string;
    url: string;
    patterns: string[];
  }[];
}
```

<div id="example-response">
  ##### Ejemplo de respuesta
</div>

```json  theme={null}
{
  "repos": [
    {
      "id": "repo_123",
      "url": "https://github.com/company/sensitive-repo",
      "patterns": ["*.env", "config/*", "secrets/**"]
    },
    {
      "id": "repo_456",
      "url": "https://github.com/company/internal-tools",
      "patterns": ["*"]
    }
  ]
}
```

##### Ejemplo de petición

```bash  theme={null}
curl -X GET https://api.cursor.com/settings/repo-blocklists/repos \
  -u TU_CLAVE_API:
```

<div id="upsert-repo-blocklists">
  #### Upsert de listas de bloqueo de repos
</div>

Reemplaza las listas de bloqueo de repositorios existentes para los repos proporcionados.
*Nota: Este endpoint solo sobrescribirá los patrones de los repositorios proporcionados. Todos los demás repos no se verán afectados.*

```
POST /settings/repo-blocklists/repos/upsert
```

<div id="request-body">
  ##### Cuerpo de la solicitud
</div>

| Parámetro | Tipo  | Requerido | Descripción                                 |
| --------- | ----- | --------- | ------------------------------------------- |
| repos     | array | Sí        | Lista de objetos de bloqueo de repositorios |

Cada objeto de repositorio debe contener:

| Campo    | Tipo      | Requerido | Descripción                                                         |
| -------- | --------- | --------- | ------------------------------------------------------------------- |
| url      | string    | Sí        | URL del repositorio a bloquear                                      |
| patterns | string\[] | Sí        | Lista de patrones de archivos a bloquear (se admiten patrones glob) |

<div id="response">
  ##### Respuesta
</div>

Devuelve la lista actualizada de listas de bloqueo del repositorio:

```typescript  theme={null}
{
  repos: {
    id: string;
    url: string;
    patterns: string[];
  }[];
}
```

<div id="example-request">
  ##### Ejemplo de solicitud
</div>

```bash  theme={null}
curl -X POST https://api.cursor.com/settings/repo-blocklists/repos/upsert \
  -u TU_CLAVE_DE_API: \
  -H "Content-Type: application/json" \
  -d '{
    "repos": [
      {
        "url": "https://github.com/company/sensitive-repo",
        "patterns": ["*.env", "config/*", "secrets/**"]
      },
      {
        "url": "https://github.com/company/internal-tools", 
        "patterns": ["*"]
      }
    ]
  }'
```

<div id="delete-repo-blocklist">
  #### Eliminar la lista de bloqueo de repositorios
</div>

Quita un repositorio específico de la lista de bloqueo.

```
DELETE /settings/repo-blocklists/repos/:repoId
```

<div id="parameters">
  ##### Parámetros
</div>

| Parámetro | Tipo   | Obligatorio | Descripción                                                    |
| --------- | ------ | ----------- | -------------------------------------------------------------- |
| repoId    | string | Sí          | ID de la lista de bloqueo del repositorio que se va a eliminar |

<div id="response">
  ##### Respuesta
</div>

Devuelve 204 No Content si la eliminación se realiza correctamente.

##### Ejemplo de petición

```bash  theme={null}
curl -X DELETE https://api.cursor.com/settings/repo-blocklists/repos/repo_123 \
  -u TU_API_KEY:
```

<div id="pattern-examples">
  #### Ejemplos de patrones
</div>

Patrones comunes de la blocklist:

* `*` - Bloquear todo el repositorio
* `*.env` - Bloquear todos los archivos .env
* `config/*` - Bloquear todos los archivos del directorio config
* `**/*.secret` - Bloquear todos los archivos .secret en cualquier subdirectorio
* `src/api/keys.ts` - Bloquear un archivo específico



# API de seguimiento de código con IA
Source: https://docs.cursor.com/es/account/teams/ai-code-tracking-api

Accede a analíticas de código generadas por IA para los repositorios de tu equipo

Accede a analíticas de código generadas por IA para los repositorios de tu equipo. Incluye uso de IA por commit y cambios de IA aceptados a nivel granular.

<Note>
  La API está en su primera versión. Estamos ampliando funcionalidades según el feedback; ¡cuéntanos qué endpoints necesitas!
</Note>

* **Disponibilidad**: Solo para equipos Enterprise
* **Estado**: Alpha (las estructuras y los campos de la respuesta pueden cambiar)

<div id="authentication">
  ## Autenticación
</div>

Todas las solicitudes a la API requieren autenticación con una clave de API. Esta API usa el mismo método de autenticación del Admin API que otros endpoints.

Para ver instrucciones detalladas de autenticación, consulta [Autenticación del Admin API](/es/account/teams/admin-api#authentication).

<div id="base-url">
  ## URL base
</div>

Todas las rutas de la API usan:

```
https://api.cursor.com
```

<div id="rate-limits">
  ## Límites de uso
</div>

* 5 solicitudes por minuto por equipo y por endpoint

<div id="query-parameters">
  ## Parámetros de consulta
</div>

Todos los endpoints a continuación aceptan los mismos parámetros a través del query string:

<div className="full-width-table">
  | Parámetro   | Tipo   | Obligatorio | Descripción                                                                                                                                                                            |                                                                                                                              |
  | :---------- | :----- | :---------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
  | `startDate` | string | date        | No                                                                                                                                                                                     | Cadena de fecha ISO, el literal "now" o días relativos como "7d" (equivale a ahora - 7 días). Predeterminado: ahora - 7 días |
  | `endDate`   | string | date        | No                                                                                                                                                                                     | Cadena de fecha ISO, el literal "now" o días relativos como "0d". Predeterminado: ahora                                      |
  | `page`      | number | No          | Número de página (base 1). Predeterminado: 1                                                                                                                                           |                                                                                                                              |
  | `pageSize`  | number | No          | Resultados por página. Predeterminado: 100, máx.: 1000                                                                                                                                 |                                                                                                                              |
  | `user`      | string | No          | Filtro opcional por un único usuario. Acepta email (p. ej., [developer@company.com](mailto:developer@company.com)), ID codificado (p. ej., user\_abc123...) o ID numérico (p. ej., 42) |                                                                                                                              |
</div>

<Note>
  Las respuestas devuelven userId como un ID externo codificado con el prefijo user\_. Esto es estable para el consumo por API.
</Note>

<div id="semantics-and-how-metrics-are-computed">
  ## Semántica y cómo se calculan las métricas
</div>

* **Origen**: "TAB" representa las completions en línea aceptadas; "COMPOSER" representa diffs aceptados desde Composer
* **Métricas de líneas**: tabLinesAdded/Deleted y composerLinesAdded/Deleted se cuentan por separado; nonAiLinesAdded/Deleted se calculan como max(0, totalLines - AI lines)
* **Modo de privacidad**: Si está habilitado en el cliente, puede omitirse cierta metadata (como fileName)
* **Información de la rama**: isPrimaryBranch es true cuando la rama actual es igual a la rama predeterminada del repo; puede ser undefined si la info del repo no está disponible

Podés escanear ese archivo para entender cómo se detectan y reportan los commits y cambios.

<div id="endpoints">
  ## Endpoints
</div>

<div id="get-ai-commit-metrics-json-paginated">
  ### Obtener métricas de commits con IA (JSON, paginadas)
</div>

Obtén métricas agregadas por commit que atribuyen líneas a TAB, COMPOSER y no IA.

```
GET /analytics/ai-code/commits
```

<div id="response">
  #### Respuesta
</div>

```typescript  theme={null}
{
  items: MetricasDeCommitAI[];
  totalCount: number;
  page: number;
  pageSize: number;
}
```

<div id="aicommitmetric-fields">
  #### Campos de AiCommitMetric
</div>

<div className="full-width-table">
  | Campo                  | Tipo    | Descripción                                       |                                          |
  | :--------------------- | :------ | :------------------------------------------------ | ---------------------------------------- |
  | `commitHash`           | string  | Hash del commit de Git                            |                                          |
  | `userId`               | string  | ID de usuario codificado (p. ej., user\_abc123)   |                                          |
  | `userEmail`            | string  | Dirección de correo electrónico del usuario       |                                          |
  | `repoName`             | string  | null                                              | Nombre del repositorio                   |
  | `branchName`           | string  | null                                              | Nombre de la rama                        |
  | `isPrimaryBranch`      | boolean | null                                              | Indica si es la rama principal           |
  | `totalLinesAdded`      | number  | Total de líneas añadidas en el commit             |                                          |
  | `totalLinesDeleted`    | number  | Total de líneas eliminadas en el commit           |                                          |
  | `tabLinesAdded`        | number  | Líneas añadidas mediante autocompletado con TAB   |                                          |
  | `tabLinesDeleted`      | number  | Líneas eliminadas mediante autocompletado con TAB |                                          |
  | `composerLinesAdded`   | number  | Líneas añadidas mediante Composer                 |                                          |
  | `composerLinesDeleted` | number  | Líneas eliminadas mediante Composer               |                                          |
  | `nonAiLinesAdded`      | number  | null                                              | Líneas no generadas por IA añadidas      |
  | `nonAiLinesDeleted`    | number  | null                                              | Líneas no generadas por IA eliminadas    |
  | `message`              | string  | null                                              | Mensaje del commit                       |
  | `commitTs`             | string  | null                                              | Marca de tiempo del commit (formato ISO) |
  | `createdAt`            | string  | Marca de tiempo de ingesta (formato ISO)          |                                          |
</div>

<div id="example-response">
  #### Ejemplo de respuesta
</div>

```json  theme={null}
{
  "items": [
    {
      "commitHash": "a1b2c3d4",
      "userId": "user_3k9x8q...",
      "userEmail": "developer@company.com",
      "repoName": "company/repo",
      "branchName": "main",
      "isPrimaryBranch": true,
      "totalLinesAdded": 120,
      "totalLinesDeleted": 30,
      "tabLinesAdded": 50,
      "tabLinesDeleted": 10,
      "composerLinesAdded": 40,
      "composerLinesDeleted": 5,
      "nonAiLinesAdded": 30,
      "nonAiLinesDeleted": 15,
      "message": "Refactor: extraer cliente de analíticas",
      "commitTs": "2025-07-30T14:12:03.000Z",
      "createdAt": "2025-07-30T14:12:30.000Z"
    }
  ],
  "totalCount": 42,
  "page": 1,
  "pageSize": 100
}
```

<div id="example-requests">
  #### Ejemplos de solicitudes
</div>

**Solicitud básica:**

```bash  theme={null}
curl -X GET "https://api.cursor.com/analytics/ai-code/commits?startDate=7d&endDate=now&page=1&pageSize=100" \
  -u TU_API_KEY:
```

**Filtrar por usuario (correo):**

```bash  theme={null}
curl -X GET "https://api.cursor.com/analytics/ai-code/commits?startDate=2025-06-01T00:00:00Z&endDate=now&user=developer@company.com" \
  -u TU_API_KEY:
```

<div id="download-ai-commit-metrics-csv-streaming">
  ### Descargar métricas de commits con IA (CSV, streaming)
</div>

Descarga métricas de commits en formato CSV para extracciones de datos de gran volumen.

```
GET /analytics/ai-code/commits.csv
```

<div id="response">
  #### Respuesta
</div>

Encabezados:

* Content-Type: text/csv; charset=utf-8

<div id="csv-columns">
  #### Columnas del CSV
</div>

<div className="full-width-table">
  | Columna                  | Tipo    | Descripción                                  |
  | :----------------------- | :------ | :------------------------------------------- |
  | `commit_hash`            | string  | Hash del commit de Git                       |
  | `user_id`                | string  | ID de usuario codificado                     |
  | `user_email`             | string  | Dirección de correo electrónico del usuario  |
  | `repo_name`              | string  | Nombre del repositorio                       |
  | `branch_name`            | string  | Nombre de la rama                            |
  | `is_primary_branch`      | boolean | Si es la rama principal                      |
  | `total_lines_added`      | number  | Total de líneas añadidas en el commit        |
  | `total_lines_deleted`    | number  | Total de líneas eliminadas en el commit      |
  | `tab_lines_added`        | number  | Líneas añadidas con autocompletado por TAB   |
  | `tab_lines_deleted`      | number  | Líneas eliminadas con autocompletado por TAB |
  | `composer_lines_added`   | number  | Líneas añadidas con Composer                 |
  | `composer_lines_deleted` | number  | Líneas eliminadas con Composer               |
  | `non_ai_lines_added`     | number  | Líneas no generadas por IA añadidas          |
  | `non_ai_lines_deleted`   | number  | Líneas no generadas por IA eliminadas        |
  | `message`                | string  | Mensaje del commit                           |
  | `commit_ts`              | string  | Marca de tiempo del commit (formato ISO)     |
  | `created_at`             | string  | Marca de tiempo de ingesta (formato ISO)     |
</div>

#### Ejemplo de salida CSV

```csv  theme={null}
commit_hash,user_id,user_email,repo_name,branch_name,is_primary_branch,total_lines_added,total_lines_deleted,tab_lines_added,tab_lines_deleted,composer_lines_added,composer_lines_deleted,non_ai_lines_added,non_ai_lines_deleted,message,commit_ts,created_at
a1b2c3d4,user_3k9x8q...,developer@company.com,company/repo,main,true,120,30,50,10,40,5,30,15,"Refactor: extraer cliente de analítica",2025-07-30T14:12:03.000Z,2025-07-30T14:12:30.000Z
e5f6g7h8,user_3k9x8q...,developer@company.com,company/repo,feature-branch,false,85,15,30,5,25,3,30,7,"Añadir manejo de errores",2025-07-30T13:45:21.000Z,2025-07-30T13:45:45.000Z
```

<div id="example-request">
  #### Ejemplo de solicitud
</div>

```bash  theme={null}
curl -L "https://api.cursor.com/analytics/ai-code/commits.csv?startDate=2025-07-01T00:00:00Z&endDate=now&user=user_3k9x8q..." \
  -u TU_API_KEY: \
  -o commits.csv
```

<div id="get-ai-code-change-metrics-json-paginated">
  ### Obtener métricas de cambios de IA (JSON, paginadas)
</div>

Obtén cambios de IA aceptados a nivel granular, agrupados por un changeId determinista. Útil para analizar eventos de IA aceptados de forma independiente a los commits.

```
GET /analytics/ai-code/changes
```

<div id="response">
  #### Respuesta
</div>

```typescript  theme={null}
{
  items: MetricaCambioCodigoIA[];
  totalCount: number;
  page: number;
  pageSize: number;
}
```

<div id="aicodechangemetric-fields">
  #### Campos de AiCodeChangeMetric
</div>

<div className="full-width-table">
  | Campo               | Tipo   | Descripción                                                              |                                   |
  | :------------------ | :----- | :----------------------------------------------------------------------- | --------------------------------- |
  | `changeId`          | string | ID determinista del cambio                                               |                                   |
  | `userId`            | string | ID de usuario codificado (p. ej., user\_abc123)                          |                                   |
  | `userEmail`         | string | Dirección de correo del usuario                                          |                                   |
  | `source`            | "TAB"  | "COMPOSER"                                                               | Origen del cambio generado por IA |
  | `model`             | string | null                                                                     | Modelo de IA usado                |
  | `totalLinesAdded`   | number | Total de líneas añadidas                                                 |                                   |
  | `totalLinesDeleted` | number | Total de líneas eliminadas                                               |                                   |
  | `createdAt`         | string | Marca de tiempo de ingesta (formato ISO)                                 |                                   |
  | `metadata`          | Array  | Metadatos del archivo (fileName puede omitirse en el modo de privacidad) |                                   |
</div>

#### Respuesta de ejemplo

```json  theme={null}
{
  "items": [
    {
      "changeId": "749356201",
      "userId": "user_3k9x8q...",
      "userEmail": "developer@company.com",
      "source": "COMPOSER",
      "model": null,
      "totalLinesAdded": 18,
      "totalLinesDeleted": 4,
      "createdAt": "2025-07-30T15:10:12.000Z",
      "metadata": [
        { "fileName": "src/analytics/report.ts", "fileExtension": "ts", "linesAdded": 12, "linesDeleted": 3 },
        { "fileName": "src/analytics/ui.tsx", "fileExtension": "tsx", "linesAdded": 6, "linesDeleted": 1 }
      ]
    }
  ],
  "totalCount": 128,
  "page": 1,
  "pageSize": 200
}
```

<div id="example-requests">
  #### Ejemplos de solicitudes
</div>

**Solicitud básica:**

```bash  theme={null}
curl -X GET "https://api.cursor.com/analytics/ai-code/changes?startDate=14d&endDate=now&page=1&pageSize=200" \
  -u TU_API_KEY:
```

**Filtrar por usuario (ID codificado):**

```bash  theme={null}
curl -X GET "https://api.cursor.com/analytics/ai-code/changes?user=user_3k9x8q..." \
  -u TU_API_KEY:
```

**Filtrar por usuario (correo):**

```bash  theme={null}
curl -X GET "https://api.cursor.com/analytics/ai-code/changes?user=developer@company.com" \
  -u TU_CLAVE_DE_API:
```

<div id="download-ai-code-change-metrics-csv-streaming">
  ### Descargar métricas de cambios de código con IA (CSV, streaming)
</div>

Descarga métricas de cambios en formato CSV para extracciones de datos a gran escala.

```
GET /analytics/ai-code/changes.csv
```

<div id="response">
  #### Respuesta
</div>

Encabezados:

* Content-Type: text/csv; charset=utf-8

<div id="csv-columns">
  #### Columnas del CSV
</div>

<div className="full-width-table">
  | Columna               | Tipo   | Descripción                                          |
  | :-------------------- | :----- | :--------------------------------------------------- |
  | `change_id`           | string | ID determinista del cambio                           |
  | `user_id`             | string | ID de usuario codificado                             |
  | `user_email`          | string | Dirección de correo del usuario                      |
  | `source`              | string | Origen del cambio de IA (TAB o COMPOSER)             |
  | `model`               | string | Modelo de IA utilizado                               |
  | `total_lines_added`   | number | Total de líneas agregadas                            |
  | `total_lines_deleted` | number | Total de líneas eliminadas                           |
  | `created_at`          | string | Marca de tiempo de ingesta (formato ISO)             |
  | `metadata_json`       | string | Arreglo de entradas de metadatos serializado en JSON |
</div>

<div id="notes">
  #### Notas
</div>

* metadata\_json es un arreglo de entradas de metadatos serializado en JSON (puede omitir fileName en modo de privacidad)
* Al consumir CSV, asegúrate de analizar los campos entre comillas

<div id="sample-csv-output">
  #### Salida de ejemplo en CSV
</div>

```csv  theme={null}
change_id,user_id,user_email,source,model,total_lines_added,total_lines_deleted,created_at,metadata_json
749356201,user_3k9x8q...,developer@company.com,COMPOSER,gpt-4o,18,4,2025-07-30T15:10:12.000Z,"[{""fileName"":""src/analytics/report.ts"",""fileExtension"":""ts"",""linesAdded"":12,""linesDeleted"":3},{""fileName"":""src/analytics/ui.tsx"",""fileExtension"":""tsx"",""linesAdded"":6,""linesDeleted"":1}]"
749356202,user_3k9x8q...,developer@company.com,TAB,,8,2,2025-07-30T15:08:45.000Z,"[{""fileName"":""src/utils/helpers.ts"",""fileExtension"":""ts"",""linesAdded"":8,""linesDeleted"":2}]"
```

<div id="example-request">
  #### Ejemplo de solicitud
</div>

```bash  theme={null}
curl -L "https://api.cursor.com/analytics/ai-code/changes.csv?startDate=30d&endDate=now" \
  -u TU_API_KEY: \
  -o changes.csv
```

<div id="tips">
  ## Consejos
</div>

* Usa el parámetro `user` para filtrar rápido a un solo usuario en todos los endpoints
* Para extracciones de datos grandes, prefiere los endpoints CSV: hacen streaming en páginas de 10.000 registros del lado del servidor
* `isPrimaryBranch` puede ser `undefined` si el cliente no pudo resolver la rama predeterminada
* `commitTs` es la marca de tiempo del commit; `createdAt` es la hora de ingesta en nuestros servidores
* Algunos campos pueden estar ausentes cuando el modo de privacidad está habilitado en el cliente

<div id="changelog">
  ## Registro de cambios
</div>

* **Versión alfa**: Endpoints iniciales para commits y cambios. Las formas de las respuestas pueden evolucionar según el feedback



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



# Analytics V2
Source: https://docs.cursor.com/es/account/teams/analyticsV2

Seguimiento avanzado de métricas de uso y actividad del equipo

Estamos trabajando en el lanzamiento de la V2 de nuestra infraestructura de analytics. Esto incluye un refactor de cómo rastreamos varias métricas.

A partir del **1 de septiembre de 2025**, y para usuarios en **Cursor versión 1.5**, analytics utilizará nuestra infraestructura V2. Las versiones anteriores habrían infracontabilizado varias métricas, incluidas:

* Total de líneas de código aceptadas
* Total de líneas de código sugeridas
* Total de pestañas aceptadas

Mantente al tanto mientras seguimos invirtiendo en analytics y lanzando nuevas funciones en este espacio.



# Panel
Source: https://docs.cursor.com/es/account/teams/dashboard

Administra la facturación, el uso y la configuración del equipo desde tu panel

El panel te permite acceder a la facturación, configurar precios basados en uso y administrar tu equipo.

<div id="overview">
  ## Resumen
</div>

Obtén un resumen rápido de la actividad de tu equipo, las estadísticas de uso y los cambios recientes. La página de resumen ofrece una visión general inmediata de tu espacio de trabajo.

<Frame>
  <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/dashboard.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=48ee98a4d9b168b93c26a03c1af74ddd" data-og-width="3456" width="3456" data-og-height="1944" height="1944" data-path="images/account/team/dashboard.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/dashboard.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=2ac6f157659354866eaa03b38cd1eb90 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/dashboard.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=8e9e84e894a3faf2846e3aae5deb9a2b 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/dashboard.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=e1034c739d961ccc69c17ba947edda90 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/dashboard.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=dbeed5506f7ae3fc4fabc7d248d69e64 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/dashboard.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=afac07ce763fccf7eded7248fb990745 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/dashboard.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=c4ed8c8161c3f2a964371a237134b1ae 2500w" />
</Frame>

<div id="settings">
  ## Configuración
</div>

<Frame>
  <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/settings.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=5edb18df1ddc2d20e69abdd83140a509" data-og-width="1390" width="1390" data-og-height="913" height="913" data-path="images/account/team/settings.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/settings.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=4d4c8f244231868bf4111f05b1f46c93 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/settings.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=582ddf5415a973010e3bcbeeb13d4f64 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/settings.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=74a5d5f4644b701adc25b6d847f5752e 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/settings.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=9250830c64e8c3490c3ca6f7b6f65eec 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/settings.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=7ce96a620ac6d447e79abd901b5c6cdc 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/settings.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=6d24738577e0ffd837d87f8926339215 2500w" />
</Frame>

Configura las preferencias y la seguridad de todo el equipo. La página de configuración incluye:

<div id="teams-enterprise-settings">
  ## Configuración de Teams y Enterprise
</div>

<AccordionGroup>
  <Accordion title="Privacy Settings">
    Controla las preferencias de uso compartido de datos de tu equipo. Configura políticas de retención cero con proveedores de IA (OpenAI, Anthropic, Google Vertex AI, xAI Grok) y gestiona la aplicación de la privacidad a nivel de equipo.
  </Accordion>

  {" "}

  <Accordion title="Usage-Based Pricing Settings">
    Activa la facturación basada en uso y establece límites de gasto. Configura límites de gasto mensuales del equipo y límites opcionales por usuario. Controla si solo los admins pueden modificar esta configuración.
  </Accordion>

  {" "}

  <Accordion title="Bedrock IAM Role">
    Configura roles de AWS Bedrock IAM para una integración segura en la nube.
  </Accordion>

  {" "}

  <Accordion title="Single Sign-On (SSO)">
    Configura la autenticación SSO para equipos Enterprise y agiliza el acceso de los usuarios y la seguridad.
  </Accordion>

  {" "}

  <Accordion title="Cursor Admin API Keys">
    Crea y gestiona claves de API para el acceso programático a las funciones de administración de Cursor.
  </Accordion>

  {" "}

  <Accordion title="Active Sessions">
    Supervisa y gestiona las sesiones activas de usuarios en todo tu equipo.
  </Accordion>

  <Accordion title="Invite Code Management">
    Crea y gestiona códigos de invitación para añadir nuevas personas al equipo.
  </Accordion>

  <Accordion title="API Endpoints">
    Accede a los endpoints de la REST API de Cursor para la integración programática. Todos los endpoints de la API están disponibles en los planes Team y Enterprise, excepto la [AI Code Tracking API](/es/docs/account/teams/ai-code-tracking-api), que requiere una suscripción Enterprise.
  </Accordion>
</AccordionGroup>

<div id="enterprise-only-settings">
  ## Configuraciones exclusivas de Enterprise
</div>

<AccordionGroup>
  {" "}

  <Accordion title="Model Access Control">
    Controla qué modelos de IA están disponibles para los miembros del equipo. Establece restricciones en
    modelos específicos o niveles de modelo para gestionar costos y garantizar un uso adecuado
    en toda tu organización.
  </Accordion>

  {" "}

  <Accordion title="Auto Run Configuration (0.49+)">
    Configura los ajustes de ejecución automática de comandos para Cursor versión 0.49 y
    posteriores. Controla qué comandos pueden ejecutarse automáticamente y define políticas de seguridad
    para la ejecución de código.
  </Accordion>

  <Accordion title="Repository Blocklist">
    Evita el acceso a repositorios específicos por razones de seguridad o cumplimiento.
  </Accordion>

  {" "}

  <Accordion title="MCP Configuration (0.51+)">
    Configura los ajustes de Model Context Protocol para Cursor versión 0.51 y posteriores.
    Administra cómo los modelos acceden y procesan el contexto desde tu entorno de
    desarrollo.
  </Accordion>

  {" "}

  <Accordion title="Cursor Ignore Configuration (0.50+)">
    Configura patrones de exclusión para archivos y directorios en Cursor versión 0.50 y
    posteriores. Controla qué archivos y directorios se excluyen del análisis de IA y de
    las sugerencias.
  </Accordion>

  <Accordion title=".cursor Directory Protection (0.51+)">
    Protege el directorio .cursor contra accesos no autorizados en la versión 0.51 y posteriores. Asegura que los archivos sensibles de configuración y caché permanezcan protegidos.
  </Accordion>

  <Accordion title="AI Code Tracking API">
    Accede a analíticas detalladas del código generado por IA para los repositorios de tu equipo. Obtén métricas de uso de IA por commit y cambios de IA aceptados a nivel granular mediante endpoints de la API REST. Requiere un plan Enterprise. Encuentra más información [aquí](/es/account/teams/ai-code-tracking-api).
  </Accordion>
</AccordionGroup>

<Note>
  El aprovisionamiento **SCIM** (System for Cross-domain Identity Management) también está
  disponible para planes Enterprise. Consulta nuestra [documentación de SCIM](/es/account/teams/scim)
  para obtener instrucciones de configuración.
</Note>

<div id="members">
  ## Miembros
</div>

Administra a los miembros de tu equipo, invita a nuevos usuarios y controla los permisos de acceso. Configura permisos por rol y monitorea la actividad de los miembros.

<Frame>
  <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/members.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=4ac43692626733caf2da4b53e4cd9055" data-og-width="1390" width="1390" data-og-height="591" height="591" data-path="images/account/team/members.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/members.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=a2a24d3282df1e875d73fd2bf29b9c04 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/members.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=1abe9715816149f577a5d9c9e2f3545d 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/members.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=ccc84260c5139119e5b16ad6c214af72 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/members.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=5fe34e422fa9540004c25a61570029c3 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/members.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=dee7c3ade8ef46b5ead5dbe2bfd2a6be 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/members.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=9a42bce921a799886b8e3e0a389b8589 2500w" />
</Frame>

<div id="integrations">
  ## Integraciones
</div>

<Frame>
  <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/integrations.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=187b9e77d6b99c77caec81e1b3063417" data-og-width="1390" width="1390" data-og-height="592" height="592" data-path="images/account/team/integrations.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/integrations.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=470d5697ff2bfb9db2ae745b2c33cce6 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/integrations.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=e1e7d589f1f208ecdba9840629897968 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/integrations.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=2285e05c99c3a6ace609b51770475a3e 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/integrations.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=7c44649c5e8cd0f2a3791a3085252eca 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/integrations.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=0cf7111171c8019f7a59adc79cb9639d 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/integrations.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=8423a209b4e1c753045dca1514cbfbad 2500w" />
</Frame>

{" "}

Conecta Cursor con tus herramientas y servicios favoritos. Configura integraciones con sistemas de control de versiones, herramientas de gestión de proyectos y otros servicios para desarrolladores.

<div id="background-agents">
  ## Agentes en segundo plano
</div>

<Frame>
  <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/integrations.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=187b9e77d6b99c77caec81e1b3063417" data-og-width="1390" width="1390" data-og-height="592" height="592" data-path="images/account/team/integrations.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/integrations.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=470d5697ff2bfb9db2ae745b2c33cce6 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/integrations.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=e1e7d589f1f208ecdba9840629897968 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/integrations.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=2285e05c99c3a6ace609b51770475a3e 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/integrations.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=7c44649c5e8cd0f2a3791a3085252eca 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/integrations.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=0cf7111171c8019f7a59adc79cb9639d 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/integrations.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=8423a209b4e1c753045dca1514cbfbad 2500w" />
</Frame>

{" "}

Monitorea y gestiona los agentes en segundo plano que se ejecutan en tu espacio de trabajo. Revisa el estado de los agentes, los registros y el uso de recursos.

<div id="bugbot">
  ## Bugbot
</div>

Accedé a funciones automatizadas para detectar y corregir bugs. Bugbot te ayuda a identificar y resolver problemas comunes en tu codebase automáticamente.

<Frame>
  <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/bugbot.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=20d841dfc7837445103a933dab18b470" alt="Code review de Bugbot" data-og-width="1390" width="1390" data-og-height="913" height="913" data-path="images/account/team/bugbot.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/bugbot.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=975f5e3f9f9a0334c8a5bcc12faf72be 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/bugbot.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=17099f8bbe0701750d0ba212879d8a93 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/bugbot.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=041c82a4c3bada0524527609dfc134a4 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/bugbot.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=90ac57ea38768ace4b9404476fafdf32 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/bugbot.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=5785673a93f899ccca7b70e7a3752ef7 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/bugbot.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=a1a1dc51872967e392e10d6b85c31a04 2500w" />
</Frame>

<div id="active-directory-management">
  ## Gestión de Active Directory
</div>

Para equipos empresariales, gestiona la autenticación de usuarios y el acceso mediante la integración con Active Directory. Configura SSO y el aprovisionamiento de usuarios.

<div id="usage">
  ## Uso
</div>

Haz un seguimiento detallado de métricas de uso, como solicitudes a la IA, uso de modelos y consumo de recursos. Supervisa el uso entre los miembros del equipo y los proyectos.

<Frame>
  <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/usage.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=8744e41430d162199d85ca8e966c91cd" data-og-width="1390" width="1390" data-og-height="913" height="913" data-path="images/account/team/usage.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/usage.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=bc43eaaeca3c2a531a56243037a7a53f 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/usage.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=34700d63fabf072e9906aab74f79f7d9 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/usage.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=7f2bcdb271d6b30e333374c798638989 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/usage.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=424bd0eeda69200668f8f0b86dc360bf 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/usage.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=f0e716c72f01a3297a53a5b63d191ef4 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/usage.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=ffa574322508a07cc5ab867b331b6d35 2500w" />
</Frame>

<div id="billing-invoices">
  ## Facturación e facturas
</div>

Gestiona tu suscripción, actualiza los métodos de pago y accede al historial de facturación. Descarga las facturas y administra la configuración de precios según el uso.

<Frame>
  <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/billing.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=d76d20a7fafc6ed2135f2f9c78ec6c2d" data-og-width="1390" width="1390" data-og-height="913" height="913" data-path="images/account/team/billing.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/billing.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=45501f34dd144ecd74e982fe5f8f8364 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/billing.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=19860b61e083a8550cb3caa16bdb1ba0 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/billing.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=7005bae381a362b39980a49113ca367c 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/billing.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=e47c9ee55e3699ba46429b0ac0563b5b 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/billing.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=039106fd5ff42f2e343b2b853614e7e7 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/billing.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=e598f83559985558f5825a3da25bb554 2500w" />
</Frame>



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



# Primeros pasos
Source: https://docs.cursor.com/es/account/teams/setup

Crea y configura un equipo de Cursor

<div id="cursor-for-teams">
  ## Cursor para equipos
</div>

Cursor funciona para personas y equipos. El plan Teams ofrece herramientas para organizaciones: SSO, gestión de equipos, controles de acceso y análisis de uso.

<div id="creating-a-team">
  ## Crear un equipo
</div>

Crea un equipo siguiendo estos pasos:

<Steps>
  <Step title="Configurar el plan Teams">
    Para crear un equipo, sigue estos pasos:

    1. **Para usuarios nuevos**: Visita [cursor.com/team/new-team](https://cursor.com/team/new-team) para crear una cuenta y un equipo nuevos
    2. **Para usuarios existentes**: Ve a tu [panel](/es/account/dashboard) y haz clic en "Upgrade to Teams"
  </Step>

  <Step title="Ingresar detalles del equipo">
    Elige un nombre para el equipo y el ciclo de facturación

    <Frame>
      <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/new-team.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=3b9df20d032b544dcbc0343d9ddf056f" data-og-width="3456" width="3456" data-og-height="2158" height="2158" data-path="images/account/team/new-team.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/new-team.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=b81f3241069a8a0fb9278b6a2e246057 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/new-team.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=c26976bf06297d36ec9224ec1496a630 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/new-team.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=fed5c7c95914ff47cfceae81f1441208 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/new-team.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=0dc5986368419ef54f45803547741cfe 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/new-team.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=4eb38a9618399ddadbf7596b185d2732 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/new-team.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=1c7d720a1e20d2aa23463a1b9001d545 2500w" />
    </Frame>
  </Step>

  <Step title="Invitar miembros">
    Invita a miembros del equipo. Los usuarios se prorratean: solo pagas por el tiempo que son miembros.

    <Frame>
      <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/invite-members.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=bbd84dd96a7003415c2d2f038b1aaa77" style={{ paddingLeft: 16, paddingRight: 16, backgroundColor: '#0c0c0c' }} data-og-width="880" width="880" data-og-height="422" height="422" data-path="images/account/invite-members.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/invite-members.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=988e36ee874f704dfaae1b0a69ed2f84 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/invite-members.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=c0f85aacd3be59e11b1bfd05f9e5d6cd 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/invite-members.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=411456e375f8c406ad2972965e0b549e 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/invite-members.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=57ae04799be300a7e61464490344146f 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/invite-members.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=2faa0cf8ed56865c19916e33fde97900 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/invite-members.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=0bdb5040f44338e748246b4f1ddf2ddf 2500w" />
    </Frame>
  </Step>

  <Step title="Habilitar SSO (opcional)">
    Habilita el [SSO](/es/account/teams/sso) para mayor seguridad y onboarding automatizado.

    <Frame>
      <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=76608c26daf1f9ab2bbc2c4ccb156c0e" data-og-width="802" width="802" data-og-height="440" height="440" data-path="images/account/sso-settings.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=334dc1fc107338d19ec7b0052e7ea0e4 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=543b3d868c19960a5fb4c526d9895bd3 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=a06655178ba10f6a72919e9f7d598191 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=e280fc911306fe8d3b8e90b7221b0c11 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=ffd8f2c0168e2ac4f95431062b226021 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=1c17e4eac666b663d676ce874f1c4ba5 2500w" />
    </Frame>
  </Step>
</Steps>

<div id="faq">
  ## Preguntas frecuentes
</div>

<AccordionGroup>
  <Accordion title="Mi equipo usa Zscaler / un proxy / una VPN, ¿funcionará Cursor?">
    Cursor usa HTTP/2 de forma predeterminada. Algunos proxies y VPN lo bloquean.

    Activa la opción de usar HTTP/1.1 como respaldo en la configuración.
  </Accordion>

  <Accordion title="¿Cómo puedo comprar licencias para mi empresa?">
    Cursor factura por usuario activo, no por plazas. Agrega o quita usuarios en cualquier momento: a los nuevos miembros se les cobra de forma prorrateada por el tiempo restante. Si un usuario eliminado ha usado créditos, su plaza sigue ocupada hasta el final del ciclo de facturación.

    Tu fecha de renovación no cambia.
  </Accordion>

  <Accordion title="¿Cómo puedo configurar un equipo si no estoy usando Cursor?">
    Ponte como [Unpaid Admin](/es/account/teams/members) para administrar sin una licencia.

    <Warning>
      Los equipos necesitan al menos un miembro de pago. Puedes configurar, invitar a un miembro y luego cambiar tu rol antes de la facturación.
    </Warning>
  </Accordion>

  <Accordion title="¿Cómo puedo agregar Cursor al MDM de mi empresa?">
    Los enlaces de descarga para todas las plataformas están disponibles en [cursor.com/downloads](https://cursor.com/downloads).

    Instrucciones de MDM:

    * [Omnissa Workspace ONE](https://docs.omnissa.com/bundle/MobileApplicationManagementVSaaS/page/DeployInternalApplications.html) (antes VMware)
    * [Microsoft Intune (Windows)](https://learn.microsoft.com/en-us/mem/intune-service/apps/apps-win32-app-management)
    * [Microsoft Intune (Mac)](https://learn.microsoft.com/en-us/mem/intune-service/apps/lob-apps-macos-dmg)
    * [Kandji MDM](https://support.kandji.io/kb/custom-apps-overview)
  </Accordion>
</AccordionGroup>



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



# Acceso a actualizaciones
Source: https://docs.cursor.com/es/account/update-access

Elige con qué frecuencia quieres recibir actualizaciones

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

Cursor tiene dos canales de actualización.

<Tabs>
  <Tab title="Default">
    El canal de actualización predeterminado con versiones comprobadas.

    * Versiones estables
    * Correcciones de errores de las pruebas previas al lanzamiento
    * Predeterminado para todos los usuarios
    * Única opción para usuarios de equipo

    <Note>
      Las cuentas de equipo y empresariales usan el modo Default.
    </Note>
  </Tab>

  <Tab title="Early Access">
    Versiones preliminares con nuevas funciones.

    <Warning>
      Las versiones de Early Access pueden tener errores o problemas de estabilidad.
    </Warning>

    * Acceso a funciones en desarrollo
    * Puede contener errores
    * No disponible para cuentas de equipo
  </Tab>
</Tabs>

<div id="change-update-channel">
  ## Cambiar el canal de actualización
</div>

1. **Abrir configuración**: Presiona <Kbd>Cmd+Shift+J</Kbd>
2. **Ir a Beta**: Selecciona Beta en la barra lateral
3. **Seleccionar canal**: Elige Default o Early Access

<Frame>
  <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/early-access.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=36c55c2deb93bc734b6ee0099a0d184c" data-og-width="1798" width="1798" data-og-height="442" height="442" data-path="images/account/early-access.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/early-access.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=624bfea7b3643f55afaa85b38b1c56e1 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/early-access.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=f32c8e59596f024223735b4f929949e0 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/early-access.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=bd8c4bf3265ab802b6188aa81a620244 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/early-access.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=e8600f42cc363c61377f158972187e01 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/early-access.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=32c83b2109587d299959c2d46ce67353 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/early-access.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=b2c4032824d39c62a7cbada5578b1a98 2500w" />
</Frame>

Reporta problemas de Early Access en el [Forum](https://forum.cursor.com).



# Apply
Source: https://docs.cursor.com/es/agent/apply

Aprende a aplicar, aceptar o rechazar sugerencias de código desde el chat con Apply

<div id="how-apply-works">
  ## Cómo funciona Apply
</div>

Apply es un modelo especializado de Cursor que toma el código generado en el chat y lo integra en tus archivos. Procesa los bloques de código de las conversaciones y aplica los cambios a tu código.

Apply no genera código por sí mismo. El modelo de chat genera el código y Apply se encarga de integrarlo en los archivos existentes. Puede procesar cambios en múltiples archivos y en bases de código grandes.

<div id="apply-code-blocks">
  ## Aplicar bloques de código
</div>

Para aplicar una sugerencia de bloque de código, haz clic en el botón de reproducir en la esquina superior derecha del bloque.

<Frame>
  <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/apply.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=634492fa2f63b4f6eada08b2a1ded47e" data-og-width="1032" width="1032" data-og-height="410" height="410" data-path="images/chat/apply.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/apply.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=7dbc88cfe20429c73e627a289b17c964 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/apply.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=721e2d51bdb16dbb817e19d96d93c9d9 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/apply.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=8faea188ca903e58d347ddfec2c9bf6e 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/apply.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=f3bc38701cab63602b54374dfaa9e024 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/apply.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=fddad51f5b12c32493e2370ed326712d 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/apply.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=1584d431007b33a595905e23b5e1b453 2500w" />
</Frame>



# Checkpoints
Source: https://docs.cursor.com/es/agent/chat/checkpoints

Guarda y restaura estados anteriores después de cambios del Agent

Los checkpoints son instantáneas automáticas de los cambios que el Agent hace en tu base de código. Te permiten deshacer las modificaciones del Agent cuando lo necesites.

<Frame>
  <video src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/restore-checkpoint.mp4?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=7cededf7892f15a6342a81953ea0aa38" autoPlay loop muted playsInline controls data-path="images/chat/restore-checkpoint.mp4" />
</Frame>

<div id="restoring-checkpoints">
  ## Restaurar checkpoints
</div>

Dos formas de restaurar:

1. **Desde el cuadro de entrada**: haz clic en el botón `Restore Checkpoint` en solicitudes anteriores
2. **Desde el mensaje**: haz clic en el botón + al pasar el cursor sobre un mensaje

<Warning>
  Los checkpoints no son control de versiones. Usa Git para el historial permanente.
</Warning>

<div id="how-they-work">
  ## Cómo funcionan
</div>

* Se guardan localmente, aparte de Git
* Solo registran cambios del Agent (no ediciones manuales)
* Se limpian automáticamente

<Note>
  Las ediciones manuales no se registran. Usa checkpoints solo para cambios del Agent.
</Note>

<div id="faq">
  ## Preguntas frecuentes
</div>

<AccordionGroup>
  <Accordion title="¿Los checkpoints afectan a Git?">
    No. Son independientes del historial de Git.
  </Accordion>

  {" "}

  <Accordion title="¿Cuánto tiempo se conservan?">
    Solo durante la sesión actual y el historial reciente. Se eliminan automáticamente.
  </Accordion>

  <Accordion title="¿Puedo crearlos manualmente?">
    No. Cursor los crea automáticamente.
  </Accordion>
</AccordionGroup>

{" "}



# Comandos
Source: https://docs.cursor.com/es/agent/chat/commands

Define comandos para flujos de trabajo reutilizables

Los comandos personalizados te permiten crear flujos de trabajo reutilizables que se pueden activar con un simple prefijo `/` en el cuadro de entrada del chat. Estos comandos ayudan a estandarizar procesos en tu equipo y hacen más eficientes las tareas comunes.

<Frame>
    <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/commands/input.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=0d25ac517b091210da1c6eff4c8e3098" alt="Commands input example" data-og-width="1689" width="1689" data-og-height="1079" height="1079" data-path="images/chat/commands/input.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/commands/input.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=680f0cbf1491ef1303171dbd18115288 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/commands/input.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=d6a5397e565ab2c90435e6fdd2b7b27a 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/commands/input.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=ae074e2f2b26741544fd8c8ecfa529e3 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/commands/input.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=564aad432affcc04e51b624725f386ad 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/commands/input.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=5c1bd5d49babc2f08eb0efcd24ba7783 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/commands/input.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=3244c3be31c9bc704468a706c6e6b38e 2500w" />
</Frame>

<Info>
  Los comandos están actualmente en versión beta. La función y la sintaxis pueden cambiar a medida que seguimos mejorándola.
</Info>

<div id="how-commands-work">
  ## Cómo funcionan los comandos
</div>

Los comandos se definen como archivos Markdown de texto plano que se pueden guardar en dos ubicaciones:

1. **Comandos del proyecto**: almacenados en el directorio `.cursor/commands` de tu proyecto
2. **Comandos globales**: almacenados en el directorio `~/.cursor/commands` de tu directorio de inicio

Cuando escribes `/` en el cuadro de entrada del chat, Cursor detecta y muestra automáticamente los comandos disponibles de ambos directorios, haciéndolos accesibles al instante en todo tu flujo de trabajo.

<div id="creating-commands">
  ## Creación de comandos
</div>

1. Crea un directorio `.cursor/commands` en la raíz de tu proyecto
2. Añade archivos `.md` con nombres descriptivos (p. ej., `review-code.md`, `write-tests.md`)
3. Escribe contenido en Markdown sencillo que describa lo que debe hacer el comando
4. Los comandos aparecerán automáticamente en el chat cuando escribas `/`

Aquí tienes un ejemplo de cómo podría verse la estructura de tu directorio de comandos:

```
.cursor/
└── commands/
    ├── atender-comentarios-de-pr-de-github.md
    ├── lista-de-verificación-para-revisión-de-código.md
    ├── crear-pr.md
    ├── revisión-ligera-de-diffs-existentes.md
    ├── incorporación-de-nuevo-desarrollador.md
    ├── ejecutar-todas-las-pruebas-y-corregir.md
    ├── auditoría-de-seguridad.md
    └── configurar-nueva-función.md
```

<div id="examples">
  ## Ejemplos
</div>

Prueba estos comandos en tus proyectos para hacerte una idea de cómo funcionan.

<AccordionGroup>
  <Accordion title="Lista de verificación para revisión de código">
    ```markdown  theme={null}
    # Lista de verificación para revisión de código

    ## Descripción general
    Lista de verificación completa para realizar revisiones de código exhaustivas y garantizar calidad, seguridad y mantenibilidad.

    ## Categorías de revisión

    ### Funcionalidad
    - [ ] El código hace lo que debe
    - [ ] Se contemplan los casos límite
    - [ ] El manejo de errores es adecuado
    - [ ] No hay errores obvios ni fallos de lógica

    ### Calidad del código
    - [ ] El código es legible y está bien estructurado
    - [ ] Las funciones son pequeñas y enfocadas
    - [ ] Los nombres de variables son descriptivos
    - [ ] No hay duplicación de código
    - [ ] Sigue las convenciones del proyecto

    ### Seguridad
    - [ ] No hay vulnerabilidades de seguridad evidentes
    - [ ] Hay validación de entradas
    - [ ] Los datos sensibles se manejan correctamente
    - [ ] No hay secretos codificados en duro
    ```
  </Accordion>

  <Accordion title="Auditoría de seguridad">
    ```markdown  theme={null}
    # Auditoría de seguridad

    ## Descripción general
    Revisión de seguridad integral para identificar y corregir vulnerabilidades en la base de código.

    ## Pasos
    1. **Auditoría de dependencias**
       - Detectar vulnerabilidades conocidas
       - Actualizar paquetes desactualizados
       - Revisar dependencias de terceros

    2. **Revisión de seguridad del código**
       - Detectar vulnerabilidades comunes
       - Revisar autenticación/autorización
       - Auditar prácticas de manejo de datos

    3. **Seguridad de la infraestructura**
       - Revisar variables de entorno
       - Verificar controles de acceso
       - Auditar la seguridad de la red

    ## Lista de verificación de seguridad
    - [ ] Dependencias actualizadas y seguras
    - [ ] Sin secretos hardcodeados
    - [ ] Validación de entradas implementada
    - [ ] Autenticación segura
    - [ ] Autorización configurada correctamente
    ```
  </Accordion>

  <Accordion title="Configurar nueva función">
    ```markdown  theme={null}
    # Configurar nueva feature

    ## Descripción general
    Configura sistemáticamente una nueva feature, desde la planificación inicial hasta la estructura de implementación.

    ## Pasos
    1. **Definir requisitos**
       - Aclarar el alcance y los objetivos de la feature
       - Identificar historias de usuario y criterios de aceptación
       - Planificar el enfoque técnico

    2. **Crear rama de la feature**
       - Ramificar desde main/develop
       - Configurar el entorno de desarrollo local
       - Configurar cualquier dependencia nueva

    3. **Planificar la arquitectura**
       - Diseñar modelos de datos y APIs
       - Planificar componentes de UI y flujos
       - Definir la estrategia de testing

    ## Checklist de configuración de la feature
    - [ ] Requisitos documentados
    - [ ] Historias de usuario redactadas
    - [ ] Enfoque técnico definido
    - [ ] Rama de la feature creada
    - [ ] Entorno de desarrollo listo
    ```
  </Accordion>

  <Accordion title="Crear pull request">
    ```markdown  theme={null}
    # Crear PR

    ## Descripción general
    Crea un pull request bien estructurado con una descripción clara, etiquetas y revisores.

    ## Pasos
    1. **Preparar la rama**
       - Asegúrate de que todos los cambios estén confirmados
       - Envía la rama al remoto
       - Verifica que la rama esté actualizada con main

    2. **Escribir la descripción del PR**
       - Resume los cambios de forma clara
       - Incluye contexto y motivación
       - Enumera cualquier cambio incompatible
       - Agrega capturas de pantalla si hay cambios en la UI

    3. **Configurar el PR**
       - Crea el PR con un título descriptivo
       - Agrega etiquetas adecuadas
       - Asigna revisores
       - Vincula issues relacionados

    ## Plantilla de PR
    - [ ] Funcionalidad A
    - [ ] Corrección de bug B
    - [ ] Pruebas unitarias aprobadas
    - [ ] Pruebas manuales completadas
    ```
  </Accordion>

  <Accordion title="Ejecuta las pruebas y corrige los fallos">
    ```markdown  theme={null}
    # Ejecuta todas las pruebas y corrige los errores

    ## Descripción general
    Ejecuta toda la batería de pruebas y corrige de forma sistemática cualquier error, garantizando la calidad y la funcionalidad del código.

    ## Pasos
    1. **Ejecuta la batería de pruebas**
       - Ejecuta todas las pruebas del proyecto
       - Captura la salida e identifica los errores
       - Revisa tanto las pruebas unitarias como las de integración

    2. **Analiza los errores**
       - Clasifícalos por tipo: intermitentes, rotos, nuevos
       - Prioriza las correcciones según el impacto
       - Revisa si los errores están relacionados con cambios recientes

    3. **Corrige los problemas de forma sistemática**
       - Empieza por los errores más críticos
       - Corrige un problema a la vez
       - Vuelve a ejecutar las pruebas después de cada corrección
    ```
  </Accordion>

  <Accordion title="Incorporar a un nuevo developer">
    ```markdown  theme={null}
    # Incorporar a un nuevo developer

    ## Descripción general
    Proceso completo de onboarding para que un developer nuevo arranque y quede listo rápido.

    ## Pasos
    1. **Configuración del entorno**
       - Instalar las herramientas requeridas
       - Configurar el entorno de desarrollo
       - Configurar el IDE y las extensiones
       - Configurar git y las claves SSH

    2. **Familiarización con el proyecto**
       - Revisar la estructura del proyecto
       - Entender la arquitectura
       - Leer la documentación clave
       - Configurar la base de datos local

    ## Lista de verificación de onboarding
    - [ ] Entorno de desarrollo listo
    - [ ] Todas las pruebas pasando
    - [ ] Puedes ejecutar la app localmente
    - [ ] Base de datos configurada y funcionando
    - [ ] Primer PR enviado
    ```
  </Accordion>
</AccordionGroup>



# Compacto
Source: https://docs.cursor.com/es/agent/chat/compact

Ahorra espacio en el chat con la interfaz en modo compacto

El modo compacto ofrece una interfaz de chat más limpia al reducir el ruido visual y aprovechar al máximo el espacio para las conversaciones.

<div id="overview">
  ## Descripción general
</div>

Cuando está activado, el modo compacto transforma la interfaz del chat al:

* **Ocultar iconos** para una apariencia más limpia y minimalista
* **Plegar automáticamente los diffs** para reducir el ruido visual
* **Plegar automáticamente el campo de entrada** para maximizar el espacio de la conversación

Esta configuración es especialmente útil cuando trabajas en pantallas más pequeñas o cuando prefieres una experiencia de chat enfocada y sin distracciones.

<div id="before-and-after">
  ## Antes y después
</div>

<div id="default-mode">
  ### Modo predeterminado
</div>

<Frame>
  <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/compact/off.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=e0f8b97ecd5201be396fcd09cec54de6" alt="Interfaz de chat en modo predeterminado que muestra todos los iconos y elementos expandidos" data-og-width="2048" width="2048" data-og-height="2350" height="2350" data-path="images/chat/compact/off.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/compact/off.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=9395c8d1f324033631508dc9cdfd6f3e 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/compact/off.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=5d8025ef65ad2fc9fe8c30e5c4fcda32 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/compact/off.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=28050b27b683af948bc1ed939f31786c 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/compact/off.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=dc443705188da9d3368acefd917cc890 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/compact/off.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=be6603e2cedb7e88e7c20d797b18599c 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/compact/off.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=3afe563c9cd4576623adce5dcaaccddf 2500w" />
</Frame>

<div id="compact-mode">
  ### Modo compacto
</div>

<Frame>
  <img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/compact/on.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=e9f068889026827422b2a9d943b55ded" alt="Interfaz de chat en modo compacto con iconos ocultos y elementos contraídos" data-og-width="2048" width="2048" data-og-height="2350" height="2350" data-path="images/chat/compact/on.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/compact/on.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=44e86a79eb893b4de6c57c65487bbe9a 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/compact/on.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=539b71c72ed2fb3508e3aec0624429c1 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/compact/on.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=2c0da715a5daf93e94dbf2a5eefbb7eb 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/compact/on.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=b5bddca39109779c9d91bb6bc8bb42e9 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/compact/on.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=8bb334bb055e49d4d51cd137d2396db0 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/compact/on.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=70730d151a24440eeb6dc31e18189c7d 2500w" />
</Frame>

<div id="enabling-compact-mode">
  ## Activar el modo compacto
</div>

Para activar el modo compacto:

1. Abre la configuración de Cursor
2. Ve a la sección de **Chat**
3. Activa **Compact Mode** para habilitarlo

La interfaz se actualizará de inmediato a una vista más compacta, dándote más espacio para concentrarte en tus conversaciones.



# Duplicar
Source: https://docs.cursor.com/es/agent/chat/duplicate

Crea ramas desde cualquier punto de una conversación

Duplica o crea forks de chats para explorar soluciones alternativas sin perder tu conversación actual.

<Frame>
  <video src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/duplicate-chat.mp4?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=29fdb23214ba3e2c5b94ccefc01f7615" autoPlay loop muted playsInline controls data-path="images/chat/duplicate-chat.mp4" />
</Frame>

<div id="how-to-duplicate">
  ## Cómo duplicar
</div>

1. Encuentra dónde quieres crear una rama
2. Haz clic en los tres puntos del mensaje
3. Selecciona "Duplicate Chat"

<div id="what-happens">
  ## Qué pasa
</div>

* Se mantiene el contexto hasta ese punto
* La conversación original no cambia
* Ambos chats conservan historiales separados



# Exportar
Source: https://docs.cursor.com/es/agent/chat/export

Exportar chats en formato Markdown

Exporta los chats del Agent como archivos Markdown para compartir o documentar.

<Frame>
  <video src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/export-chat.mp4?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=c6aa9d23a6a80ffae5864cd494907961" autoPlay loop muted playsInline controls data-path="images/chat/export-chat.mp4" />
</Frame>

<div id="whats-exported">
  ## Qué se exporta
</div>

* Todos los mensajes y respuestas
* Bloques de código con resaltado de sintaxis
* Referencias a archivos y contexto
* Flujo cronológico de la conversación

<div id="how-to-export">
  ## Cómo exportar
</div>

1. Ve al chat que quieres exportar
2. Haz clic en el menú contextual → "Export Chat"
3. Guarda el archivo localmente

<Warning>
  Revisa las exportaciones en busca de datos sensibles: claves de API, URL internas, código propietario,
  información personal
</Warning>



# Historial
Source: https://docs.cursor.com/es/agent/chat/history

Ver y gestionar conversaciones de chat

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

Accede a conversaciones anteriores del agente desde el panel de historial.

<Frame>
  <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/chat-history.jpeg?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=d9ec96fad0c8c2fb132bbf5ce8ea35f7" alt="Historial de chat" data-og-width="2048" width="2048" data-og-height="1317" height="1317" data-path="images/chat/chat-history.jpeg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/chat-history.jpeg?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=a3ad71e9891c3c9642f4288953a78e97 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/chat-history.jpeg?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=76139a177ebfeb0c55add7fb955f9000 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/chat-history.jpeg?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=1af22180859c017542777ab36b434b7a 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/chat-history.jpeg?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=751e7fa0888e5790f841432ef7521337 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/chat-history.jpeg?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=86b447c18601a9d44af8866d0042719e 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/chat-history.jpeg?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=88c84a8fb1b764ad3070e3211f539408 2500w" />
</Frame>

<div id="opening-history">
  ## Abrir el historial
</div>

* Haz clic en el icono de historial en el panel lateral de Agent
* Presiona <Kbd tooltip="Open chat history">Opt Cmd '</Kbd>

<div id="managing-chats">
  ## Administrar chats
</div>

* **Editar títulos**: Haz clic para cambiar el nombre
* **Eliminar**: Borra los chats que no necesitas
* **Abrir**: Haz clic para revisar la conversación completa

El historial de chats se guarda localmente en una base de datos SQLite en tu equipo.

<Note>
  Para conservar los chats, [expórtalos](/es/agent/chats/export) como Markdown.
</Note>

<div id="background-agents">
  ## Agentes en segundo plano
</div>

Los chats de agentes en segundo plano no aparecen en el historial habitual; en su lugar, se guardan en una base de datos remota. Usa <Kbd tooltip="Open background agent control panel">Cmd E</Kbd> para verlos.

<div id="referencing-past-chats">
  ## Referenciar chats anteriores
</div>

Usa [@Past Chats](/es/context/@-symbols/@-past-chats) para incluir contexto de conversaciones anteriores en tu chat actual.



# Resumen
Source: https://docs.cursor.com/es/agent/chat/summarization

Gestión del contexto para conversaciones largas en el chat

<div id="message-summarization">
  ## Resumen de mensajes
</div>

A medida que las conversaciones crecen, Cursor resume y gestiona el contexto automáticamente para mantener tus chats eficientes. Aprende a usar el menú contextual y a entender cómo se condensan los archivos para ajustarse a las ventanas de contexto del modelo.

<div id="using-the-summarize-command">
  ### Usar el comando /summarize
</div>

Podés activar manualmente un resumen usando el comando `/summarize` en el chat. Este comando ayuda a gestionar el contexto cuando las conversaciones se hacen demasiado largas, así podés seguir trabajando de forma eficiente sin perder información importante.

<Info>
  Para profundizar en cómo funciona el contexto en Cursor, mirá nuestra guía [Working with
  Context](/es/guides/working-with-context).
</Info>

<div id="how-summarization-works">
  ### Cómo funciona el resumen
</div>

Cuando las conversaciones se alargan, superan el límite de la ventana de contexto del modelo:

<Frame>
  <div className="font-mono text-xs w-full bg-neutral-100 p-4 rounded-lg">
    <div className="relative">
      <div className="bg-white px-3 py-2 mb-2 rounded border border-dashed border-neutral-400 w-full">
        <div className="text-xs text-neutral-700 font-medium">User</div>
      </div>

      <div className="bg-white px-3 py-2 mb-2 rounded border border-dashed border-neutral-400 w-full">
        <div className="text-xs text-neutral-700 font-medium">Cursor</div>
      </div>

      <div className="bg-white px-3 py-2 mb-2 rounded border border-dashed border-neutral-400 w-full">
        <div className="text-xs text-neutral-700 font-medium">User</div>
      </div>

      <div className="relative my-4">
        <div className="absolute top-0 left-1/2 transform -translate-x-1/2 -translate-y-1/2 text-center text-xs text-black bg-neutral-100 px-2">Límite de la ventana de contexto</div>

        <div className="w-full h-px bg-black" />
      </div>

      <div className="bg-white px-3 py-2 mb-2 rounded border border-neutral-400 w-full">
        <div className="text-xs text-neutral-700 font-medium">Cursor</div>
      </div>

      <div className="bg-white px-3 py-2 mb-2 rounded border border-neutral-400 w-full">
        <div className="text-xs text-neutral-700 font-medium">User</div>
      </div>

      <div className="bg-white px-3 py-2 mb-2 rounded border border-neutral-400 w-full">
        <div className="text-xs text-neutral-700 font-medium">Cursor</div>
      </div>
    </div>
  </div>
</Frame>

Para resolver esto, Cursor resume los mensajes más antiguos para hacer espacio a conversaciones nuevas.

<Frame>
  <div className="font-mono text-xs w-full bg-neutral-100 p-4 rounded-lg">
    <div className="relative">
      <div className="relative my-4">
        <div className="absolute top-0 left-1/2 transform -translate-x-1/2 -translate-y-1/2 text-center text-xs text-black bg-neutral-100 px-2">
          Límite de la ventana de contexto
        </div>

        <div className="w-full h-px bg-black" />
      </div>

      <div className="bg-neutral-100 px-3 py-2 mb-2 rounded border border-dashed border-neutral-400 w-full">
        <div className="text-xs text-neutral-700 font-medium">
          Mensajes resumidos
        </div>
      </div>

      <div className="bg-white px-3 py-2 mb-2 rounded border border-neutral-400 w-full">
        <div className="text-xs text-neutral-700 font-medium">Cursor</div>
      </div>

      <div className="bg-white px-3 py-2 mb-2 rounded border border-neutral-400 w-full">
        <div className="text-xs text-neutral-700 font-medium">User</div>
      </div>

      <div className="bg-white px-3 py-2 mb-2 rounded border border-neutral-400 w-full">
        <div className="text-xs text-neutral-700 font-medium">Cursor</div>
      </div>
    </div>
  </div>
</Frame>

<div id="file-folder-condensation">
  ## Condensación de archivos y carpetas
</div>

Aunque el resumen del chat se encarga de conversaciones largas, Cursor usa una estrategia distinta para manejar archivos y carpetas grandes: **condensación inteligente**. Cuando incluyes archivos en tu conversación, Cursor decide la mejor forma de presentarlos según su tamaño y el espacio de contexto disponible.

Estos son los diferentes estados en los que puede estar un archivo o carpeta:

<div id="condensed">
  ### Resumen
</div>

Cuando los archivos o carpetas son demasiado grandes para entrar en la ventana de contexto, Cursor los condensa automáticamente. Al condensar, el modelo ve elementos estructurales clave como firmas de funciones, clases y métodos. Desde esta vista condensada, el modelo puede elegir expandir archivos específicos si hace falta. Este enfoque maximiza el uso efectivo de la ventana de contexto disponible.

<Frame>
  <img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/context-management/condensed.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=0c3a07b6fef6402945138f7ee38b44c1" alt="Menú contextual" data-og-width="1226" width="1226" data-og-height="793" height="793" data-path="images/context/context-management/condensed.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/context-management/condensed.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=4cc08626f9cfce1d186cdd6aa96c7d09 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/context-management/condensed.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=fa49ce9605bdb0186c98712f4c0a32cc 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/context-management/condensed.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=84874b2f40bff0a2cd54796865469914 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/context-management/condensed.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=050290a85c154e92f9298883afcdf892 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/context-management/condensed.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=f953aa28f11926b2d6fdf734cf928402 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/context-management/condensed.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=50aa9973ccf2027814860f3d97a2b031 2500w" />
</Frame>

<div id="significantly-condensed">
  ### Significativamente comprimido
</div>

Cuando un nombre de archivo aparece con la etiqueta “Significantly Condensed”, significa que el archivo es demasiado grande para incluirlo completo, incluso en una versión comprimida. Solo se mostrará el nombre del archivo al modelo.

<div id="not-included">
  ### No incluido
</div>

Cuando aparece un icono de advertencia junto a un archivo o carpeta, el elemento es demasiado grande para incluirlo en la ventana de contexto, incluso en versión condensada. Esto te ayuda a entender qué partes de tu codebase son accesibles para el modelo.

<Frame>
  <img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/context-management/not-included.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=06df9854c74c257d1ceb7d18b1864ceb" alt="Menú de contexto" data-og-width="1090" width="1090" data-og-height="346" height="346" data-path="images/context/context-management/not-included.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/context-management/not-included.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=072e75878f27a151f1310007d0e5e534 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/context-management/not-included.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=c6f3f71351ddf8e367096651b455bf9d 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/context-management/not-included.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=c407f7870412007549f8eb2871f9ca12 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/context-management/not-included.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=b0d17023b5734c8d7584c56f5419bd1a 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/context-management/not-included.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=f1bedff398cee6c957fe62877f7d2012 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/context-management/not-included.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=8b00fbaff658c384f69bfddf3f3a4cfe 2500w" />
</Frame>



# Pestañas
Source: https://docs.cursor.com/es/agent/chat/tabs

Ejecuta varias conversaciones del Agente a la vez

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

<Frame>
  <video src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/chat-tabs.mp4?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=57fd5305279dc0a3139055b353ce4b7a" autoPlay loop muted playsInline controls data-path="images/chat/chat-tabs.mp4" />
</Frame>

<div id="overview">
  ## Descripción general
</div>

Presiona <Kbd>Cmd+T</Kbd> para crear pestañas nuevas. Cada pestaña mantiene por separado el historial de la conversación, el contexto y la selección de modelo.

<Tip>
  Para trabajar en paralelo, prueba los [Background Agents](/es/background-agents)
</Tip>

<div id="managing-tabs">
  ## Gestión de pestañas
</div>

* Creá nuevas pestañas con <Kbd>Cmd+T</Kbd>. Cada pestaña inicia una conversación nueva y mantiene su propio contexto.

* Cambiá entre pestañas haciendo clic en sus encabezados o usando <Kbd>Ctrl+Tab</Kbd> para recorrerlas.

* Los títulos de las pestañas se generan automáticamente después del primer mensaje, pero podés renombrarlos con el botón derecho en el encabezado de la pestaña.

<Tip>
  Usá una tarea por pestaña, brindá descripciones iniciales claras y cerrá las
  pestañas terminadas para mantener tu espacio de trabajo organizado.
</Tip>

<div id="conflicts">
  ### Conflictos
</div>

Cursor evita que varias pestañas editen los mismos archivos. Se te pedirá que resuelvas los conflictos.

<div id="reference-other-chats">
  ## Referenciar otros chats
</div>

Usa [@Past Chats](/es/context/@-symbols/@-past-chats) para incluir contexto de otras pestañas o sesiones anteriores.



# Modos
Source: https://docs.cursor.com/es/agent/modes

Elige el modo adecuado para tu tarea: de codificación autónoma a ediciones enfocadas

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

Agent ofrece distintos modos optimizados para tareas específicas. Cada modo tiene diferentes capacidades y herramientas activadas para adaptarse a tu flujo de trabajo.

<div className="full-width-table">
  | Modo                  | Para                                       | Capacidades                                          | Herramientas                     |
  | :-------------------- | :----------------------------------------- | :--------------------------------------------------- | :------------------------------- |
  | **[Agent](#agent)**   | Funcionalidades complejas, refactorización | Exploración autónoma, edición en múltiples archivos  | Todas las herramientas activadas |
  | **[Ask](#ask)**       | Aprendizaje, planificación, preguntas      | Exploración de solo lectura, sin cambios automáticos | Solo herramientas de búsqueda    |
  | **[Custom](#custom)** | Flujos de trabajo especializados           | Capacidades definidas por el usuario                 | Configurable                     |
</div>

<div id="agent">
  ## Agent
</div>

El modo predeterminado para tareas de programación complejas. Agent explora tu base de código de forma autónoma, edita varios archivos, ejecuta comandos y corrige errores para completar tus solicitudes.

<Frame>
  <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/agent.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=9cd06dd9f59e019b3d76aa0fd9f934ba" data-og-width="3600" width="3600" data-og-height="2025" height="2025" data-path="images/chat/agent.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/agent.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=d979435c61e2112ebcb784f16a49327f 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/agent.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=1a88e2085ffe80f02daea9a523887282 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/agent.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=de98a8bf766c3f35a6187e87190e30f9 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/agent.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=8648638c4240b718e0512a6ec2274171 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/agent.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=45b9898d65f5b425d276eaa44d4e1940 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/agent.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=30fef2b190d453ee0166e554a4005bd1 2500w" />
</Frame>

<div id="ask">
  ## Ask
</div>

Modo de solo lectura para aprender y explorar. Ask busca en tu código y te da respuestas sin hacer ningún cambio: perfecto para entender el código antes de modificarlo.

<Frame>
  <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/ask.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=15e531cb84f0a18228723870fd84fa4f" data-og-width="3600" width="3600" data-og-height="2025" height="2025" data-path="images/chat/ask.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/ask.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=592ac5a681910a075ae88dec89bee25d 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/ask.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=74b98cce3b5bb83c79d0566cd3c65c34 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/ask.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=c4d80f50e20e7ca28db5a3ee71718979 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/ask.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=a4a6e017fd64149cf68d997114bbf6b6 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/ask.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=7354479ecd644b86ddbcb9fe1131f100 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/ask.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=274125e614eadd17522e0dacfcc6a38e 2500w" />
</Frame>

<div id="custom">
  ## Personalizado
</div>

Crea tus propios modos con combinaciones específicas de herramientas e instrucciones. Mezcla capacidades según lo que mejor encaje con tu flujo de trabajo.

<Note>
  Los modos personalizados están en beta. Actívalos en `Cursor Settings` → `Chat` → `Custom
      Modes`
</Note>

<div id="examples">
  ### Ejemplos
</div>

<AccordionGroup>
  <Accordion title="Learn">
    **Herramientas:** All Search\
    **Instrucciones:** Enfócate en explicar los conceptos a fondo y haz preguntas para aclarar
  </Accordion>

  {" "}

  <Accordion title="Refactor">
    **Herramientas:** Edit & Reapply **Instrucciones:** Mejora la estructura del código sin
    agregar nueva funcionalidad
  </Accordion>

  {" "}

  <Accordion title="Plan">
    **Herramientas:** Codebase, Read file, Terminal **Instrucciones:** Crea planes de implementación detallados en `plan.md`
  </Accordion>

  <Accordion title="Debug">
    **Herramientas:** All Search, Terminal, Edit & Reapply\
    **Instrucciones:** Investiga a fondo los problemas antes de proponer soluciones
  </Accordion>
</AccordionGroup>

<div id="switching-modes">
  ## Cambiar de modo
</div>

* Usa el menú desplegable del selector de modo en Agent
* Presiona <Kbd>Cmd+.</Kbd> para cambiar rápidamente
* Configura los atajos de teclado en [configuración](#settings)

<div id="settings">
  ## Configuración
</div>

Todos los modos comparten opciones de configuración comunes:

<div className="full-width-table">
  | Configuración     | Descripción                            |
  | :---------------- | :------------------------------------- |
  | Modelo            | Elige qué modelo de IA usar            |
  | Atajos de teclado | Define atajos para cambiar entre modos |
</div>

Configuraciones específicas por modo:

<div className="full-width-table">
  | Modo       | Configuraciones               | Descripción                                                 |
  | :--------- | :---------------------------- | :---------------------------------------------------------- |
  | **Agent**  | Auto-run y Auto-fix Errors    | Ejecuta comandos automáticamente y corrige errores          |
  | **Ask**    | Search Codebase               | Encuentra automáticamente los archivos relevantes           |
  | **Custom** | Tool selection & Instructions | Configura [tools](/es/agent/tools) y prompts personalizados |
</div>



# Descripción general
Source: https://docs.cursor.com/es/agent/overview

Asistente para tareas de programación autónomas, comandos de terminal y edición de código

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

Agent es el asistente de Cursor que puede completar tareas de programación complejas por sí solo, ejecutar comandos en la terminal y editar código. Accede desde el panel lateral con <Kbd>Cmd+I</Kbd>.

<Frame caption="Agent en el panel lateral">
  <video src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/overview.mp4?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=b17d6a1225b4992ea19978b6a6c259e1" autoPlay loop muted playsInline data-path="images/chat/overview.mp4" />
</Frame>

<div className="mt-24 flex flex-col gap-12">
  <Columns className="gap-4">
    <div>
      <h2 className="text-lg font-medium mb-2">
        <a href="/es/agent/modes" className="hover:text-primary transition-colors">
          Modos
        </a>
      </h2>

      <p className="text-sm">
        Elegí entre Agent, Ask o creá modos personalizados. Cada modo ofrece
        distintas capacidades y herramientas para adaptarse a tu flujo de trabajo.
      </p>
    </div>

    <Frame>
      <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/agent.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=9cd06dd9f59e019b3d76aa0fd9f934ba" alt="Modos de Agent" data-og-width="3600" width="3600" data-og-height="2025" height="2025" data-path="images/chat/agent.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/agent.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=d979435c61e2112ebcb784f16a49327f 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/agent.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=1a88e2085ffe80f02daea9a523887282 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/agent.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=de98a8bf766c3f35a6187e87190e30f9 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/agent.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=8648638c4240b718e0512a6ec2274171 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/agent.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=45b9898d65f5b425d276eaa44d4e1940 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/agent.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=30fef2b190d453ee0166e554a4005bd1 2500w" />
    </Frame>
  </Columns>

  <Columns className="gap-4">
    <div>
      <h3 className="text-lg font-medium mb-2">
        <a href="/es/agent/tools" className="hover:text-primary transition-colors">
          Herramientas
        </a>
      </h3>

      <p className="text-sm">
        Agent utiliza herramientas para buscar, editar y ejecutar comandos. Desde la
        búsqueda semántica en la base de código hasta la ejecución en la terminal, estas
        herramientas permiten completar tareas de forma autónoma.
      </p>
    </div>

    <div>
      <Frame>
        <img src="https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=3135722076a5aa636d27dbedec665bae" alt="Herramientas de Agent" data-og-width="1624" width="1624" data-og-height="1012" height="1012" data-path="images/agent/auto-run.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=280&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=9f2e2bed8f634201adc51ccb2bd96cd2 280w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=560&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=51704cac2f270a04856fffbeaccf9700 560w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=840&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=01a5034975497a8dff4f41dca0d19f2e 840w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=1100&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=5f19026a0c6e5fb28c935ce795edb706 1100w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=1650&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=a108fc86f8ee7c0db6e5b7ab80ede738 1650w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=2500&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=9ce5f45879c29049640bb5a1494db11e 2500w" />
      </Frame>
    </div>
  </Columns>

  <Columns className="gap-4">
    <div>
      <h3 className="text-lg font-medium mb-2">
        <a href="/es/agent/apply" className="hover:text-primary transition-colors">
          Aplicar cambios
        </a>
      </h3>

      <p className="text-sm">
        Integra bloques de código sugeridos por IA en tu codebase. Apply gestiona
        cambios a gran escala de forma eficiente sin perder precisión.
      </p>
    </div>

    <div>
      <Frame>
        <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/apply.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=634492fa2f63b4f6eada08b2a1ded47e" alt="Aplicar cambios" data-og-width="1032" width="1032" data-og-height="410" height="410" data-path="images/chat/apply.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/apply.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=7dbc88cfe20429c73e627a289b17c964 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/apply.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=721e2d51bdb16dbb817e19d96d93c9d9 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/apply.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=8faea188ca903e58d347ddfec2c9bf6e 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/apply.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=f3bc38701cab63602b54374dfaa9e024 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/apply.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=fddad51f5b12c32493e2370ed326712d 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/apply.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=1584d431007b33a595905e23b5e1b453 2500w" />
      </Frame>
    </div>
  </Columns>

  <Columns className="gap-4">
    <div>
      <h3 className="text-lg font-medium mb-2">
        <a href="/es/agent/review" className="hover:text-primary transition-colors">
          Revisar diffs
        </a>
      </h3>

      <p className="text-sm">
        Revisa los cambios antes de aceptarlos. La interfaz de revisión muestra añadidos
        y eliminaciones con líneas codificadas por color para que tengas control sobre las modificaciones.
      </p>
    </div>

    <div>
      <Frame>
        <video src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/review/review-bar.mp4?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=5dca0fe7aba3c79e6760cb264821a617" autoPlay loop muted playsInline controls data-path="images/chat/review/review-bar.mp4" />
      </Frame>
    </div>
  </Columns>

  <Columns className="gap-4">
    <div>
      <h3 className="text-lg font-medium mb-2">
        <a href="/es/agent/chats/tabs" className="hover:text-primary transition-colors">
          Pestañas de chat
        </a>
      </h3>

      <p className="text-sm">
        Lleva varias conversaciones a la vez con <Kbd>Cmd+T</Kbd>. Cada pestaña
        mantiene su propio contexto, historial y modelo seleccionado.
      </p>
    </div>

    <div>
      <Frame>
        <video src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/chat-tabs.mp4?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=57fd5305279dc0a3139055b353ce4b7a" autoPlay loop muted playsInline controls data-path="images/chat/chat-tabs.mp4" />
      </Frame>
    </div>
  </Columns>

  <Columns className="gap-4">
    <div>
      <h3 className="text-lg font-medium mb-2">
        <a href="/es/agent/chats/checkpoints" className="hover:text-primary transition-colors">
          Checkpoints
        </a>
      </h3>

      <p className="text-sm">
        Las instantáneas automáticas registran los cambios del Agent. Restaura estados anteriores si
        los cambios no funcionan como esperabas o para probar enfoques distintos.
      </p>
    </div>

    <div>
      <Frame>
        <video src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/restore-checkpoint.mp4?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=7cededf7892f15a6342a81953ea0aa38" autoPlay loop muted playsInline controls data-path="images/chat/restore-checkpoint.mp4" />
      </Frame>
    </div>
  </Columns>

  <Columns className="gap-4">
    <div>
      <h3 className="text-lg font-medium mb-2">
        <a href="/es/agent/terminal" className="hover:text-primary transition-colors">
          Integración con la terminal
        </a>
      </h3>

      <p className="text-sm">
        Agent ejecuta comandos en la terminal, supervisa la salida y gestiona procesos
        de varios pasos. Configura la ejecución automática para flujos de trabajo de
        confianza o pide confirmación por seguridad.
      </p>
    </div>

    <div>
      <Frame>
        <img src="https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=3135722076a5aa636d27dbedec665bae" alt="Integración con la terminal" data-og-width="1624" width="1624" data-og-height="1012" height="1012" data-path="images/agent/auto-run.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=280&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=9f2e2bed8f634201adc51ccb2bd96cd2 280w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=560&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=51704cac2f270a04856fffbeaccf9700 560w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=840&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=01a5034975497a8dff4f41dca0d19f2e 840w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=1100&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=5f19026a0c6e5fb28c935ce795edb706 1100w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=1650&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=a108fc86f8ee7c0db6e5b7ab80ede738 1650w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=2500&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=9ce5f45879c29049640bb5a1494db11e 2500w" />
      </Frame>
    </div>
  </Columns>

  <Columns className="gap-4">
    <div>
      <h3 className="text-lg font-medium mb-2">
        <a href="/es/agent/chats/history" className="hover:text-primary transition-colors">
          Historial de chat
        </a>
      </h3>

      <p className="text-sm">
        Accede a conversaciones anteriores con <Kbd>Opt Cmd '</Kbd>. Revisa
        chats previos, sigue tus sesiones de código y consulta el contexto de
        conversaciones anteriores.
      </p>
    </div>

    <div>
      <Frame>
        <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/chat-history.jpeg?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=d9ec96fad0c8c2fb132bbf5ce8ea35f7" alt="Historial de chat" data-og-width="2048" width="2048" data-og-height="1317" height="1317" data-path="images/chat/chat-history.jpeg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/chat-history.jpeg?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=a3ad71e9891c3c9642f4288953a78e97 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/chat-history.jpeg?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=76139a177ebfeb0c55add7fb955f9000 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/chat-history.jpeg?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=1af22180859c017542777ab36b434b7a 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/chat-history.jpeg?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=751e7fa0888e5790f841432ef7521337 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/chat-history.jpeg?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=86b447c18601a9d44af8866d0042719e 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/chat-history.jpeg?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=88c84a8fb1b764ad3070e3211f539408 2500w" />
      </Frame>
    </div>
  </Columns>

  <Columns className="gap-4">
    <div>
      <h3 className="text-lg font-medium mb-2">
        <a href="/es/agent/chats/export" className="hover:text-primary transition-colors">
          Exportar chats
        </a>
      </h3>

      <p className="text-sm">
        Exporta conversaciones en formato Markdown. Comparte soluciones con tu equipo, documenta decisiones o crea bases de conocimiento a partir de sesiones de programación.
      </p>
    </div>

    <div>
      <Frame>
        <video src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/export-chat.mp4?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=c6aa9d23a6a80ffae5864cd494907961" autoPlay loop muted playsInline controls data-path="images/chat/export-chat.mp4" />
      </Frame>
    </div>
  </Columns>

  <Columns className="gap-4">
    <div>
      <h3 className="text-lg font-medium mb-2">
        <a href="/es/context/rules" className="hover:text-primary transition-colors">
          Reglas
        </a>
      </h3>

      <p className="text-sm">
        Define instrucciones personalizadas para el comportamiento de Agent. Las reglas ayudan a mantener estándares de codificación, aplicar patrones y personalizar cómo Agent te asiste en tu proyecto.
      </p>
    </div>

    <div>
      <Frame>
        <img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rules-applied.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=e637bab83cfd5dcc8a3b15ed6fd9fc15" alt="Reglas de Agent" data-og-width="1198" width="1198" data-og-height="674" height="674" data-path="images/context/rules/rules-applied.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rules-applied.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=78e3c392987c6f95a02fc106753c5f98 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rules-applied.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=9d3a8b76ba99ada5ca302cba9fb63810 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rules-applied.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=f5ab7fb374a1a4c5fe2f50e2e50d233a 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rules-applied.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=5d25394a29c1da4172a3e673ee384c07 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rules-applied.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=0fc125bd3c2a93551674252c0523d3ec 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rules-applied.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=c576ea053ee18c30d2781c6bdd394a70 2500w" />
      </Frame>
    </div>
  </Columns>
</div>



# Planificación
Source: https://docs.cursor.com/es/agent/planning

Cómo Agent planifica y gestiona tareas complejas con to-dos y colas

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

Agent puede planificar con anticipación y gestionar tareas complejas con listas de tareas estructuradas y cola de mensajes, lo que facilita entender y hacer seguimiento de tareas de largo plazo.

<div id="agent-to-dos">
  ## Tareas pendientes de Agent
</div>

Agent puede dividir tareas largas en pasos manejables con dependencias, creando un plan estructurado que se actualiza conforme avanza el trabajo.

<video autoPlay loop muted playsInline controls>
  <source src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/agent/planning/agent-todo.mp4?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=b0285913832a3ef123fe149516ee37ea" type="video/mp4" data-path="images/agent/planning/agent-todo.mp4" />
</video>

<div id="how-it-works">
  ### Cómo funciona
</div>

* Agent crea automáticamente listas de pendientes para tareas complejas
* Cada ítem puede depender de otras tareas
* La lista se actualiza en tiempo real a medida que avanza el trabajo
* Las tareas completadas se marcan automáticamente

<div id="visibility">
  ### Visibilidad
</div>

* Las tareas pendientes aparecen en la interfaz del chat
* Si la [integración con Slack](/es/slack) está configurada, las tareas también se ven ahí
* Podés ver el desglose completo de la tarea en cualquier momento

<Tip>
  Para planificar mejor, describí claramente tu objetivo final. Agent creará desgloses de tareas más
  precisos cuando entienda el alcance completo.
</Tip>

<Note>La planificación y las tareas pendientes no están disponibles actualmente en el modo auto.</Note>

<div id="queued-messages">
  ## Mensajes en cola
</div>

Pon mensajes de seguimiento en cola mientras Agent trabaja en la tarea actual. Tus instrucciones esperan su turno y se ejecutan automáticamente cuando estén listas.

<video autoPlay loop muted playsInline controls>
  <source src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/agent/planning/agent-queue.mp4?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=4cdd6a7d1e12c67e520bc3ba67a42e0d" type="video/mp4" data-path="images/agent/planning/agent-queue.mp4" />
</video>

<div id="using-the-queue">
  ### Uso de la cola
</div>

1. Mientras Agent está trabajando, escribe tu siguiente instrucción
2. Pulsa <Kbd>Ctrl+Enter</Kbd> para añadirla a la cola
3. Los mensajes aparecen en orden debajo de la tarea activa
4. Reordena los mensajes en cola haciendo clic en la flecha
5. Agent los procesa secuencialmente al terminar

<div id="override-the-queue">
  ### Omitir la cola
</div>

Para poner tu mensaje en cola en lugar de usar la mensajería predeterminada, usa <Kbd>Ctrl+Enter</Kbd>. Para enviar un mensaje de inmediato sin ponerlo en cola, usa <Kbd>Cmd+Enter</Kbd>. Esto “empuja” tu mensaje a la fuerza, omitiendo la cola para ejecutarlo de inmediato.

<div id="default-messaging">
  ## Mensajería predeterminada
</div>

De forma predeterminada, los mensajes se envían lo más rápido posible, generalmente apareciendo justo después de que Agent complete una llamada a una herramienta. Esto ofrece la experiencia más ágil.

<div id="how-default-messaging-works">
  ### Cómo funciona la mensajería predeterminada
</div>

* Tu mensaje se añade al mensaje de usuario más reciente en el chat
* Los mensajes suelen adjuntarse a los resultados de las herramientas y se envían en cuanto están listos
* Esto crea un flujo de conversación más natural sin interrumpir el trabajo actual de Agent
* Por defecto, esto ocurre cuando presionas Enter mientras Agent está trabajando



# Diffs y revisión
Source: https://docs.cursor.com/es/agent/review

Revisa y gestiona los cambios de código generados por el agente de IA

Cuando Agent genera cambios de código, se muestran en una interfaz de revisión que marca adiciones y eliminaciones con líneas codificadas por color. Esto te permite revisar y controlar qué cambios se aplican a tu base de código.

La interfaz de revisión muestra los cambios de código en un formato diff familiar:

<div id="diffs">
  ## Diffs
</div>

<div className="full-width-table">
  | Tipo                   | Significado                      | Ejemplo                                                                                               |
  | :--------------------- | :------------------------------- | :---------------------------------------------------------------------------------------------------- |
  | **Líneas añadidas**    | Nuevas incorporaciones de código | <code className="bg-green-100 text-green-800 px-2 py-1 rounded">+ const newVariable = 'hello';</code> |
  | **Líneas eliminadas**  | Eliminaciones de código          | <code className="bg-red-100 text-red-800 px-2 py-1 rounded">- const oldVariable = 'goodbye';</code>   |
  | **Líneas de contexto** | Código circundante sin cambios   | <code className="bg-gray-100 text-gray-600 px-2 py-1 rounded"> function example() {}</code>           |
</div>

<div id="review">
  ## Revisión
</div>

Cuando termine la generación, vas a ver un aviso para revisar todos los cambios antes de continuar. Esto te da una vista general de lo que se va a modificar.

<Frame>
  <img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/review/input-review.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=10633167c76c24c1e69748ef93dc3888" alt="Interfaz de revisión de entrada" data-og-width="2095" width="2095" data-og-height="1178" height="1178" data-path="images/chat/review/input-review.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/review/input-review.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=f462337898ca48f71cd2b570b140d30d 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/review/input-review.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=07c91dfc92110cce444da8bbf3d0b3b5 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/review/input-review.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=492522862dabae6243fa8d33f6fd77f2 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/review/input-review.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=c897e19ce7f508bad4e24fcf8efb2512 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/review/input-review.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=3956c2d2c5c9156181b19e262e301b5b 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/review/input-review.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=907f90b1db432128964a7f4e59523bb6 2500w" />
</Frame>

<div id="file-by-file">
  ### Archivo por archivo
</div>

Aparece una barra de revisión flotante en la parte inferior de tu pantalla que te permite:

* **Aceptar** o **rechazar** cambios del archivo actual
* Ir al **siguiente archivo** con cambios pendientes
  <Frame>
    <video src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/review/review-bar.mp4?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=5dca0fe7aba3c79e6760cb264821a617" autoPlay loop muted playsInline controls data-path="images/chat/review/review-bar.mp4">
      Tu navegador no admite la etiqueta de video.
    </video>
  </Frame>

<div id="selective-acceptance">
  ### Aceptación selectiva
</div>

Para un control más preciso:

* Para aceptar la mayoría de los cambios: rechazá las líneas que no querés y después hacé clic en **Aceptar todo**
* Para rechazar la mayoría de los cambios: aceptá las líneas que sí querés y después hacé clic en **Rechazar todo**

<div id="review-changes">
  ## Revisar cambios
</div>

Al final de la respuesta del agente, haz clic en el botón **Revisar cambios** para ver el diff completo de las modificaciones.

<Frame>
  <video src="https://www.cursor.com/changelog/049/review-ui.mp4" autoPlay loop muted playsInline controls />
</Frame>



# Terminal
Source: https://docs.cursor.com/es/agent/terminal

Ejecuta comandos de la terminal automáticamente como parte de las operaciones del agente

El agente ejecuta comandos en la terminal nativa de Cursor y conserva el historial. Haz clic en Skip para enviar <kbd>Ctrl+C</kbd> y detener los comandos.

<div id="troubleshooting">
  ## Solución de problemas
</div>

<Info>
  Algunos temas de shell (por ejemplo, Powerlevel9k/Powerlevel10k) pueden interferir con
  la salida del terminal en línea. Si la salida de tu comando aparece truncada o
  con un formato incorrecto, desactiva el tema o cambia a un prompt más simple cuando se ejecute Agent.
</Info>

<div id="disable-heavy-prompts-for-agent-sessions">
  ### Desactiva prompts pesados para sesiones de Agent
</div>

Usa la variable de entorno `CURSOR_AGENT` en la configuración de tu shell para detectar cuándo
se está ejecutando Agent y saltarte la inicialización de prompts/temas vistosos.

```zsh  theme={null}

# ~/.zshrc — desactiva Powerlevel10k cuando se ejecute Cursor Agent
if [[ -n "$CURSOR_AGENT" ]]; then
  # Omitir la inicialización del tema para mejorar la compatibilidad
else
  [[ -r ~/.p10k.zsh ]] && source ~/.p10k.zsh
fi
```

```bash  theme={null}

# ~/.bashrc — usar un prompt simple en sesiones del Agent
if [[ -n "$CURSOR_AGENT" ]]; then
  PS1='\u@\h \W \$ '
fi
```



# Herramientas
Source: https://docs.cursor.com/es/agent/tools

Herramientas disponibles para que los agentes busquen, editen y ejecuten código

Una lista de todas las herramientas disponibles para los modos dentro de [Agent](/es/agent/overview), que podés habilitar o deshabilitar al crear tus propios [modos personalizados](/es/agent/modes#custom).

<Note>
  No hay límite en la cantidad de llamadas a herramientas que Agent puede hacer durante una tarea. Agent seguirá usando herramientas según sea necesario para completar tu pedido.
</Note>

<div id="search">
  ## Búsqueda
</div>

Herramientas para buscar en tu código y en la web y encontrar información relevante.

<AccordionGroup>
  <Accordion title="Read File" icon="file-lines">
    Lee hasta 250 líneas (750 en modo máximo) de un archivo.
  </Accordion>

  <Accordion title="List Directory" icon="folder-open">
    Lee la estructura de un directorio sin leer el contenido de los archivos.
  </Accordion>

  <Accordion title="Codebase" icon="database">
    Realiza búsquedas semánticas en tu [código
    indexado](/es/context/codebase-indexing).
  </Accordion>

  <Accordion title="Grep" icon="magnifying-glass">
    Busca palabras clave o patrones exactos dentro de archivos.
  </Accordion>

  <Accordion title="Search Files" icon="file-magnifying-glass">
    Encuentra archivos por nombre usando coincidencia difusa.
  </Accordion>

  <Accordion title="Web" icon="globe">
    Genera consultas y realiza búsquedas en la web.
  </Accordion>

  <Accordion title="Fetch Rules" icon="gavel">
    Obtén [reglas](/es/context/rules) específicas según el tipo y la descripción.
  </Accordion>
</AccordionGroup>

<div id="edit">
  ## Editar
</div>

Herramientas para hacer cambios específicos en tus archivos y tu código.

<AccordionGroup>
  <Accordion title="Editar y reaplicar" icon="pencil">
    Sugiere cambios en archivos y [aplícalos](/es/agent/apply) automáticamente.
  </Accordion>

  <Accordion title="Eliminar archivo" icon="trash">
    Elimina archivos de forma autónoma (puedes desactivarlo en la configuración).
  </Accordion>
</AccordionGroup>

<div id="run">
  ## Ejecutar
</div>

Chat puede interactuar con tu terminal.

<AccordionGroup>
  <Accordion title="Terminal" icon="terminal">
    Ejecuta comandos en la terminal y monitorea la salida.
  </Accordion>
</AccordionGroup>

<Note>De forma predeterminada, Cursor usa el primer perfil de terminal disponible.</Note>

Para establecer tu perfil de terminal preferido:

1. Abre la paleta de comandos (`Cmd/Ctrl+Shift+P`)
2. Busca "Terminal: Select Default Profile"
3. Elige el perfil que quieras

<div id="mcp">
  ## MCP
</div>

Chat puede usar servidores MCP configurados para interactuar con servicios externos, como bases de datos o API de terceros.

<AccordionGroup>
  <Accordion title="Activar/desactivar servidores MCP" icon="server">
    Activa o desactiva los servidores MCP disponibles. Respeta la configuración de ejecución automática.
  </Accordion>
</AccordionGroup>

Aprende más sobre el [Model Context Protocol](/es/context/model-context-protocol) y explora los servidores disponibles en el [directorio de MCP](/es/tools).

<div id="advanced-options">
  ## Opciones avanzadas
</div>

<AccordionGroup>
  <Accordion title="Aplicar ediciones automáticamente" icon="check">
    Aplica las ediciones automáticamente sin confirmación manual.
  </Accordion>

  <Accordion title="Ejecución automática" icon="play">
    Ejecuta automáticamente comandos de terminal y acepta ediciones. Útil para ejecutar suites de pruebas y verificar cambios.

    <Frame>
      <img src="https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=3135722076a5aa636d27dbedec665bae" data-og-width="1624" width="1624" data-og-height="1012" height="1012" data-path="images/agent/auto-run.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=280&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=9f2e2bed8f634201adc51ccb2bd96cd2 280w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=560&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=51704cac2f270a04856fffbeaccf9700 560w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=840&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=01a5034975497a8dff4f41dca0d19f2e 840w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=1100&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=5f19026a0c6e5fb28c935ce795edb706 1100w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=1650&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=a108fc86f8ee7c0db6e5b7ab80ede738 1650w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=2500&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=9ce5f45879c29049640bb5a1494db11e 2500w" />
    </Frame>
  </Accordion>

  <Accordion title="Guardrails" icon="shield">
    Configura listas de permitidos para especificar qué herramientas pueden ejecutarse automáticamente. Estas listas mejoran la seguridad al definir explícitamente las operaciones permitidas.
  </Accordion>

  <Accordion title="Corregir errores automáticamente" icon="wrench">
    Resuelve automáticamente los errores y advertencias del linter cuando el Agent los encuentre.
  </Accordion>
</AccordionGroup>



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



# Agregar seguimiento
Source: https://docs.cursor.com/es/background-agent/api/add-followup

en/background-agent/api/openapi.yaml post /v0/agents/{id}/followup
Envía una instrucción adicional a un agente en segundo plano que está en ejecución.




# Conversación del agente
Source: https://docs.cursor.com/es/background-agent/api/agent-conversation

en/background-agent/api/openapi.yaml get /v0/agents/{id}/conversation
Recupera el historial de conversaciones de un agente en segundo plano.

Si el agente en segundo plano se eliminó, no vas a poder acceder a la conversación.



# Estado del agente
Source: https://docs.cursor.com/es/background-agent/api/agent-status

en/background-agent/api/openapi.yaml get /v0/agents/{id}
Obtén el estado actual y los resultados de un agente específico en segundo plano.




# Información de la clave de API
Source: https://docs.cursor.com/es/background-agent/api/api-key-info

en/background-agent/api/openapi.yaml get /v0/me
Obtén metadatos sobre la clave de API utilizada para la autenticación.




# Eliminar un agente
Source: https://docs.cursor.com/es/background-agent/api/delete-agent

en/background-agent/api/openapi.yaml delete /v0/agents/{id}
Eliminar permanentemente un agente en segundo plano y sus recursos asociados.




# Iniciar un agente
Source: https://docs.cursor.com/es/background-agent/api/launch-an-agent

en/background-agent/api/openapi.yaml post /v0/agents
Inicia un nuevo agente en segundo plano para trabajar en tu repositorio.




# Listar agentes
Source: https://docs.cursor.com/es/background-agent/api/list-agents

en/background-agent/api/openapi.yaml get /v0/agents
Obtén una lista paginada de todos los agentes en segundo plano del usuario autenticado.




# Listar modelos
Source: https://docs.cursor.com/es/background-agent/api/list-models

en/background-agent/api/openapi.yaml get /v0/models
Obtén una lista de modelos recomendados para agentes en segundo plano.

Si querés definir el modelo del agente en segundo plano al crearlo, podés usar este endpoint para ver una lista de modelos recomendados.

En ese caso, también te recomendamos ofrecer una opción "Auto", en la que no envíes un nombre de modelo al endpoint de creación y nosotros elegimos el modelo más adecuado.



# Listar repositorios de GitHub
Source: https://docs.cursor.com/es/background-agent/api/list-repositories

en/background-agent/api/openapi.yaml get /v0/repositories
Obtén una lista de repositorios de GitHub a los que tiene acceso el usuario autenticado.

<Warning>
  **Este endpoint tiene límites de tasa muy estrictos.**

  Limita las solicitudes a **1/usuario/minuto** y **30/usuario/hora**.

  Esta solicitud puede tardar decenas de segundos en responder para usuarios con acceso a muchos repositorios.

  Asegúrate de manejar correctamente cuando esta información no esté disponible.
</Warning>



# Descripción general
Source: https://docs.cursor.com/es/background-agent/api/overview

Crea y administra por programación agentes en segundo plano que trabajen en tus repositorios

<div id="background-agents-api">
  # API de Background Agents
</div>

<Badge variant="beta">Beta</Badge>

La API de Background Agents te permite crear y gestionar de forma programática agentes de codificación con IA que trabajan de manera autónoma en tus repositorios.
Podés usar la API para responder automáticamente al feedback de usuarios, corregir bugs, actualizar la documentación y mucho más.

<Info>
  La API de Background Agents está en beta, ¡nos encantaría tu feedback!
</Info>

<div id="key-features">
  ## Funcionalidades clave
</div>

* **Generación de código autónoma** - Crea agentes que entiendan tu prompt y hagan cambios en tu base de código
* **Integración con repositorios** - Trabaja directamente con repositorios de GitHub
* Prompts de seguimiento - Añade instrucciones adicionales a agentes en ejecución
* **Precios según uso** - Paga solo por los tokens que uses
* **Escalable** - Compatible con hasta 256 agentes activos por clave de API

<div id="quick-start">
  ## Inicio rápido
</div>

<div id="1-get-your-api-key">
  ### 1. Obtén tu clave de API
</div>

**Ve** a [Cursor Dashboard → Integrations](https://cursor.com/dashboard?tab=integrations) para crear tu clave de API.

<div id="2-start-using-the-api">
  ### 2. Empieza a usar la API
</div>

Todos los endpoints de la API son relativos a:

```
https://api.cursor.com
```

Consulta la [referencia de la API](/es/background-agent/api/launch-an-agent) para obtener una lista detallada de endpoints.

<div id="authentication">
  ## Autenticación
</div>

Todas las solicitudes a la API requieren autenticación con un token Bearer:

```
Authorization: Bearer TU_CLAVE_DE_API
```

Las claves de API se crean en el [Cursor Dashboard](https://cursor.com/dashboard?tab=integrations). Las claves están asociadas a tu cuenta y te permiten crear y administrar agentes (según los límites de tu plan y el acceso a los repositorios).

<div id="pricing">
  ## Precios
</div>

La API está actualmente en beta y tiene la misma tarifa que Background Agents. Los precios pueden cambiar a medida que escalemos el servicio. Consulta [Background Agent pricing](/es/account/pricing#background-agent).

<div id="next-steps">
  ## Próximos pasos
</div>

* Lee la [introducción general a Background Agents](/es/background-agent) para entender entornos, permisos y flujos de trabajo.
* Prueba Background Agents desde [web y móvil](/es/background-agent/web-and-mobile).
* Únete a la discusión en [Discord #background-agent](https://discord.gg/jfgpZtYpmb) o escribe a [background-agent-feedback@cursor.com](mailto:background-agent-feedback@cursor.com).



# Webhooks
Source: https://docs.cursor.com/es/background-agent/api/webhooks

Recibe notificaciones en tiempo real sobre cambios en el estado del agente en segundo plano

<div id="webhooks">
  # Webhooks
</div>

Cuando creas un agente con una URL de webhook, Cursor enviará solicitudes HTTP POST para notificarte sobre cambios de estado. Actualmente, solo se admiten eventos `statusChange`, específicamente cuando un agente entra en estado `ERROR` o `FINISHED`.

<div id="webhook-verification">
  ## Verificación de webhooks
</div>

Para asegurarte de que las solicitudes de webhook provienen auténticamente de Cursor, verificá la firma incluida con cada solicitud:

<div id="headers">
  ### Encabezados
</div>

Cada solicitud de webhook incluye los siguientes encabezados:

* **`X-Webhook-Signature`** – Contiene la firma HMAC-SHA256 con el formato `sha256=<hex_digest>`
* **`X-Webhook-ID`** – Un identificador único para esta entrega (útil para el logging)
* **`X-Webhook-Event`** – El tipo de evento (actualmente solo `statusChange`)
* **`User-Agent`** – Siempre establecido en `Cursor-Agent-Webhook/1.0`

<div id="signature-verification">
  ### Verificación de firma
</div>

Para verificar la firma del webhook, calculá la firma esperada y comparala con la firma recibida:

```javascript  theme={null}
const crypto = require('crypto');

function verifyWebhook(secret, rawBody, signature) {
  const firmaEsperada = 'sha256=' +
    crypto.createHmac('sha256', secret)
          .update(rawBody)
          .digest('hex');
  
  return signature === expectedSignature;
}
```

```python  theme={null}
import hmac
import hashlib

def verify_webhook(secret, raw_body, signature):
    firma_esperada = 'sha256=' + hmac.new(
        secret.encode(),
        raw_body,
        hashlib.sha256
    ).hexdigest()
    
    return signature == expected_signature
```

Usa siempre el cuerpo sin procesar de la solicitud (antes de cualquier parsing) al calcular la firma.

<div id="payload-format">
  ## Formato del payload
</div>

El payload del webhook se envía como JSON con la siguiente estructura:

```json  theme={null}
{
  "event": "statusChange",
  "timestamp": "2024-01-15T10:30:00Z",
  "id": "bc_abc123",
  "status": "FINISHED",
  "source": {
    "repository": "https://github.com/your-org/your-repo",
    "ref": "main"
  },
  "target": {
    "url": "https://cursor.com/agents?id=bc_abc123",
    "branchName": "cursor/add-readme-1234",
    "prUrl": "https://github.com/your-org/your-repo/pull/1234"
  },
  "summary": "Se agregó README.md con instrucciones de instalación"
}
```

Ten en cuenta que algunos campos son opcionales y solo se incluirán cuando estén disponibles.

<div id="best-practices">
  ## Mejores prácticas
</div>

* **Verifica las firmas** – Verifica siempre la firma del webhook para asegurarte de que la solicitud venga de Cursor
* **Maneja los reintentos** – Los webhooks pueden reintentarse si tu endpoint devuelve un código de estado de error
* **Responde rápido** – Devuelve un código de estado 2xx lo antes posible
* **Usa HTTPS** – Usa siempre URLs HTTPS para los endpoints de webhooks en producción
* **Almacena el payload sin procesar** – Guarda el payload del webhook sin procesar para depuración y verificación futuras



# Web y móvil
Source: https://docs.cursor.com/es/background-agent/web-and-mobile

Ejecuta agentes de código desde cualquier dispositivo con traspaso fluido al escritorio

<div id="overview">
  ## Descripción general
</div>

El agente de Cursor en la web lleva un potente asistente de código a cualquier dispositivo. Ya sea que estés con el teléfono mientras caminás o trabajando en el navegador, ahora podés arrancar agentes de código potentes que trabajan en segundo plano.
Cuando terminen, retomá su trabajo en Cursor, revisá y mergeá cambios, o compartí enlaces con tu equipo para colaborar.

Empezá en [cursor.com/agents](https://cursor.com/agents).

<Frame><img src="https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/webagent/cursor-web-1.png?fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=79c7d14df82cfcae369bccb8a1431cf3" alt="Interfaz del agente web de Cursor" data-og-width="4095" width="4095" data-og-height="2048" height="2048" data-path="images/webagent/cursor-web-1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/webagent/cursor-web-1.png?w=280&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=099c28633151e6c20eebc7fe03b3d420 280w, https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/webagent/cursor-web-1.png?w=560&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=452e0216c7e270d760072032f1e2b36d 560w, https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/webagent/cursor-web-1.png?w=840&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=baaa4a73d4822b5daa293814dc201d37 840w, https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/webagent/cursor-web-1.png?w=1100&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=8c5255fbf16aa60924e78a8285afb95d 1100w, https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/webagent/cursor-web-1.png?w=1650&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=7cc5a04ff6b24ad4ce0cfb4a35a9919c 1650w, https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/webagent/cursor-web-1.png?w=2500&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=f5f1b15fa508e20f89a4089f81417774 2500w" /></Frame>

<div id="getting-started">
  ## Primeros pasos
</div>

<div id="quick-setup">
  ### Configuración rápida
</div>

1. **Visita la app web**: Entra a [cursor.com/agents](https://cursor.com/agents) desde cualquier dispositivo
2. **Inicia sesión**: Accede con tu cuenta de Cursor
3. **Conecta GitHub**: Vincula tu cuenta de GitHub para acceder a los repositorios
4. **Inicia tu primer agente**: Escribe una tarea y mira cómo el agente se pone a trabajar

<div id="mobile-installation">
  ### Instalación en móvil
</div>

Para la mejor experiencia en móvil, instala Cursor como una app web progresiva (PWA):

* **iOS**: Abre [cursor.com/agents](https://cursor.com/agents) en Safari, toca el botón de compartir y luego “Add to Home Screen”
* **Android**: Abre la URL en Chrome, toca el menú y luego “Add to Home Screen” o “Install App”

<Tip>
  Instalar como PWA ofrece una experiencia similar a una app nativa con: - Interfaz de pantalla completa - Arranques más rápidos - Ícono de la app en tu pantalla de inicio
</Tip>

<div id="working-across-devices">
  ## Trabajar en varios dispositivos
</div>

El Web and Mobile Agent está diseñado para funcionar con tu flujo de trabajo en el escritorio; haz clic en "Open in Cursor" para continuar el trabajo del agente en tu IDE.

<Frame><img src="https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/webagent/cursor-web-2.png?fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=352140fd4bf3f3d98a1e1b9f4a995cad" alt="Revisión y traspaso" data-og-width="4095" width="4095" data-og-height="2048" height="2048" data-path="images/webagent/cursor-web-2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/webagent/cursor-web-2.png?w=280&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=eedd50318503fd3d3961b6da27a386d9 280w, https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/webagent/cursor-web-2.png?w=560&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=fd8c730cf62a0af6f873945a6a23b90b 560w, https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/webagent/cursor-web-2.png?w=840&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=ac537cc639471556f1afa0e09425ef30 840w, https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/webagent/cursor-web-2.png?w=1100&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=d512cddda6890c0749a7ad6396682def 1100w, https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/webagent/cursor-web-2.png?w=1650&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=e208297f414976bcfeea6850b39e8abb 1650w, https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/webagent/cursor-web-2.png?w=2500&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=54683ff7f25750fdc788e87c30bb6d6d 2500w" /></Frame>

<div id="team-collaboration">
  ### Colaboración en equipo
</div>

* **Acceso compartido**: Comparte enlaces con miembros del equipo para colaborar en ejecuciones del agente.
* **Proceso de revisión**: Los colaboradores pueden revisar diffs y dar feedback.
* **Gestión de pull requests**: Crea, revisa y fusiona pull requests directamente desde la interfaz web.

<div id="slack-integration">
  ### Integración con Slack
</div>

Lanza agentes directamente desde Slack mencionando `@Cursor`, y, al iniciar agentes desde la web o el móvil, elige recibir notificaciones de Slack al finalizar.

<Card title="Usar Cursor en Slack" icon="slack" href="/es/slack">
  Obtén más información sobre cómo configurar y usar la integración con Slack, incluyendo
  cómo disparar agentes y recibir notificaciones.
</Card>

<div id="pricing">
  ## Precios
</div>

Los agentes web y móviles usan el mismo modelo de precios que los Agentes en Segundo Plano.

Obtén más información sobre los [precios de los Agentes en Segundo Plano](/es/account/pricing#background-agent).

<div id="troubleshooting">
  ## Solución de problemas
</div>

<AccordionGroup>
  <Accordion title="Agent runs are not starting">
    * Asegúrate de haber iniciado sesión y de tener conectada tu cuenta de GitHub. - Revisa
      que tengas los permisos necesarios en el repositorio. - También necesitas
      estar en una Prueba Pro o en un plan de pago con la facturación por uso habilitada. Para habilitar
      la facturación por uso, ve a la pestaña de configuración de tu
      [Dashboard](https://www.cursor.com/dashboard?tab=settings).
  </Accordion>

  <Accordion title="Can't see agent runs on mobile">
    Intenta actualizar la página o borrar la caché de tu navegador. Asegúrate de usar
    la misma cuenta en todos tus dispositivos.
  </Accordion>

  <Accordion title="Slack integration not working">
    Verifica que el administrador de tu espacio de trabajo haya instalado la app de Slack de Cursor y que
    tengas los permisos necesarios.
  </Accordion>
</AccordionGroup>



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

**Navigation:** [← Previous](./07-slack.md) | [Index](./index.md) | [Next →](./09-code-review.md)