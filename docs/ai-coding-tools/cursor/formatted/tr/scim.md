---
title: "SCIM"
source: "https://docs.cursor.com/tr/account/teams/scim"
language: "tr"
language_name: "Turkish"
---

# SCIM
Source: https://docs.cursor.com/tr/account/teams/scim

Otomatik kullanıcı ve grup yönetimi için SCIM provizyonunu kur

<div id="overview">
  ## Genel Bakış
</div>

SCIM 2.0 provizyonu, kimlik sağlayıcın üzerinden ekip üyelerini ve dizin gruplarını otomatik olarak yönetir. SSO’nun etkin olduğu Enterprise planlarında kullanılabilir.

<product_visual type="screenshot">
  SCIM ayarları kontrol paneli, Active Directory Management yapılandırmasını gösteriyor
</product_visual>

<div id="prerequisites">
  ## Önkoşullar
</div>

* Cursor Enterprise planı
* SSO önce yapılandırılmalı — **SCIM için etkin bir SSO bağlantısı gerekir**
* Kimlik sağlayıcında (Okta, Azure AD, vb.) yönetici erişimi
* Cursor organizasyonunda yönetici erişimi

<div id="how-it-works">
  ## Nasıl çalışır
</div>

<div id="user-provisioning">
  ### Kullanıcı sağlama
</div>

Kullanıcılar, kimlik sağlayıcındaki SCIM uygulamasına atandığında otomatik olarak Cursor’a eklenir. Atama kaldırıldığında kaldırılırlar. Değişiklikler gerçek zamanlı olarak senkronize edilir.

<div id="directory-groups">
  ### Dizin grupları
</div>

Dizin grupları ve bu grupların üyelikleri kimlik sağlayıcından senkronize edilir. Grup ve kullanıcı yönetimi kimlik sağlayıcın üzerinden yapılmalıdır — Cursor bu bilgileri salt okunur olarak gösterir.

<div id="spend-management">
  ### Harcama yönetimi
</div>

Her dizin grubu için kullanıcı başına farklı harcama limitleri belirle. Dizin grubu limitleri, takım düzeyi limitlere göre önceliklidir. Birden fazla grupta olan kullanıcılar, geçerli en yüksek harcama limitini alır.

<div id="setup">
  ## Kurulum
</div>

