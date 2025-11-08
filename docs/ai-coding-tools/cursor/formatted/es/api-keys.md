---
title: "API Keys"
source: "https://docs.cursor.com/es/settings/api-keys"
language: "es"
language_name: "Spanish"
---

# API Keys
Source: https://docs.cursor.com/es/settings/api-keys

Usa tu propio proveedor de LLM

Usa tus propias claves de API para enviar mensajes de IA ilimitados por tu cuenta. Cuando lo configures, Cursor usará tus claves de API para llamar directamente a los proveedores de LLM.

Para usar tu clave de API, ve a `Cursor Settings` > `Models` y escribe tus claves de API. Haz clic en **Verify**. Una vez validada, tu clave de API quedará habilitada.

<Warning>
  Las claves de API personalizadas solo funcionan con modelos de chat estándar. Las funciones que requieren modelos especializados (como Tab Completion) seguirán usando los modelos integrados de Cursor.
</Warning>

<div id="supported-providers">
  ## Proveedores compatibles
</div>

* **OpenAI** - Solo modelos de chat estándar, sin razonamiento. El selector de modelos mostrará los modelos de OpenAI disponibles.
* **Anthropic** - Todos los modelos de Claude disponibles a través de la API de Anthropic.
* **Google** - Modelos Gemini disponibles a través de la API de Google AI.
* **Azure OpenAI** - Modelos implementados en tu instancia de Azure OpenAI Service.
* **AWS Bedrock** - Usa claves de acceso de AWS, claves secretas o roles de IAM. Funciona con los modelos disponibles en tu configuración de Bedrock.

Se genera un ID externo único tras validar tu rol de IAM de Bedrock, que puedes añadir a la política de confianza de tu rol de IAM para mayor seguridad.

<div id="faq">
  ## Preguntas frecuentes
</div>

<AccordionGroup>
  <Accordion title="¿Mi clave de API se almacenará o saldrá de mi dispositivo?">
    Tu clave de API no se almacena, pero se envía a nuestro servidor con cada solicitud. Todas las solicitudes pasan por nuestro backend para el ensamblado final del prompt.
  </Accordion>
</AccordionGroup>

---

← Previous: [Modelos](./modelos.md) | [Index](./index.md) | Next: [Tab](./tab.md) →