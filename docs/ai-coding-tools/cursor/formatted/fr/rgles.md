---
title: "Règles"
source: "https://docs.cursor.com/fr/context/rules"
language: "fr"
language_name: "French"
---

# Règles
Source: https://docs.cursor.com/fr/context/rules

Contrôle le comportement du modèle Agent avec des instructions réutilisables et à portée définie.

Les règles fournissent des instructions au niveau système à Agent et Inline Edit. Pense-les comme un contexte persistant, des préférences ou des workflows pour tes projets.

Cursor prend en charge quatre types de règles :

<CardGroup cols={2}>
  <Card title="Project Rules" icon="folder-tree">
    Stockées dans `.cursor/rules`, versionnées et limitées à ta base de code.
  </Card>

  <Card title="User Rules" icon="user">
    Globales à ton environnement Cursor. Définies dans les paramètres et toujours appliquées.
  </Card>

  <Card title="AGENTS.md" icon="robot">
    Instructions d’Agent au format Markdown. Alternative simple à `.cursor/rules`.
  </Card>

  <Card title=".cursorrules (Legacy)" icon="clock-rotate-left">
    Toujours pris en charge, mais obsolète. Utilise plutôt les Project Rules.
  </Card>
</CardGroup>

<div id="how-rules-work">
  ## Comment fonctionnent les règles
</div>

Les grands modèles de langage ne gardent pas de mémoire entre les complétions. Les règles fournissent un contexte persistant et réutilisable au niveau du prompt.

Quand elles sont appliquées, le contenu des règles est inclus au début du contexte du modèle. Ça donne à l’IA des consignes cohérentes pour générer du code, interpréter des modifications ou aider dans les workflows.

<Frame>
  <img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rules-applied.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=e637bab83cfd5dcc8a3b15ed6fd9fc15" alt="Règle appliquée dans le contexte avec le chat" data-og-width="1198" width="1198" data-og-height="674" height="674" data-path="images/context/rules/rules-applied.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rules-applied.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=78e3c392987c6f95a02fc106753c5f98 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rules-applied.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=9d3a8b76ba99ada5ca302cba9fb63810 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rules-applied.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=f5ab7fb374a1a4c5fe2f50e2e50d233a 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rules-applied.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=5d25394a29c1da4172a3e673ee384c07 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rules-applied.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=0fc125bd3c2a93551674252c0523d3ec 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rules-applied.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=c576ea053ee18c30d2781c6bdd394a70 2500w" />
</Frame>

<Info>
  Les règles s’appliquent à [Chat](/fr/chat/overview) et à [Inline
  Edit](/fr/inline-edit/overview). Les règles actives s’affichent dans la barre latérale de l’Agent.
</Info>

<div id="project-rules">
  ## Règles du projet
</div>

Les règles du projet se trouvent dans `.cursor/rules`. Chaque règle est un fichier versionné. Elles peuvent être ciblées via des motifs de chemin, invoquées manuellement, ou incluses en fonction de leur pertinence. Les sous-répertoires peuvent inclure leur propre dossier `.cursor/rules` limité à ce dossier.

Utilise les règles du projet pour :

* Encoder des connaissances spécifiques à ton codebase
* Automatiser des workflows ou des templates propres au projet
* Standardiser les décisions de style ou d’architecture

<div id="rule-anatomy">
  ### Anatomie d’une règle
</div>

Chaque fichier de règle est écrit en **MDC** (`.mdc`), un format qui prend en charge les métadonnées et le contenu. Gère comment les règles sont appliquées via la liste déroulante du type, qui modifie les propriétés `description`, `globs`, `alwaysApply`.

| <span class="no-wrap">Rule Type</span>         | Description                                                                        |
| :--------------------------------------------- | :--------------------------------------------------------------------------------- |
| <span class="no-wrap">`Always`</span>          | Toujours inclus dans le contexte du modèle                                         |
| <span class="no-wrap">`Auto Attached`</span>   | Inclus quand des fichiers correspondant à un motif glob sont référencés            |
| <span class="no-wrap">`Agent Requested`</span> | Disponible pour l’IA, qui décide s’il faut l’inclure. Doit fournir une description |
| <span class="no-wrap">`Manual`</span>          | Inclus uniquement quand il est explicitement mentionné avec `@ruleName`            |

```
---
description: Modèle de service RPC
globs:
alwaysApply: false
---

- Utilise notre schéma RPC interne pour définir les services
- Utilise toujours snake_case pour les noms de services.

@service-template.ts
```

<div id="nested-rules">
  ### Règles imbriquées
</div>

Organise les règles en les plaçant dans des répertoires `.cursor/rules` à travers ton projet. Les règles imbriquées s’appliquent automatiquement quand des fichiers de leur répertoire sont référencés.

```
project/
  .cursor/rules/        # Règles à l’échelle du projet
  backend/
    server/
      .cursor/rules/    # Règles spécifiques au backend
  frontend/
    .cursor/rules/      # Règles spécifiques au frontend
```

<div id="creating-a-rule">
  ### Créer une règle
</div>

