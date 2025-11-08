---
title: "Configuration"
source: "https://docs.cursor.com/fr/cli/reference/configuration"
language: "fr"
language_name: "French"
---

# Configuration
Source: https://docs.cursor.com/fr/cli/reference/configuration

Référence de configuration de l’Agent CLI pour cli-config.json

Configure l’Agent CLI à l’aide du fichier `cli-config.json`.

<div id="file-location">
  ## Emplacement du fichier
</div>

<div class="full-width-table">
  | Type   | Plateforme  | Chemin                                     |
  | :----- | :---------- | :----------------------------------------- |
  | Global | macOS/Linux | `~/.cursor/cli-config.json`                |
  | Global | Windows     | `$env:USERPROFILE\.cursor\cli-config.json` |
  | Projet | Tous        | `<project>/.cursor/cli.json`               |
</div>

<Note>Seules les autorisations peuvent être configurées au niveau du projet. Tous les autres réglages du CLI doivent être définis globalement.</Note>

Remplacer via des variables d’environnement :

* **`CURSOR_CONFIG_DIR`** : chemin de répertoire personnalisé
* **`XDG_CONFIG_HOME`** (Linux/BSD) : utilise `$XDG_CONFIG_HOME/cursor/cli-config.json`

<div id="schema">
  ## Schéma
</div>

<div id="required-fields">
  ### Champs requis
</div>

<div class="full-width-table">
  | Champ               | Type      | Description                                                               |
  | :------------------ | :-------- | :------------------------------------------------------------------------ |
  | `version`           | number    | Version du schéma de configuration (actuelle : `1`)                       |
  | `editor.vimMode`    | boolean   | Activer les raccourcis Vim (par défaut : `false`)                         |
  | `permissions.allow` | string\[] | Opérations autorisées (voir [Permissions](/fr/cli/reference/permissions)) |
  | `permissions.deny`  | string\[] | Opérations interdites (voir [Permissions](/fr/cli/reference/permissions)) |
</div>

<div id="optional-fields">
  ### Champs optionnels
</div>

<div class="full-width-table">
  | Champ                    | Type    | Description                                          |
  | :----------------------- | :------ | :--------------------------------------------------- |
  | `model`                  | object  | Configuration du modèle sélectionné                  |
  | `hasChangedDefaultModel` | boolean | Indicateur de remplacement du modèle géré par la CLI |
</div>

<div id="examples">
  ## Exemples
</div>

<div id="minimal-config">
  ### Configuration minimale
</div>

```json  theme={null}
{
  "version": 1,
  "editor": { "vimMode": false },
  "permissions": { "allow": ["Shell(ls)"], "deny": [] }
}
```

<div id="enable-vim-mode">
  ### Activer le mode Vim
</div>

```json  theme={null}
{
  "version": 1,
  "editor": { "vimMode": true },
  "permissions": { "allow": ["Shell(ls)"], "deny": [] }
}
```

<div id="configure-permissions">
  ### Configurer les permissions
</div>

```json  theme={null}
{
  "version": 1,
  "editor": { "vimMode": false },
  "permissions": {
    "allow": ["Shell(ls)", "Shell(echo)"],
    "deny": ["Shell(rm)"]
  }
}
```

Consulte [Permissions](/fr/cli/reference/permissions) pour les types d’autorisations disponibles et des exemples.

<div id="troubleshooting">
  ## Dépannage
</div>

**Erreurs de configuration** : Mets le fichier de côté et redémarre :

```bash  theme={null}
mv ~/.cursor/cli-config.json ~/.cursor/cli-config.json.bad
```

**Les modifications ne sont pas conservées** : Assure-toi que le JSON est valide et que tu as les autorisations d’écriture. Certains champs sont gérés par la CLI et peuvent être écrasés.

<div id="notes">
  ## Notes
</div>

* Format JSON pur (sans commentaires)
* La CLI répare automatiquement les champs manquants
* Les fichiers corrompus sont sauvegardés en `.bad` puis recréés
* Les entrées d’autorisations sont des chaînes exactes (voir [Permissions](/fr/cli/reference/permissions) pour plus de détails)

---

← Previous: [Authentification](./authentification.md) | [Index](./index.md) | Next: [Format de sortie](./format-de-sortie.md) →