<Steps>
  <Step title="SSO'nun yapılandırıldığından emin ol">
    SCIM'in çalışması için önce SSO kurulmalı. Henüz SSO'yu yapılandırmadıysan,
    devam etmeden önce [SSO kurulum rehberi](/tr/account/teams/sso)
    adımlarını takip et.
  </Step>

  <Step title="Active Directory Yönetimine eriş">
    Yönetici hesabınla
    [cursor.com/dashboard?tab=active-directory](https://www.cursor.com/dashboard?tab=active-directory)
    adresine git ya da kontrol paneli ayarlarına gidip "Active Directory Management"
    sekmesini seç.
  </Step>

  <Step title="SCIM kurulumunu başlat">
    SSO doğrulandıktan sonra, adım adım SCIM kurulumu için bir bağlantı göreceksin.
    Yapılandırma sihirbazını başlatmak için buna tıkla.
  </Step>

  <Step title="Kimlik sağlayıcında SCIM'i yapılandır">
    Kimlik sağlayıcında: - SCIM uygulamasını oluştur ya da yapılandır - Cursor'ın
    sağladığı SCIM uç noktasını ve token'ını kullan - Kullanıcı ve grup sağlama
    (provisioning) özelliğini etkinleştir - Bağlantıyı test et
  </Step>

  <Step title="Harcama limitlerini yapılandır (opsiyonel)">
    Cursor'ın Active Directory Yönetimi sayfasına geri dön: - Senkronize edilmiş
    dizin gruplarını görüntüle - Gerektiğinde belirli gruplar için kullanıcı başına
    harcama limitleri belirle - Birden fazla grupta olan kullanıcılara hangi
    limitlerin uygulandığını gözden geçir
  </Step>
</Steps>

<div id="identity-provider-setup">
  ### Kimlik sağlayıcı kurulumu
</div>

Sağlayıcıya özel kurulum talimatları için:

<Card title="Kimlik Sağlayıcı Rehberleri" icon="book" href="https://workos.com/docs/integrations">
  Okta, Azure AD, Google Workspace ve daha fazlası için kurulum talimatları.
</Card>

<div id="managing-users-and-groups">
  ## Kullanıcı ve grup yönetimi
</div>

<Warning>
  Tüm kullanıcı ve grup yönetimini kimlik sağlayıcın üzerinden yapmalısın.
  Kimlik sağlayıcında yaptığın değişiklikler otomatik olarak Cursor’a senkronize edilir, ama
  kullanıcıları veya grupları doğrudan Cursor’da değiştiremezsin.
</Warning>

<div id="user-management">
  ### Kullanıcı yönetimi
</div>

* Kimlik sağlayıcında SCIM uygulamana atayarak kullanıcı ekle
* SCIM uygulamasındaki atamasını kaldırarak kullanıcıyı çıkar
* Kullanıcı profili değişiklikleri (ad, e‑posta) kimlik sağlayıcından otomatik olarak senkronize edilir

<div id="group-management">
  ### Grup yönetimi
</div>

* Dizin grupları kimlik sağlayıcından otomatik olarak senkronize edilir
* Grup üyeliği değişiklikleri gerçek zamanlı yansır
* Kullanıcıları düzenlemek ve farklı harcama limitleri belirlemek için grupları kullan

<div id="spend-limits">
  ### Harcama limitleri
</div>

* Her dizin grubu için kullanıcı başına farklı limitler ayarla
* Kullanıcılar, gruplarından en yüksek harcama limitini devralır
* Grup limitleri, varsayılan ekip genelindeki kullanıcı başına limiti geçersiz kılar

<div id="faq">
  ## SSS
</div>

<div id="why-isnt-scim-management-showing-up-in-my-dashboard">
  ### SCIM yönetimi neden kontrol panelimde görünmüyor?
</div>

SCIM’i kurmadan önce SSO’nun doğru yapılandırıldığından ve çalıştığından emin ol. SCIM’in çalışması için etkin bir SSO bağlantısı gerekir.

<div id="why-arent-users-syncing">
  ### Kullanıcılar neden senkronize olmuyor?
</div>

Kimlik sağlayıcında kullanıcıların SCIM uygulamasına atandığını doğrula. Kullanıcıların Cursor’da görünmesi için açıkça atanmış olmaları gerekir.

<div id="why-arent-groups-appearing">
  ### Gruplar neden görünmüyor?
</div>

Kimlik sağlayıcının SCIM ayarlarında grup itme (push group provisioning) özelliğinin etkin olduğundan emin ol. Grup senkronizasyonu, kullanıcı senkronizasyonundan ayrı yapılandırılır.

<div id="why-arent-spend-limits-applying">
  ### Harcama limitleri neden uygulanmıyor?
</div>

Kullanıcıların kimlik sağlayıcında ilgili gruplara doğru şekilde atandığını doğrula. Hangi harcama limitlerinin geçerli olacağını grup üyeliği belirler.

<div id="can-i-manage-scim-users-and-groups-directly-in-cursor">
  ### SCIM kullanıcılarını ve gruplarını doğrudan Cursor’da yönetebilir miyim?
</div>

Hayır. Tüm kullanıcı ve grup yönetimi kimlik sağlayıcın üzerinden yapılmalı. Cursor bu bilgileri yalnızca salt okunur olarak gösterir.

<div id="how-quickly-do-changes-sync">
  ### Değişiklikler ne kadar hızlı senkronize olur?
</div>

Kimlik sağlayıcında yapılan değişiklikler gerçek zamanlı olarak Cursor’a senkronize edilir. Büyük toplu işlemlerde kısa bir gecikme olabilir.

---

← Previous: [Üyeler ve Roller](./yeler-ve-roller.md) | [Index](./index.md) | Next: [Başlarken](./balarken.md) →