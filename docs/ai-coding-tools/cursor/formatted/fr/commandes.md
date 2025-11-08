---
title: "Commandes"
source: "https://docs.cursor.com/fr/agent/chat/commands"
language: "fr"
language_name: "French"
---

# Commandes
Source: https://docs.cursor.com/fr/agent/chat/commands

Définir des commandes pour des flux de travail réutilisables

Les commandes personnalisées te permettent de créer des workflows réutilisables, déclenchables avec un simple préfixe « / » dans la zone de saisie du chat. Elles aident à standardiser les processus au sein de ton équipe et rendent les tâches courantes plus efficaces.

<Frame>
    <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/commands/input.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=0d25ac517b091210da1c6eff4c8e3098" alt="Commands input example" data-og-width="1689" width="1689" data-og-height="1079" height="1079" data-path="images/chat/commands/input.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/commands/input.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=680f0cbf1491ef1303171dbd18115288 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/commands/input.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=d6a5397e565ab2c90435e6fdd2b7b27a 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/commands/input.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=ae074e2f2b26741544fd8c8ecfa529e3 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/commands/input.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=564aad432affcc04e51b624725f386ad 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/commands/input.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=5c1bd5d49babc2f08eb0efcd24ba7783 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/commands/input.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=3244c3be31c9bc704468a706c6e6b38e 2500w" />
</Frame>

<Info>
  Les commandes sont actuellement en bêta. La fonctionnalité et la syntaxe peuvent évoluer au fur et à mesure que nous les améliorons.
</Info>

<div id="how-commands-work">
  ## Comment fonctionnent les commandes
</div>

Les commandes sont définies comme de simples fichiers Markdown et peuvent être stockées à deux emplacements :

1. **Commandes de projet** : stockées dans le répertoire `.cursor/commands` de ton projet
2. **Commandes globales** : stockées dans le répertoire `~/.cursor/commands` de ton dossier personnel

Quand tu tapes `/` dans le champ de saisie du chat, Cursor détecte et affiche automatiquement les commandes disponibles dans les deux répertoires, ce qui les rend instantanément accessibles dans tout ton workflow.

<div id="creating-commands">
  ## Créer des commandes
</div>

1. Crée un répertoire `.cursor/commands` à la racine de ton projet
2. Ajoute des fichiers `.md` avec des noms explicites (p. ex. `review-code.md`, `write-tests.md`)
3. Écris du contenu Markdown simple décrivant ce que la commande doit faire
4. Les commandes s’afficheront automatiquement dans le chat quand tu tapes `/`

Voici un exemple de la structure que pourrait avoir ton répertoire de commandes :

```
.cursor/
└── commands/
    ├── traiter-les-commentaires-des-PR-GitHub.md
    ├── liste-de-contrôle-revue-de-code.md
    ├── créer-une-PR.md
    ├── revue-rapide-des-diffs-existants.md
    ├── onboard-un-nouveau-développeur.md
    ├── exécuter-tous-les-tests-et-corriger.md
    ├── audit-de-sécurité.md
    └── configurer-une-nouvelle-fonctionnalité.md
```

<div id="examples">
  ## Exemples
</div>

Essaie ces commandes dans tes projets pour te faire une idée de leur fonctionnement.

