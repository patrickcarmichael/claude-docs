---
title: "JetBrains"
source: "https://docs.cursor.com/es/guides/migration/jetbrains"
language: "es"
language_name: "Spanish"
---

# JetBrains
Source: https://docs.cursor.com/es/guides/migration/jetbrains

Migra de los IDE de JetBrains a Cursor con herramientas familiares

Cursor ofrece una experiencia de programación moderna con IA que puede reemplazar tus IDE de JetBrains. Aunque el cambio pueda sentirse distinto al principio, la base de Cursor en VS Code ofrece funciones potentes y amplias opciones de personalización.

<div id="editor-components">
  ## Componentes del editor
</div>

<div id="extensions">
  ### Extensiones
</div>

Los IDE de JetBrains son herramientas geniales, ya que vienen preconfigurados para los lenguajes y frameworks para los que están pensados.

Cursor es diferente: como un lienzo en blanco desde el principio, podés personalizarlo a tu gusto, sin estar limitado por los lenguajes y frameworks para los que el IDE fue pensado.

Cursor tiene acceso a un vasto ecosistema de extensiones, y casi todas las funcionalidades (¡y más!) que ofrecen los IDE de JetBrains se pueden recrear mediante estas extensiones.

Mirá algunas de estas extensiones populares a continuación:

<CardGroup cols={4}>
  <Card title="Remote SSH" icon="network-wired" href="cursor:extension/anysphere.remote-ssh">
    Extensión SSH
  </Card>

  <Card title="Project Manager" icon="folder-tree" href="cursor:extension/alefragnani.project-manager">
    Gestioná múltiples proyectos
  </Card>

  <Card title="GitLens" icon="git" href="cursor:extension/eamodio.gitlens">
    Integración de Git mejorada
  </Card>

  <Card title="Local History" icon="clock-rotate-left" href="cursor:extension/xyz.local-history">
    Rastreá cambios locales de archivos
  </Card>

  <Card title="Error Lens" icon="bug" href="cursor:extension/usernamehw.errorlens">
    Resaltado de errores en línea
  </Card>

  <Card title="ESLint" icon="code-compare" href="cursor:extension/dbaeumer.vscode-eslint">
    Linting de código
  </Card>

  <Card title="Prettier" icon="wand-magic-sparkles" href="cursor:extension/esbenp.prettier-vscode">
    Formateo de código
  </Card>

  <Card title="Todo Tree" icon="folder-tree" href="cursor:extension/Gruntfuggly.todo-tree">
    Rastreá TODO y FIXME
  </Card>
</CardGroup>

<div id="keyboard-shortcuts">
  ### Atajos de teclado
</div>

Cursor tiene un gestor de atajos de teclado incorporado que te permite mapear tus atajos favoritos a acciones.

Con esta extensión, podés traer casi todos los atajos de los IDE de JetBrains directamente a Cursor.
Asegurate de leer la documentación de la extensión para aprender cómo configurarla a tu gusto:

<Card title="IntelliJ IDEA Keybindings" icon="keyboard" href="cursor:extension/k--kato.intellij-idea-keybindings">
  Instalá esta extensión para traer los atajos de los IDE de JetBrains a Cursor.
</Card>

<Note>
  Atajos comunes que difieren:

  * Find Action: ⌘/Ctrl+Shift+P  (vs. ⌘/Ctrl+Shift+A)
  * Quick Fix: ⌘/Ctrl+.  (vs. Alt+Enter)
  * Go to File: ⌘/Ctrl+P  (vs. ⌘/Ctrl+Shift+N)
</Note>

<div id="themes">
  ### Temas
</div>

Recreá la apariencia y la sensación de tus IDE favoritos de JetBrains en Cursor con estos temas de la comunidad.

Elegí entre el tema estándar Darcula o seleccioná un tema que coincida con el resaltado de sintaxis de tus herramientas de JetBrains.

<CardGroup cols={1}>
  <Card title="JetBrains - Darcula Theme" icon="moon" horizontal href="cursor:extension/rokoroku.vscode-theme-darcula">
    Experimentá el clásico tema oscuro Darcula de JetBrains
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
    Obtené los íconos de archivos y carpetas de JetBrains que ya conocés
  </Card>
</CardGroup>

<div id="font">
  ### Fuente
