---
title: "Bugbot"
source: "https://docs.cursor.com/tr/bugbot"
language: "tr"
language_name: "Turkish"
---

# Bugbot
Source: https://docs.cursor.com/tr/bugbot

Pull request’ler için yapay zekâ kod incelemesi

Bugbot, pull request’leri inceleyip hataları, güvenlik açıklarını ve kod kalitesi sorunlarını tespit eder.

<Tip>
  Bugbot’ta ücretsiz bir katman var: her kullanıcı her ay sınırlı sayıda ücretsiz PR incelemesi alır. Bu sınıra ulaştığında, bir sonraki faturalandırma döngüne kadar incelemeler durur. Sınırsız inceleme için istediğin zaman 14 günlük ücretsiz Pro denemesine geçebilirsin (standart kötüye kullanım korumaları geçerlidir).
</Tip>

<Frame>
  <video src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/bugbot/bugbot-report-cropped.mp4?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=013060fbd22f397ac81f2c32bb8b6b14" alt="Bugbot bir PR’da yorum bırakıyor" autoPlay loop muted playsInline controls data-path="images/bugbot/bugbot-report-cropped.mp4" />
</Frame>

<div id="how-it-works">
  ## Nasıl çalışır
</div>

Bugbot, PR diff’lerini analiz eder ve açıklamalarla birlikte düzeltme önerileri içeren yorumlar bırakır. Her PR güncellemesinde otomatik olarak çalışır ya da elle tetiklendiğinde devreye girer.

