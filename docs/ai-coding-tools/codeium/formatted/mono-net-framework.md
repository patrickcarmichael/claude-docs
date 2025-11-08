---
title: "Mono / .NET Framework"
source: ""
---

# Mono / .NET Framework
$ mcs Program.cs
$ mono Program.exe
```

### .NET Framework Limitations

⚠️ **Important**: .NET Framework codebases with mixed assemblies (C++/CLI) or complex Visual Studio dependencies have significant limitations in Windsurf. These codebases typically require Visual Studio's proprietary build system and cannot be fully compiled or debugged in Windsurf due to dependencies on Microsoft-specific tooling and assembly reference resolution.

**Recommended approaches for .NET Framework projects:**

* Use Windsurf alongside Visual Studio for code generation and editing
* Migrate compatible portions to .NET Core where possible

***

## 2. C / C++ development

**Required Extensions:**

| Extension                                                                                                        | Purpose                                                                                                                                                    |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **[Windsurf C++ Tools](https://open-vsx.org/extension/Codeium/windsurf-cpptools)** (`Codeium.windsurf-cpptools`) | This is a bundle of the three extensions we recommend using to get started. Package that contains C/C++ LSP support, debugging support, and CMake support. |

> **Note:** Installing the Windsurf C++ Tools bundle will automatically install the individual extensions listed below, so you only need to install the bundle.

| Extension                                                                                                                                           | Purpose                                                                                                                        |
| --------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| **[clangd](https://marketplace.windsurf.com/vscode/item?itemName=llvm-vs-code-extensions.vscode-clangd)** (`llvm-vs-code-extensions.vscode-clangd`) | **clangd** language‑server integration. If `clangd` is missing it will offer to download the correct binary for your platform. |
| **[CodeLLDB](https://marketplace.windsurf.com/extension/vadimcn/vscode-lldb)** (`vadimcn.vscode-lldb`)                                              | Native debugger based on LLDB for C/C++ and Rust code.                                                                         |
| **[CMake Tools](https://marketplace.windsurf.com/vscode/item?itemName=ms-vscode.cmake-tools)** (`ms-vscode.cmake-tools`)                            | Project configuration, build, test, and debug integration for **CMake**‑based projects.                                        |

For non‑CMake workflows you can still invoke `make`, `ninja`, etc. via custom `tasks.json` targets.

### Configure C/C++ Build Tasks

**Create/edit `.vscode/tasks.json`** for your C/C++ project:

```jsonc  theme={null}
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "build-cpp",
      "type": "shell",
      "command": "clang++",
      "args": ["-g", "main.cpp", "-o", "main"], // ← Edit for your files
      "group": "build",
      "problemMatcher": "$gcc"
    }
  ]
}
```

***

## 3. Notes & Gotchas

* **Open‑source only** – decline any prompt to install proprietary Microsoft tooling; Windsurf containers cannot ship it.
* **Container vs Host** – SDKs/compilers must be present **inside** the Windsurf workspace container.
* **Keyboard shortcuts**
  * <kbd>Ctrl/⌘ + Shift + B</kbd> → compile using the active build task
  * <kbd>F5</kbd> → debug using the selected `launch.json` config

***

## 4. Setup Checklist

* Install the required extensions for your language stack
* **Create and customize** `.vscode/tasks.json` with your project's build commands
* **Create and customize** `.vscode/launch.json` with correct paths to your executables
* For Mono: install the runtime and verify `mono --version`
* Update file paths, project names, and build arguments to match your codebase
* Test your setup: Press <kbd>Ctrl/⌘ + Shift + B</kbd> to build, then <kbd>F5</kbd> to debug

> 💡 **Tip**: The configuration files are project-specific. You'll need to adapt the examples above for each workspace.

---

← Previous: [.NET Core](./net-core.md) | [Index](./index.md) | Next: [DeepWiki](./deepwiki.md) →