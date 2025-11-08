---
title: "JetBrains"
source: "https://docs.cursor.com/tr/guides/migration/jetbrains"
language: "tr"
language_name: "Turkish"
---

# JetBrains
Source: https://docs.cursor.com/tr/guides/migration/jetbrains

Tanıdık araçlarla JetBrains IDE'lerinden Cursor'a geç

Cursor, JetBrains IDE'lerinin yerini alabilecek modern, yapay zekâ destekli bir kodlama deneyimi sunar. Geçiş ilk başta farklı hissettirse de, Cursor’ın VS Code tabanlı altyapısı güçlü özellikler ve kapsamlı özelleştirme seçenekleri sunar.

<div id="editor-components">
  ## Editör Bileşenleri
</div>

<div id="extensions">
  ### Uzantılar
</div>

JetBrains IDE’leri, hedefledikleri dil ve framework’ler için önceden yapılandırılmış geldikleri için harika araçlar.

Cursor farklı — kutudan çıktığı haliyle boş bir tuval; IDE’nin hedeflediği dil ve framework’lerle sınırlı kalmadan zevkine göre özelleştirebilirsin.

Cursor’ın geniş bir uzantı ekosistemine erişimi var ve JetBrains IDE’lerinin sunduğu işlevlerin neredeyse tamamı (ve daha fazlası!) bu uzantılarla yeniden oluşturulabiliyor.

Aşağıdaki popüler uzantılara göz at:

<CardGroup cols={4}>
  <Card title="Remote SSH" icon="network-wired" href="cursor:extension/anysphere.remote-ssh">
    SSH uzantısı
  </Card>

  <Card title="Project Manager" icon="folder-tree" href="cursor:extension/alefragnani.project-manager">
    Birden fazla projeyi yönet
  </Card>

  <Card title="GitLens" icon="git" href="cursor:extension/eamodio.gitlens">
    Gelişmiş Git entegrasyonu
  </Card>

  <Card title="Local History" icon="clock-rotate-left" href="cursor:extension/xyz.local-history">
    Yerel dosya değişikliklerini izle
  </Card>

  <Card title="Error Lens" icon="bug" href="cursor:extension/usernamehw.errorlens">
    Satır içi hata vurgulama
  </Card>

  <Card title="ESLint" icon="code-compare" href="cursor:extension/dbaeumer.vscode-eslint">
    Kod lintleme
  </Card>

  <Card title="Prettier" icon="wand-magic-sparkles" href="cursor:extension/esbenp.prettier-vscode">
    Kod biçimlendirme
  </Card>

  <Card title="Todo Tree" icon="folder-tree" href="cursor:extension/Gruntfuggly.todo-tree">
    TODO ve FIXME’leri takip et
  </Card>
</CardGroup>

<div id="keyboard-shortcuts">
  ### Klavye Kısayolları
</div>

Cursor, favori klavye kısayollarını eylemlerle eşlemeni sağlayan yerleşik bir kısayol yöneticisine sahip.

Bu uzantıyla JetBrains IDE kısayollarının neredeyse tamamını doğrudan Cursor’a taşıyabilirsin!
Nasıl yapılandıracağını öğrenmek için uzantının dokümantasyonunu mutlaka oku:

<Card title="IntelliJ IDEA Keybindings" icon="keyboard" href="cursor:extension/k--kato.intellij-idea-keybindings">
  JetBrains IDE klavye kısayollarını Cursor’a taşımak için bu uzantıyı kur.
</Card>

<Note>
  Farklı olan yaygın kısayollar:

  * Find Action: ⌘/Ctrl+Shift+P  (⌘/Ctrl+Shift+A yerine)
  * Quick Fix: ⌘/Ctrl+.  (Alt+Enter yerine)
  * Go to File: ⌘/Ctrl+P  (⌘/Ctrl+Shift+N yerine)
</Note>

<div id="themes">
  ### Temalar
</div>

Bu topluluk temalarıyla Cursor’da favori JetBrains IDE’lerinin görünüm ve hissini yeniden oluştur.

Standart Darcula temasını seçebilir ya da JetBrains araçlarının sözdizimi vurgulamasına uyan bir tema tercih edebilirsin.

<CardGroup cols={1}>
  <Card title="JetBrains - Darcula Theme" icon="moon" horizontal href="cursor:extension/rokoroku.vscode-theme-darcula">
    Klasik JetBrains Darcula koyu temasını deneyimle
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
    Tanıdık JetBrains dosya ve klasör simgelerini edin
  </Card>
