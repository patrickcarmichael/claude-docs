---
title: "Üyeler ve Roller"
source: "https://docs.cursor.com/tr/account/teams/members"
language: "tr"
language_name: "Turkish"
---

# Üyeler ve Roller
Source: https://docs.cursor.com/tr/account/teams/members

Ekip üyelerini ve rolleri yönet

Cursor ekiplerinde üç rol bulunur:

<div id="roles">
  ## Roller
</div>

**Members**, Cursor’ın Pro özelliklerine erişimi olan varsayılan roldür.

* Cursor’ın Pro özelliklerine tam erişim
* Faturalandırma ayarlarına veya yönetici paneline erişim yok
* Kendi kullanımlarını ve kalan kullanım bazlı bütçelerini görebilirler

**Admins** ekip yönetimi ve güvenlik ayarlarını kontrol eder.

* Pro özelliklere tam erişim
* Üye ekleme/çıkarma, rol değiştirme, SSO kurulumu
* Kullanım bazlı fiyatlandırma ve harcama limitlerini yapılandırma
* Ekip analizlerine erişim

**Unpaid Admins**, ücretli bir koltuk kullanmadan ekipleri yönetir — Cursor’a erişime ihtiyaç duymayan BT veya finans ekibi için idealdir.

* Faturalandırılmaz, Pro özelliklere erişim yok
* Admins ile aynı yönetim yetkileri

<Info>Unpaid Admins için ekipte en az bir ücretli kullanıcı bulunmalıdır.</Info>

<div id="role-comparison">
  ## Rol Karşılaştırması
</div>

<div className="full-width-table">
  | Yetkinlik                     | Üye | Admin | Ücretsiz Admin |
  | ----------------------------- | :-: | :---: | :------------: |
  | Cursor özelliklerini kullanma |  ✓  |   ✓   |                |
  | Üye davet etme                |  ✓  |   ✓   |        ✓       |
  | Üye kaldırma                  |     |   ✓   |        ✓       |
  | Kullanıcı rolü değiştirme     |     |   ✓   |        ✓       |
  | Admin paneli                  |     |   ✓   |        ✓       |
  | SSO/Güvenlik yapılandırma     |     |   ✓   |        ✓       |
  | Faturalandırma yönetimi       |     |   ✓   |        ✓       |
  | Analitikleri görüntüleme      |     |   ✓   |        ✓       |
  | Erişim yönetimi               |     |   ✓   |        ✓       |
  | Kullanım denetimleri ayarlama |     |   ✓   |        ✓       |
  | Ücretli koltuk gerekir        |  ✓  |   ✓   |                |
</div>

<div id="managing-members">
  ## Üyeleri yönetme
</div>

Tüm ekip üyeleri başkalarını davet edebilir. Şu anda davetleri kısıtlamıyoruz.

<div id="add-member">
  ### Üye ekle
</div>

Üyeleri üç yolla ekleyebilirsin:

1. **E-posta daveti**

   * `Invite Members`'a tıkla
   * E-posta adreslerini gir
   * Kullanıcılar e-posta daveti alır

2. **Davet bağlantısı**

   * `Invite Members`'a tıkla
   * `Invite Link`'i kopyala
   * Ekip üyeleriyle paylaş

3. **SSO**
   * [admin dashboard](/tr/account/teams/sso)'da SSO'yu yapılandır
   * Kullanıcılar SSO e-postasıyla giriş yaptığında otomatik katılır

<Warning>
  Davet bağlantılarının süresi uzundur — bağlantıya sahip olan herkes katılabilir.
  Bunları iptal et veya [SSO](/tr/account/teams/sso) kullan
</Warning>

<div id="remove-member">
  ### Üye kaldır
</div>

Yöneticiler, bağlam menüsü → "Remove" üzerinden istedikleri zaman üyeleri kaldırabilir. Bir üye herhangi bir kredi kullandıysa, koltuğu faturalama döngüsünün sonuna kadar dolu kalır.

<div id="change-role">
  ### Rol değiştir
</div>

Yöneticiler, bağlam menüsüne tıklayıp "Change role" seçeneğini kullanarak diğer üyelerin rollerini değiştirebilir.<br />

Ekipte her zaman en az bir Yönetici ve en az bir ücretli üye olmalıdır.

