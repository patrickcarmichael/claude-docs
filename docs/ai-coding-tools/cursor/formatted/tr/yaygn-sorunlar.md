---
title: "Yaygın Sorunlar"
source: "https://docs.cursor.com/tr/troubleshooting/common-issues"
language: "tr"
language_name: "Turkish"
---

# Yaygın Sorunlar
Source: https://docs.cursor.com/tr/troubleshooting/common-issues

Yaygın sorunlar ve SSS için çözümler

Aşağıda yaygın sorunlar ve çözümleri bulunuyor.

<div id="networking-issues">
  ### Ağ Sorunları
</div>

Önce ağ bağlantını kontrol et. `Cursor Settings` > `Network` bölümüne git ve `Run Diagnostics`'e tıkla. Bu, Cursor’ın sunucularına olan bağlantını test eder ve yapay zeka özelliklerini, güncellemeleri veya diğer çevrimiçi işlevleri etkileyebilecek ağ kaynaklı sorunları belirlemeye yardımcı olur.

Cursor, akışlı yanıtları verimli yönettiği için yapay zeka özelliklerinde HTTP/2 kullanır. Ağın HTTP/2’yi desteklemiyorsa, indeksleme hataları ve yapay zeka özelliklerinde sorunlar yaşayabilirsin.

Bu durum kurumsal ağlarda, VPN’lerde veya Zscaler gibi proxy’ler kullanılırken görülebilir.

Bunu çözmek için uygulama ayarlarında (Cursor ayarları değil) HTTP/1.1 geri dönüşünü etkinleştir: `CMD/CTRL + ,` tuşlarına bas, `HTTP/2` ara, ardından `Disable HTTP/2`’yi etkinleştir. Bu, HTTP/1.1 kullanımını zorlar ve sorunu çözer.

Otomatik algılama ve geri dönüş eklemeyi planlıyoruz.

<div id="resource-issues-cpu-ram-etc">
  ### Kaynak Sorunları (CPU, RAM, vb.)
</div>

Yüksek CPU veya RAM kullanımı makinenin yavaşlamasına ya da kaynak uyarılarının çıkmasına neden olabilir.

Büyük kod tabanları daha fazla kaynak gerektirse de, yüksek kullanım genellikle uzantılardan veya ayar kaynaklı sorunlardan kaynaklanır.

<Note>
  **MacOS**’ta düşük RAM uyarısı görüyorsan, bazı kullanıcılar için aşırı hatalı değerler gösterebilen bir bug olduğunu unutma. Bunu görüyorsan, lütfen Activity Monitor’ü aç ve doğru bellek kullanımını görmek için “Memory” sekmesine bak.
</Note>

Yüksek CPU veya RAM kullanımı yaşıyorsan, şu adımları dene:

