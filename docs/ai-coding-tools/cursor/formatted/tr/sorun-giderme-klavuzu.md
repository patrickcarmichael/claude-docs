---
title: "Sorun Giderme Kılavuzu"
source: "https://docs.cursor.com/tr/troubleshooting/troubleshooting-guide"
language: "tr"
language_name: "Turkish"
---

# Sorun Giderme Kılavuzu
Source: https://docs.cursor.com/tr/troubleshooting/troubleshooting-guide

Sorunları çözme ve hataları bildirme adımları

Cursor’daki sorunlar eklentilerden, uygulama verilerinden veya sistem kaynaklı problemlerden kaynaklanabilir. Şu sorun giderme adımlarını dene.

<CardGroup cols={1}>
  <Card horizontal title="Sorun Bildirme" icon="bug" href="#reporting-an-issue">
    Cursor ekibine bir sorunu bildirme adımları
  </Card>
</CardGroup>

<div id="troubleshooting">
  ## Sorun Giderme
</div>

<Steps>
  <Step title="Ağ bağlantısını kontrol et">
    Önce Cursor’ın servislerine bağlanabildiğini kontrol et.

    **Ağ tanılamasını çalıştır:** `Cursor Settings` > `Network` bölümüne git ve `Run Diagnostics`’e tıkla. Bu, Cursor’ın sunucularına bağlantını test eder ve yapay zeka özelliklerini, güncellemeleri ya da diğer çevrimiçi işlevleri etkileyen ağ sorunlarını belirler.

    Tanılama bağlantı sorunları gösteriyorsa, Cursor’ın erişimini engelleyebilecek güvenlik duvarı ayarlarını, proxy yapılandırmasını ya da ağ kısıtlamalarını kontrol et.
  </Step>

  <Step title="Eklenti verilerini temizleme">
    Eklenti sorunları için:

    **Tüm eklentileri geçici olarak devre dışı bırak:** Komut satırında `cursor --disable-extensions` çalıştır. Sorunlar çözülürse, sorunlu olanı bulmak için eklentileri tek tek yeniden etkinleştir.

    **Eklenti verilerini sıfırla:** Depolanan verileri sıfırlamak için sorunlu eklentileri kaldırıp yeniden yükle. Yeniden yüklemeden sonra da kalabilen eklenti yapılandırmaları için ayarları kontrol et.
  </Step>

  <Step title="Uygulama verilerini temizleme">
    <Warning>
      Bu işlem eklentiler, temalar, snippet’ler ve kurulumla ilgili veriler dahil olmak üzere uygulama verilerini siler. Bu verileri korumak için önce profilini dışa aktar.
    </Warning>

    Cursor, güncellemeler ve yeniden yüklemeler arasında geri yükleyebilmek için uygulama verilerini uygulamanın dışında saklar.

    Uygulama verilerini temizlemek için:

    **Windows:** Komut İstemi’nde şu komutları çalıştır:

    ```txt  theme={null}
    rd /s /q "%USERPROFILE%\AppData\Local\Programs\Cursor"
    rd /s /q "%USERPROFILE%\AppData\Local\Cursor"
    rd /s /q "%USERPROFILE%\AppData\Roaming\Cursor"
    del /f /q "%USERPROFILE%\.cursor*"
    rd /s /q "%USERPROFILE%\.cursor"
    ```

    **macOS:** Terminal’de `sudo rm -rf ~/Library/Application\ Support/Cursor` ve `rm -f ~/.cursor.json` komutlarını çalıştır.

    **Linux:** Terminal’de `rm -rf ~/.cursor ~/.config/Cursor/` komutunu çalıştır.
  </Step>

  <Step title="Cursor’ı kaldırma">
    Cursor’ı kaldırmak için:

    <CardGroup cols={1}>
      <Card horizontal title="Windows" icon="windows">
        Başlat Menüsü’nde “Add or Remove Programs”ı ara, “Cursor”ı bul, “Uninstall”a tıkla.
      </Card>

      <Card horizontal title="macOS" icon="apple">
        Applications klasörünü aç, “Cursor”a sağ tıkla, “Move to Trash”ı seç.
      </Card>

      <Card horizontal title="Linux" icon="linux">
        **.deb paketleri için:** `sudo apt remove cursor`

        **.rpm paketleri için:** `sudo dnf remove cursor` veya `sudo yum remove cursor`

        **AppImage için:** Bulunduğu konumdan Cursor.appimage dosyasını sil.
      </Card>
    </CardGroup>
  </Step>

  <Step title="Cursor’ı yeniden yükleme">
    [Downloads sayfası](https://www.cursor.com/downloads) üzerinden yeniden yükle. Uygulama verileri temizlenmediyse Cursor önceki durumuna geri döner. Temizlendiyse tertemiz bir kurulum alırsın.
  </Step>
</Steps>

<div id="reporting-an-issue">
  ## Bir Sorun Bildirme
</div>

Bu adımlar işe yaramazsa, [forum](https://forum.cursor.com/)'a bildir.

<Card horizontal title="Cursor Forum" icon="message" href="https://forum.cursor.com/">
  Cursor forumunda bir hata ya da sorun bildir
</Card>

Hızlı çözüm için şunları sağla:

<CardGroup cols={2}>
  <Card title="Sorunun Ekran Görüntüsü" icon="image">
    Bir ekran görüntüsü al, hassas bilgileri karart.
  </Card>

  <Card title="Tekrarlama Adımları" icon="list-check">
    Sorunu yeniden üretmek için tam adımları belgele.
  </Card>

  <Card title="Sistem Bilgileri" icon="computer">
    Sistem bilgilerini şuradan al:

    <br />

    `Cursor` > `Help` > `About`
  </Card>

  <Card title="İstek Kimlikleri" icon="shield-halved" href="/tr/troubleshooting/request-reporting">
    İstek kimliklerini toplama rehberimizi görmek için tıkla
  </Card>

  <Card title="Konsol Hataları" icon="bug">
    Geliştirici konsolunu kontrol et: <br />
    `Developer: Toggle Developer Tools`
  </Card>

  <Card title="Günlükler" icon="file-lines">
    Günlüklere eriş: <br />
    `Developer: Open Logs Folder`
  </Card>
</CardGroup>

---

← Previous: [İstek Kimliği Alma](./istek-kimlii-alma.md) | [Index](./index.md) | Next: [Welcome](./welcome.md) →