---
title: "Kurallar"
source: "https://docs.cursor.com/tr/context/rules"
language: "tr"
language_name: "Turkish"
---

# Kurallar
Source: https://docs.cursor.com/tr/context/rules

Agent modelinin yeniden kullanılabilir, kapsamlı talimatlarla nasıl davrandığını kontrol et.

Kurallar, Agent ve Inline Edit için sistem düzeyinde talimatlar sağlar. Bunları projelerin için kalıcı bağlam, tercihler veya iş akışları olarak düşün.

Cursor dört tür kuralı destekler:

<CardGroup cols={2}>
  <Card title="Project Rules" icon="folder-tree">
    `.cursor/rules` içinde saklanır, sürüm kontrolünde tutulur ve kod tabanına özelleştirilir.
  </Card>

  <Card title="User Rules" icon="user">
    Cursor ortamında geneldir. Ayarlarda tanımlanır ve her zaman uygulanır.
  </Card>

  <Card title="AGENTS.md" icon="robot">
    Agent talimatları markdown formatında. `.cursor/rules` için basit bir alternatif.
  </Card>

  <Card title=".cursorrules (Legacy)" icon="clock-rotate-left">
    Hâlâ destekleniyor ama kullanım dışı. Bunun yerine Project Rules kullan.
  </Card>
</CardGroup>

<div id="how-rules-work">
  ## Kurallar nasıl çalışır
</div>

Büyük dil modelleri tamamlamalar arasında belleği korumaz. Kurallar, istem düzeyinde kalıcı ve yeniden kullanılabilir bağlam sağlar.

Uygulandığında, kural içeriği model bağlamının başına eklenir. Bu, yapay zekâya kod üretme, düzenlemeleri yorumlama veya iş akışlarına yardımcı olma konusunda tutarlı yönlendirme sağlar.

<Frame>
  <img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rules-applied.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=e637bab83cfd5dcc8a3b15ed6fd9fc15" alt="Sohbet bağlamında uygulanan kural" data-og-width="1198" width="1198" data-og-height="674" height="674" data-path="images/context/rules/rules-applied.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rules-applied.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=78e3c392987c6f95a02fc106753c5f98 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rules-applied.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=9d3a8b76ba99ada5ca302cba9fb63810 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rules-applied.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=f5ab7fb374a1a4c5fe2f50e2e50d233a 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rules-applied.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=5d25394a29c1da4172a3e673ee384c07 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rules-applied.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=0fc125bd3c2a93551674252c0523d3ec 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rules-applied.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=c576ea053ee18c30d2781c6bdd394a70 2500w" />
</Frame>

<Info>
  Kurallar [Chat](/tr/chat/overview) ve [Inline
  Edit](/tr/inline-edit/overview) için geçerlidir. Etkin kurallar Agent kenar çubuğunda görünür.
</Info>

<div id="project-rules">
  ## Proje kuralları
</div>

Proje kuralları `.cursor/rules` içinde bulunur. Her kural bir dosyadır ve sürüm kontrolü altındadır. Yol kalıplarıyla kapsamlanabilir, elle tetiklenebilir ya da ilgililik durumuna göre dahil edilebilir. Alt dizinler, yalnızca o klasöre uygulanacak şekilde kapsamlanan kendi `.cursor/rules` dizinlerini barındırabilir.

Proje kurallarını şunlar için kullan:

* Kod tabanına ilişkin alan-özel bilgiyi kodlamak
* Projeye özgü iş akışlarını veya şablonları otomatikleştirmek
* Stil veya mimari kararları standartlaştırmak

<div id="rule-anatomy">
  ### Kural yapısı
</div>

Her kural dosyası, meta veriler ve içeriği destekleyen **MDC** (`.mdc`) formatında yazılır. `description`, `globs`, `alwaysApply` özelliklerini değiştiren tür açılır menüsünden kuralların nasıl uygulanacağını kontrol et.