</CardGroup>

<div id="font">
  ### Yazı tipi
</div>

JetBrains benzeri deneyimi tamamlamak için resmi JetBrains Mono yazı tipini kullanabilirsin:

1. JetBrains Mono yazı tipini indir ve sistemine kur:

<CardGroup cols={1}>
  <Card title="Download JetBrains Mono" icon="link" horizontal href="https://www.jetbrains.com/lp/mono/" />
</CardGroup>

2. Yazı tipini kurduktan sonra Cursor’ı yeniden başlat
3. Cursor’da Ayarlar’ı aç (⌘/Ctrl + ,)
4. “Font Family” için ara
5. Yazı tipi ailesini ‘JetBrains Mono’ olarak ayarla

<Note>
  En iyi deneyim için, ayarlarında `"editor.fontLigatures": true` olarak ayarlayarak yazı tipi birleşimlerini (ligature) da etkinleştirebilirsin.
</Note>

<div id="ide-specific-migration">
  ## IDE'ye Özgü Geçiş
</div>

Birçok kullanıcı, hedeflendiği dil ve framework’ler için kutudan çıkar çıkmaz destek sunan JetBrains IDE’lerini seviyordu. Cursor farklı — kutudan çıktığı haliyle boş bir tuval; dilediğin gibi özelleştirebilirsin, IDE’nin hedeflendiği dil ve framework’lerle sınırlı kalmazsın.

Cursor zaten VS Code’un eklenti ekosistemine erişiyor ve JetBrains IDE’lerinin sunduğu neredeyse tüm işlevler (ve daha fazlası!) bu eklentilerle yeniden oluşturulabilir.

Aşağıda her JetBrains IDE için önerilen eklentilere göz at.

<div id="intellij-idea-java">
  ### IntelliJ IDEA (Java)
</div>

<CardGroup cols={2}>
  <Card title="Language Support for Java" icon="java" href="cursor:extension/redhat.java">
    Temel Java dil özellikleri
  </Card>

  <Card title="Debugger for Java" icon="bug" href="cursor:extension/vscjava.vscode-java-debug">
    Java hata ayıklama desteği
  </Card>

  <Card title="Test Runner for Java" icon="vial" href="cursor:extension/vscjava.vscode-java-test">
    Java testlerini çalıştırma ve hata ayıklama
  </Card>

  <Card title="Maven for Java" icon="box" href="cursor:extension/vscjava.vscode-maven">
    Maven desteği
  </Card>
</CardGroup>

<CardGroup cols={1}>
  <Card title="Project Manager for Java" icon="folder-tree" href="cursor:extension/vscjava.vscode-java-dependency" horizontal>
    Proje yönetim araçları
  </Card>
</CardGroup>

<Warning>
  Önemli farklar:

  * Build/Run yapılandırmaları launch.json üzerinden yönetilir
  * Spring Boot araçları ["Spring Boot Extension Pack"](cursor:extension/vmware.vscode-boot-dev-pack) eklentisiyle sunulur
  * Gradle desteği ["Gradle for Java"](cursor:extension/vscjava.vscode-gradle) eklentisiyle sağlanır
</Warning>

<div id="pycharm-python">
  ### PyCharm (Python)
</div>

<CardGroup cols={2}>
  <Card title="Python" icon="python" href="cursor:extension/ms-python.python">
    Temel Python desteği
  </Card>

  <Card title="Cursor Pyright" icon="bolt" href="cursor:extension/anysphere.cursorpyright">
    Hızlı tip denetimi
  </Card>

  <Card title="Jupyter" icon="notebook" href="cursor:extension/ms-toolsai.jupyter">
    Notebook desteği
  </Card>

  <Card title="Ruff" icon="wand-magic-sparkles" href="cursor:extension/charliermarsh.ruff">
    Python biçimlendirici ve linter
  </Card>
</CardGroup>

<Note>
  Önemli farklar:

  * Sanal ortamlar komut paleti üzerinden yönetilir
  * Hata ayıklama yapılandırmaları launch.json içinde
  * Gereksinim yönetimi requirements.txt veya Poetry ile
</Note>

<div id="webstorm-javascripttypescript">
  ### WebStorm (JavaScript/TypeScript)
</div>