<AccordionGroup>
  <Accordion title="Uzantılarını Kontrol Et">
    Uzantılar performansı etkileyebilir.

    Extension Monitor, yüklü ve yerleşik tüm uzantıların kaynak tüketimini gösterir.

    `Settings` > `Application` > `Experimental` yolundan Extension Monitor’ü etkinleştir ve `Extension Monitor: Enabled`’ı aç. Bu, Cursor’ı yeniden başlatmanı isteyecek.

    Aç: `Cmd/Ctrl + Shift + P` → `Developer: Open Extension Monitor`.

    Cursor, uzantılarını bir veya daha fazla **extension host** içinde çalıştırır. Genellikle uzantılarının çoğu aynı extension host içinde çalışır; bu da çok CPU zamanı tüketen bir uzantının komşu uzantıları boğabileceği anlamına gelir!

    Extension Monitor şunları gösterir:

    * Bir uzantı tarafından başlatılan tüm uzun ömürlü süreçler (yalnızca MacOS ve Linux).
    * **% Ext Host**: Bu uzantının tükettiği toplam extension host süresinin yüzdesi. Diğerlerine göre en çok zamanı hangi uzantıların kullandığını belirlemeye yardımcı olur.
    * **Max Blocking**: İzleme aralığı başına bir uzantının en uzun kesintisiz yürütme bloğu.
    * **% CPU**:
      * Uzantılar için: Uzantının koduna atfedilen toplam CPU kullanım yüzdesi.
      * Süreçler için: Başlatılan sürece atfedilen toplam CPU kullanım yüzdesi (yalnızca MacOS ve Linux).
    * **Memory**:
      * Uzantılar için: Uzantının kodu tarafından kullanılan JS heap belleği miktarı (harici ayırmalar dahil değil).
      * Süreçler için: Başlatılan sürecin kullandığı sistem belleği miktarı (yalnızca MacOS ve Linux).

    Komut satırından `cursor --disable-extensions` çalıştırarak da test edebilirsin. Performans iyileşirse, sorunlu uzantıyı bulmak için uzantıları teker teker yeniden etkinleştir.

    Sorunlu uzantıları belirlemek için Extension Bisect’i dene. Daha fazlasını [buradan](https://code.visualstudio.com/blogs/2021/02/16/extension-bisect#_welcome-extension-bisect) oku. Not: Bu yöntem, kademeli performans düşüşlerinden ziyade anlık sorunlarda en iyi çalışır.
  </Accordion>

  <Accordion title="Process Explorer'ı Kullan">
    Process Explorer, hangi süreçlerin kaynak tükettiğini gösterir.

    Aç: Komut Paleti (`Cmd/Ctrl + Shift + P`) → `Developer: Open Process Explorer`.

    Şu başlıklar altındaki süreçleri incele:

    * **`extensionHost`**: Uzantı kaynaklı sorunlar
    * **`ptyHost`**: Terminal kaynak tüketimi

    Process Explorer, teşhis için her terminali ve çalışan komutlarını gösterir.

    Diğer yüksek kullanım gösteren süreçler için [forum](https://forum.cursor.com/)'a bildir.
  </Accordion>

  <Accordion title="Sistem Kaynaklarını İzle">
    Sorunun Cursor’a özgü mü yoksa sistem genelinde mi olduğunu belirlemek için işletim sisteminin izleme araçlarını kullan.
  </Accordion>

  <Accordion title="Minimal Bir Kurulumu Test Et">
    Sorunlar sürerse, minimal bir Cursor kurulumunu test et.
  </Accordion>
</AccordionGroup>

<div id="general-faqs">
  ## Genel SSS
</div>

<AccordionGroup>
  <Accordion title="Değişiklik günlüğünde güncelleme görüyorum ama Cursor güncellenmiyor">
    Yeni güncellemeler kademeli olarak yayınlanır — rastgele seçilen kullanıcılar önce alır. Güncellemenin birkaç gün içinde gelmesini bekle.
  </Accordion>

  <Accordion title="Cursor'da GitHub girişimde sorun var / Cursor'da GitHub'dan nasıl çıkış yaparım?">
    Komut paletinde `Ctrl/⌘ + Shift + P` ile `Sign Out of GitHub` komutunu kullan.
  </Accordion>

  <Accordion title="GitHub Codespaces'ı kullanamıyorum">
    GitHub Codespaces henüz desteklenmiyor.
  </Accordion>

  <Accordion title="Remote SSH'ye bağlanırken hatalar alıyorum">
    Mac veya Windows makinelerine SSH desteklenmiyor. Diğer sorunlar için günlüklerle birlikte [forum](https://forum.cursor.com/)'a bildirim yap.
  </Accordion>

  <Accordion title="Windows'ta SSH Bağlantı Sorunları">
    "SSH is only supported in Microsoft versions of VS Code" uyarısını görüyorsan:

    1. Remote-SSH'yi kaldır:
       * Uzantılar görünümünü aç (`Ctrl + Shift + X`)
       * "Remote-SSH" ara
       * Dişli simgesine tıkla → "Uninstall"

    2. Anysphere Remote SSH'yi yükle:
       * Cursor marketplace'i aç
       * "SSH" ara
       * Anysphere Remote SSH uzantısını yükle

    3. Kurulumdan sonra:
       * Aktif SSH bağlantıları olan tüm VS Code örneklerini kapat
       * Cursor'ı yeniden başlat
       * SSH ile yeniden bağlan

    SSH yapılandırmanın ve anahtarlarının doğru şekilde ayarlı olduğundan emin ol.
  </Accordion>

  <Accordion title="Cursor Tab ve Inline Edit kurumsal proxy arkasında çalışmıyor">
    Cursor Tab ve Inline Edit, daha düşük gecikme ve kaynak kullanımı için HTTP/2 kullanır. Bazı kurumsal proxy'ler (örn. Zscaler) HTTP/2'yi engeller. Ayarlarda `"cursor.general.disableHttp2": true` yaparak düzelt (`Cmd/Ctrl + ,`, `http2` ara).
  </Accordion>

  <Accordion title="Az önce Pro'ya abone oldum ama uygulamada hâlâ ücretsiz plandayım">
    Cursor Ayarları'ndan çıkış yapıp tekrar giriş yap.
  </Accordion>

  <Accordion title="Kullanımım ne zaman sıfırlanacak?">
    Pro aboneleri: Yenileme tarihini görmek için [Dashboard](https://cursor.com/dashboard) içinde `Manage Subscription`'a tıkla.

    Ücretsiz kullanıcılar: İlk Cursor e-postanın tarihini kontrol et. Kullanım her ay o tarihte sıfırlanır.
  </Accordion>

  <Accordion title="Güncellemeden sonra Chat/Composer geçmişim kayboldu">
    Düşük disk alanı, güncellemeler sırasında Cursor'ın geçmiş verileri temizlemesine neden olabilir. Bunu önlemek için:

    1. Güncellemeden önce yeterli boş disk alanı bulundur
    2. Gereksiz sistem dosyalarını düzenli olarak temizle
    3. Güncellemeden önce önemli konuşmaları yedekle
  </Accordion>

  <Accordion title="Cursor'ı nasıl kaldırırım?">
    [Bu kılavuzu](https://code.visualstudio.com/docs/setup/uninstall) izle. "VS Code" veya "Code"u "Cursor" ile, ".vscode"u ".cursor" ile değiştir.
  </Accordion>

  <Accordion title="Hesabımı nasıl silerim?">
    [Dashboard](https://cursor.com/dashboard) içinde `Delete Account`'a tıkla. Bu işlem hesabını ve ilişkili tüm verileri kalıcı olarak siler.
  </Accordion>

  <Accordion title="Cursor'ı komut satırından nasıl açarım?">
    Terminalinde `cursor` çalıştır. Komut yoksa:

    1. Komut paletini aç `⌘⇧P`
    2. `install command` yaz
    3. `Install 'cursor' command` seç (isteğe bağlı olarak VS Code'un komutunun yerine geçmesi için `code` komutunu da yükleyebilirsin)
  </Accordion>

  <Accordion title="Cursor'a giriş yapılamıyor">
    Sign In'a tıklayınca cursor.com'a yönlendiriyor ama giriş yapmıyorsa, güvenlik duvarını veya antivirüs yazılımını devre dışı bırak — oturum açma işlemini engelliyor olabilirler.
  </Accordion>

  <Accordion title="Şüpheli Aktivite Mesajı">
    Sistemimizin son dönemde artan kötüye kullanımından dolayı isteğin bir güvenlik önlemi olarak engellenmiş olabilir. Bunu çözmek için:

    Önce VPN'ini kontrol et. VPN kullanıyorsan kapatmayı dene; VPN'ler bazen güvenlik sistemlerimizi tetikleyebilir.

    Bu da işe yaramazsa şunları deneyebilirsin:

    * Yeni bir sohbet oluşturmak
    * Biraz bekleyip sonra tekrar denemek
    * Google veya GitHub kimlik doğrulamasıyla yeni bir hesap oluşturmak
    * Cursor Pro'ya yükseltmek
  </Accordion>
</AccordionGroup>

---

← Previous: [MCP Sunucuları](./mcp-sunucular.md) | [Index](./index.md) | Next: [İstek Kimliği Alma](./istek-kimlii-alma.md) →