---
title: "Windsurf Development Environment Setup Guide"
source: ""
---

# Windsurf Development Environment Setup Guide

## Overview

Windsurf workspaces rely **exclusively on open‑source tooling** for compiling, linting, and debugging. Microsoft's proprietary Visual Studio components cannot be redistributed, so we integrate community‑maintained language servers, debuggers, and compilers instead.

This guide covers two stacks:

1. **.NET / C#** – targeting both .NET Core and .NET Framework (via Mono)
2. **C / C++** – using clang‑based tooling

You can install either or both in the same workspace.

> ⚠️ **Important**: The examples below are templates that you must customize for your specific project. You'll need to edit file paths, project names, and build commands to match your codebase.

***

## 1. .NET / C# development

> **Choose the flavour that matches your codebase.**

### .NET Core / .NET 6+

**Extensions:**

* **[C#](https://marketplace.windsurf.com/vscode/item?itemName=muhammad-sammy.csharp)** (`muhammad-sammy.csharp`) – bundles **OmniSharp LS** and **NetCoreDbg**, so you can hit <kbd>F5</kbd> immediately

* **[.NET Install Tool](https://marketplace.windsurf.com/vscode/item?itemName=ms-dotnettools.vscode-dotnet-runtime)** (`ms-dotnettools.vscode-dotnet-runtime`) – auto‑installs missing runtimes/SDKs

* **[Solution Explorer](https://marketplace.windsurf.com/vscode/item?itemName=fernandoescolar.vscode-solution-explorer)** (`fernandoescolar.vscode-solution-explorer`) – navigate and manage .NET solutions and projects

**Debugger:** Nothing else is required—the extension already contains the language server and an open‑source debugger suitable for .NET Core.

**Build:** `dotnet build`

### .NET Framework via Mono

**Extensions:**

* **[Mono Debug](https://marketplace.windsurf.com/vscode/item?itemName=chrisatwindsurf.mono-debug)** (`chrisatwindsurf.mono-debug`) – debug adapter for Mono ([Open VSX](https://open-vsx.org/extension/chrisatwindsurf/mono-debug))
* **[C#](https://marketplace.windsurf.com/vscode/item?itemName=muhammad-sammy.csharp)** (`muhammad-sammy.csharp`) for language features

**Debugger:** **You must also install the Mono tool‑chain inside the workspace.** Follow the install guide in the [Mono repo](https://gitlab.winehq.org/mono/mono#compilation-and-installation). The debugger extension connects to that runtime at debug time.

> **⚠️ .NET Framework Configuration**: After installing Mono, to use the C# extension with .NET Framework projects, you need to toggle a specific setting in the IDE Settings. Go to **Settings** (in the C# Extension section) and toggle off  **"Omnisharp: Use Modern Net"**. This setting uses the OmniSharp build for .NET 6, which provides significant performance improvements for SDK-style Framework, .NET Core, and .NET 5+ projects. Note that this version *does not* support non-SDK-style .NET Framework projects, including Unity.

**Build:** `mcs Program.cs`

### Configure `tasks.json` for Your Project

**You must create/edit `.vscode/tasks.json` in your workspace root** and customize these templates:

```jsonc  theme={null}
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "build-dotnet",
      "type": "shell",
      "command": "dotnet",
      "args": ["build", "YourProject.csproj"], // ← Edit this
      "group": "build",
      "problemMatcher": "$msCompile"
    },
    {
      "label": "build-mono",
      "type": "shell",
      "command": "mcs",
      "args": ["YourProgram.cs"], // ← Edit this
      "group": "build"
    }
  ]
}
```

### Configure `launch.json` for Debugging

**You must create/edit `.vscode/launch.json` in your workspace root** and update the paths:

```jsonc  theme={null}
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": ".NET Core Launch",
      "type": "coreclr",
      "request": "launch",
      "preLaunchTask": "build-dotnet",
      "program": "${workspaceFolder}/bin/Debug/net6.0/YourApp.dll", // ← Edit this path
      "cwd": "${workspaceFolder}",
      "args": [] // Add command line arguments if needed
    },
    {
      "name": "Mono Launch",
      "type": "mono",
      "request": "launch",
      "preLaunchTask": "build-mono",
      "program": "${workspaceFolder}/YourProgram.exe", // ← Edit this path
      "cwd": "${workspaceFolder}"
    }
  ]
}
```

### CLI equivalents

```bash  theme={null}

---

← Previous: [C#, .NET, and CPP](./c-net-and-cpp.md) | [Index](./index.md) | Next: [.NET Core](./net-core.md) →