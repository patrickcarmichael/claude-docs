---
title: "JavaScript & TypeScript"
source: "https://docs.cursor.com/en/guides/languages/javascript"
language: "en"
language_name: "English"
---

# JavaScript & TypeScript
Source: https://docs.cursor.com/en/guides/languages/javascript

JavaScript and TypeScript development with framework support

Welcome to JavaScript and TypeScript development in Cursor! The editor provides exceptional support for JS/TS development through its extension ecosystem. Here's what you need to know to get the most out of Cursor.

## Essential Extensions

While Cursor works great with any extensions you prefer, we recommend these for those just getting started:

* **ESLint** - Required for Cursor's AI-powered lint fixing capabilities
* **JavaScript and TypeScript Language Features** - Enhanced language support and IntelliSense
* **Path Intellisense** - Intelligent path completion for file paths

## Cursor Features

Cursor enhances your existing JavaScript/TypeScript workflow with:

* **Tab Completions**: Context-aware code completions that understand your project structure
* **Automatic Imports**: Tab can automatically import libraries as soon as you use them
* **Inline Editing**: Use `CMD+K` on any line to edit with perfect syntax
* **Composer Guidance**: Plan and edit your code across multiple files with the Composer

### Framework Intelligence with @Docs

Cursor's @Docs feature lets you supercharge your JavaScript development by adding custom documentation sources that the AI can reference. Add documentation from MDN, Node.js, or your favorite framework to get more accurate and contextual code suggestions.

<Card title="Learn more about @Docs" icon="book" href="/en/context/@-symbols/@-docs">
  Discover how to add and manage custom documentation sources in Cursor.
</Card>

### Automatic Linting Resolution

One of Cursor's standout features is its seamless integration with Linter extensions.
Ensure you have a linter, like ESLint, setup, and enable the 'Iterate on Lints' setting.

Then, when using the Agent mode in Composer, once the AI has attempted to answer your query, and has made any code changes, it will automatically read the output of the linter and will attempt to fix any lint errors it might not have known about.

## Framework Support

Cursor works seamlessly with all major JavaScript frameworks and libraries, such as:

### React & Next.js

* Full JSX/TSX support with intelligent component suggestions
* Server component and API route intelligence for Next.js
* Recommended: [**React Developer Tools**](cursor:extension/msjsdiag.vscode-react-native) extension

### Vue.js

* Template syntax support with Volar integration
* Component auto-completion and type checking
* Recommended: [**Vue Language Features**](cursor:extension/vue.volar)

### Angular

* Template validation and TypeScript decorator support
* Component and service generation
* Recommended: [**Angular Language Service**](cursor:extension/Angular.ng-template)

### Svelte

* Component syntax highlighting and intelligent completions
* Reactive statement and store suggestions
* Recommended: [**Svelte for VS Code**](cursor:extension/svelte.svelte-vscode)

### Backend Frameworks (Express/NestJS)

* Route and middleware intelligence
* TypeScript decorator support for NestJS
* API testing tools integration

Remember, Cursor's AI features work well with all these frameworks, understanding their patterns and best practices to provide relevant suggestions. The AI can help with everything from component creation to complex refactoring tasks, while respecting your project's existing patterns.

---

← Previous: [Java](./java.md) | [Index](./index.md) | Next: [Python](./python.md) →