| <span class="no-wrap">Kural Türü</span>        | Açıklama                                                               |
| :--------------------------------------------- | :--------------------------------------------------------------------- |
| <span class="no-wrap">`Always`</span>          | Model bağlamına her zaman eklenir                                      |
| <span class="no-wrap">`Auto Attached`</span>   | Glob desenini eşleyen dosyalara referans verildiğinde eklenir          |
| <span class="no-wrap">`Agent Requested`</span> | Dahil edilip edilmeyeceğine AI karar verir. Bir açıklama sağlanmalıdır |
| <span class="no-wrap">`Manual`</span>          | Yalnızca `@ruleName` kullanılarak açıkça belirtildiğinde eklenir       |

```
---
description: RPC Servis kalıbı
globs:
alwaysApply: false
---

- Servisleri tanımlarken dahili RPC kalıbımızı kullan
- Servis adları için her zaman snake_case kullan

@service-template.ts
```

<div id="nested-rules">
  ### İç içe kurallar
</div>

Kuralları proje genelinde `.cursor/rules` dizinlerine yerleştirerek düzenle. Kendi dizinlerindeki dosyalar referans alındığında, iç içe kurallar otomatik olarak uygulanır.

```
project/
  .cursor/rules/        # Proje genelinde geçerli kurallar
  backend/
    server/
      .cursor/rules/    # Backend’e özel kurallar
  frontend/
    .cursor/rules/      # Frontend’e özel kurallar
```

<div id="creating-a-rule">
  ### Kural oluşturma
</div>

`New Cursor Rule` komutunu kullanarak veya `Cursor Settings > Rules` bölümüne giderek kural oluştur. Bu, `.cursor/rules` içinde yeni bir kural dosyası oluşturur. Ayarlardan tüm kuralları ve durumlarını görebilirsin.

<Frame>
  <img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rule-settings.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=db8142786bbb7b7771ae0db8b2704b0b" alt="Kısa ve uzun kuralların karşılaştırması" data-og-width="6016" width="6016" data-og-height="3334" height="3334" data-path="images/context/rules/rule-settings.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rule-settings.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=0b6e9b8d6ca799d1af62957726b1cc52 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rule-settings.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=8bfe1482ab9afc0995fe13371b26074b 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rule-settings.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=a847d915b3f106c42cba7cb1245bb138 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rule-settings.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=356963b3607152f7ffe128cd1a2d050e 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rule-settings.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=1b1e50d3721d42c691a434189729921c 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rule-settings.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=d2081cf016d65053f1e517eb5734079e 2500w" />
</Frame>

<div id="generating-rules">
  ### Kurallar oluşturma
</div>

Sohbetlerde `/Generate Cursor Rules` komutunu kullanarak kuralları doğrudan oluştur. Aracın davranışıyla ilgili kararlar verdiğinde ve bunları yeniden kullanmak istediğinde işine yarar.

<Frame>
  <video src="https://www.cursor.com/changelog/049/generate-rules.mp4" controls>
    Tarayıcın video etiketini desteklemiyor.
  </video>
</Frame>

<div id="best-practices">
  ## En iyi uygulamalar
</div>

İyi kurallar odaklı, uygulanabilir ve iyi tanımlanmış kapsamda olmalı.

* Kuralları 500 satırın altında tut
* Büyük kuralları birden çok, birleştirilebilir kurala böl
* Somut örnekler ya da referans verilen dosyalar ekle
* Belirsiz yönlendirmelerden kaçın. Kuralları net iç dokümanlar gibi yaz
* Sohbette tekrarlayan istemlerde kuralları yeniden kullan

<div id="examples">
  ## Örnekler
</div>

