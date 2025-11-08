---
title: "Ignoring files"
source: ""
---

# Ignoring files

If you'd like Cascade to ignore files, you can add your files to `.codeiumignore` at the root of your workspace. This will prevent Cascade from viewing, editing or creating files inside of the paths designated. You can declare the file paths in a format similar to `.gitignore`.

## Global .codeiumignore

For enterprise customers managing multiple repositories, you can enforce ignore rules across all repositories by placing a global `.codeiumignore` file in the `~/.codeium/` folder. This global configuration will apply to all Windsurf workspaces on your system and works in addition to any repository-specific `.codeiumignore` files.

---

← Previous: [Explain and fix](./explain-and-fix.md) | [Index](./index.md) | Next: [Linter integration](./linter-integration.md) →