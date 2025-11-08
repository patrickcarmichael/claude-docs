---
title: "Dev Containers"
source: ""
---

# Dev Containers

Windsurf supports Development Containers on Mac, Windows, and Linux for both local and remote (via SSH) workflows.

Prerequisites:

* Local: Docker must be installed on your machine and accessible from the Windsurf terminal.
* Remote over SSH: Connect to a remote host using Windsurf Remote-SSH. Docker must be installed and accessible on the remote host (from the remote shell). Your project should include a `devcontainer.json` or equivalent config.

Available commands (in both local and remote windows):

1. `Dev Containers: Open Folder in Container`
   * Open a new workspace using a specified `devcontainer.json`.
2. `Dev Containers: Reopen in Container`
   * Reopen the current workspace in a new container defined by your `devcontainer.json`.
3. `Dev Containers: Attach to Running Container`
   * Attach to an existing Docker container and connect your current workspace to it. If the container does not follow the [Development Container Specificaton](https://containers.dev/implementors/spec/), Windsurf will attempt best-effort detection of the remote user and environment.
4. `Dev Containers: Reopen Folder Locally`
   * When connected to a development container, disconnect and reopen the workspace on the local filesystem.
5. `Dev Containers: Show Windsurf Dev Containers Log`
   * Open the Dev Containers log output for troubleshooting.

These commands are available from the Command Palette and will also appear when you click the `Open a Remote Window` button in the bottom left (including when you are connected to a remote host via SSH).

Related:

* `Remote Explorer: Focus on Dev Containers (Windsurf) View` — quickly open the Dev Containers view.

---

← Previous: [SSH Support](./ssh-support.md) | [Index](./index.md) | Next: [WSL (Beta)](./wsl-beta.md) →