<AccordionGroup>
  <Accordion title="Liste de contrôle pour la revue de code">
    ```markdown  theme={null}
    # Checklist de revue de code

    ## Vue d’ensemble
    Checklist complète pour mener des revues de code approfondies afin de garantir la qualité, la sécurité et la maintenabilité.

    ## Catégories de revue

    ### Fonctionnalité
    - [ ] Le code fait ce qu’il est censé faire
    - [ ] Les cas limites sont correctement gérés
    - [ ] La gestion des erreurs est appropriée
    - [ ] Pas de bugs évidents ni d’erreurs logiques

    ### Qualité du code
    - [ ] Le code est lisible et bien structuré
    - [ ] Les fonctions sont courtes et ciblées
    - [ ] Les noms de variables sont explicites
    - [ ] Pas de duplication de code
    - [ ] Respecte les conventions du projet

    ### Sécurité
    - [ ] Pas de vulnérabilités de sécurité évidentes
    - [ ] La validation des entrées est en place
    - [ ] Les données sensibles sont correctement traitées
    - [ ] Pas de secrets codés en dur
    ```
  </Accordion>

  <Accordion title="Audit de sécurité">
    ```markdown  theme={null}
    # Audit de sécurité

    ## Vue d’ensemble
    Revue de sécurité complète pour identifier et corriger les vulnérabilités dans la base de code.

    ## Étapes
    1. **Audit des dépendances**
       - Vérifier les vulnérabilités connues
       - Mettre à jour les paquets obsolètes
       - Passer en revue les dépendances tierces

    2. **Revue de la sécurité du code**
       - Rechercher les vulnérabilités courantes
       - Passer en revue l’authentification et l’autorisation
       - Auditer les pratiques de gestion des données

    3. **Sécurité de l’infrastructure**
       - Passer en revue les variables d’environnement
       - Vérifier les contrôles d’accès
       - Auditer la sécurité réseau

    ## Liste de vérification de sécurité
    - [ ] Dépendances à jour et sécurisées
    - [ ] Aucun secret en dur dans le code
    - [ ] Validation des entrées mise en œuvre
    - [ ] Authentification sécurisée
    - [ ] Autorisation correctement configurée
    ```
  </Accordion>

  <Accordion title="Configurer une nouvelle fonctionnalité">
    ```markdown  theme={null}
    # Configurer une nouvelle fonctionnalité

    ## Vue d’ensemble
    Mettre en place une nouvelle fonctionnalité de façon systématique, de la planification initiale jusqu’à la structure d’implémentation.

    ## Étapes
    1. **Définir les exigences**
       - Clarifier le périmètre et les objectifs de la fonctionnalité
       - Identifier les user stories et les critères d’acceptation
       - Planifier l’approche technique

    2. **Créer une branche de fonctionnalité**
       - Partir de main/develop
       - Configurer l’environnement de développement local
       - Configurer toute nouvelle dépendance

    3. **Concevoir l’architecture**
       - Concevoir les modèles de données et les API
       - Planifier les composants UI et les flux
       - Définir la stratégie de test

    ## Liste de contrôle de configuration de la fonctionnalité
    - [ ] Exigences documentées
    - [ ] User stories rédigées
    - [ ] Approche technique définie
    - [ ] Branche de fonctionnalité créée
    - [ ] Environnement de développement prêt
    ```
  </Accordion>

  <Accordion title="Créer une pull request">
    ```markdown  theme={null}
    # Créer une PR

    ## Vue d’ensemble
    Créer une pull request bien structurée avec une description claire, des labels et des reviewers.

    ## Étapes
    1. **Préparer la branche**
       - S’assurer que toutes les modifications sont commitées
       - Pousser la branche vers le dépôt distant
       - Vérifier que la branche est à jour avec main

    2. **Rédiger la description de la PR**
       - Résumer clairement les changements
       - Inclure le contexte et la motivation
       - Lister toute modification cassante
       - Ajouter des captures d’écran si l’UI change

    3. **Configurer la PR**
       - Créer la PR avec un titre descriptif
       - Ajouter les labels appropriés
       - Assigner des reviewers
       - Lier les issues associées

    ## Modèle de PR
    - [ ] Fonctionnalité A
    - [ ] Correction de bug B
    - [ ] Les tests unitaires passent
    - [ ] Tests manuels terminés
    ```
  </Accordion>

  <Accordion title="Lance les tests et corrige les échecs">
    ```markdown  theme={null}
    # Exécuter tous les tests et corriger les échecs

    ## Vue d’ensemble
    Exécuter l’ensemble de la suite de tests et corriger systématiquement tous les échecs afin de garantir la qualité et la fonctionnalité du code.

    ## Étapes
    1. **Exécuter la suite de tests**
       - Exécuter tous les tests du projet
       - Capturer la sortie et identifier les échecs
       - Vérifier les tests unitaires et d’intégration

    2. **Analyser les échecs**
       - Catégoriser par type : instables, cassés, nouveaux échecs
       - Prioriser les correctifs selon l’impact
       - Vérifier si les échecs sont liés aux changements récents

    3. **Corriger les problèmes de manière systématique**
       - Commencer par les échecs les plus critiques
       - Corriger un problème à la fois
       - Relancer les tests après chaque correctif
    ```
  </Accordion>

  <Accordion title="Intégrer un·e nouveau·elle développeur·euse">
    ```markdown  theme={null}
    # Intégrer un·e nouveau·elle développeur·euse

    ## Vue d’ensemble
    Processus d’onboarding complet pour permettre à un·e nouveau·elle développeur·euse d’être opérationnel·le rapidement.

    ## Étapes
    1. **Configuration de l’environnement**
       - Installer les outils requis
       - Configurer l’environnement de développement
       - Configurer l’IDE et les extensions
       - Configurer Git et les clés SSH

    2. **Prise en main du projet**
       - Passer en revue la structure du projet
       - Comprendre l’architecture
       - Lire la documentation principale
       - Configurer la base de données locale

    ## Checklist d’onboarding
    - [ ] Environnement de développement prêt
    - [ ] Tous les tests passent
    - [ ] Peut exécuter l’application en local
    - [ ] Base de données configurée et fonctionnelle
    - [ ] Première PR soumise
    ```
  </Accordion>
</AccordionGroup>

---

← Previous: [Points de contrôle](./points-de-contrle.md) | [Index](./index.md) | Next: [Compact](./compact.md) →