## Güvenlik & SSO

SAML 2.0 Single Sign-On (SSO) Team planlarında sunulur. Öne çıkan özellikler:

* SSO bağlantılarını yapılandır ([daha fazlasını öğren](/tr/account/teams/sso))
* Alan doğrulamasını ayarla
* Otomatik kullanıcı kaydı
* SSO zorunluluğu seçenekleri
* Kimlik sağlayıcı entegrasyonu (Okta vb.)

<Note>
  <p className="!mb-0">SSO’yu etkinleştirmek için alan doğrulaması zorunludur.</p>
</Note>

<Frame>
  <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=76608c26daf1f9ab2bbc2c4ccb156c0e" style={{ padding: `32px 64px`, backgroundColor: "#0c0c0c" }} data-og-width="802" width="802" data-og-height="440" height="440" data-path="images/account/sso-settings.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=334dc1fc107338d19ec7b0052e7ea0e4 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=543b3d868c19960a5fb4c526d9895bd3 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=a06655178ba10f6a72919e9f7d598191 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=e280fc911306fe8d3b8e90b7221b0c11 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=ffd8f2c0168e2ac4f95431062b226021 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=1c17e4eac666b663d676ce874f1c4ba5 2500w" />
</Frame>

<div id="usage-controls">
  ## Kullanım Kontrolleri
</div>

Kullanım ayarlarına erişerek şunları yapabilirsin:

* Kullanım bazlı fiyatlandırmayı etkinleştir
* Premium modeller için etkinleştir
* Yalnızca adminin düzenleyebileceği değişiklikleri ayarla
* Aylık harcama limitleri belirle
* Ekip genelindeki kullanımı izle

<Frame>
  <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/usage-based-pricing.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=e8149f830c27308af1bcc329c25e38b5" style={{ backgroundColor: "#0c0c0c" }} data-og-width="1668" width="1668" data-og-height="1160" height="1160" data-path="images/account/usage-based-pricing.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/usage-based-pricing.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=bc308a967251694ad7b03189c1083c61 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/usage-based-pricing.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=ddc293e19fa993e65be8c09ced649b4f 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/usage-based-pricing.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=3a4df7d48d75c6166ab215550a641ca6 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/usage-based-pricing.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=f9051947c802ae54fd964196c50a3701 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/usage-based-pricing.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=ed775e3e98611ead1b938aedaf917f11 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/usage-based-pricing.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=b26f86bce94dc981d3cf71853a965374 2500w" />
</Frame>

<div id="billing">
  ## Faturalandırma
</div>

Takım üyeleri eklerken:

* Her üye veya admin, faturalandırılabilir bir koltuk ekler (bkz. [pricing](https://cursor.com/pricing))
* Yeni üyeler, faturalandırma döneminde kalan süre için orantılı (pro-rata) ücretlendirilir
* Ücretsiz admin koltukları sayılmaz

Ay ortasında yapılan eklemelerde yalnızca kullanılan günler için ücret alınır. Kredilerini kullanmış üyeleri kaldırdığında, koltukları faturalandırma döngüsü sonuna kadar dolu kalır — orantılı geri ödeme yapılmaz.

Rol değişiklikleri (ör. Admin’den Ücretsiz Admin’e) faturalandırmayı değişiklik tarihinden itibaren günceller. Aylık veya yıllık faturalandırmayı seç.

Aylık/yıllık yenileme, üye değişikliklerinden bağımsız olarak, ilk kayıt olduğun tarihte gerçekleşir.

<div id="switch-to-yearly-billing">
  ### Yıllık faturalandırmaya geç
</div>

Aylıktan yıllığa geçerek **%20** tasarruf et:

1. [Dashboard](https://cursor.com/dashboard)’a git
2. Hesap bölümünde “Advanced”e tıkla, ardından “Upgrade to yearly billing”

<Note>
  Aylıktan yıllığa yalnızca dashboard üzerinden geçebilirsin. Yıllıktan
  aylığa geçmek için [hi@cursor.com](mailto:hi@cursor.com) ile iletişime geç.
</Note>

---

← Previous: [Kurumsal Ayarlar](./kurumsal-ayarlar.md) | [Index](./index.md) | Next: [SCIM](./scim.md) →