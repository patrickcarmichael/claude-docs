---
title: "Java"
source: "https://docs.cursor.com/tr/guides/languages/java"
language: "tr"
language_name: "Turkish"
---

# Java
Source: https://docs.cursor.com/tr/guides/languages/java

JDK, uzantılar ve derleme araçlarıyla Java geliştirmeyi kur

Bu rehber, JDK’yi ayarlama, gerekli uzantıları yükleme, hata ayıklama, Java uygulamalarını çalıştırma ve Maven ile Gradle gibi derleme araçlarını entegre etme dahil Java geliştirme için Cursor’ı yapılandırmana yardımcı olur. Ayrıca IntelliJ veya VS Code’a benzer iş akışı özelliklerini de kapsar.

<Note>
  Başlamadan önce, Cursor’ın kurulu olduğundan ve en son
  sürüme güncellendiğinden emin ol.
</Note>

<div id="setting-up-java-for-cursor">
  ## Cursor için Java kurulumu
</div>

<div id="java-installation">
  ### Java kurulumu
</div>

Cursor’ı kurmadan önce, makinene Java yüklü olmalı.

<Warning>
  Cursor bir Java derleyicisiyle gelmez, bu yüzden eğer henüz yüklü değilse bir JDK kurman gerekir.
</Warning>

<CardGroup cols={1}>
  <Card title="Windows Kurulumu" icon="windows">
    Bir JDK indirip kur (örn. OpenJDK, Oracle JDK, Microsoft Build of
    OpenJDK).

    <br />

    JAVA\_HOME’u ayarla ve JAVA\_HOME\bin klasörünü PATH’ine ekle.
  </Card>

  <Card title="macOS Kurulumu" icon="apple">
    Homebrew ile kur (`brew install openjdk`) ya da bir yükleyici indir.

    <br />

    JAVA\_HOME’un kurulu JDK’yi işaret ettiğinden emin ol.
  </Card>

  <Card title="Linux Kurulumu" icon="linux">
    Paket yöneticini kullan (`sudo apt install openjdk-17-jdk` veya muadili)
    ya da SDKMAN ile kur.
  </Card>
</CardGroup>

Kurulumu doğrulamak için şunu çalıştır:

```bash  theme={null}
java -version
javac -version
```

<Info>
  Cursor JDK’yi algılamazsa, settings.json içinde elle yapılandır:
</Info>

```json  theme={null}
{
  "java.jdt.ls.java.home": "/jdk/yolu",
  "java.configuration.runtimes": [
    {
      "name": "JavaSE-17",
      "path": "/jdk-17/yolu"
      "default": true
    }
  ]
}
```

<Warning>Değişiklikleri uygulamak için Cursor’ı yeniden başlat.</Warning>

<div id="cursor-setup">
  ### Cursor Kurulumu
</div>

<Info>Cursor, VS Code eklentilerini destekler. Aşağıdakileri elle yükle:</Info>

<CardGroup cols={2}>
  <Card title="Extension Pack for Java" icon="java" href="cursor:extension/vscjava.vscode-java-pack">
    Java dil desteği, hata ayıklayıcı, test çalıştırıcı, Maven desteği ve
    proje yöneticisi içerir
  </Card>

  <Card title="Gradle for Java" icon="gears" href="cursor:extension/vscjava.vscode-gradle">
    Gradle derleme sistemiyle çalışmak için gerekli
  </Card>

  <Card title="Spring Boot Extension Pack" icon="leaf" href="cursor:extension/vmware.vscode-boot-dev-pack">
    Spring Boot geliştirme için gerekli
  </Card>

  <Card title="Kotlin" icon="window" href="cursor:extension/fwcd.kotlin">
    Kotlin uygulamaları geliştirmek için gerekli
  </Card>
</CardGroup>

<div id="configure-build-tools">
  ### Derleme Araçlarını Yapılandır
</div>

<div id="maven">
  #### Maven
</div>

