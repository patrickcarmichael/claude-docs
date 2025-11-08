---
title: "Outils"
source: "https://docs.cursor.com/fr/agent/tools"
language: "fr"
language_name: "French"
---

# Outils
Source: https://docs.cursor.com/fr/agent/tools

Outils disponibles pour les agents pour rechercher, modifier et exécuter du code

La liste de tous les outils disponibles pour les modes de l’[Agent](/fr/agent/overview), que tu peux activer ou désactiver lorsque tu crées tes propres [modes personnalisés](/fr/agent/modes#custom).

<Note>
  Il n’y a aucune limite au nombre d’appels d’outils que l’Agent peut effectuer pendant une tâche. L’Agent continuera d’utiliser les outils nécessaires pour accomplir ta demande.
</Note>

<div id="search">
  ## Recherche
</div>

Outils pour explorer ta base de code et le web afin de trouver des infos pertinentes.

<AccordionGroup>
  <Accordion title="Read File" icon="file-lines">
    Lit jusqu’à 250 lignes (750 en mode max) d’un fichier.
  </Accordion>

  <Accordion title="List Directory" icon="folder-open">
    Lit la structure d’un répertoire sans lire le contenu des fichiers.
  </Accordion>

  <Accordion title="Codebase" icon="database">
    Effectue des recherches sémantiques dans ta [base de code
    indexée](/fr/context/codebase-indexing).
  </Accordion>

  <Accordion title="Grep" icon="magnifying-glass">
    Cherche des mots-clés ou des motifs exacts dans les fichiers.
  </Accordion>

  <Accordion title="Search Files" icon="file-magnifying-glass">
    Trouve des fichiers par nom via une correspondance approximative (fuzzy matching).
  </Accordion>

  <Accordion title="Web" icon="globe">
    Génère des requêtes et effectue des recherches sur le web.
  </Accordion>

  <Accordion title="Fetch Rules" icon="gavel">
    Récupère des [règles](/fr/context/rules) spécifiques selon le type et la description.
  </Accordion>
</AccordionGroup>

<div id="edit">
  ## Modification
</div>

Outils pour apporter des modifications ciblées à tes fichiers et à ton codebase.

<AccordionGroup>
  <Accordion title="Modifier et réappliquer" icon="pencil">
    Suggère des modifications aux fichiers et [applique](/fr/agent/apply) ces modifications automatiquement.
  </Accordion>

  <Accordion title="Supprimer des fichiers" icon="trash">
    Supprime des fichiers de façon autonome (désactivable dans les paramètres).
  </Accordion>
</AccordionGroup>

<div id="run">
  ## Exécution
</div>

Le chat peut interagir avec ton terminal.

<AccordionGroup>
  <Accordion title="Terminal" icon="terminal">
    Exécute des commandes dans le terminal et surveille la sortie.
  </Accordion>
</AccordionGroup>

<Note>Par défaut, Cursor utilise le premier profil de terminal disponible.</Note>

Pour définir ton profil de terminal préféré :

1. Ouvre la palette de commandes (`Cmd/Ctrl+Shift+P`)
2. Recherche « Terminal : Select Default Profile »
3. Choisis le profil que tu veux

<div id="mcp">
  ## MCP
</div>

Chat peut utiliser des serveurs MCP configurés pour interagir avec des services externes, comme des bases de données ou des API tierces.

<AccordionGroup>
  <Accordion title="Activer/désactiver les serveurs MCP" icon="server">
    Active ou désactive les serveurs MCP disponibles. Respecte la configuration d’exécution automatique.
  </Accordion>
</AccordionGroup>

En savoir plus sur le [Model Context Protocol](/fr/context/model-context-protocol) et explore les serveurs disponibles dans l’[annuaire MCP](/fr/tools).

<div id="advanced-options">
  ## Options avancées
</div>

<AccordionGroup>
  <Accordion title="Application auto des modifications" icon="check">
    Appliquer automatiquement les modifications sans confirmation manuelle.
  </Accordion>

  <Accordion title="Exécution auto" icon="play">
    Exécuter automatiquement les commandes du terminal et accepter les modifications. Pratique pour lancer des suites de tests et vérifier les changements.

    <Frame>
      <img src="https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=3135722076a5aa636d27dbedec665bae" data-og-width="1624" width="1624" data-og-height="1012" height="1012" data-path="images/agent/auto-run.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=280&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=9f2e2bed8f634201adc51ccb2bd96cd2 280w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=560&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=51704cac2f270a04856fffbeaccf9700 560w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=840&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=01a5034975497a8dff4f41dca0d19f2e 840w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=1100&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=5f19026a0c6e5fb28c935ce795edb706 1100w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=1650&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=a108fc86f8ee7c0db6e5b7ab80ede738 1650w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=2500&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=9ce5f45879c29049640bb5a1494db11e 2500w" />
    </Frame>
  </Accordion>

  <Accordion title="Garde-fous" icon="shield">
    Configurer des listes autorisées pour spécifier quels outils peuvent s’exécuter automatiquement. Les listes autorisées renforcent la sécurité en définissant explicitement les opérations permises.
  </Accordion>

  <Accordion title="Correction auto des erreurs" icon="wrench">
    Corriger automatiquement les erreurs et avertissements du linter lorsqu’Agent les rencontre.
  </Accordion>
</AccordionGroup>

---

← Previous: [Terminal](./terminal.md) | [Index](./index.md) | Next: [Agents en arrière-plan](./agents-en-arrire-plan.md) →