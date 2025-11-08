---
title: "JetBrains"
source: "https://docs.cursor.com/fr/guides/migration/jetbrains"
language: "fr"
language_name: "French"
---

# JetBrains
Source: https://docs.cursor.com/fr/guides/migration/jetbrains

Passe des IDE JetBrains à Cursor avec des outils familiers

Cursor offre une expérience de développement moderne, alimentée par l’IA, qui peut remplacer tes IDE JetBrains. Même si la transition peut sembler déroutante au début, la base de Cursor sur VS Code apporte des fonctionnalités puissantes et de vastes options de personnalisation.

<div id="editor-components">
  ## Composants de l’éditeur
</div>

<div id="extensions">
  ### Extensions
</div>

Les IDE JetBrains sont d’excellents outils, car ils arrivent déjà préconfigurés pour les langages et frameworks auxquels ils sont destinés.

Cursor est différent — c’est une toile vierge dès l’installation : tu peux le personnaliser comme tu veux, sans être limité par les langages et frameworks pour lesquels l’IDE a été conçu.

Cursor a accès à un vaste écosystème d’extensions, et presque toutes les fonctionnalités (et plus encore !) offertes par les IDE JetBrains peuvent être reproduites via ces extensions.

Jette un œil à quelques-unes des extensions populaires ci-dessous :

<CardGroup cols={4}>
  <Card title="Remote SSH" icon="network-wired" href="cursor:extension/anysphere.remote-ssh">
    Extension SSH
  </Card>

  <Card title="Project Manager" icon="folder-tree" href="cursor:extension/alefragnani.project-manager">
    Gérer plusieurs projets
  </Card>

  <Card title="GitLens" icon="git" href="cursor:extension/eamodio.gitlens">
    Intégration Git avancée
  </Card>

  <Card title="Local History" icon="clock-rotate-left" href="cursor:extension/xyz.local-history">
    Suivre les modifications locales des fichiers
  </Card>

  <Card title="Error Lens" icon="bug" href="cursor:extension/usernamehw.errorlens">
    Surlignage des erreurs en ligne
  </Card>

  <Card title="ESLint" icon="code-compare" href="cursor:extension/dbaeumer.vscode-eslint">
    Linting du code
  </Card>

  <Card title="Prettier" icon="wand-magic-sparkles" href="cursor:extension/esbenp.prettier-vscode">
    Formatage du code
  </Card>

  <Card title="Todo Tree" icon="folder-tree" href="cursor:extension/Gruntfuggly.todo-tree">
    Suivre les TODO et FIXME
  </Card>
</CardGroup>

<div id="keyboard-shortcuts">
  ### Raccourcis clavier
</div>

Cursor dispose d’un gestionnaire intégré de raccourcis clavier qui te permet d’associer tes raccourcis préférés à des actions.

Avec cette extension, tu peux retrouver presque tous les raccourcis des IDE JetBrains directement dans Cursor !
Assure-toi de lire la doc de l’extension pour apprendre à la configurer comme tu veux :

<Card title="IntelliJ IDEA Keybindings" icon="keyboard" href="cursor:extension/k--kato.intellij-idea-keybindings">
  Installe cette extension pour retrouver les raccourcis clavier des IDE JetBrains dans Cursor.
</Card>

<Note>
  Raccourcis courants qui diffèrent :

  * Find Action : ⌘/Ctrl+Shift+P  (vs ⌘/Ctrl+Shift+A)
  * Quick Fix : ⌘/Ctrl+.  (vs Alt+Enter)
  * Go to File : ⌘/Ctrl+P  (vs ⌘/Ctrl+Shift+N)
</Note>

<div id="themes">
  ### Thèmes
</div>

Recrée l’apparence de tes IDE JetBrains préférés dans Cursor avec ces thèmes de la communauté.

Choisis le thème standard Darcula, ou prends un thème qui correspond à la coloration syntaxique de tes outils JetBrains.

<CardGroup cols={1}>
  <Card title="JetBrains - Darcula Theme" icon="moon" horizontal href="cursor:extension/rokoroku.vscode-theme-darcula">
    Découvre le classique thème sombre JetBrains Darcula
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
    Retrouve les icônes de fichiers et dossiers familières de JetBrains
  </Card>
