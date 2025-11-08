---
title: "JetBrains"
source: "https://docs.cursor.com/de/guides/migration/jetbrains"
language: "de"
language_name: "German"
---

# JetBrains
Source: https://docs.cursor.com/de/guides/migration/jetbrains

Mit vertrauten Tools von JetBrains-IDEs zu Cursor wechseln

Cursor bietet ein modernes, KI-gestütztes Coding-Erlebnis, das deine JetBrains-IDEs ersetzen kann. Auch wenn sich der Umstieg anfangs ungewohnt anfühlt, bietet Cursors auf VS Code basierende Grundlage leistungsstarke Features und umfangreiche Anpassungsmöglichkeiten.

<div id="editor-components">
  ## Editor Components
</div>

<div id="extensions">
  ### Extensions
</div>

JetBrains-IDEs sind großartige Tools, da sie bereits für die vorgesehenen Sprachen und Frameworks vorkonfiguriert sind.

Cursor ist anders – als leere Leinwand out of the box kannst du es nach deinen Vorlieben anpassen, ohne durch die Sprachen und Frameworks eingeschränkt zu sein, für die die IDE gedacht war.

Cursor hat Zugriff auf ein riesiges Ökosystem an Erweiterungen, und fast die gesamte Funktionalität (und mehr!), die JetBrains-IDEs bieten, lässt sich über diese Erweiterungen nachbilden.

Schau dir unten einige dieser beliebten Erweiterungen an:

<CardGroup cols={4}>
  <Card title="Remote SSH" icon="network-wired" href="cursor:extension/anysphere.remote-ssh">
    SSH-Erweiterung
  </Card>

  <Card title="Project Manager" icon="folder-tree" href="cursor:extension/alefragnani.project-manager">
    Mehrere Projekte verwalten
  </Card>

  <Card title="GitLens" icon="git" href="cursor:extension/eamodio.gitlens">
    Erweiterte Git-Integration
  </Card>

  <Card title="Local History" icon="clock-rotate-left" href="cursor:extension/xyz.local-history">
    Lokale Dateiversionshistorie nachverfolgen
  </Card>

  <Card title="Error Lens" icon="bug" href="cursor:extension/usernamehw.errorlens">
    Inline-Fehlerhervorhebung
  </Card>

  <Card title="ESLint" icon="code-compare" href="cursor:extension/dbaeumer.vscode-eslint">
    Code-Linting
  </Card>

  <Card title="Prettier" icon="wand-magic-sparkles" href="cursor:extension/esbenp.prettier-vscode">
    Code-Formatierung
  </Card>

  <Card title="Todo Tree" icon="folder-tree" href="cursor:extension/Gruntfuggly.todo-tree">
    TODOs und FIXMEs nachverfolgen
  </Card>
</CardGroup>

<div id="keyboard-shortcuts">
  ### Keyboard Shortcuts
</div>

Cursor hat einen integrierten Shortcut-Manager, mit dem du deine Lieblingskürzel Aktionen zuordnen kannst.

Mit dieser Erweiterung kannst du fast alle Shortcuts der JetBrains-IDEs direkt in Cursor verwenden!
Lies unbedingt die Dokumentation der Erweiterung, um zu erfahren, wie du sie nach deinen Wünschen konfigurierst:

<Card title="IntelliJ IDEA Keybindings" icon="keyboard" href="cursor:extension/k--kato.intellij-idea-keybindings">
  Installiere diese Erweiterung, um JetBrains-IDE-Shortcuts in Cursor zu nutzen.
</Card>

<Note>
  Häufig abweichende Shortcuts:

  * Aktion finden: ⌘/Ctrl+Shift+P  (vs. ⌘/Ctrl+Shift+A)
  * Quick Fix: ⌘/Ctrl+.  (vs. Alt+Enter)
  * Datei öffnen: ⌘/Ctrl+P  (vs. ⌘/Ctrl+Shift+N)
</Note>

<div id="themes">
  ### Themes
</div>

Repliziere das Look-and-Feel deiner Lieblings-JetBrains-IDEs in Cursor mit diesen Community-Themes.

Wähle das Standard-Darcula-Theme oder ein Theme, das zum Syntax-Highlighting deiner JetBrains-Tools passt.

<CardGroup cols={1}>
  <Card title="JetBrains - Darcula Theme" icon="moon" horizontal href="cursor:extension/rokoroku.vscode-theme-darcula">
    Erlebe das klassische JetBrains-Darcula-Dark-Theme
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
    Hol dir die vertrauten JetBrains-Datei- und Ordnersymbole
  </Card>
