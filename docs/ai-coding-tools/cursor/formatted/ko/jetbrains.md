---
title: "JetBrains"
source: "https://docs.cursor.com/ko/guides/migration/jetbrains"
language: "ko"
language_name: "Korean"
---

# JetBrains
Source: https://docs.cursor.com/ko/guides/migration/jetbrains

익숙한 도구로 JetBrains IDE에서 Cursor로 마이그레이션

Cursor는 JetBrains IDE를 대체할 수 있는 현대적인 AI 기반 코딩 경험을 제공해. 처음엔 전환이 다르게 느껴질 수 있지만, VS Code 기반인 Cursor는 강력한 기능과 폭넓은 커스터마이징 옵션을 제공해.

<div id="editor-components">
  ## Editor Components
</div>

<div id="extensions">
  ### Extensions
</div>

JetBrains IDE는 대상 언어와 프레임워크에 맞게 이미 사전 구성되어 있어서 훌륭한 도구야.

Cursor는 달라 — 처음엔 말 그대로 빈 캔버스라 IDE가 의도한 언어나 프레임워크에 묶이지 않고 원하는 대로 커스터마이즈할 수 있어.

Cursor는 거대한 확장 생태계에 접근할 수 있고, JetBrains IDE가 제공하는 거의 모든 기능(그 이상도!)을 이 확장들로 재현할 수 있어.

아래 인기 확장들을 살펴봐:

<CardGroup cols={4}>
  <Card title="Remote SSH" icon="network-wired" href="cursor:extension/anysphere.remote-ssh">
    SSH 확장
  </Card>

  <Card title="Project Manager" icon="folder-tree" href="cursor:extension/alefragnani.project-manager">
    여러 프로젝트 관리
  </Card>

  <Card title="GitLens" icon="git" href="cursor:extension/eamodio.gitlens">
    강화된 Git 통합
  </Card>

  <Card title="Local History" icon="clock-rotate-left" href="cursor:extension/xyz.local-history">
    로컬 파일 변경 추적
  </Card>

  <Card title="Error Lens" icon="bug" href="cursor:extension/usernamehw.errorlens">
    인라인 오류 하이라이트
  </Card>

  <Card title="ESLint" icon="code-compare" href="cursor:extension/dbaeumer.vscode-eslint">
    코드 린팅
  </Card>

  <Card title="Prettier" icon="wand-magic-sparkles" href="cursor:extension/esbenp.prettier-vscode">
    코드 포매팅
  </Card>

  <Card title="Todo Tree" icon="folder-tree" href="cursor:extension/Gruntfuggly.todo-tree">
    TODO와 FIXME 추적
  </Card>
</CardGroup>

<div id="keyboard-shortcuts">
  ### Keyboard Shortcuts
</div>

Cursor엔 즐겨 쓰는 키보드 단축키를 액션에 매핑할 수 있는 내장 단축키 관리자가 있어.

이 확장으로 JetBrains IDE의 단축키 대부분을 그대로 Cursor에 가져올 수 있어!
원하는 대로 설정하려면 확장 문서를 꼭 읽어봐:

<Card title="IntelliJ IDEA Keybindings" icon="keyboard" href="cursor:extension/k--kato.intellij-idea-keybindings">
  JetBrains IDE의 키보드 단축키를 Cursor로 가져오려면 이 확장을 설치해.
</Card>

<Note>
  달라지는 대표 단축키:

  * Find Action: ⌘/Ctrl+Shift+P  (vs. ⌘/Ctrl+Shift+A)
  * Quick Fix: ⌘/Ctrl+.  (vs. Alt+Enter)
  * Go to File: ⌘/Ctrl+P  (vs. ⌘/Ctrl+Shift+N)
</Note>

<div id="themes">
  ### Themes
</div>

이 커뮤니티 테마로 Cursor에서 좋아하는 JetBrains IDE의 룩앤필을 그대로 재현해.

표준 Darcula 테마를 쓰거나, JetBrains 도구의 문법 하이라이트와 맞는 테마를 골라봐.

<CardGroup cols={1}>
  <Card title="JetBrains - Darcula Theme" icon="moon" horizontal href="cursor:extension/rokoroku.vscode-theme-darcula">
    클래식한 JetBrains Darcula 다크 테마를 경험해봐
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
    익숙한 JetBrains 파일·폴더 아이콘 사용
  </Card>
