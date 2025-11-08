---
title: "Reglas"
source: "https://docs.cursor.com/es/context/rules"
language: "es"
language_name: "Spanish"
---

# Reglas
Source: https://docs.cursor.com/es/context/rules

Controla cómo se comporta el modelo Agent con instrucciones reutilizables y con alcance.

Las reglas proporcionan instrucciones a nivel de sistema para Agent e Inline Edit. Pensalas como contexto, preferencias o flujos de trabajo persistentes para tus proyectos.

Cursor admite cuatro tipos de reglas:

<CardGroup cols={2}>
  <Card title="Project Rules" icon="folder-tree">
    Almacenadas en `.cursor/rules`, con control de versiones y aplicadas al alcance de tu base de código.
  </Card>

  <Card title="User Rules" icon="user">
    Globales para tu entorno de Cursor. Definidas en la configuración y siempre aplicadas.
  </Card>

  <Card title="AGENTS.md" icon="robot">
    Instrucciones para Agent en formato Markdown. Alternativa simple a `.cursor/rules`.
  </Card>

  <Card title=".cursorrules (Legacy)" icon="clock-rotate-left">
    Aún compatibles, pero obsoletas. Usá Project Rules en su lugar.
  </Card>
</CardGroup>

<div id="how-rules-work">
  ## Cómo funcionan las reglas
</div>

Los modelos de lenguaje grandes no retienen memoria entre completions. Las reglas proporcionan contexto persistente y reutilizable a nivel de prompt.

Cuando se aplican, los contenidos de las reglas se incluyen al inicio del contexto del modelo. Esto le da a la IA una guía coherente para generar código, interpretar ediciones o ayudar con flujos de trabajo.

<Frame>
  <img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rules-applied.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=e637bab83cfd5dcc8a3b15ed6fd9fc15" alt="Regla aplicada en el contexto con el chat" data-og-width="1198" width="1198" data-og-height="674" height="674" data-path="images/context/rules/rules-applied.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rules-applied.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=78e3c392987c6f95a02fc106753c5f98 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rules-applied.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=9d3a8b76ba99ada5ca302cba9fb63810 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rules-applied.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=f5ab7fb374a1a4c5fe2f50e2e50d233a 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rules-applied.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=5d25394a29c1da4172a3e673ee384c07 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rules-applied.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=0fc125bd3c2a93551674252c0523d3ec 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rules-applied.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=c576ea053ee18c30d2781c6bdd394a70 2500w" />
</Frame>

<Info>
  Las reglas se aplican a [Chat](/es/chat/overview) y a [Inline Edit](/es/inline-edit/overview). Las reglas activas se muestran en la barra lateral del agente.
</Info>

<div id="project-rules">
  ## Reglas del proyecto
</div>

Las reglas del proyecto se encuentran en `.cursor/rules`. Cada regla es un archivo y está bajo control de versiones. Pueden limitarse mediante patrones de ruta, invocarse manualmente o incluirse según su relevancia. Los subdirectorios pueden incluir su propio directorio `.cursor/rules` con alcance limitado a esa carpeta.

Usa las reglas del proyecto para:

* Codificar conocimiento específico del dominio sobre tu base de código
* Automatizar flujos de trabajo o plantillas específicos del proyecto
* Estandarizar decisiones de estilo o de arquitectura

<div id="rule-anatomy">
  ### Anatomía de una regla
</div>

Cada archivo de regla está escrito en **MDC** (`.mdc`), un formato que admite metadatos y contenido. Controla cómo se aplican las reglas desde el menú desplegable de tipo, que modifica las propiedades `description`, `globs`, `alwaysApply`.

| <span class="no-wrap">Rule Type</span>         | Description                                                                       |
| :--------------------------------------------- | :-------------------------------------------------------------------------------- |
| <span class="no-wrap">`Always`</span>          | Siempre incluida en el contexto del modelo                                        |
| <span class="no-wrap">`Auto Attached`</span>   | Incluida cuando se referencian archivos que coinciden con un patrón glob          |
| <span class="no-wrap">`Agent Requested`</span> | Disponible para la IA, que decide si incluirla. Debe proporcionar una descripción |
| <span class="no-wrap">`Manual`</span>          | Solo se incluye cuando se menciona explícitamente usando `@ruleName`              |

```
---
description: Plantilla de servicio RPC
globs:
alwaysApply: false
---

- Usa nuestro patrón interno de RPC al definir servicios
- Usa siempre snake_case para los nombres de los servicios.

@service-template.ts
```

<div id="nested-rules">
  ### Reglas anidadas
</div>

Organiza las reglas colocándolas en directorios `.cursor/rules` a lo largo de tu proyecto. Las reglas anidadas se aplican automáticamente cuando se hace referencia a archivos dentro de su directorio.

```
project/
  .cursor/rules/        # Reglas para todo el proyecto
  backend/
    server/
      .cursor/rules/    # Reglas específicas del backend
  frontend/
    .cursor/rules/      # Reglas específicas del frontend
```

<div id="creating-a-rule">
  ### Crear una regla
</div>

Crea reglas con el comando `New Cursor Rule` o desde `Cursor Settings > Rules`. Esto crea un nuevo archivo de regla en `.cursor/rules`. Desde la configuración puedes ver todas las reglas y su estado.