</CardGroup>

<div id="font">
  ### Font
</div>

Um dein JetBrains-ähnliches Setup abzurunden, kannst du die offizielle Schriftart JetBrains Mono verwenden:

1. Lade die Schriftart JetBrains Mono herunter und installiere sie auf deinem System:

<CardGroup cols={1}>
  <Card title="Download JetBrains Mono" icon="link" horizontal href="https://www.jetbrains.com/lp/mono/" />
</CardGroup>

2. Starte Cursor nach der Installation der Schriftart neu
3. Öffne die Einstellungen in Cursor (⌘/Ctrl + ,)
4. Suche nach "Font Family"
5. Setze die Schriftfamilie auf 'JetBrains Mono'

<Note>
  Für das beste Erlebnis kannst du außerdem Schriftligaturen aktivieren, indem du in deinen Einstellungen `"editor.fontLigatures": true` festlegst.
</Note>

<div id="ide-specific-migration">
  ## IDE-spezifische Migration
</div>

Viele Nutzer lieben die JetBrains-IDEs wegen ihrer Out-of-the-box-Unterstützung für die Sprachen und Frameworks, für die sie gedacht sind. Cursor ist anders – als leere Leinwand out of the box kannst du ihn nach deinem Geschmack anpassen, ohne durch die Sprachen und Frameworks eingeschränkt zu sein, für die die IDE ursprünglich vorgesehen war.

Cursor hat bereits Zugriff auf das Erweiterungs-Ökosystem von VS Code, und fast die gesamte Funktionalität (und mehr!), die JetBrains-IDEs bieten, lässt sich durch diese Erweiterungen nachbilden.

Schau dir die folgenden empfohlenen Erweiterungen für jede JetBrains-IDE an.

<div id="intellij-idea-java">
  ### IntelliJ IDEA (Java)
</div>

<CardGroup cols={2}>
  <Card title="Language Support for Java" icon="java" href="cursor:extension/redhat.java">
    Zentrale Java-Sprachfunktionen
  </Card>

  <Card title="Debugger for Java" icon="bug" href="cursor:extension/vscjava.vscode-java-debug">
    Java-Debugging
  </Card>

  <Card title="Test Runner for Java" icon="vial" href="cursor:extension/vscjava.vscode-java-test">
    Java-Tests ausführen und debuggen
  </Card>

  <Card title="Maven for Java" icon="box" href="cursor:extension/vscjava.vscode-maven">
    Maven-Unterstützung
  </Card>
</CardGroup>

<CardGroup cols={1}>
  <Card title="Project Manager for Java" icon="folder-tree" href="cursor:extension/vscjava.vscode-java-dependency" horizontal>
    Projektmanagement-Tools
  </Card>
</CardGroup>

<Warning>
  Wesentliche Unterschiede:

  * Build-/Run-Konfigurationen werden über launch.json verwaltet
  * Spring-Boot-Tools über die Erweiterung ["Spring Boot Extension Pack"](cursor:extension/vmware.vscode-boot-dev-pack) verfügbar
  * Gradle-Unterstützung über die Erweiterung ["Gradle for Java"](cursor:extension/vscjava.vscode-gradle)
</Warning>

<div id="pycharm-python">
  ### PyCharm (Python)
</div>

<CardGroup cols={2}>
  <Card title="Python" icon="python" href="cursor:extension/ms-python.python">
    Zentrale Python-Unterstützung
  </Card>

  <Card title="Cursor Pyright" icon="bolt" href="cursor:extension/anysphere.cursorpyright">
    Schnelles Type-Checking
  </Card>

  <Card title="Jupyter" icon="notebook" href="cursor:extension/ms-toolsai.jupyter">
    Notebook-Unterstützung
  </Card>

  <Card title="Ruff" icon="wand-magic-sparkles" href="cursor:extension/charliermarsh.ruff">
    Python-Formatter und Linter
  </Card>
</CardGroup>

<Note>
  Wesentliche Unterschiede:

  * Virtuelle Umgebungen über die Befehlspalette verwaltet
  * Debug-Konfigurationen in launch.json
  * Requirements-Management über requirements.txt oder Poetry
</Note>

<div id="webstorm-javascripttypescript">
  ### WebStorm (JavaScript/TypeScript)
</div>

