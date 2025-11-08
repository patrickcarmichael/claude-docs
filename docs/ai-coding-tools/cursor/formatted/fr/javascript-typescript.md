---
title: "JavaScript & TypeScript"
source: "https://docs.cursor.com/fr/guides/languages/javascript"
language: "fr"
language_name: "French"
---

# JavaScript & TypeScript
Source: https://docs.cursor.com/fr/guides/languages/javascript

Développement JavaScript et TypeScript avec prise en charge des frameworks

Bienvenue dans le développement JavaScript et TypeScript avec Cursor ! L’éditeur offre une excellente prise en charge du dev JS/TS grâce à son écosystème d’extensions. Voici ce qu’il faut savoir pour tirer le meilleur parti de Cursor.

<div id="essential-extensions">
  ## Extensions essentielles
</div>

Même si Cursor fonctionne très bien avec les extensions que tu préfères, on te recommande celles-ci pour bien démarrer :

* **ESLint** - Requis pour les capacités de correction de lint propulsées par l'IA de Cursor
* **JavaScript and TypeScript Language Features** - Prise en charge du langage améliorée et IntelliSense
* **Path Intellisense** - Autocomplétion intelligente des chemins de fichiers

<div id="cursor-features">
  ## Fonctionnalités de Cursor
</div>

Cursor améliore ton workflow JavaScript/TypeScript avec :

* **Complétions par tabulation** : des propositions de code contextuelles qui comprennent la structure de ton projet
* **Imports automatiques** : Tab peut importer automatiquement les bibliothèques dès que tu les utilises
* **Édition inline** : utilise `CMD+K` sur n’importe quelle ligne pour modifier avec une syntaxe parfaite
* **Assistance du Composer** : planifie et édite ton code sur plusieurs fichiers avec le Composer

<div id="framework-intelligence-with-docs">
  ### Intelligence des frameworks avec @Docs
</div>

La fonctionnalité @Docs de Cursor te permet de booster ton développement JavaScript en ajoutant des sources de documentation personnalisées que l’IA peut consulter. Ajoute de la documentation depuis MDN, Node.js ou ton framework préféré pour obtenir des suggestions de code plus précises et contextuelles.

<Card title="En savoir plus sur @Docs" icon="book" href="/fr/context/@-symbols/@-docs">
  Découvre comment ajouter et gérer des sources de documentation personnalisées dans Cursor.
</Card>

<div id="automatic-linting-resolution">
  ### Résolution automatique des lints
</div>

L’une des fonctionnalités phares de Cursor est son intégration fluide avec les extensions de linter.
Assure-toi d’avoir configuré un linter, comme ESLint, et active le paramètre « Iterate on Lints ».

Ensuite, quand tu utilises le mode Agent dans le Composer, une fois que l’IA a tenté de répondre à ta requête et a apporté des modifications au code, elle lira automatiquement la sortie du linter et tentera de corriger les erreurs de lint qu’elle n’aurait pas détectées.

<div id="framework-support">
  ## Prise en charge des frameworks
</div>

Cursor fonctionne parfaitement avec tous les principaux frameworks et bibliothèques JavaScript, comme :

### React & Next.js

* Prise en charge complète de JSX/TSX avec des suggestions de composants intelligentes
* Intelligence pour les Server Components et les routes API dans Next.js
* Recommandé : extension [**React Developer Tools**](cursor:extension/msjsdiag.vscode-react-native)

<div id="vuejs">
  ### Vue.js
</div>

* Prise en charge de la syntaxe des templates avec intégration Volar
* Auto-complétion des composants et vérification des types
* Recommandé : [**Vue Language Features**](cursor:extension/vue.volar)

<div id="angular">
  ### Angular
</div>

* Validation des templates et prise en charge des décorateurs TypeScript
* Génération de composants et de services
* Recommandé : [**Angular Language Service**](cursor:extension/Angular.ng-template)

<div id="svelte">
  ### Svelte
</div>

* Surlignage de la syntaxe des composants et complétions intelligentes
* Suggestions pour les statements réactifs et les stores
* Recommandé : [**Svelte for VS Code**](cursor:extension/svelte.svelte-vscode)

<div id="backend-frameworks-expressnestjs">
  ### Frameworks backend (Express/NestJS)
</div>

* Intelligence pour les routes et les middlewares
* Prise en charge des décorateurs TypeScript pour NestJS
* Intégration d’outils de test d’API

N’oublie pas : les fonctionnalités d’IA de Cursor fonctionnent avec tous ces frameworks, comprennent leurs patterns et bonnes pratiques, et fournissent des suggestions pertinentes. L’IA peut t’aider pour tout, de la création de composants aux refactorings complexes, tout en respectant les patterns existants de ton projet.

---

← Previous: [Java](./java.md) | [Index](./index.md) | Next: [Python](./python.md) →