Maven’ın kurulu olduğundan emin ol (`mvn -version`). Gerekirse [maven.apache.org](https://maven.apache.org/download.cgi) adresinden yükle:

1. İkili arşivi indir
2. İstediğin konuma çıkar
3. MAVEN\_HOME ortam değişkenini çıkarılan klasöre ayarla
4. PATH’e %MAVEN\_HOME%\bin (Windows) veya \$MAVEN\_HOME/bin (Unix) ekle

<div id="gradle">
  #### Gradle
</div>

Gradle’ın kurulu olduğundan emin ol (`gradle -version`). Gerekirse [gradle.org](https://gradle.org/install/) adresinden yükle:

1. İkili dağıtımı indir
2. İstediğin konuma çıkar
3. GRADLE\_HOME ortam değişkenini çıkarılan klasöre ayarla
4. PATH’e %GRADLE\_HOME%\bin (Windows) veya \$GRADLE\_HOME/bin (Unix) ekle

Alternatif olarak, doğru Gradle sürümünü otomatik olarak indirip kullanacak Gradle Wrapper’ı kullan:

<div id="running-and-debugging">
  ## Çalıştırma ve Hata Ayıklama
</div>

Artık her şey hazır, Java kodunu çalıştırıp hata ayıklama zamanı.
İhtiyaçlarına göre aşağıdaki yöntemleri kullanabilirsin:

<CardGroup cols={2}>
  <Card title="Run" icon="play">
    Herhangi bir main metodunun üstünde görünen "Run" bağlantısına tıklayarak
    programını hızlıca çalıştır
  </Card>

  <Card title="Debug" icon="bug">
    Run and Debug kenar çubuğu panelini aç ve uygulamanı başlatmak için Run
    düğmesini kullan
  </Card>
</CardGroup>

<CardGroup cols={1}>
  <Card title="Terminal" icon="terminal">
    Komut satırından Maven veya Gradle komutlarıyla çalıştır
  </Card>

  <Card title="Spring Boot" icon="leaf">
    Spring Boot uygulamalarını Spring Boot Dashboard
    uzantısından doğrudan başlat
  </Card>
</CardGroup>

<div id="java-x-cursor-workflow">
  ## Java x Cursor İş Akışı
</div>

Cursor’ın yapay zekâ destekli özellikleri, Java geliştirme iş akışını ciddi şekilde hızlandırır. İşte özellikle Java için Cursor’ın yeteneklerinden yararlanmanın bazı yolları:

<CardGroup cols={2}>
  <Card title="Sekme Tamamlama" icon="arrow-right">
    <div className="text-sm">
      Metotlar, imzalar ve getter/setter gibi Java kalıpları için akıllı tamamlamalar.
    </div>
  </Card>

  <Card title="Agent Mode" icon="pen-to-square">
    <div className="text-sm">
      Tasarım kalıplarını uygula, kodu refaktör et veya doğru kalıtımla sınıflar oluştur.
    </div>
  </Card>

  <Card title="Satır İçi Düzenleme" icon="code">
    <div className="text-sm">
      Metotlarda hızlı satır içi düzenlemeler yap, hataları düzelt veya akışı bozmadan birim testleri üret.
    </div>
  </Card>

  <Card title="Sohbet" icon="message">
    <div className="text-sm">
      Java kavramlarında yardım al, istisnaları hata ayıkla veya framework özelliklerini öğren.
    </div>
  </Card>
</CardGroup>

<div id="example-workflows">
  ### Örnek İş Akışları
</div>

1. **Java Kalıbı Oluştur**\
   [Sekme tamamlama](/tr/tab/overview) kullanarak constructor’lar, getter/setter’lar, equals/hashCode metotları ve diğer tekrarlayan Java kalıplarını hızlıca oluştur.

2. **Karmaşık Java İstisnalarını Hata Ayıkla**\
   Anlaşılması güç bir Java stack trace’ine denk geldiğinde, onu seç ve kök nedeni açıklayıp olası düzeltmeleri önermesi için [Ask](/tr/chat/overview) kullan.

3. **Eski Java Kodunu Refaktör Et**\
   Daha eski Java kodunu modernleştirmek için [Agent mode](/tr/chat/agent) kullan — anonim sınıfları lambda’lara çevir, daha yeni Java dil özelliklerine yükselt veya tasarım kalıplarını uygula.

4. **Framework Geliştirme**\
   Belgelerini @docs ile Cursor’ın bağlamına ekle ve Cursor genelinde framework’e özel kod üret.

---

← Previous: [Dokümantasyonla Çalışma](./dokmantasyonla-alma.md) | [Index](./index.md) | Next: [JavaScript & TypeScript](./javascript-typescript.md) →