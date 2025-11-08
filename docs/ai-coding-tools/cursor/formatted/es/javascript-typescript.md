---
title: "JavaScript & TypeScript"
source: "https://docs.cursor.com/es/guides/languages/javascript"
language: "es"
language_name: "Spanish"
---

# JavaScript & TypeScript
Source: https://docs.cursor.com/es/guides/languages/javascript

Desarrollo de JavaScript y TypeScript con soporte para frameworks

¡Bienvenido al desarrollo de JavaScript y TypeScript en Cursor! El editor ofrece soporte excepcional para el desarrollo en JS/TS a través de su ecosistema de extensiones. Esto es lo que necesitas saber para sacarle el máximo partido a Cursor.

<div id="essential-extensions">
  ## Extensiones esenciales
</div>

Aunque Cursor funciona muy bien con cualquier extensión que prefieras, recomendamos estas si apenas estás empezando:

* **ESLint** - Necesario para las funciones de corrección de lint con IA de Cursor
* **JavaScript and TypeScript Language Features** - Compatibilidad de lenguaje e IntelliSense mejoradas
* **Path Intellisense** - Autocompletado inteligente de rutas de archivos

<div id="cursor-features">
  ## Funciones de Cursor
</div>

Cursor potencia tu flujo de trabajo en JavaScript/TypeScript con:

* **Tab Completions**: autocompletados con contexto que entienden la estructura de tu proyecto
* **Automatic Imports**: Tab puede importar bibliotecas automáticamente en cuanto las usas
* **Inline Editing**: usa `CMD+K` en cualquier línea para editar con sintaxis perfecta
* **Composer Guidance**: planifica y edita tu código en múltiples archivos con el Composer

<div id="framework-intelligence-with-docs">
  ### Inteligencia de frameworks con @Docs
</div>

La función @Docs de Cursor te permite potenciar tu desarrollo en JavaScript agregando fuentes de documentación personalizadas que la IA puede consultar. Agrega documentación de MDN, Node.js o tu framework favorito para obtener sugerencias de código más precisas y con más contexto.

<Card title="Learn more about @Docs" icon="book" href="/es/context/@-symbols/@-docs">
  Descubre cómo agregar y gestionar fuentes de documentación personalizadas en Cursor.
</Card>

<div id="automatic-linting-resolution">
  ### Resolución automática de lint
</div>

Una de las funciones destacadas de Cursor es su integración fluida con extensiones de linters.
Asegúrate de tener configurado un linter, como ESLint, y habilita la opción "Iterate on Lints".

Luego, cuando uses el modo Agent en Composer, una vez que la IA haya intentado responder tu consulta y haya realizado cambios en el código, leerá automáticamente la salida del linter e intentará corregir cualquier error de lint que quizá no haya detectado.

<div id="framework-support">
  ## Compatibilidad con frameworks
</div>

Cursor funciona sin problemas con los principales frameworks y librerías de JavaScript, como:

### React & Next.js

* Soporte completo para JSX/TSX con sugerencias inteligentes de componentes
* Inteligencia para server components y rutas de API en Next.js
* Recomendado: extensión [**React Developer Tools**](cursor:extension/msjsdiag.vscode-react-native)

<div id="vuejs">
  ### Vue.js
</div>

* Soporte de sintaxis de plantillas con integración de Volar
* Autocompletado de componentes y comprobación de tipos
* Recomendado: [**Vue Language Features**](cursor:extension/vue.volar)

<div id="angular">
  ### Angular
</div>

* Validación de plantillas y soporte para decoradores de TypeScript
* Generación de componentes y servicios
* Recomendado: [**Angular Language Service**](cursor:extension/Angular.ng-template)

<div id="svelte">
  ### Svelte
</div>

* Resaltado de sintaxis de componentes y sugerencias inteligentes
* Sugerencias para sentencias reactivas y stores
* Recomendado: [**Svelte for VS Code**](cursor:extension/svelte.svelte-vscode)

<div id="backend-frameworks-expressnestjs">
  ### Frameworks de backend (Express/NestJS)
</div>

* Inteligencia para rutas y middleware
* Soporte para decoradores de TypeScript en NestJS
* Integración con herramientas de prueba de APIs

Recuerda: las funciones de IA de Cursor funcionan bien con todos estos frameworks, entienden sus patrones y mejores prácticas para ofrecer sugerencias relevantes. La IA puede ayudarte con todo, desde la creación de componentes hasta refactorizaciones complejas, respetando los patrones existentes de tu proyecto.

---

← Previous: [Java](./java.md) | [Index](./index.md) | Next: [Python](./python.md) →