</CardGroup>

<div id="font">
  ### Font
</div>

JetBrains 같은 경험을 완성하려면 공식 JetBrains Mono 폰트를 써봐:

1. 시스템에 JetBrains Mono 폰트를 다운로드해 설치해:

<CardGroup cols={1}>
  <Card title="Download JetBrains Mono" icon="link" horizontal href="https://www.jetbrains.com/lp/mono/" />
</CardGroup>

2. 폰트 설치 후 Cursor를 재시작해
3. Cursor에서 Settings 열기 (⌘/Ctrl + ,)
4. "Font Family"를 검색해
5. 폰트 패밀리를 'JetBrains Mono'로 설정해

<Note>
  최적의 사용 경험을 위해 설정에서 "editor.fontLigatures": true 로 설정해 폰트 합자를 활성화할 수도 있어.
</Note>

<div id="ide-specific-migration">
  ## IDE별 마이그레이션
</div>

많은 사용자가 각 언어와 프레임워크에 최적화된 기본 지원 때문에 JetBrains IDE를 좋아했어. Cursor는 달라 — 처음부터 빈 캔버스라서, IDE가 의도한 언어나 프레임워크에 얽매이지 않고 원하는 대로 커스터마이즈할 수 있어.

Cursor는 이미 VS Code의 확장 생태계를 그대로 쓸 수 있고, JetBrains IDE가 제공하는 거의 모든 기능(그 이상!)을 이 확장들로 재현할 수 있어.

아래에서 각 JetBrains IDE별 추천 확장을 확인해봐.

<div id="intellij-idea-java">
  ### IntelliJ IDEA (Java)
</div>

<CardGroup cols={2}>
  <Card title="Language Support for Java" icon="java" href="cursor:extension/redhat.java">
    핵심 Java 언어 기능
  </Card>

  <Card title="Debugger for Java" icon="bug" href="cursor:extension/vscjava.vscode-java-debug">
    Java 디버깅 지원
  </Card>

  <Card title="Test Runner for Java" icon="vial" href="cursor:extension/vscjava.vscode-java-test">
    Java 테스트 실행 및 디버깅
  </Card>

  <Card title="Maven for Java" icon="box" href="cursor:extension/vscjava.vscode-maven">
    Maven 지원
  </Card>
</CardGroup>

<CardGroup cols={1}>
  <Card title="Project Manager for Java" icon="folder-tree" href="cursor:extension/vscjava.vscode-java-dependency" horizontal>
    프로젝트 관리 도구
  </Card>
</CardGroup>

<Warning>
  주요 차이:

  * 빌드/실행 설정은 launch.json에서 관리
  * Spring Boot 도구는 ["Spring Boot Extension Pack"](cursor:extension/vmware.vscode-boot-dev-pack) 확장을 통해 제공
  * Gradle 지원은 ["Gradle for Java"](cursor:extension/vscjava.vscode-gradle) 확장을 통해 제공
</Warning>

<div id="pycharm-python">
  ### PyCharm (Python)
</div>

<CardGroup cols={2}>
  <Card title="Python" icon="python" href="cursor:extension/ms-python.python">
    핵심 Python 지원
  </Card>

  <Card title="Cursor Pyright" icon="bolt" href="cursor:extension/anysphere.cursorpyright">
    빠른 타입 체크
  </Card>

  <Card title="Jupyter" icon="notebook" href="cursor:extension/ms-toolsai.jupyter">
    노트북 지원
  </Card>

  <Card title="Ruff" icon="wand-magic-sparkles" href="cursor:extension/charliermarsh.ruff">
    Python 포매터 및 린터
  </Card>
</CardGroup>

<Note>
  주요 차이:

  * 가상 환경은 커맨드 팔레트에서 관리
  * 디버그 설정은 launch.json에 정의
  * 의존성 관리는 requirements.txt 또는 Poetry로 수행
</Note>

<div id="webstorm-javascripttypescript">
  ### WebStorm (JavaScript/TypeScript)
</div>

