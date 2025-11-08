---
title: "Paramètres"
source: "https://docs.cursor.com/fr/cli/reference/parameters"
language: "fr"
language_name: "French"
---

# Paramètres
Source: https://docs.cursor.com/fr/cli/reference/parameters

Référence complète des commandes du CLI Cursor Agent

<div id="global-options">
  ## Options globales
</div>

Les options globales peuvent être utilisées avec n'importe quelle commande :

<div class="full-width-table">
  | Option                     | Description                                                                                                                            |
  | -------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
  | `-v, --version`            | Affiche le numéro de version                                                                                                           |
  | `-a, --api-key <key>`      | Clé API pour l'authentification (tu peux aussi utiliser la variable d'env `CURSOR_API_KEY`)                                            |
  | `-p, --print`              | Affiche les réponses dans la console (pour les scripts ou l'usage non interactif). A accès à tous les outils, y compris write et bash. |
  | `--output-format <format>` | Format de sortie (ne fonctionne qu'avec `--print`) : `text`, `json` ou `stream-json` (par défaut : `stream-json`)                      |
  | `-b, --background`         | Démarre en arrière-plan (ouvre le sélecteur de composition au lancement)                                                               |
  | `--fullscreen`             | Active le mode plein écran                                                                                                             |
  | `--resume [chatId]`        | Rétablit une session de chat                                                                                                           |
  | `-m, --model <model>`      | Modèle à utiliser                                                                                                                      |
  | `-f, --force`              | Force l'autorisation des commandes sauf refus explicite                                                                                |
  | `-h, --help`               | Affiche l'aide de la commande                                                                                                          |
</div>

<div id="commands">
  ## Commandes
</div>

<div class="full-width-table">
  | Commande          | Description                                            | Utilisation                                     |
  | ----------------- | ------------------------------------------------------ | ----------------------------------------------- |
  | `login`           | S’authentifier avec Cursor                             | `cursor-agent login`                            |
  | `logout`          | Se déconnecter et effacer les identifiants enregistrés | `cursor-agent logout`                           |
  | `status`          | Vérifier l’état de l’authentification                  | `cursor-agent status`                           |
  | `mcp`             | Gérer les serveurs MCP                                 | `cursor-agent mcp`                              |
  | `update\|upgrade` | Mettre à jour Cursor Agent vers la dernière version    | `cursor-agent update` ou `cursor-agent upgrade` |
  | `ls`              | Reprendre une session de chat                          | `cursor-agent ls`                               |
  | `resume`          | Reprendre la dernière session de chat                  | `cursor-agent resume`                           |
  | `help [command]`  | Afficher l’aide d’une commande                         | `cursor-agent help [command]`                   |
</div>

<Note>
  Si tu ne précises aucune commande, Cursor Agent démarre par défaut en mode chat interactif.
</Note>

<div id="mcp">
  ## MCP
</div>

Gère les serveurs MCP configurés pour Cursor Agent.

<div class="full-width-table">
  | Sous-commande             | Description                                                                   | Utilisation                                |
  | ------------------------- | ----------------------------------------------------------------------------- | ------------------------------------------ |
  | `login <identifier>`      | S’authentifie auprès d’un serveur MCP défini dans `.cursor/mcp.json`          | `cursor-agent mcp login <identifier>`      |
  | `list`                    | Liste les serveurs MCP configurés et leur état                                | `cursor-agent mcp list`                    |
  | `list-tools <identifier>` | Liste les outils disponibles et les noms de leurs arguments pour un MCP donné | `cursor-agent mcp list-tools <identifier>` |
</div>

Toutes les commandes MCP acceptent `-h, --help` pour obtenir l’aide spécifique à la commande.

<div id="arguments">
  ## Arguments
</div>

Quand tu démarres en mode chat (comportement par défaut), tu peux fournir un prompt initial :

**Arguments :**

* `prompt` — Prompt initial pour l’agent

<div id="getting-help">
  ## Obtenir de l’aide
</div>

Toutes les commandes prennent en charge l’option globale `-h, --help` pour afficher l’aide propre à chaque commande.

---

← Previous: [Format de sortie](./format-de-sortie.md) | [Index](./index.md) | Next: [Permissions](./permissions.md) →