<AccordionGroup>
  <Accordion title="Frontend bileşenleri ve API doğrulaması için standartlar">
    Bu kural, frontend bileşenleri için standartlar sunar:

    components dizininde çalışırken:

    * Stil için her zaman Tailwind kullan
    * Animasyonlar için Framer Motion kullan
    * Bileşen adlandırma kurallarına uy

    Bu kural, API uç noktaları için doğrulamayı zorunlu kılar:

    API dizininde:

    * Tüm doğrulamalar için zod kullan
    * Dönüş tiplerini zod şemalarıyla tanımla
    * Şemalardan üretilen tipleri dışa aktar
  </Accordion>

  <Accordion title="Express servisleri ve React bileşenleri için şablonlar">
    Bu kural, Express servisleri için bir şablon sağlar:

    Express servisi oluştururken bu şablonu kullan:

    * RESTful ilkeleri takip et
    * Hata yakalama middleware’i ekle
    * Doğru loglamayı yapılandır

    @express-service-template.ts

    Bu kural, React bileşen yapısını tanımlar:

    React bileşenleri şu düzeni takip etmeli:

    * En üstte Props arayüzü
    * Bileşen named export olarak
    * En altta stiller

    @component-template.tsx
  </Accordion>

  <Accordion title="Geliştirme iş akışlarının otomasyonu ve dokümantasyon üretimi">
    Bu kural, uygulama analizini otomatikleştirir:

    Uygulamayı analiz etmen istendiğinde:

    1. `npm run dev` ile geliştirme sunucusunu çalıştır
    2. Konsoldan logları al
    3. Performans iyileştirmeleri öner

    Bu kural, dokümantasyon üretimine yardımcı olur:

    Dokümantasyon taslağı hazırlarken:

    * Kod yorumlarını çıkar
    * README.md dosyasını analiz et
    * Markdown dokümantasyonu üret
  </Accordion>

  <Accordion title="Cursor’da yeni bir ayar ekleme">
    İlk olarak `@reactiveStorageTypes.ts` içinde aç/kapa yapılacak bir özellik (property) oluştur.

    `@reactiveStorageService.tsx` içindeki `INIT_APPLICATION_USER_PERSISTENT_STORAGE` içine varsayılan değeri ekle.

    Beta özellikleri için toggle’ı `@settingsBetaTab.tsx` içine, diğer durumlarda `@settingsGeneralTab.tsx` içine ekle. Toggle’lar, genel onay kutuları için `<SettingsSubSection>` olarak eklenebilir. Örnekler için dosyanın geri kalanına bak.

    ```
    <SettingsSubSection
    				label="Özellik adı"
    				description="Özellik açıklaması"
    				value={
    					vsContext.reactiveStorageService.applicationUserPersistentStorage
    						.myNewProperty ?? false
    				}
    				onChange={(newVal) => {
    					vsContext.reactiveStorageService.setApplicationUserPersistentStorage(
    						'myNewProperty',
    						newVal
    					);
    				}}
    			/>
    ```

    Uygulamada kullanmak için reactiveStorageService’i içe aktar ve özelliği kullan:

    ```
    const flagIsEnabled = vsContext.reactiveStorageService.applicationUserPersistentStorage.myNewProperty
    ```
  </Accordion>
</AccordionGroup>

Sağlayıcılar ve framework’lerden birçok örnek mevcut. Topluluk katkılı kurallar, çevrimiçi kitle kaynaklı koleksiyonlar ve depolarda bulunur.

<div id="agentsmd">
  ## AGENTS.md
</div>

`AGENTS.md`, ajan talimatlarını tanımlamak için basit bir markdown dosyasıdır. Basit kullanım senaryoları için `.cursor/rules`’a alternatif olarak proje kök dizinine yerleştir.

Project Rules’dan farklı olarak `AGENTS.md`, meta veri veya karmaşık yapılandırmalar içermeyen düz bir markdown dosyasıdır. Yapılandırılmış kuralların ek yükü olmadan basit ve okunabilir talimatlara ihtiyaç duyan projeler için idealdir.

```markdown  theme={null}

---

← Previous: [Anılar](./anlar.md) | [Index](./index.md) | Next: [Kavramlar](./kavramlar.md) →