<CardGroup cols={2}>
  <Card title="JavaScript and TypeScript Nightly" icon="js" href="cursor:extension/ms-vscode.vscode-typescript-next">
    En yeni dil özellikleri
  </Card>

  <Card title="ES7+ React/Redux Snippets" icon="react" href="cursor:extension/dsznajder.es7-react-js-snippets">
    React geliştirme
  </Card>

  <Card title="Vue Language Features" icon="vuejs" href="cursor:extension/Vue.volar">
    Vue.js desteği
  </Card>

  <Card title="Angular Language Service" icon="angular" href="cursor:extension/Angular.ng-template">
    Angular geliştirme
  </Card>
</CardGroup>

<Info>
  WebStorm özelliklerinin çoğu Cursor/VS Code’da yerleşik olarak bulunur, şunlar dahil:

  * npm script’leri görünümü
  * Hata ayıklama
  * Git entegrasyonu
  * TypeScript desteği
</Info>

<div id="phpstorm-php">
  ### PhpStorm (PHP)
</div>

<CardGroup cols={2}>
  <Card title="PHP Intelephense" icon="php" href="cursor:extension/bmewburn.vscode-intelephense-client">
    PHP dil sunucusu
  </Card>

  <Card title="PHP Debug" icon="bug" href="cursor:extension/xdebug.php-debug">
    Xdebug entegrasyonu
  </Card>

  <Card title="PHP Intellisense" icon="brain" href="cursor:extension/felixfbecker.php-intellisense">
    Kod zekâsı
  </Card>

  <Card title="PHP DocBlocker" icon="comment-dots" href="cursor:extension/neilbrayfield.php-docblocker">
    Dokümantasyon araçları
  </Card>
</CardGroup>

<Note>
  Önemli farklar:

  * Xdebug yapılandırması launch.json üzerinden
  * Composer entegrasyonu terminal aracılığıyla
  * Veritabanı araçları ["SQLTools"](cursor:extension/mtxr.sqltools) eklentisiyle
</Note>

<div id="rider-net">
  ### Rider (.NET)
</div>

<CardGroup cols={2}>
  <Card title="C#" icon="code" href="cursor:extension/anysphere.csharp">
    Temel C# desteği
  </Card>

  <Card title="DotRush" icon="toolbox" href="cursor:extension/nromanov.dotrush">
    Açık kaynak C# geliştirme ortamı
  </Card>

  <Card title="ReSharper Plugin" icon="box" href="https://www.jetbrains.com/help/resharper-vscode/Get_started.html#installation">
    JetBrains C# eklentisi
  </Card>

  <Card title=".NET Install Tool" icon="box-open" href="cursor:extension/ms-dotnettools.vscode-dotnet-runtime">
    .NET SDK yönetimi
  </Card>
</CardGroup>

<Warning>
  Temel farklar:

  * Çözüm gezgini, dosya gezgini üzerinden
  * NuGet paket yönetimi, CLI veya eklentilerle
  * Test koşucu entegrasyonu, test gezgini üzerinden
</Warning>

<div id="goland-go">
  ### GoLand (Go)
</div>

<CardGroup cols={1}>
  <Card title="Go" icon="golang" href="cursor:extension/golang.Go">
    Resmi Go uzantısı
  </Card>
</CardGroup>

<Note>
  Temel farklar:

  * Go araçlarının kurulumu otomatik olarak tetiklenir
  * Hata ayıklama launch.json üzerinden yapılır
  * Paket yönetimi go.mod ile entegredir
</Note>

<div id="tips-for-a-smooth-transition">
  ## Sorunsuz Geçiş İçin İpuçları
</div>

<Steps>
  <Step title="Komut Paletini Kullan">
    Komutları bulmak için <kbd>⌘</kbd>/<kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd> tuşlarına bas
  </Step>

  <Step title="Yapay Zekâ Özellikleri">
    Kod tamamlama ve yeniden düzenleme için Cursor’ın yapay zekâ özelliklerinden yararlan
  </Step>

  <Step title="Ayarları Özelleştir">
    İş akışını en iyi hale getirmek için settings.json dosyanı ince ayar yap
  </Step>

  <Step title="Terminal Entegrasyonu">
    Komut satırı işlemleri için yerleşik terminali kullan
  </Step>

  <Step title="Eklentiler">
    Ek araçlar için VS Code Marketplace’te göz at
  </Step>
</Steps>

<Info>
  Bazı iş akışları farklı olsa da, Cursor, geleneksel IDE yeteneklerinin ötesine geçen ve verimliliği artıran güçlü yapay zekâ destekli kodlama özellikleri sunar.
</Info>

---

← Previous: [iOS & macOS (Swift)](./ios-macos-swift.md) | [Index](./index.md) | Next: [VS Code](./vs-code.md) →