</div>

Para completar tu experiencia al estilo JetBrains, podés usar la fuente oficial JetBrains Mono:

1. Descargá e instalá la fuente JetBrains Mono en tu sistema:

<CardGroup cols={1}>
  <Card title="Download JetBrains Mono" icon="link" horizontal href="https://www.jetbrains.com/lp/mono/" />
</CardGroup>

2. Reiniciá Cursor después de instalar la fuente
3. Abrí Settings en Cursor (⌘/Ctrl + ,)
4. Buscá "Font Family"
5. Configurá la familia tipográfica en `'JetBrains Mono'`

<Note>
  Para una mejor experiencia, también podés habilitar las ligaduras tipográficas configurando "editor.fontLigatures": true en tus ajustes.
</Note>

<div id="ide-specific-migration">
  ## Migración específica del IDE
</div>

A muchxs usuarixs les encantaban los IDE de JetBrains por su soporte listo para usar para los lenguajes y frameworks para los que fueron diseñados. Cursor es diferente: como un lienzo en blanco desde el inicio, podés personalizarlo a tu gusto, sin estar limitadx por los lenguajes y frameworks para los que el IDE fue pensado.

Cursor ya tiene acceso al ecosistema de extensiones de VS Code, y casi toda la funcionalidad (¡y más!) que ofrecen los IDE de JetBrains se puede recrear mediante estas extensiones.

Echale un vistazo a las siguientes extensiones sugeridas para cada IDE de JetBrains.

<div id="intellij-idea-java">
  ### IntelliJ IDEA (Java)
</div>

<CardGroup cols={2}>
  <Card title="Language Support for Java" icon="java" href="cursor:extension/redhat.java">
    Funcionalidades básicas del lenguaje Java
  </Card>

  <Card title="Debugger for Java" icon="bug" href="cursor:extension/vscjava.vscode-java-debug">
    Soporte de depuración para Java
  </Card>

  <Card title="Test Runner for Java" icon="vial" href="cursor:extension/vscjava.vscode-java-test">
    Ejecutá y depurá tests de Java
  </Card>

  <Card title="Maven for Java" icon="box" href="cursor:extension/vscjava.vscode-maven">
    Soporte para Maven
  </Card>
</CardGroup>

<CardGroup cols={1}>
  <Card title="Project Manager for Java" icon="folder-tree" href="cursor:extension/vscjava.vscode-java-dependency" horizontal>
    Herramientas de gestión de proyectos
  </Card>
</CardGroup>

<Warning>
  Diferencias clave:

  * Las configuraciones de Build/Run se gestionan mediante launch.json
  * Herramientas de Spring Boot disponibles a través de la extensión ["Spring Boot Extension Pack"](cursor:extension/vmware.vscode-boot-dev-pack)
  * Soporte para Gradle mediante la extensión ["Gradle for Java"](cursor:extension/vscjava.vscode-gradle)
</Warning>

<div id="pycharm-python">
  ### PyCharm (Python)
</div>

<CardGroup cols={2}>
  <Card title="Python" icon="python" href="cursor:extension/ms-python.python">
    Soporte básico para Python
  </Card>

  <Card title="Cursor Pyright" icon="bolt" href="cursor:extension/anysphere.cursorpyright">
    Chequeo de tipos rápido
  </Card>

  <Card title="Jupyter" icon="notebook" href="cursor:extension/ms-toolsai.jupyter">
    Soporte para notebooks
  </Card>

  <Card title="Ruff" icon="wand-magic-sparkles" href="cursor:extension/charliermarsh.ruff">
    Formateador y linter de Python
  </Card>
</CardGroup>

<Note>
  Diferencias clave:

  * Entornos virtuales gestionados desde la paleta de comandos
  * Configuraciones de depuración en launch.json
  * Gestión de dependencias con requirements.txt o Poetry
</Note>

<div id="webstorm-javascripttypescript">
  ### WebStorm (JavaScript/TypeScript)
</div>