</CardGroup>

<div id="font">
  ### Police
</div>

Pour compléter ton expérience façon JetBrains, tu peux utiliser la police officielle JetBrains Mono :

1. Télécharge et installe la police JetBrains Mono sur ton système :

<CardGroup cols={1}>
  <Card title="Download JetBrains Mono" icon="link" horizontal href="https://www.jetbrains.com/lp/mono/" />
</CardGroup>

2. Redémarre Cursor après l’installation de la police
3. Ouvre les paramètres de Cursor (⌘/Ctrl+,)
4. Recherche « Font Family »
5. Définis la famille de polices sur `'JetBrains Mono'`

<Note>
  Pour une meilleure expérience, tu peux aussi activer les ligatures de police en ajoutant « "editor.fontLigatures": true » dans tes paramètres.
</Note>

<div id="ide-specific-migration">
  ## Migration spécifique à chaque IDE
</div>

Beaucoup d'utilisateurs adoraient les IDE JetBrains pour leur prise en charge prête à l'emploi des langages et frameworks auxquels ils étaient destinés. Cursor est différent : c’est une toile vierge dès l’installation, tu peux le personnaliser comme tu veux, sans être limité par les langages et frameworks pour lesquels l’IDE était prévu.

Cursor a déjà accès à l’écosystème d’extensions de VS Code, et presque toutes les fonctionnalités (et plus encore !) offertes par les IDE JetBrains peuvent être recréées via ces extensions.

Jette un œil aux extensions recommandées ci-dessous pour chaque IDE JetBrains.

<div id="intellij-idea-java">
  ### IntelliJ IDEA (Java)
</div>

<CardGroup cols={2}>
  <Card title="Language Support for Java" icon="java" href="cursor:extension/redhat.java">
    Fonctionnalités de base du langage Java
  </Card>

  <Card title="Debugger for Java" icon="bug" href="cursor:extension/vscjava.vscode-java-debug">
    Prise en charge du débogage Java
  </Card>

  <Card title="Test Runner for Java" icon="vial" href="cursor:extension/vscjava.vscode-java-test">
    Exécuter et déboguer des tests Java
  </Card>

  <Card title="Maven for Java" icon="box" href="cursor:extension/vscjava.vscode-maven">
    Prise en charge de Maven
  </Card>
</CardGroup>

<CardGroup cols={1}>
  <Card title="Project Manager for Java" icon="folder-tree" href="cursor:extension/vscjava.vscode-java-dependency" horizontal>
    Outils de gestion de projet
  </Card>
</CardGroup>

<Warning>
  Principales différences :

  * Les configurations Build/Run sont gérées via launch.json
  * Outils Spring Boot disponibles via l’extension ["Spring Boot Extension Pack"](cursor:extension/vmware.vscode-boot-dev-pack)
  * Prise en charge de Gradle via l’extension ["Gradle for Java"](cursor:extension/vscjava.vscode-gradle)
</Warning>

<div id="pycharm-python">
  ### PyCharm (Python)
</div>

<CardGroup cols={2}>
  <Card title="Python" icon="python" href="cursor:extension/ms-python.python">
    Prise en charge de base de Python
  </Card>

  <Card title="Cursor Pyright" icon="bolt" href="cursor:extension/anysphere.cursorpyright">
    Vérification de types rapide
  </Card>

  <Card title="Jupyter" icon="notebook" href="cursor:extension/ms-toolsai.jupyter">
    Prise en charge des notebooks
  </Card>

  <Card title="Ruff" icon="wand-magic-sparkles" href="cursor:extension/charliermarsh.ruff">
    Formateur et linter Python
  </Card>
</CardGroup>

<Note>
  Principales différences :

  * Environnements virtuels gérés via la palette de commandes
  * Configurations de débogage dans launch.json
  * Gestion des dépendances via requirements.txt ou Poetry
</Note>

<div id="webstorm-javascripttypescript">
  ### WebStorm (JavaScript/TypeScript)
</div>