Crée des règles avec la commande `New Cursor Rule` ou via `Cursor Settings > Rules`. Ça crée un nouveau fichier de règle dans `.cursor/rules`. Depuis les paramètres, tu peux voir toutes les règles et leur état.

<Frame>
  <img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rule-settings.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=db8142786bbb7b7771ae0db8b2704b0b" alt="Comparaison entre règles concises et longues" data-og-width="6016" width="6016" data-og-height="3334" height="3334" data-path="images/context/rules/rule-settings.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rule-settings.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=0b6e9b8d6ca799d1af62957726b1cc52 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rule-settings.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=8bfe1482ab9afc0995fe13371b26074b 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rule-settings.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=a847d915b3f106c42cba7cb1245bb138 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rule-settings.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=356963b3607152f7ffe128cd1a2d050e 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rule-settings.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=1b1e50d3721d42c691a434189729921c 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rule-settings.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=d2081cf016d65053f1e517eb5734079e 2500w" />
</Frame>

<div id="generating-rules">
  ### Génération de règles
</div>

Génère des règles directement dans les conversations avec la commande `/Generate Cursor Rules`. Pratique quand t’as défini le comportement de l’agent et que tu veux le réutiliser.

<Frame>
  <video src="https://www.cursor.com/changelog/049/generate-rules.mp4" controls>
    Ton navigateur ne prend pas en charge la balise vidéo.
  </video>
</Frame>

<div id="best-practices">
  ## Bonnes pratiques
</div>

De bonnes règles sont ciblées, actionnables et bien délimitées.

* Garde les règles sous la barre des 500 lignes
* Scinde les règles volumineuses en plusieurs règles composables
* Fournis des exemples concrets ou des fichiers de référence
* Évite les consignes vagues. Écris les règles comme une doc interne claire
* Réutilise les règles quand tu répètes des prompts dans le chat

<div id="examples">
  ## Exemples
</div>

<AccordionGroup>
  <Accordion title="Normes pour les composants frontend et la validation d’API">
    Cette règle définit des normes pour les composants frontend :

    Dans le répertoire components :

    * Utilise toujours Tailwind pour le style
    * Utilise Framer Motion pour les animations
    * Suis les conventions de nommage des composants

    Cette règle impose la validation des endpoints d’API :

    Dans le répertoire API :

    * Utilise zod pour toute validation
    * Définit les types de retour avec des schémas zod
    * Exporte les types générés à partir des schémas
  </Accordion>

  <Accordion title="Modèles pour les services Express et les composants React">
    Cette règle fournit un modèle pour les services Express :

    Utilise ce modèle lors de la création d’un service Express :

    * Suis les principes RESTful
    * Inclue un middleware de gestion des erreurs
    * Mets en place une journalisation adéquate

    @express-service-template.ts

    Cette règle définit la structure des composants React :

    Les composants React doivent suivre cette structure :

    * Interface des props en haut
    * Composant exporté nommément
    * Styles en bas

    @component-template.tsx
  </Accordion>

  <Accordion title="Automatisation des workflows de dev et génération de documentation">
    Cette règle automatise l’analyse de l’app :

    Quand on te demande d’analyser l’app :

    1. Lance le serveur de dev avec `npm run dev`
    2. Récupère les logs depuis la console
    3. Propose des améliorations de performance

    Cette règle aide à générer la documentation :

    Aide à rédiger la doc en :

    * Extrayant les commentaires de code
    * Analysant README.md
    * Générant de la documentation Markdown
  </Accordion>

  <Accordion title="Ajouter un nouveau réglage dans Cursor">
    Commence par créer une propriété à basculer dans `@reactiveStorageTypes.ts`.

    Ajoute une valeur par défaut dans `INIT_APPLICATION_USER_PERSISTENT_STORAGE` dans `@reactiveStorageService.tsx`.

    Pour les fonctionnalités bêta, ajoute un toggle dans `@settingsBetaTab.tsx`, sinon ajoute-le dans `@settingsGeneralTab.tsx`. Les toggles peuvent être ajoutés comme `<SettingsSubSection>` pour les cases à cocher générales. Regarde le reste du fichier pour des exemples.

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

    Pour l’utiliser dans l’app, importe reactiveStorageService et utilise la propriété :

    ```
    const flagIsEnabled = vsContext.reactiveStorageService.applicationUserPersistentStorage.myNewProperty
    ```
  </Accordion>
</AccordionGroup>

De nombreux exemples sont disponibles auprès des fournisseurs et des frameworks. Des règles proposées par la communauté se trouvent dans des collections et dépôts collaboratifs en ligne.

<div id="agentsmd">
  ## AGENTS.md
</div>

`AGENTS.md` est un simple fichier Markdown pour définir des instructions d’agent. Place-le à la racine de ton projet comme alternative à `.cursor/rules` pour des cas d’usage simples.

Contrairement aux règles de projet, `AGENTS.md` est un fichier Markdown brut, sans métadonnées ni configurations complexes. C’est parfait pour les projets qui ont besoin d’instructions simples et lisibles, sans le surcoût de règles structurées.

```markdown  theme={null}

---

← Previous: [Memories](./memories.md) | [Index](./index.md) | Next: [Concepts](./concepts.md) →