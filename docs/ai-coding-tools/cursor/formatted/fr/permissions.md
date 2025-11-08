---
title: "Permissions"
source: "https://docs.cursor.com/fr/cli/reference/permissions"
language: "fr"
language_name: "French"
---

# Permissions
Source: https://docs.cursor.com/fr/cli/reference/permissions

Types d’autorisations pour contrôler l’accès de l’agent aux fichiers et aux commandes

Configure ce que l’agent est autorisé à faire en utilisant des jetons d’autorisation dans ta configuration CLI. Les autorisations se définissent dans `~/.cursor/cli-config.json` (global) ou `<project>/.cursor/cli.json` (spécifique au projet).

<div id="permission-types">
  ## Types d’autorisations
</div>

<div id="shell-commands">
  ### Commandes shell
</div>

**Format :** `Shell(commandBase)`

Contrôle l’accès aux commandes shell. Le `commandBase` est le premier jeton de la ligne de commande.

<div class="full-width-table">
  | Exemple      | Description                                                           |
  | ------------ | --------------------------------------------------------------------- |
  | `Shell(ls)`  | Autoriser l’exécution des commandes `ls`                              |
  | `Shell(git)` | Autoriser toutes les sous-commandes `git`                             |
  | `Shell(npm)` | Autoriser les commandes du gestionnaire de paquets npm                |
  | `Shell(rm)`  | Refuser la suppression destructrice de fichiers (souvent dans `deny`) |
</div>

<div id="file-reads">
  ### Lectures de fichiers
</div>

**Format :** `Read(pathOrGlob)`

Contrôle l’accès en lecture aux fichiers et aux répertoires. Prend en charge les motifs glob.

<div class="full-width-table">
  | Exemple             | Description                                             |
  | ------------------- | ------------------------------------------------------- |
  | `Read(src/**/*.ts)` | Autoriser la lecture des fichiers TypeScript dans `src` |
  | `Read(**/*.md)`     | Autoriser la lecture des fichiers Markdown partout      |
  | `Read(.env*)`       | Refuser la lecture des fichiers d’environnement         |
  | `Read(/etc/passwd)` | Refuser la lecture des fichiers système                 |
</div>

<div id="file-writes">
  ### Écritures de fichiers
</div>

**Format :** `Write(pathOrGlob)`

Contrôle l’accès en écriture aux fichiers et aux répertoires. Prend en charge les motifs glob. En mode impression, `--force` est requis pour écrire des fichiers.

<div class="full-width-table">
  | Exemple               | Description                                                 |
  | --------------------- | ----------------------------------------------------------- |
  | `Write(src/**)`       | Autoriser l’écriture dans n’importe quel fichier sous `src` |
  | `Write(package.json)` | Autoriser la modification de `package.json`                 |
  | `Write(**/*.key)`     | Refuser l’écriture de fichiers de clés privées              |
  | `Write(**/.env*)`     | Refuser l’écriture des fichiers d’environnement             |
</div>

<div id="configuration">
  ## Configuration
</div>

Ajoute des permissions à l’objet `permissions` dans ton fichier de configuration du CLI :

```json  theme={null}
{
  "permissions": {
    "allow": [
      "Shell(ls)",
      "Shell(git)", 
      "Read(src/**/*.ts)",
      "Write(package.json)"
    ],
    "deny": [
      "Shell(rm)",
      "Read(.env*)",
      "Write(**/*.key)"
    ]
  }
}
```

<div id="pattern-matching">
  ## Correspondance de motifs
</div>

* Les motifs glob utilisent les caractères génériques `**`, `*` et `?`
* Les chemins relatifs sont limités à l’espace de travail actuel
* Les chemins absolus peuvent cibler des fichiers en dehors du projet
* Les règles de refus priment sur les règles d’autorisation

---

← Previous: [Paramètres](./paramtres.md) | [Index](./index.md) | Next: [Commandes slash](./commandes-slash.md) →