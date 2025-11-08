---
title: "JetBrains"
source: "https://docs.cursor.com/en/guides/migration/jetbrains"
language: "en"
language_name: "English"
---

# JetBrains
Source: https://docs.cursor.com/en/guides/migration/jetbrains

Migrate from JetBrains IDEs to Cursor with familiar tools

Cursor offers a modern, AI-powered coding experience that can replace your JetBrains IDEs. While the transition might feel different at first, Cursor's VS Code-based foundation provides powerful features and extensive customization options.

## Editor Components

### Extensions

JetBrains IDEs are great tools, as they come already pre-configured for the languages and frameworks they are intended for.

Cursor is different - being a blank canvas out of the box, you can customize it to your liking, not being limited by the languages and frameworks the IDE was intended for.

Cursor has access to a vast ecosystem of extensions, and almost all of the functionality (and more!) that JetBrains IDEs offer can be recreated through these extensions.

Take a look at some of these popular extensions below:

<CardGroup cols={4}>
  <Card title="Remote SSH" icon="network-wired" href="cursor:extension/anysphere.remote-ssh">
    SSH Extension
  </Card>

  <Card title="Project Manager" icon="folder-tree" href="cursor:extension/alefragnani.project-manager">
    Manage multiple projects
  </Card>

  <Card title="GitLens" icon="git" href="cursor:extension/eamodio.gitlens">
    Enhanced Git integration
  </Card>

  <Card title="Local History" icon="clock-rotate-left" href="cursor:extension/xyz.local-history">
    Track local file changes
  </Card>

  <Card title="Error Lens" icon="bug" href="cursor:extension/usernamehw.errorlens">
    Inline error highlighting
  </Card>

  <Card title="ESLint" icon="code-compare" href="cursor:extension/dbaeumer.vscode-eslint">
    Code linting
  </Card>

  <Card title="Prettier" icon="wand-magic-sparkles" href="cursor:extension/esbenp.prettier-vscode">
    Code formatting
  </Card>

  <Card title="Todo Tree" icon="folder-tree" href="cursor:extension/Gruntfuggly.todo-tree">
    Track TODOs and FIXMEs
  </Card>
</CardGroup>

### Keyboard Shortcuts

Cursor has a built-in keyboard shortcut manager that allows you to map your favorite keyboard shortcuts to actions.

With this extension, you can bring almost all of the JetBrains IDEs shortcuts directly to Cursor!
Be sure to read the extension's documentation to learn how to configure it to your liking:

<Card title="IntelliJ IDEA Keybindings" icon="keyboard" href="cursor:extension/k--kato.intellij-idea-keybindings">
  Install this extension to bring JetBrains IDEs keyboard shortcuts to Cursor.
</Card>

<Note>
  Common shortcuts that differ:

  * Find Action: ⌘/Ctrl+Shift+P  (vs. ⌘/Ctrl+Shift+A)
  * Quick Fix: ⌘/Ctrl+.  (vs. Alt+Enter)
  * Go to File: ⌘/Ctrl+P  (vs. ⌘/Ctrl+Shift+N)
</Note>

### Themes

Recreate the look and feel of your favorite JetBrains IDEs in Cursor with these community themes.

Choose from the standard Darcula Theme, or pick a theme to match the syntax highlighting of your JetBrains tools.

<CardGroup cols={1}>
  <Card title="JetBrains - Darcula Theme" icon="moon" horizontal href="cursor:extension/rokoroku.vscode-theme-darcula">
    Experience the classic JetBrains Darcula dark theme
  </Card>
</CardGroup>

<CardGroup cols={2}>
  <Card title="JetBrains PyCharm" icon="python" horizontal href="cursor:extension/gabemahoney.pycharm-dark-theme-for-python" />

  <Card title="IntelliJ" icon="java" horizontal href="cursor:extension/compassak.intellij-idea-new-ui" />

  <Card title="JetBrains Fleet" icon="code" horizontal href="cursor:extension/MichaelZhou.fleet-theme" />

  <Card title="JetBrains Rider" icon="hashtag" horizontal href="cursor:extension/muhammad-sammy.rider-theme" />
</CardGroup>

<CardGroup cols={1}>
  <Card title="JetBrains Icons" icon="icons" horizontal href="cursor:extension/ardonplay.vscode-jetbrains-icon-theme">
    Get the familiar JetBrains file and folder icons
  </Card>
</CardGroup>

### Font

To complete your JetBrains-like experience, you can use the official JetBrains Mono font:

1. Download and install JetBrains Mono font onto your system:

<CardGroup cols={1}>
  <Card title="Download JetBrains Mono" icon="link" horizontal href="https://www.jetbrains.com/lp/mono/" />
</CardGroup>

2. Restart Cursor after installing the font
3. Open Settings in Cursor (⌘/Ctrl + ,)
4. Search for "Font Family"
5. Set the font family to `'JetBrains Mono'`

<Note>
  For the best experience, you can also enable font ligatures by setting `"editor.fontLigatures": true` in your settings.
</Note>

## IDE-Specific Migration

Many users loved the JetBrains IDEs for their out-the-box support for the languages and frameworks they were intended for. Cursor is different - being a blank canvas out of the box, you can customize it to your liking, not being limited by the languages and frameworks the IDE was intended for.

Cursor already has access to the extension ecosystem of VS Code, and almost all of the functionality (and more!) that JetBrains IDEs offer can be recreated through these extensions.

Take a look at the following suggested extensions for each JetBrains IDE below.

### IntelliJ IDEA (Java)

