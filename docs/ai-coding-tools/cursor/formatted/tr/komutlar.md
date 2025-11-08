---
title: "Komutlar"
source: "https://docs.cursor.com/tr/agent/chat/commands"
language: "tr"
language_name: "Turkish"
---

# Komutlar
Source: https://docs.cursor.com/tr/agent/chat/commands

Yeniden kullanılabilir iş akışları için komutlar tanımla

Özel komutlar, sohbet giriş kutusunda basit bir `/` önekiyle tetikleyebileceğin, yeniden kullanılabilir iş akışları oluşturmanı sağlar. Bu komutlar, ekip genelinde süreçleri standartlaştırmana yardımcı olur ve yaygın görevleri daha verimli hale getirir.

<Frame>
    <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/commands/input.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=0d25ac517b091210da1c6eff4c8e3098" alt="Komut girişi örneği" data-og-width="1689" width="1689" data-og-height="1079" height="1079" data-path="images/chat/commands/input.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/commands/input.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=680f0cbf1491ef1303171dbd18115288 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/commands/input.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=d6a5397e565ab2c90435e6fdd2b7b27a 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/commands/input.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=ae074e2f2b26741544fd8c8ecfa529e3 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/commands/input.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=564aad432affcc04e51b624725f386ad 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/commands/input.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=5c1bd5d49babc2f08eb0efcd24ba7783 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/commands/input.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=3244c3be31c9bc704468a706c6e6b38e 2500w" />
</Frame>

<Info>
  Komutlar şu anda beta aşamasında. Geliştirmeye devam ettikçe özellikler ve sözdizimi değişebilir.
</Info>

<div id="how-commands-work">
  ## Komutlar nasıl çalışır
</div>

Komutlar, iki konumda saklanabilen düz Markdown dosyaları olarak tanımlanır:

1. **Proje komutları**: Projendeki `.cursor/commands` dizininde saklanır
2. **Genel komutlar**: Ev dizinindeki `~/.cursor/commands` dizininde saklanır

Sohbet giriş kutusuna `/` yazdığında, Cursor her iki dizindeki mevcut komutları otomatik olarak algılar ve görüntüler; böylece bunlara iş akışın boyunca anında erişebilirsin.

<div id="creating-commands">
  ## Komut oluşturma
</div>

1. Proje kökünde `.cursor/commands` dizini oluştur
2. Açıklayıcı adlara sahip `.md` dosyaları ekle (ör. `review-code.md`, `write-tests.md`)
3. Komutun ne yapması gerektiğini anlatan düz Markdown içeriği yaz
4. Sohbette `/` yazdığında komutlar otomatik olarak görünecek

Komutlar dizin yapısının nasıl görünebileceğine dair bir örnek:

```
.cursor/
└── commands/
    ├── address-github-pr-comments.md
    ├── code-review-checklist.md
    ├── create-pr.md
    ├── light-review-existing-diffs.md
    ├── onboard-new-developer.md
    ├── run-all-tests-and-fix.md
    ├── security-audit.md
    └── setup-new-feature.md
```

<div id="examples">
  ## Örnekler
</div>

Bu komutları projelerinde deneyerek nasıl çalıştıklarını gör.

