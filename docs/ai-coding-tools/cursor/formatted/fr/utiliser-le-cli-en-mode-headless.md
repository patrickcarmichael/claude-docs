---
title: "Utiliser le CLI en mode headless"
source: "https://docs.cursor.com/fr/cli/headless"
language: "fr"
language_name: "French"
---

# Utiliser le CLI en mode headless
Source: https://docs.cursor.com/fr/cli/headless

Découvre comment écrire des scripts avec Cursor CLI pour l’analyse, la génération et la modification automatisées de code

Utilise Cursor CLI dans des scripts et des workflows d’automatisation pour des tâches d’analyse de code, de génération et de refactorisation.

<div id="how-it-works">
  ## Comment ça marche
</div>

Utilise le [mode d’impression](/fr/cli/using#non-interactive-mode) (`-p, --print`) pour les scripts non interactifs et l’automatisation.

<div id="file-modification-in-scripts">
  ### Modification de fichiers dans des scripts
</div>

Combine `--print` avec `--force` pour modifier des fichiers dans des scripts :

```bash  theme={null}

---

← Previous: [GitHub Actions](./github-actions.md) | [Index](./index.md) | Next: [Installation](./installation.md) →