<CardGroup cols={2}>
  <Card title="JavaScript and TypeScript Nightly" icon="js" href="cursor:extension/ms-vscode.vscode-typescript-next">
    Últimas funcionalidades del lenguaje
  </Card>

  <Card title="ES7+ React/Redux Snippets" icon="react" href="cursor:extension/dsznajder.es7-react-js-snippets">
    Desarrollo con React
  </Card>

  <Card title="Vue Language Features" icon="vuejs" href="cursor:extension/Vue.volar">
    Soporte para Vue.js
  </Card>

  <Card title="Angular Language Service" icon="angular" href="cursor:extension/Angular.ng-template">
    Desarrollo con Angular
  </Card>
</CardGroup>

<Info>
  La mayoría de las funcionalidades de WebStorm están integradas en Cursor/VS Code, incluidas:

  * Vista de scripts de npm
  * Depuración
  * Integración con Git
  * Soporte para TypeScript
</Info>

<div id="phpstorm-php">
  ### PhpStorm (PHP)
</div>

<CardGroup cols={2}>
  <Card title="PHP Intelephense" icon="php" href="cursor:extension/bmewburn.vscode-intelephense-client">
    Servidor de lenguaje para PHP
  </Card>

  <Card title="PHP Debug" icon="bug" href="cursor:extension/xdebug.php-debug">
    Integración con Xdebug
  </Card>

  <Card title="PHP Intellisense" icon="brain" href="cursor:extension/felixfbecker.php-intellisense">
    Inteligencia de código
  </Card>

  <Card title="PHP DocBlocker" icon="comment-dots" href="cursor:extension/neilbrayfield.php-docblocker">
    Herramientas de documentación
  </Card>
</CardGroup>

<Note>
  Diferencias clave:

  * Configuración de Xdebug mediante launch.json
  * Integración con Composer vía terminal
  * Herramientas de base de datos a través de la extensión ["SQLTools"](cursor:extension/mtxr.sqltools)
</Note>

<div id="rider-net">
  ### Rider (.NET)
</div>

<CardGroup cols={2}>
  <Card title="C#" icon="code" href="cursor:extension/anysphere.csharp">
    Compatibilidad básica con C#
  </Card>

  <Card title="DotRush" icon="toolbox" href="cursor:extension/nromanov.dotrush">
    Entorno de desarrollo C# de código abierto
  </Card>

  <Card title="ReSharper Plugin" icon="box" href="https://www.jetbrains.com/help/resharper-vscode/Get_started.html#installation">
    Complemento de JetBrains para C#
  </Card>

  <Card title=".NET Install Tool" icon="box-open" href="cursor:extension/ms-dotnettools.vscode-dotnet-runtime">
    Gestión del SDK de .NET
  </Card>
</CardGroup>

<Warning>
  Diferencias clave:

  * Explorador de soluciones a través del explorador de archivos
  * Gestión de paquetes NuGet mediante CLI o extensiones
  * Integración del runner de tests a través del explorador de tests
</Warning>

<div id="goland-go">
  ### GoLand (Go)
</div>

<CardGroup cols={1}>
  <Card title="Go" icon="golang" href="cursor:extension/golang.Go">
    Extensión oficial de Go
  </Card>
</CardGroup>

<Note>
  Diferencias clave:

  * Instalación de herramientas de Go solicitada automáticamente
  * Depuración mediante launch.json
  * Gestión de paquetes integrada con go.mod
</Note>

<div id="tips-for-a-smooth-transition">
  ## Consejos para una transición fluida
</div>

<Steps>
  <Step title="Usa la paleta de comandos">
    Presiona <kbd>⌘</kbd>/<kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd> para buscar comandos
  </Step>

  <Step title="Funciones de IA">
    Aprovecha las funciones de IA de Cursor para autocompletar y refactorizar código
  </Step>

  <Step title="Personaliza la configuración">
    Ajusta tu settings.json para un flujo de trabajo óptimo
  </Step>

  <Step title="Integración del terminal">
    Usa el terminal integrado para operaciones en la línea de comandos
  </Step>

  <Step title="Extensiones">
    Explora el Marketplace de VS Code para herramientas adicionales
  </Step>
</Steps>

<Info>
  Recuerda que, aunque algunos flujos de trabajo pueden ser diferentes, Cursor ofrece potentes funciones de programación asistida por IA que pueden aumentar tu productividad más allá de las capacidades de los IDE tradicionales.
</Info>

---

← Previous: [iOS y macOS (Swift)](./ios-y-macos-swift.md) | [Index](./index.md) | Next: [VS Code](./vs-code.md) →