<CardGroup cols={2}>
  <Card title="JavaScript and TypeScript Nightly" icon="js" href="cursor:extension/ms-vscode.vscode-typescript-next">
    Neueste Sprachfeatures
  </Card>

  <Card title="ES7+ React/Redux Snippets" icon="react" href="cursor:extension/dsznajder.es7-react-js-snippets">
    React-Entwicklung
  </Card>

  <Card title="Vue Language Features" icon="vuejs" href="cursor:extension/Vue.volar">
    Vue.js-Unterstützung
  </Card>

  <Card title="Angular Language Service" icon="angular" href="cursor:extension/Angular.ng-template">
    Angular-Entwicklung
  </Card>
</CardGroup>

<Info>
  Die meisten WebStorm-Features sind in Cursor/VS Code integriert, darunter:

  * npm-Skripte-Ansicht
  * Debugging
  * Git-Integration
  * TypeScript-Unterstützung
</Info>

<div id="phpstorm-php">
  ### PhpStorm (PHP)
</div>

<CardGroup cols={2}>
  <Card title="PHP Intelephense" icon="php" href="cursor:extension/bmewburn.vscode-intelephense-client">
    PHP Language Server
  </Card>

  <Card title="PHP Debug" icon="bug" href="cursor:extension/xdebug.php-debug">
    Xdebug-Integration
  </Card>

  <Card title="PHP Intellisense" icon="brain" href="cursor:extension/felixfbecker.php-intellisense">
    Code-Intelligenz
  </Card>

  <Card title="PHP DocBlocker" icon="comment-dots" href="cursor:extension/neilbrayfield.php-docblocker">
    Dokumentations-Tools
  </Card>
</CardGroup>

<Note>
  Wesentliche Unterschiede:

  * Xdebug-Konfiguration über launch.json
  * Composer-Integration über das Terminal
  * Datenbank-Tools über die Erweiterung ["SQLTools"](cursor:extension/mtxr.sqltools)
</Note>

<div id="rider-net">
  ### Rider (.NET)
</div>

<CardGroup cols={2}>
  <Card title="C#" icon="code" href="cursor:extension/anysphere.csharp">
    Kernsupport für C#
  </Card>

  <Card title="DotRush" icon="toolbox" href="cursor:extension/nromanov.dotrush">
    Open-Source-C#-Entwicklungsumgebung
  </Card>

  <Card title="ReSharper Plugin" icon="box" href="https://www.jetbrains.com/help/resharper-vscode/Get_started.html#installation">
    JetBrains-C#-Plugin
  </Card>

  <Card title=".NET Install Tool" icon="box-open" href="cursor:extension/ms-dotnettools.vscode-dotnet-runtime">
    .NET-SDK-Management
  </Card>
</CardGroup>

<Warning>
  Wesentliche Unterschiede:

  * Projektmappen-Explorer über Dateiexplorer
  * NuGet-Paketmanagement über CLI oder Erweiterungen
  * Testrunner-Integration über Test-Explorer
</Warning>

<div id="goland-go">
  ### GoLand (Go)
</div>

<CardGroup cols={1}>
  <Card title="Go" icon="golang" href="cursor:extension/golang.Go">
    Offizielle Go-Erweiterung
  </Card>
</CardGroup>

<Note>
  Wesentliche Unterschiede:

  * Installation der Go-Tools wird automatisch angestoßen
  * Debugging über launch.json
  * Paketmanagement integriert mit go.mod
</Note>

<div id="tips-for-a-smooth-transition">
  ## Tipps für einen reibungslosen Umstieg
</div>

<Steps>
  <Step title="Befehlspalette verwenden">
    Drück <kbd>⌘</kbd>/<kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd>, um Befehle zu finden
  </Step>

  <Step title="KI-Funktionen">
    Nutz die KI-Funktionen von Cursor für Codevervollständigung und Refactoring
  </Step>

  <Step title="Einstellungen anpassen">
    Feine deine settings.json für einen optimalen Workflow ab
  </Step>

  <Step title="Terminal-Integration">
    Nutz das integrierte Terminal für Befehlszeilen-Operationen
  </Step>

  <Step title="Erweiterungen">
    Stöber im VS Code Marketplace nach zusätzlichen Tools
  </Step>
</Steps>

<Info>
  Denk dran: Auch wenn einige Workflows anders sind, bietet Cursor leistungsstarke KI-unterstützte Coding-Funktionen, die deine Produktivität über die Möglichkeiten traditioneller IDEs hinaus steigern können.
</Info>

---

← Previous: [iOS & macOS (Swift)](./ios-macos-swift.md) | [Index](./index.md) | Next: [VS Code](./vs-code.md) →