<CardGroup cols={2}>
  <Card title="Language Support for Java" icon="java" href="cursor:extension/redhat.java">
    Core Java language features
  </Card>

  <Card title="Debugger for Java" icon="bug" href="cursor:extension/vscjava.vscode-java-debug">
    Java debugging support
  </Card>

  <Card title="Test Runner for Java" icon="vial" href="cursor:extension/vscjava.vscode-java-test">
    Run and debug Java tests
  </Card>

  <Card title="Maven for Java" icon="box" href="cursor:extension/vscjava.vscode-maven">
    Maven support
  </Card>
</CardGroup>

<CardGroup cols={1}>
  <Card title="Project Manager for Java" icon="folder-tree" href="cursor:extension/vscjava.vscode-java-dependency" horizontal>
    Project management tools
  </Card>
</CardGroup>

<Warning>
  Key differences:

  * Build/Run configurations are managed through launch.json
  * Spring Boot tools available through ["Spring Boot Extension Pack"](cursor:extension/vmware.vscode-boot-dev-pack) extension
  * Gradle support via ["Gradle for Java"](cursor:extension/vscjava.vscode-gradle) extension
</Warning>

### PyCharm (Python)

<CardGroup cols={2}>
  <Card title="Python" icon="python" href="cursor:extension/ms-python.python">
    Core Python support
  </Card>

  <Card title="Cursor Pyright" icon="bolt" href="cursor:extension/anysphere.cursorpyright">
    Fast type checking
  </Card>

  <Card title="Jupyter" icon="notebook" href="cursor:extension/ms-toolsai.jupyter">
    Notebook support
  </Card>

  <Card title="Ruff" icon="wand-magic-sparkles" href="cursor:extension/charliermarsh.ruff">
    Python formatter and linter
  </Card>
</CardGroup>

<Note>
  Key differences:

  * Virtual environments managed through command palette
  * Debug configurations in launch.json
  * Requirements management through requirements.txt or Poetry
</Note>

### WebStorm (JavaScript/TypeScript)

<CardGroup cols={2}>
  <Card title="JavaScript and TypeScript Nightly" icon="js" href="cursor:extension/ms-vscode.vscode-typescript-next">
    Latest language features
  </Card>

  <Card title="ES7+ React/Redux Snippets" icon="react" href="cursor:extension/dsznajder.es7-react-js-snippets">
    React development
  </Card>

  <Card title="Vue Language Features" icon="vuejs" href="cursor:extension/Vue.volar">
    Vue.js support
  </Card>

  <Card title="Angular Language Service" icon="angular" href="cursor:extension/Angular.ng-template">
    Angular development
  </Card>
</CardGroup>

<Info>
  Most WebStorm features are built into Cursor/VS Code, including:

  * npm scripts view
  * Debugging
  * Git integration
  * TypeScript support
</Info>

### PhpStorm (PHP)

<CardGroup cols={2}>
  <Card title="PHP Intelephense" icon="php" href="cursor:extension/bmewburn.vscode-intelephense-client">
    PHP language server
  </Card>

  <Card title="PHP Debug" icon="bug" href="cursor:extension/xdebug.php-debug">
    Xdebug integration
  </Card>

  <Card title="PHP Intellisense" icon="brain" href="cursor:extension/felixfbecker.php-intellisense">
    Code intelligence
  </Card>

  <Card title="PHP DocBlocker" icon="comment-dots" href="cursor:extension/neilbrayfield.php-docblocker">
    Documentation tools
  </Card>
</CardGroup>

<Note>
  Key differences:

  * Xdebug configuration through launch.json
  * Composer integration via terminal
  * Database tools through ["SQLTools"](cursor:extension/mtxr.sqltools) extension
</Note>

### Rider (.NET)

<CardGroup cols={2}>
  <Card title="C#" icon="code" href="cursor:extension/anysphere.csharp">
    Core C# support
  </Card>

  <Card title="DotRush" icon="toolbox" href="cursor:extension/nromanov.dotrush">
    Open-Source C# Development Environment
  </Card>

  <Card title="ReSharper Plugin" icon="box" href="https://www.jetbrains.com/help/resharper-vscode/Get_started.html#installation">
    JetBrains C# Plugin
  </Card>

  <Card title=".NET Install Tool" icon="box-open" href="cursor:extension/ms-dotnettools.vscode-dotnet-runtime">
    .NET SDK management
  </Card>
</CardGroup>

<Warning>
  Key differences:

  * Solution explorer through file explorer
  * NuGet package management through CLI or extensions
  * Test runner integration through test explorer
</Warning>

### GoLand (Go)

<CardGroup cols={1}>
  <Card title="Go" icon="golang" href="cursor:extension/golang.Go">
    Official Go extension
  </Card>
</CardGroup>

<Note>
  Key differences:

  * Go tools installation prompted automatically
  * Debugging through launch.json
  * Package management integrated with go.mod
</Note>

## Tips for a Smooth Transition

<Steps>
  <Step title="Use Command Palette">
    Press <kbd>⌘</kbd>/<kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd> to find commands
  </Step>

  <Step title="AI Features">
    Leverage Cursor's AI features for code completion and refactoring
  </Step>

  <Step title="Customize Settings">
    Fine-tune your settings.json for optimal workflow
  </Step>

  <Step title="Terminal Integration">
    Use the built-in terminal for command-line operations
  </Step>

  <Step title="Extensions">
    Browse the VS Code marketplace for additional tools
  </Step>
</Steps>

<Info>
  Remember that while some workflows might be different, Cursor offers powerful AI-assisted coding features that can enhance your productivity beyond traditional IDE capabilities.
</Info>

---

← Previous: [iOS & macOS (Swift)](./ios-macos-swift.md) | [Index](./index.md) | Next: [VS Code](./vs-code.md) →