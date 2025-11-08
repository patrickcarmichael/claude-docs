---
title: "GitHub"
source: "https://docs.cursor.com/tr/integrations/github"
language: "tr"
language_name: "Turkish"
---

# GitHub
Source: https://docs.cursor.com/tr/integrations/github

Arka plan ajanları için resmi Cursor GitHub uygulaması

[Background Agents](/tr/background-agent) ve [Bugbot](/tr/bugbot), depoları klonlamak ve değişiklikleri push'lamak için Cursor GitHub uygulamasını gerektirir.

<div id="installation">
  ## Kurulum
</div>

1. [Dashboard'da Integrations](https://cursor.com/dashboard?tab=integrations) sayfasına git
2. GitHub’ın yanındaki **Connect**’e tıkla
3. Depoları seç: **All repositories** veya **Selected repositories**

GitHub hesabının bağlantısını kesmek için Integrations dashboard’a dön ve **Disconnect Account**’a tıkla.

## GitHub'da Agent kullanma

GitHub entegrasyonu, arka planda çalışan agent iş akışlarını doğrudan pull request'ler ve issue'lar üzerinden etkinleştirir. Herhangi bir PR veya issue'ya `@cursor [prompt]` yorumunu yazarak bir agent'ın bağlamı okumasını, düzeltmeleri uygulamasını ve commit'leri push etmesini tetikleyebilirsin.

[Bugbot](/tr/bugbot) etkinse, Bugbot'un önerdiği düzeltmeyi okuyup sorunu ele alacak arka plan agent'ını tetiklemek için `@cursor fix` yorumunu yazabilirsin.

<div id="permissions">
  ## İzinler
</div>

GitHub uygulaması, arka plandaki agent'larla çalışmak için belirli izinler gerektirir:

<div className="full-width-table">
  | İzin                       | Amaç                                                                |
  | -------------------------- | ------------------------------------------------------------------- |
  | **Depo erişimi**           | Kodunu klonlamak ve çalışma branch’leri oluşturmak                  |
  | **Pull request’ler**       | İncelemene sunulmak üzere agent değişiklikleriyle PR’ler oluşturmak |
  | **Issues**                 | Agent’ların bulduğu veya düzelttiği hata ve görevleri takip etmek   |
  | **Kontroller ve durumlar** | Kod kalitesi ve test sonuçlarını raporlamak                         |
  | **Actions ve iş akışları** | CI/CD pipeline’larını ve dağıtım durumunu izlemek                   |
</div>

Tüm izinler, arka plandaki agent işlevselliği için gereken asgari ayrıcalık ilkesine göre belirlenir.

<div id="ip-allow-list-configuration">
  ## IP Allow List Yapılandırması
</div>

Kuruluşun, depolarına erişimi kısıtlamak için GitHub’ın IP allow list özelliğini kullanıyorsa, ekibin için IP allowlist işlevini etkinleştirmek adına önce destekle iletişime geçmen gerekir.

<div id="contact-support">
  ### Destekle İletişime Geç
</div>

IP allowlist’leri yapılandırmadan önce, bu özelliği ekibin için etkinleştirmek üzere [hi@cursor.com](mailto:hi@cursor.com) adresiyle iletişime geç. Aşağıdaki her iki yapılandırma yöntemi için de bu gereklidir.

<div id="enable-ip-allow-list-configuration-for-installed-github-apps-recommended">
  ### Yüklü GitHub Uygulamaları için IP allow list yapılandırmasını etkinleştir (Önerilir)
</div>

Cursor GitHub uygulaması, IP listesini zaten önceden yapılandırılmış olarak içerir. Bu listeyi otomatik olarak devralmak için yüklü uygulamalar için allowlist’i etkinleştirebilirsin. Bu **önerilen yaklaşım**, çünkü listeyi bizim güncellememize olanak tanır ve kuruluşun güncellemeleri otomatik olarak alır.

Bunu etkinleştirmek için:

1. Kuruluşunun Security ayarlarına git
2. IP allow list ayarlarına ilerle
3. **“Allow access by GitHub Apps”** seçeneğini işaretle

Ayrıntılı talimatlar için [GitHub’ın belgelerine](https://docs.github.com/en/enterprise-cloud@latest/organizations/keeping-your-organization-secure/managing-security-settings-for-your-organization/managing-allowed-ip-addresses-for-your-organization#allowing-access-by-github-apps) bak.

<div id="add-ips-directly-to-your-allowlist">
  ### IP’leri allowlist’ine doğrudan ekle
</div>

Kuruluşun GitHub’da IdP tanımlı allowlist’ler kullanıyorsa veya önceden yapılandırılmış allowlist’i kullanamıyorsa, IP adreslerini manuel olarak ekleyebilirsin:

```
184.73.225.134
3.209.66.12
52.44.113.131
```

<Note>
  IP adresleri listesi ara sıra değişebilir. IP allow list kullanan takımlara, IP adresleri eklenmeden veya kaldırılmadan önce önceden haber verilir.
</Note>

<div id="troubleshooting">
  ## Sorun Giderme
</div>

<AccordionGroup>
  <Accordion title="Aracı depoya erişemiyor">
    * Depoya erişim yetkisiyle GitHub uygulamasını yükle
    * Özel depolar için depo izinlerini kontrol et
    * GitHub hesabı izinlerini doğrula
  </Accordion>

  <Accordion title="Pull request'ler için izin reddedildi">
    * Uygulamaya pull request'lere yazma izni ver
    * Dal koruma kurallarını kontrol et
    * Uygulamanın kurulumu süresi dolduysa yeniden yükle
  </Accordion>

  <Accordion title="Uygulama GitHub ayarlarında görünmüyor">
    * Organizasyon düzeyinde kurulup kurulmadığını kontrol et
    * [github.com/apps/cursor](https://github.com/apps/cursor) üzerinden yeniden yükle
    * Kurulum bozulduysa destekle iletişime geç
  </Accordion>
</AccordionGroup>

---

← Previous: [Git](./git.md) | [Index](./index.md) | Next: [Linear](./linear.md) →