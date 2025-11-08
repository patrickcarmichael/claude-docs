---
title: "JavaScript & TypeScript"
source: "https://docs.cursor.com/de/guides/languages/javascript"
language: "de"
language_name: "German"
---

# JavaScript & TypeScript
Source: https://docs.cursor.com/de/guides/languages/javascript

JavaScript- und TypeScript-Entwicklung mit Framework-Unterstützung

Willkommen bei der JavaScript- und TypeScript-Entwicklung in Cursor! Der Editor bietet über sein Erweiterungs-Ökosystem hervorragende Unterstützung für JS/TS. Hier ist, was du wissen musst, um das Beste aus Cursor herauszuholen.

<div id="essential-extensions">
  ## Wichtige Erweiterungen
</div>

Cursor funktioniert zwar gut mit allen Erweiterungen, die du magst, aber für den Einstieg empfehlen wir diese:

* **ESLint** – erforderlich für Cursors KI-gestützte Lint-Fix-Funktionen
* **JavaScript and TypeScript Language Features** – erweiterte Sprachunterstützung und IntelliSense
* **Path Intellisense** – intelligente Pfadvervollständigung für Dateipfade

<div id="cursor-features">
  ## Cursor-Funktionen
</div>

Cursor erweitert deinen bestehenden JavaScript/TypeScript-Workflow um:

* **Tab-Vervollständigungen**: Kontextbewusste Code-Vervollständigungen, die deine Projektstruktur verstehen
* **Automatische Importe**: Tab kann Bibliotheken automatisch importieren, sobald du sie verwendest
* **Inline-Editing**: Nutze `CMD+K` in jeder Zeile, um mit perfekter Syntax zu bearbeiten
* **Composer-Guidance**: Plane und bearbeite deinen Code über mehrere Dateien hinweg mit dem Composer

<div id="framework-intelligence-with-docs">
  ### Framework-Intelligence mit @Docs
</div>

Das @Docs-Feature von Cursor lässt dich deine JavaScript-Entwicklung auf ein neues Level heben, indem du benutzerdefinierte Dokumentationsquellen hinzufügst, auf die die KI zugreifen kann. Füge Dokumentation von MDN, Node.js oder deinem Lieblings-Framework hinzu, um präzisere und kontextbezogene Codevorschläge zu erhalten.

<Card title="Erfahre mehr über @Docs" icon="book" href="/de/context/@-symbols/@-docs">
  Entdecke, wie du benutzerdefinierte Dokumentationsquellen in Cursor hinzufügen und verwalten kannst.
</Card>

<div id="automatic-linting-resolution">
  ### Automatische Linting-Behebung
</div>

Eines der herausragenden Features von Cursor ist die nahtlose Integration mit Linter-Erweiterungen.
Stell sicher, dass du einen Linter wie ESLint eingerichtet hast und aktiviere die Einstellung „Iterate on Lints“.

Wenn du dann den Agent-Modus im Composer verwendest, liest die KI, nachdem sie deine Anfrage beantwortet und Codeänderungen vorgenommen hat, automatisch die Ausgabe des Linters und versucht, alle Lint-Fehler zu beheben, die ihr möglicherweise zuvor nicht bekannt waren.

<div id="framework-support">
  ## Framework-Unterstützung
</div>

Cursor funktioniert nahtlos mit allen gängigen JavaScript-Frameworks und -Bibliotheken, zum Beispiel:

### React & Next.js

* Vollständige JSX/TSX-Unterstützung mit intelligenten Komponenten-Vorschlägen
* Intelligenz für Server Components und API-Routen in Next.js
* Empfohlen: [**React Developer Tools**](cursor:extension/msjsdiag.vscode-react-native) Erweiterung

<div id="vuejs">
  ### Vue.js
</div>

* Unterstützung der Template-Syntax mit Volar-Integration
* Autovervollständigung für Komponenten und Typprüfung
* Empfohlen: [**Vue Language Features**](cursor:extension/vue.volar)

<div id="angular">
  ### Angular
</div>

* Template-Validierung und Unterstützung für TypeScript-Decorators
* Generierung von Komponenten und Services
* Empfohlen: [**Angular Language Service**](cursor:extension/Angular.ng-template)

<div id="svelte">
  ### Svelte
</div>

* Syntaxhervorhebung für Komponenten und intelligente Vervollständigungen
* Vorschläge für reaktive Statements und Stores
* Empfohlen: [**Svelte for VS Code**](cursor:extension/svelte.svelte-vscode)

<div id="backend-frameworks-expressnestjs">
  ### Backend-Frameworks (Express/NestJS)
</div>

* Intelligenz für Routen und Middleware
* Unterstützung für TypeScript-Decorators in NestJS
* Integration von API-Testtools

Denk dran: Die KI-Features von Cursor funktionieren mit all diesen Frameworks richtig gut, verstehen ihre Patterns und Best Practices und liefern passende Vorschläge. Die KI kann bei allem helfen – von der Komponentenerstellung bis hin zu komplexen Refactorings – und respektiert dabei die bestehenden Patterns in deinem Projekt.

---

← Previous: [Java](./java.md) | [Index](./index.md) | Next: [Python](./python.md) →