<CardGroup cols={2}>
  <Card title="JavaScript and TypeScript Nightly" icon="js" href="cursor:extension/ms-vscode.vscode-typescript-next">
    Dernières fonctionnalités du langage
  </Card>

  <Card title="ES7+ React/Redux Snippets" icon="react" href="cursor:extension/dsznajder.es7-react-js-snippets">
    Développement React
  </Card>

  <Card title="Vue Language Features" icon="vuejs" href="cursor:extension/Vue.volar">
    Prise en charge de Vue.js
  </Card>

  <Card title="Angular Language Service" icon="angular" href="cursor:extension/Angular.ng-template">
    Développement Angular
  </Card>
</CardGroup>

<Info>
  La plupart des fonctionnalités de WebStorm sont intégrées à Cursor/VS Code, notamment :

  * Vue des scripts npm
  * Débogage
  * Intégration Git
  * Prise en charge de TypeScript
</Info>

<div id="phpstorm-php">
  ### PhpStorm (PHP)
</div>

<CardGroup cols={2}>
  <Card title="PHP Intelephense" icon="php" href="cursor:extension/bmewburn.vscode-intelephense-client">
    Serveur de langage PHP
  </Card>

  <Card title="PHP Debug" icon="bug" href="cursor:extension/xdebug.php-debug">
    Intégration Xdebug
  </Card>

  <Card title="PHP Intellisense" icon="brain" href="cursor:extension/felixfbecker.php-intellisense">
    Intelligence de code
  </Card>

  <Card title="PHP DocBlocker" icon="comment-dots" href="cursor:extension/neilbrayfield.php-docblocker">
    Outils de documentation
  </Card>
</CardGroup>

<Note>
  Principales différences :

  * Configuration de Xdebug via launch.json
  * Intégration de Composer via le terminal
  * Outils de base de données via l’extension ["SQLTools"](cursor:extension/mtxr.sqltools)
</Note>

<div id="rider-net">
  ### Rider (.NET)
</div>

<CardGroup cols={2}>
  <Card title="C#" icon="code" href="cursor:extension/anysphere.csharp">
    Prise en charge C# essentielle
  </Card>

  <Card title="DotRush" icon="toolbox" href="cursor:extension/nromanov.dotrush">
    Environnement de développement C# open source
  </Card>

  <Card title="ReSharper Plugin" icon="box" href="https://www.jetbrains.com/help/resharper-vscode/Get_started.html#installation">
    Plugin C# JetBrains
  </Card>

  <Card title=".NET Install Tool" icon="box-open" href="cursor:extension/ms-dotnettools.vscode-dotnet-runtime">
    Gestion du SDK .NET
  </Card>
</CardGroup>

<Warning>
  Principales différences :

  * Explorateur de solutions via l’explorateur de fichiers
  * Gestion des packages NuGet via la CLI ou des extensions
  * Intégration du test runner via l’explorateur de tests
</Warning>

<div id="goland-go">
  ### GoLand (Go)
</div>

<CardGroup cols={1}>
  <Card title="Go" icon="golang" href="cursor:extension/golang.Go">
    Extension Go officielle
  </Card>
</CardGroup>

<Note>
  Principales différences :

  * Installation des outils Go proposée automatiquement
  * Débogage via launch.json
  * Gestion des packages intégrée avec go.mod
</Note>

<div id="tips-for-a-smooth-transition">
  ## Conseils pour une transition fluide
</div>

<Steps>
  <Step title="Use Command Palette">
    Appuie sur <kbd>⌘</kbd>/<kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd> pour rechercher des commandes
  </Step>

  <Step title="AI Features">
    Exploite les fonctionnalités d’IA de Cursor pour l’autocomplétion et le refactoring de code
  </Step>

  <Step title="Customize Settings">
    Peaufine ton settings.json pour un workflow optimal
  </Step>

  <Step title="Terminal Integration">
    Utilise le terminal intégré pour les opérations en ligne de commande
  </Step>

  <Step title="Extensions">
    Parcours la marketplace de VS Code pour des outils supplémentaires
  </Step>
</Steps>

<Info>
  Souviens-toi que même si certains workflows peuvent être différents, Cursor propose de puissantes fonctionnalités de codage assisté par IA qui peuvent booster ta productivité au-delà des capacités d’un IDE traditionnel.
</Info>

---

← Previous: [iOS & macOS (Swift)](./ios-macos-swift.md) | [Index](./index.md) | Next: [VS Code](./vs-code.md) →