* Her PR güncellemesinde **otomatik inceleme** çalıştırır
* Herhangi bir PR’da `cursor review` veya `bugbot run` yorumunu yazarak **elle tetikle**
* **Cursor’da Düzelt** bağlantıları sorunları doğrudan Cursor’da açar
* **Web’de Düzelt** bağlantıları sorunları doğrudan [cursor.com/agents](https://cursor.com/agents) üzerinde açar

<div id="setup">
  ## Kurulum
</div>

Cursor admin erişimi ve GitHub org admin erişimi gerekir.

1. [cursor.com/dashboard](https://cursor.com/dashboard?tab=bugbot) adresine git
2. Bugbot sekmesine geç
3. `Connect GitHub`’a tıkla (zaten bağlıysa `Manage Connections`)
4. GitHub kurulum akışını izle
5. Belirli depolarda Bugbot’u etkinleştirmek için panele geri dön

<Frame>
  <video src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/bugbot/bugbot-install.mp4?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=75745d4464b183c306a44571db86a0c4" alt="Bugbot GitHub kurulumu" autoPlay loop muted playsInline controls data-path="images/bugbot/bugbot-install.mp4" />
</Frame>

<div id="configuration">
  ## Yapılandırma
</div>

<Tabs defaultValue="Team">
  <Tab title="Individual">
    ### Depo ayarları

    Kurulumlar listenden depo bazında Bugbot'u etkinleştir ya da devre dışı bırak. Bugbot yalnızca senin açtığın PR'larda çalışır.

    ### Kişisel ayarlar

    * Yalnızca `cursor review` ya da `bugbot run` yorumuyla anıldığında çalıştır
    * PR başına yalnızca bir kez çalıştır, sonraki commit'leri atla
  </Tab>

  <Tab title="Team">
    ### Depo ayarları

    Takım yöneticileri, depo bazında Bugbot'u etkinleştirip, inceleyiciler için izin/reddet listeleri yapılandırabilir ve şunları ayarlayabilir:

    * Kurulum başına PR başına yalnızca bir kez çalıştır, sonraki commit'leri atla
    * Bugbot'un doğrudan kod satırlarına yorum bırakmasını önlemek için satır içi incelemeleri devre dışı bırak

    Takım üyeliğinden bağımsız olarak, etkinleştirilmiş depolardaki tüm katkıda bulunanlar için Bugbot çalışır.

    ### Kişisel ayarlar

    Takım üyeleri kendi PR'ları için ayarları geçersiz kılabilir:

    * Yalnızca `cursor review` ya da `bugbot run` yorumuyla anıldığında çalıştır
    * PR başına yalnızca bir kez çalıştır, sonraki commit'leri atla
    * Taslak çekme isteklerini otomatik incelemelere dahil etmek için taslak PR'larda incelemeleri etkinleştir
  </Tab>
</Tabs>

<div id="analytics">
  ### Analitikler
</div>

<Frame>
  <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/bugbot/bugbot-dashboard.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=0b09bc0e61d1c92017c3ca42957c70e1" alt="Bugbot gösterge paneli" data-og-width="1832" width="1832" data-og-height="2022" height="2022" data-path="images/bugbot/bugbot-dashboard.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/bugbot/bugbot-dashboard.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=fe3c6151118fa404a0a5a100968649cf 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/bugbot/bugbot-dashboard.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=7a602dfdaa6f737dc6d5010ea90a74b8 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/bugbot/bugbot-dashboard.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=6a21a6cb4b32248fb2b8cbea9afb8bcc 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/bugbot/bugbot-dashboard.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=27df9beda1ee9efc84e6f2c339ff1076 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/bugbot/bugbot-dashboard.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=80cb6507ca96d1c2aa74bcc30170b517 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/bugbot/bugbot-dashboard.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=ce35818f10c462b16b2d697519557019 2500w" />
</Frame>

<div id="rules">
  ## Kurallar
</div>

İncelemelere proje özelinde bağlam sağlamak için `.cursor/BUGBOT.md` dosyaları oluştur. Bugbot, her zaman kök dizindeki `.cursor/BUGBOT.md` dosyasını ve değişen dosyalardan yukarı doğru çıkarken bulunan tüm ek dosyaları dahil eder.

```
project/
  .cursor/BUGBOT.md          # Her zaman dahil (proje genelinde kurallar)
  backend/
    .cursor/BUGBOT.md        # Backend dosyaları gözden geçirilirken dahil edilir
    api/
      .cursor/BUGBOT.md      # API dosyaları gözden geçirilirken dahil edilir
  frontend/
    .cursor/BUGBOT.md        # Frontend dosyaları gözden geçirilirken dahil edilir
```

<AccordionGroup>
  <Accordion title="Örnek .cursor/BUGBOT.md">
    ```markdown  theme={null}
    # Proje inceleme yönergeleri

    ## Güvenlik odaklı alanlar

    - API uç noktalarında kullanıcı girdisini doğrula
    - Veritabanı sorgularında SQL enjeksiyonu açıklarını kontrol et
    - Korumalı rotalarda doğru kimlik doğrulamasını sağla

    ## Mimari desenler

    - Servisler için bağımlılık enjeksiyonu kullan
    - Veri erişimi için repository desenini uygula
    - Özel hata sınıflarıyla doğru hata yönetimi uygula

    ## Yaygın sorunlar

    - React bileşenlerinde bellek sızıntıları (useEffect temizliğini kontrol et)
    - UI bileşenlerinde eksik error boundary'ler
    - Tutarsız adlandırma kuralları (fonksiyonlar için camelCase kullan)

    ```
  </Accordion>
</AccordionGroup>

<div id="pricing">
  ## Fiyatlandırma
</div>

Bugbot iki plan sunar: **Free** ve **Pro**.

<div id="free-tier">
  ### Ücretsiz katman
</div>

Her kullanıcı her ay sınırlı sayıda ücretsiz PR incelemesi alır. Takımlarda, her takım üyesinin kendi ücretsiz incelemeleri olur. Sınıra ulaştığında incelemeler bir sonraki faturalandırma döngüne kadar duraklatılır. Sınırsız inceleme için istediğin zaman 14 günlük ücretsiz Pro denemesine geçebilirsin.

<div id="pro-tier">
  ### Pro katmanı
</div>

<Tabs defaultValue="Teams">
  <Tab title="Individuals">
    ### Sabit ücret

    Tüm depolarda ayda en fazla 200 PR için sınırsız Bugbot incelemesi: ayda \$40.

    ### Başlarken

    Hesap ayarların üzerinden abone ol.
  </Tab>

  <Tab title="Teams">
    ### Kullanıcı başına faturalandırma

    Takımlar, sınırsız inceleme için kullanıcı başına ayda \$40 öder.

    Bir kullanıcıyı, o ay içinde Bugbot tarafından incelenen PR’leri yazmış biri olarak sayıyoruz.

    Tüm lisanslar her faturalandırma döngüsünün başında boşa çıkar ve ilk gelen ilk alır esasına göre atanır. Bir kullanıcı bir ay içinde Bugbot tarafından incelenen herhangi bir PR yazmazsa, koltuk başka bir kullanıcı tarafından kullanılabilir.

    ### Koltuk limitleri

    Takım yöneticileri maliyetleri kontrol etmek için aylık maksimum Bugbot koltuğu belirleyebilir.

    ### Başlarken

    Faturalandırmayı etkinleştirmek için takım panon üzerinden abone ol.

    ### Kötüye kullanım önlemleri

    Kötüye kullanımı önlemek için, her Bugbot lisansı için ayda 200 pull request’lik ortak bir üst sınırımız var. Ayda 200’den fazla pull request’e ihtiyacın varsa, lütfen [hi@cursor.com](mailto:hi@cursor.com) adresinden bizimle iletişime geç, sana yardımcı olmaktan memnun oluruz.

    Örneğin, takımında 100 kullanıcı varsa, organizasyonun başlangıçta ayda 20.000 pull request’i inceleyebilir. Bu sınıra doğal olarak ulaşırsan, lütfen bize ulaş, limiti artırmaktan memnun oluruz.
  </Tab>
</Tabs>

<div id="troubleshooting">
  ## Sorun Giderme
</div>

Bugbot çalışmıyorsa:

1. Ayrıntılı günlükler ve istek kimliği için `cursor review verbose=true` veya `bugbot run verbose=true` satırını yorum olarak ekleyerek **ayrıntılı modu etkinleştir**
2. Bugbot’un depoya erişimi olduğundan emin olmak için **izinleri kontrol et**
3. GitHub uygulamasının kurulu ve etkin olduğundan emin olmak için **kurulumu doğrula**

Sorun bildirirken ayrıntılı moddaki istek kimliğini ekle.

<div id="faq">
  ## SSS
</div>

<AccordionGroup>
  <Accordion title="Bugbot gizlilik moduna uygun mu?">
    Evet, Bugbot Cursor’la aynı gizlilik uyumluluğunu izler ve verileri diğer Cursor istekleriyle aynı şekilde işler.
  </Accordion>

  <Accordion title="Ücretsiz katman limitine ulaştığımda ne olur?">
    Aylık ücretsiz katman limitine ulaştığında, Bugbot incelemeleri bir sonraki faturalama döngüne kadar duraklar. Sınırsız inceleme için (standart kötüye kullanım önlemlerine tabi) 14 günlük ücretsiz Pro denemesine geçebilirsin.
  </Accordion>
</AccordionGroup>

```
```

---

← Previous: [Web ve Mobil](./web-ve-mobil.md) | [Index](./index.md) | Next: [Kod İncelemesi](./kod-incelemesi.md) →