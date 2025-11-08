---
title: "Uso de la CLI en modo headless"
source: "https://docs.cursor.com/es/cli/headless"
language: "es"
language_name: "Spanish"
---

# Uso de la CLI en modo headless
Source: https://docs.cursor.com/es/cli/headless

Aprende a escribir scripts con la CLI de Cursor para análisis de código automatizado, generación y modificación

Usa la CLI de Cursor en scripts y flujos de automatización para tareas de análisis, generación y refactorización de código.

<div id="how-it-works">
  ## Cómo funciona
</div>

Usa [print mode](/es/cli/using#non-interactive-mode) (`-p, --print`) para scripting y automatización no interactivos.

<div id="file-modification-in-scripts">
  ### Modificación de archivos en scripts
</div>

Combina `--print` con `--force` para modificar archivos desde scripts:

```bash  theme={null}

---

← Previous: [GitHub Actions](./github-actions.md) | [Index](./index.md) | Next: [Instalación](./instalacin.md) →