<CardGroup cols={2}>
  <Card title="JavaScript and TypeScript Nightly" icon="js" href="cursor:extension/ms-vscode.vscode-typescript-next">
    최신 언어 기능
  </Card>

  <Card title="ES7+ React/Redux Snippets" icon="react" href="cursor:extension/dsznajder.es7-react-js-snippets">
    React 개발
  </Card>

  <Card title="Vue Language Features" icon="vuejs" href="cursor:extension/Vue.volar">
    Vue.js 지원
  </Card>

  <Card title="Angular Language Service" icon="angular" href="cursor:extension/Angular.ng-template">
    Angular 개발
  </Card>
</CardGroup>

<Info>
  대부분의 WebStorm 기능은 Cursor/VS Code에 기본 포함돼 있어:

  * npm 스크립트 뷰
  * 디버깅
  * Git 통합
  * TypeScript 지원
</Info>

<div id="phpstorm-php">
  ### PhpStorm (PHP)
</div>

<CardGroup cols={2}>
  <Card title="PHP Intelephense" icon="php" href="cursor:extension/bmewburn.vscode-intelephense-client">
    PHP 언어 서버
  </Card>

  <Card title="PHP Debug" icon="bug" href="cursor:extension/xdebug.php-debug">
    Xdebug 통합
  </Card>

  <Card title="PHP Intellisense" icon="brain" href="cursor:extension/felixfbecker.php-intellisense">
    코드 인텔리전스
  </Card>

  <Card title="PHP DocBlocker" icon="comment-dots" href="cursor:extension/neilbrayfield.php-docblocker">
    문서화 도구
  </Card>
</CardGroup>

<Note>
  주요 차이:

  * Xdebug 설정은 launch.json으로 관리
  * Composer는 터미널로 통합 사용
  * 데이터베이스 도구는 ["SQLTools"](cursor:extension/mtxr.sqltools) 확장을 통해 제공
</Note>

<div id="rider-net">
  ### Rider (.NET)
</div>

<CardGroup cols={2}>
  <Card title="C#" icon="code" href="cursor:extension/anysphere.csharp">
    기본 C# 지원
  </Card>

  <Card title="DotRush" icon="toolbox" href="cursor:extension/nromanov.dotrush">
    오픈 소스 C# 개발 환경
  </Card>

  <Card title="ReSharper Plugin" icon="box" href="https://www.jetbrains.com/help/resharper-vscode/Get_started.html#installation">
    JetBrains C# 플러그인
  </Card>

  <Card title=".NET Install Tool" icon="box-open" href="cursor:extension/ms-dotnettools.vscode-dotnet-runtime">
    .NET SDK 관리
  </Card>
</CardGroup>

<Warning>
  주요 차이:

  * 파일 탐색기를 통한 솔루션 탐색
  * CLI 또는 확장을 통한 NuGet 패키지 관리
  * 테스트 탐색기를 통한 테스트 러너 통합
</Warning>

<div id="goland-go">
  ### GoLand (Go)
</div>

<CardGroup cols={1}>
  <Card title="Go" icon="golang" href="cursor:extension/golang.Go">
    공식 Go 확장
  </Card>
</CardGroup>

<Note>
  주요 차이:

  * Go 도구 설치 자동 안내
  * launch.json 기반 디버깅
  * go.mod와 통합된 패키지 관리
</Note>

<div id="tips-for-a-smooth-transition">
  ## 원활한 전환을 위한 팁
</div>

<Steps>
  <Step title="Command Palette 사용">
    명령을 찾으려면 <kbd>⌘</kbd>/<kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd> 눌러
  </Step>

  <Step title="AI 기능">
    코드 자동 완성과 리팩터링에 Cursor의 AI 기능을 적극 활용해
  </Step>

  <Step title="설정 사용자화">
    최적의 워크플로를 위해 settings.json을 세밀하게 조정해
  </Step>

  <Step title="터미널 통합">
    커맨드라인 작업에는 내장 터미널을 써
  </Step>

  <Step title="확장 프로그램">
    추가 도구는 VS Code 마켓플레이스에서 찾아봐
  </Step>
</Steps>

<Info>
  워크플로가 조금 달라질 수는 있지만, Cursor는 전통적인 IDE를 넘어 생산성을 높여주는 강력한 AI 보조 코딩 기능을 제공해.
</Info>

---

← Previous: [iOS & macOS (Swift)](./ios-macos-swift.md) | [Index](./index.md) | Next: [VS Code](./vs-code.md) →