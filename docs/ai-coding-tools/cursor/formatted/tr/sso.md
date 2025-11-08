---
title: "SSO"
source: "https://docs.cursor.com/tr/account/teams/sso"
language: "tr"
language_name: "Turkish"
---

# SSO
Source: https://docs.cursor.com/tr/account/teams/sso

Ekibin için tek oturum açmayı ayarla

<div id="overview">
  ## Genel Bakış
</div>

SAML 2.0 SSO, Business planlarında ek ücret olmadan sunulur. Ayrı Cursor hesaplarına gerek kalmadan ekip üyelerini kimlik doğrulamak için mevcut kimlik sağlayıcını (IdP) kullan.

<Frame>
  <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=76608c26daf1f9ab2bbc2c4ccb156c0e" style={{ padding: 32, backgroundColor: "#0c0c0c" }} data-og-width="802" width="802" data-og-height="440" height="440" data-path="images/account/sso-settings.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=334dc1fc107338d19ec7b0052e7ea0e4 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=543b3d868c19960a5fb4c526d9895bd3 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=a06655178ba10f6a72919e9f7d598191 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=e280fc911306fe8d3b8e90b7221b0c11 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=ffd8f2c0168e2ac4f95431062b226021 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=1c17e4eac666b663d676ce874f1c4ba5 2500w" />
</Frame>

<div id="prerequisites">
  ## Önkoşullar
</div>

* Cursor Team planı
* Kimlik sağlayıcında (örn. Okta) yönetici erişimi
* Cursor organizasyonunda yönetici erişimi

<div id="configuration-steps">
  ## Yapılandırma Adımları
</div>

<Steps>
  <Step title="Cursor hesabında oturum aç">
    Yönetici hesabınla [cursor.com/dashboard?tab=settings](https://www.cursor.com/dashboard?tab=settings) adresine git.
  </Step>

  <Step title="SSO yapılandırmasını bul">
    "Single Sign-On (SSO)" bölümünü bul ve genişlet.
  </Step>

  <Step title="Kurulumu başlat">
    SSO kurulumunu başlatmak için "SSO Provider Connection settings" düğmesine tıkla ve sihirbazı izle.
  </Step>

  <Step title="Kimlik sağlayıcını yapılandır">
    Kimlik sağlayıcında (örn. Okta):

    * Yeni bir SAML uygulaması oluştur
    * SAML ayarlarını Cursor’ın bilgilerini kullanarak yapılandır
    * Just-in-Time (JIT) sağlama (provisioning) ayarını yap
  </Step>

  <Step title="Etki alanını doğrula">
    Cursor’da kullanıcılarının etki alanını doğrulamak için "Domain verification settings" düğmesine tıkla.
  </Step>
</Steps>

<div id="identity-provider-setup-guides">
  ### Kimlik Sağlayıcı Kurulum Kılavuzları
</div>

Sağlayıcıya özel kurulum talimatları için:

<Card title="Kimlik Sağlayıcı Kılavuzları" icon="book" href="https://workos.com/docs/integrations">
  Okta, Azure AD, Google Workspace ve daha fazlası için kurulum talimatları.
</Card>

<div id="additional-settings">
  ## Ek Ayarlar
</div>

* SSO zorlamasını admin panosundan yönet
* Yeni kullanıcılar SSO ile giriş yaptığında otomatik kaydolur
* Kullanıcı yönetimini kimlik sağlayıcın üzerinden yap

<div id="troubleshooting">
  ## Sorun Giderme
</div>

Sorun yaşarsan:

* Alan adının Cursor’da doğrulandığını kontrol et
* SAML özniteliklerinin doğru eşlendiğinden emin ol
* Yönetici panelinde SSO’nun etkin olduğunu kontrol et
* Kimlik sağlayıcıyla Cursor’daki ad ve soyadların eşleştiğinden emin ol
* Yukarıdaki sağlayıcıya özel kılavuzları gözden geçir
* Sorun devam ederse [hi@cursor.com](mailto:hi@cursor.com) adresine yaz

---

← Previous: [Başlarken](./balarken.md) | [Index](./index.md) | Next: [Güncelleme Erişimi](./gncelleme-eriimi.md) →