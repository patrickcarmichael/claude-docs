---
title: "Indexation de la base de code"
source: "https://docs.cursor.com/fr/context/codebase-indexing"
language: "fr"
language_name: "French"
---

# Indexation de la base de code
Source: https://docs.cursor.com/fr/context/codebase-indexing

Comment Cursor apprend ta base de code pour mieux la comprendre

Cursor indexe ta base de code en calculant des embeddings pour chaque fichier. Ça améliore les réponses générées par l’IA sur ton code. Quand tu ouvres un projet, Cursor commence l’indexation automatiquement. Les nouveaux fichiers sont indexés au fil de l’eau.
Vérifie l’état de l’indexation dans : `Cursor Settings` > `Indexing & Docs`

<Frame>
  <img src="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/codebase-indexing.png?fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=47c946c1a46c8047feda127ef84faa9d" alt="Indicateur de progression de l’indexation de la base de code" data-og-width="2048" width="2048" data-og-height="1183" height="1183" data-path="images/get-started/codebase-indexing.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/codebase-indexing.png?w=280&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=3d628d1692d4cc512f4a81ece7e4a2c5 280w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/codebase-indexing.png?w=560&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=d5e20a24a9f38c97eb83249cd063ae41 560w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/codebase-indexing.png?w=840&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=ea26f1d9bf65ae5093333d15035ec96d 840w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/codebase-indexing.png?w=1100&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=1d532fe92021c50bee36b97e541419df 1100w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/codebase-indexing.png?w=1650&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=01c4cfe42a58ac06f6ac18e6e565782e 1650w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/codebase-indexing.png?w=2500&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=41d02dff523bfa3a33c6d4e86e79732a 2500w" />
</Frame>

<div id="configuration">
  ## Configuration
</div>

Cursor indexe tous les fichiers, sauf ceux dans les [fichiers d’exclusion](/fr/context/ignore-files) (p. ex. `.gitignore`, `.cursorignore`).

Clique sur `Show Settings` pour :

* Activer l’indexation automatique pour les nouveaux dépôts
* Configurer les fichiers à ignorer

<Tip>
  [Ignorer les fichiers volumineux](/fr/context/ignore-files) améliore la précision des réponses.
</Tip>

<div id="view-indexed-files">
  ### Voir les fichiers indexés
</div>

Pour voir les chemins des fichiers indexés : `Cursor Settings` > `Indexing & Docs` > `View included files`

Ça ouvre un fichier `.txt` listant tous les fichiers indexés.

<div id="multi-root-workspaces">
  ## Espaces de travail multi-racines
</div>

Cursor prend en charge les [espaces de travail multi‑racines](https://code.visualstudio.com/docs/editor/workspaces#_multiroot-workspaces), ce qui te permet de bosser avec plusieurs bases de code :

* Toutes les bases de code sont indexées automatiquement
* Le contexte de chaque base de code est accessible à l’IA
* `.cursor/rules` s’applique dans tous les dossiers

<div id="pr-search">
  ## Recherche de PR
</div>

La recherche de PR t’aide à comprendre l’évolution de ta base de code en rendant les changements historiques consultables et accessibles via l’IA.

<div id="how-it-works">
  ### Comment ça marche
</div>

Cursor **indexe automatiquement toutes les PR fusionnées** dans l’historique de ton dépôt. Des résumés apparaissent dans les résultats de recherche sémantique, avec un filtrage intelligent pour donner la priorité aux changements récents.

Agent peut **ajouter des PR, commits, issues ou branches** au contexte en utilisant `@[PR number]`, `@[commit hash]` ou `@[branch name]`. Inclut les commentaires GitHub et les revues Bugbot lorsqu’il est connecté.

**Plateformes prises en charge** : GitHub, GitHub Enterprise et Bitbucket. GitLab n’est pas encore pris en charge.

<Note>
  Utilisateurs GitHub Enterprise : l’outil de récupération bascule sur des commandes git en raison
  des limitations d’authentification de VSCode.
</Note>

<div id="using-pr-search">
  ### Utiliser la recherche de PR
</div>

Pose des questions comme « Comment les services sont-ils implémentés dans d’autres PR ? » et Agent récupérera automatiquement les PR pertinentes dans le contexte pour fournir des réponses complètes basées sur l’historique de ton dépôt.

<div id="faq">
  ## FAQ
</div>

<AccordionGroup>
  <Accordion title="Where can I see all indexed codebases?">
    Il n’existe pas encore de liste globale. Vérifie chaque projet individuellement en l’ouvrant dans
    Cursor et en consultant les paramètres de Codebase Indexing.
  </Accordion>

  <Accordion title="How do I delete all indexed codebases?">
    Supprime ton compte Cursor depuis Settings pour retirer toutes les bases de code indexées.
    Sinon, supprime les bases de code individuellement dans les paramètres de Codebase Indexing
    de chaque projet.
  </Accordion>

  <Accordion title="How long are indexed codebases retained?">
    Les bases de code indexées sont supprimées après 6 semaines d’inactivité. La réouverture du
    projet déclenche un réindexage.
  </Accordion>

  <Accordion title="Is my source code stored on Cursor servers?">
    Non. Cursor crée des embeddings sans stocker les noms de fichiers ni le code source. Les noms de fichiers sont masqués et les fragments de code sont chiffrés.

    Quand Agent recherche dans la base de code, Cursor récupère les embeddings depuis le serveur et déchiffre les fragments.
  </Accordion>
</AccordionGroup>

---

← Previous: [/command](./command.md) | [Index](./index.md) | Next: [Ignorer des fichiers](./ignorer-des-fichiers.md) →