<AccordionGroup>
  <Accordion title="Kod inceleme kontrol listesi">
    ```markdown  theme={null}
    # Kod İnceleme Kontrol Listesi

    ## Genel Bakış
    Kalite, güvenlik ve sürdürülebilirliği sağlamak için kapsamlı kod incelemeleri yapmak üzere hazırlanmış ayrıntılı kontrol listesi.

    ## İnceleme Kategorileri

    ### İşlevsellik
    - [ ] Kod bekleneni yapıyor
    - [ ] Sınır durumları ele alınmış
    - [ ] Hata yönetimi uygun
    - [ ] Bariz bug veya mantık hatası yok

    ### Kod Kalitesi
    - [ ] Kod okunabilir ve iyi yapılandırılmış
    - [ ] Fonksiyonlar küçük ve odaklı
    - [ ] Değişken adları açıklayıcı
    - [ ] Kod tekrarı yok
    - [ ] Proje kurallarına uyuyor

    ### Güvenlik
    - [ ] Bariz güvenlik açıkları yok
    - [ ] Girdi doğrulaması mevcut
    - [ ] Hassas veriler doğru şekilde işleniyor
    - [ ] Hardcoded sırlar yok
    ```
  </Accordion>

  <Accordion title="Güvenlik denetimi">
    ```markdown  theme={null}
    # Güvenlik Denetimi

    ## Genel Bakış
    Kod tabanındaki güvenlik açıklarını tespit edip gidermek için kapsamlı bir güvenlik incelemesi.

    ## Adımlar
    1. **Bağımlılık denetimi**
       - Bilinen güvenlik açıklarını kontrol et
       - Güncelliğini yitirmiş paketleri güncelle
       - Üçüncü taraf bağımlılıkları gözden geçir

    2. **Kod güvenliği incelemesi**
       - Yaygın güvenlik açıklarını kontrol et
       - Kimlik doğrulama/yetkilendirmeyi gözden geçir
       - Veri işleme uygulamalarını denetle

    3. **Altyapı güvenliği**
       - Ortam değişkenlerini gözden geçir
       - Erişim kontrollerini denetle
       - Ağ güvenliğini denetle

    ## Güvenlik Kontrol Listesi
    - [ ] Bağımlılıklar güncel ve güvenli
    - [ ] Sabit kodlanmış sırlar yok
    - [ ] Girdi doğrulama uygulanmış
    - [ ] Kimlik doğrulama güvenli
    - [ ] Yetkilendirme doğru şekilde yapılandırılmış
    ```
  </Accordion>

  <Accordion title="Yeni özelliği kur">
    ```markdown  theme={null}
    # Yeni Özellik Kurulumu

    ## Genel Bakış
    Yeni bir özelliği ilk planlamadan uygulama yapısına kadar sistematik şekilde hazırla.

    ## Adımlar
    1. **Gereksinimleri tanımla**
       - Özelliğin kapsamını ve hedeflerini netleştir
       - Kullanıcı hikâyelerini ve kabul kriterlerini belirle
       - Teknik yaklaşımı planla

    2. **Özellik dalı oluştur**
       - main/develop’tan dal çıkar
       - Yerel geliştirme ortamını kur
       - Yeni bağımlılıkları yapılandır

    3. **Mimariyi planla**
       - Veri modellerini ve API’leri tasarla
       - UI bileşenlerini ve akışı planla
       - Test stratejisini belirle

    ## Özellik Kurulum Kontrol Listesi
    - [ ] Gereksinimler belgelendi
    - [ ] Kullanıcı hikâyeleri yazıldı
    - [ ] Teknik yaklaşım planlandı
    - [ ] Özellik dalı oluşturuldu
    - [ ] Geliştirme ortamı hazır
    ```
  </Accordion>

  <Accordion title="Pull request oluştur">
    ```markdown  theme={null}
    # PR Oluştur

    ## Genel Bakış
    Uygun açıklama, etiketler ve gözden geçirenlerle iyi yapılandırılmış bir pull request oluştur.

    ## Adımlar
    1. **Branşı hazırla**
       - Tüm değişikliklerin commit’lendiğinden emin ol
       - Branşı remote’a pushla
       - Branşın main ile güncel olduğunu doğrula

    2. **PR açıklamasını yaz**
       - Değişiklikleri net şekilde özetle
       - Bağlam ve motivasyonu ekle
       - Herhangi bir breaking change’i listele
       - UI değişiklikleri varsa ekran görüntüleri ekle

    3. **PR’ı ayarla**
       - Açıklayıcı bir başlıkla PR oluştur
       - Uygun etiketleri ekle
       - Gözden geçirenler ata
       - İlgili issue’ları bağla

    ## PR Şablonu
    - [ ] Feature A
    - [ ] Bug fix B
    - [ ] Unit test’ler geçiyor
    - [ ] Manuel test tamamlandı
    ```
  </Accordion>

  <Accordion title="Testleri çalıştır ve hataları düzelt">
    ```markdown  theme={null}
    # Tüm Testleri Çalıştır ve Hataları Düzelt

    ## Genel Bakış
    Tüm test süitini çalıştır ve olası hataları sistematik olarak gider, kod kalitesini ve işlevselliği güvence altına al.

    ## Adımlar
    1. **Test süitini çalıştır**
       - Projedeki tüm testleri çalıştır
       - Çıktıyı kaydet ve hataları tespit et
       - Hem birim hem de entegrasyon testlerini kontrol et

    2. **Hataları analiz et**
       - Türe göre sınıflandır: flaky, bozuk, yeni hatalar
       - Etkisine göre düzeltmelere öncelik ver
       - Hataların yakın zamanda yapılan değişikliklerle ilişkili olup olmadığını kontrol et

    3. **Sorunları sistematik olarak gider**
       - En kritik hatalardan başla
       - Her seferinde tek bir sorunu düzelt
       - Her düzeltmeden sonra testleri yeniden çalıştır
    ```
  </Accordion>

  <Accordion title="Yeni geliştireni işe al">
    ```markdown  theme={null}
    # Yeni Geliştiriciyi Ekibe Kazandır

    ## Genel Bakış
    Yeni bir geliştiriciyi hızlıca üretken hale getirmek için kapsamlı bir işe alıştırma süreci.

    ## Adımlar
    1. **Ortam kurulumu**
       - Gerekli araçları yükle
       - Geliştirme ortamını kur
       - IDE ve eklentileri yapılandır
       - Git ve SSH anahtarlarını ayarla

    2. **Projeye alışma**
       - Proje yapısını gözden geçir
       - Mimarinin anlaşılmasını sağla
       - Temel dökümantasyonu oku
       - Yerel veritabanını kur

    ## İse Alıştırma Kontrol Listesi
    - [ ] Geliştirme ortamı hazır
    - [ ] Tüm testler geçiyor
    - [ ] Uygulama yerelde çalıştırılabiliyor
    - [ ] Veritabanı kuruldu ve çalışıyor
    - [ ] İlk PR gönderildi
    ```
  </Accordion>
</AccordionGroup>

---

← Previous: [Checkpoints](./checkpoints.md) | [Index](./index.md) | Next: [Compact](./compact.md) →