<Frame>
  <img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rule-settings.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=db8142786bbb7b7771ae0db8b2704b0b" alt="Comparación entre reglas concisas y extensas" data-og-width="6016" width="6016" data-og-height="3334" height="3334" data-path="images/context/rules/rule-settings.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rule-settings.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=0b6e9b8d6ca799d1af62957726b1cc52 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rule-settings.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=8bfe1482ab9afc0995fe13371b26074b 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rule-settings.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=a847d915b3f106c42cba7cb1245bb138 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rule-settings.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=356963b3607152f7ffe128cd1a2d050e 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rule-settings.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=1b1e50d3721d42c691a434189729921c 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rule-settings.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=d2081cf016d65053f1e517eb5734079e 2500w" />
</Frame>

<div id="generating-rules">
  ### Generar reglas
</div>

Genera reglas directamente en las conversaciones usando el comando `/Generate Cursor Rules`. Útil cuando ya definiste el comportamiento del agente y quieres reutilizarlo.

<Frame>
  <video src="https://www.cursor.com/changelog/049/generate-rules.mp4" controls>
    Tu navegador no admite la etiqueta de video.
  </video>
</Frame>

<div id="best-practices">
  ## Mejores prácticas
</div>

Las buenas reglas son concretas, accionables y bien acotadas.

* Mantén las reglas por debajo de 500 líneas
* Divide las reglas grandes en varias reglas componibles
* Proporciona ejemplos concretos o archivos de referencia
* Evita las indicaciones vagas. Escribe las reglas como documentación interna clara
* Reutiliza reglas cuando repitas prompts en el chat

<div id="examples">
  ## Ejemplos
</div>

<AccordionGroup>
  <Accordion title="Estándares para componentes de frontend y validación de API">
    Esta regla define estándares para componentes de frontend:

    Al trabajar en el directorio de components:

    * Usa siempre Tailwind para estilos
    * Usa Framer Motion para animaciones
    * Sigue las convenciones de nomenclatura de componentes

    Esta regla aplica validación para endpoints de API:

    En el directorio de API:

    * Usa zod para toda la validación
    * Define los tipos de retorno con esquemas de zod
    * Exporta los tipos generados a partir de los esquemas
  </Accordion>

  <Accordion title="Plantillas para servicios de Express y componentes de React">
    Esta regla proporciona una plantilla para servicios de Express:

    Usa esta plantilla al crear un servicio de Express:

    * Sigue los principios RESTful
    * Incluye middleware de manejo de errores
    * Configura un logging adecuado

    @express-service-template.ts

    Esta regla define la estructura de los componentes de React:

    Los componentes de React deben seguir este esquema:

    * Interfaz de Props al inicio
    * Componente como export nombrado
    * Estilos al final

    @component-template.tsx
  </Accordion>

  <Accordion title="Automatización de flujos de desarrollo y generación de documentación">
    Esta regla automatiza el análisis de la app:

    Cuando te pidan analizar la app:

    1. Ejecuta el servidor de desarrollo con `npm run dev`
    2. Obtén los logs de la consola
    3. Sugiere mejoras de rendimiento

    Esta regla ayuda a generar documentación:

    Ayuda a redactar documentación:

    * Extrayendo comentarios del código
    * Analizando README.md
    * Generando documentación en Markdown
  </Accordion>

  <Accordion title="Añadir una nueva configuración en Cursor">
    Primero crea una propiedad con toggle en `@reactiveStorageTypes.ts`.

    Añade el valor por defecto en `INIT_APPLICATION_USER_PERSISTENT_STORAGE` en `@reactiveStorageService.tsx`.

    Para funciones beta, agrega el toggle en `@settingsBetaTab.tsx`; de lo contrario, agrégalo en `@settingsGeneralTab.tsx`. Los toggles se pueden añadir como `<SettingsSubSection>` para checkboxes generales. Revisa el resto del archivo para ver ejemplos.

    ```
    <SettingsSubSection
    				label="Your feature name"
    				description="Your feature description"
    				value={
    					vsContext.reactiveStorageService.applicationUserPersistentStorage
    						.myNewProperty ?? false
    				}
    				onChange={(newVal) => {
    					vsContext.reactiveStorageService.setApplicationUserPersistentStorage(
    						'myNewProperty',
    						newVal
    					);
    				}}
    			/>
    ```

    Para usarlo en la app, importa reactiveStorageService y usa la propiedad:

    ```
    const flagIsEnabled = vsContext.reactiveStorageService.applicationUserPersistentStorage.myNewProperty
    ```
  </Accordion>
</AccordionGroup>

Hay muchos ejemplos disponibles de proveedores y frameworks. Las reglas aportadas por la comunidad se encuentran en colecciones y repositorios colaborativos en línea.

<div id="agentsmd">
  ## AGENTS.md
</div>

`AGENTS.md` es un archivo markdown simple para definir instrucciones de agentes. Ponlo en la raíz de tu proyecto como alternativa a `.cursor/rules` para casos de uso sencillos.

A diferencia de las Reglas del proyecto, `AGENTS.md` es un archivo markdown sin metadatos ni configuraciones complejas. Es perfecto para proyectos que necesitan instrucciones simples y fáciles de leer, sin la sobrecarga de reglas estructuradas.

```markdown  theme={null}

---

← Previous: [Memories](./memories.md) | [Index](./index.md) | Next: [Conceptos](./conceptos.md) →