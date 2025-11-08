---
title: "Kurumsal Ayarlar"
source: "https://docs.cursor.com/tr/account/teams/enterprise-settings"
language: "tr"
language_name: "Turkish"
---

# Kurumsal Ayarlar
Source: https://docs.cursor.com/tr/account/teams/enterprise-settings

Kuruluşun için Cursor ayarlarını merkezi olarak yönet

<div id="enterprise-settings">
  # Kurumsal ayarlar
</div>

Cursor’ın belirli özelliklerini cihaz yönetimi çözümleriyle merkezi olarak yöneterek kuruluşunun ihtiyaçlarını karşıladığından emin olabilirsin. Bir Cursor ilkesi belirlediğinde, bu değeri kullanıcıların cihazlarındaki ilgili Cursor ayarının yerini alır.

Ayarlar düzenleyicisi, 'Extensions: Allowed' ayarının kuruluş tarafından yönetildiğini gösteriyor.

Cursor şu anda aşağıdaki yönetici kontrolündeki özellikleri yönetmek için ilkeler sunar:

| Policy            | Description                                                                                                                                             | Cursor setting           | Available since |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------ | --------------- |
| AllowedExtensions | Hangi uzantıların kurulabileceğini kontrol eder.                                                                                                        | extensions.allowed       | 1.2             |
| AllowedTeamId     | Hangi takım kimliklerinin (ID) giriş yapmasına izin verildiğini kontrol eder. Yetkisiz takım kimliklerine sahip kullanıcıların oturumu zorla kapatılır. | cursorAuth.allowedTeamId | 1.3             |

<div id="configure-allowed-extensions">
  ## İzin verilen uzantıları yapılandır
</div>

`extensions.allowed` Cursor ayarı, hangi uzantıların kurulabileceğini kontrol eder. Bu ayar, anahtarların yayıncı adları, değerlerin ise o yayıncıdan gelen uzantıların izinli olup olmadığını belirten boolean olduğu bir JSON nesnesi kabul eder.

Örneğin, `extensions.allowed` değerini `{"anysphere": true, "github": true}` olarak ayarlamak Anysphere ve GitHub yayıncılarından uzantılara izin verirken, `{"anysphere": false}` olarak ayarlamak Anysphere uzantılarını engeller.

Kuruluşun için izin verilen uzantıları merkezi olarak yönetmek istiyorsan, cihaz yönetimi çözümünü kullanarak `AllowedExtensions` ilkesini yapılandır. Bu ilke, kullanıcıların cihazlarındaki `extensions.allowed` ayarının üzerine yazar. Bu ilkenin değeri, izin verilen yayıncıları tanımlayan bir JSON dizesidir.

Cursor’daki uzantılar hakkında daha fazla bilgi edinmek istiyorsan, uzantılar dokümantasyonuna göz at.

<div id="configure-allowed-team-ids">
  ## İzin verilen takım ID’lerini yapılandır
</div>

`cursorAuth.allowedTeamId` Cursor ayarı, Cursor’a hangi takım ID’leriyle giriş yapılabileceğini kontrol eder. Bu ayar, erişim yetkisi olan takım ID’lerinin virgülle ayrılmış bir listesini kabul eder.

Örneğin, `cursorAuth.allowedTeamId` değerini `"1,3,7"` olarak ayarlamak, bu belirli takım ID’lerindeki kullanıcıların giriş yapmasına izin verir.

Bir kullanıcı, izin verilen listede olmayan bir takım ID’siyle giriş yapmaya çalıştığında:

* Oturumu anında zorla kapatılır
* Bir hata mesajı gösterilir
* Uygulama, geçerli bir takım ID’si kullanılana kadar daha fazla kimlik doğrulama denemesini engeller

Kuruluşun için izin verilen takım ID’lerini merkezi olarak yönetmek istiyorsan, cihaz yönetimi çözümünü kullanarak `AllowedTeamId` ilkesini yapılandır. Bu ilke, kullanıcıların cihazlarındaki `cursorAuth.allowedTeamId` ayarını geçersiz kılar. Bu ilkenin değeri, yetkilendirilmiş takım ID’lerinin virgülle ayrılmış listesini içeren bir string’dir.

<div id="group-policy-on-windows">
  ## Windows'ta Grup İlkesi
</div>

Cursor, Windows Kayıt Defteri tabanlı Grup İlkesi'ni (Group Policy) destekler. İlke tanımları yüklendiğinde, yöneticiler ilke değerlerini yönetmek için Yerel Grup İlkesi Düzenleyicisi'ni kullanabilir.

Bir ilke eklemek için:

1. `AppData\Local\Programs\cursor\policies` konumundan ADMX ve ADML ilke dosyalarını kopyala.
2. ADMX dosyasını `C:\Windows\PolicyDefinitions` dizinine, ADML dosyasını ise `C:\Windows\PolicyDefinitions\<your-locale>\` dizinine yapıştır.
3. Yerel Grup İlkesi Düzenleyicisi'ni yeniden başlat.
4. Uygun ilke değerlerini ayarla (ör. `AllowedExtensions` ilkesi için `{"anysphere": true, "github": true}`) Yerel Grup İlkesi Düzenleyicisi içinde.

İlkeler hem Bilgisayar düzeyinde hem de Kullanıcı düzeyinde ayarlanabilir. İkisi de ayarlandıysa, Bilgisayar düzeyi önceliklidir. Bir ilke değeri ayarlandığında, bu değer herhangi bir düzeyde (varsayılan, kullanıcı, çalışma alanı vb.) yapılandırılmış Cursor ayarını geçersiz kılar.

## macOS'ta yapılandırma profilleri

Yapılandırma profilleri, macOS cihazlarındaki ayarları yönetir. Profil, mevcut ilkelere karşılık gelen anahtar/değer çiftlerini içeren bir XML dosyasıdır. Bu profiller, Mobile Device Management (MDM) çözümleriyle dağıtılabilir veya manuel olarak yüklenebilir.

<Accordion title="Örnek .mobileconfig dosyası">
  macOS için bir `.mobileconfig` dosyası örneği aşağıda gösterilmiştir:

  ```
  <?xml version="1.0" encoding="UTF-8"?>
  <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
  <plist version="1.0">
  	<dict>
  		<key>PayloadContent</key>
  		<array>
  			<dict>
  				<key>PayloadDisplayName</key>
  				<string>Cursor</string>
  				<key>PayloadIdentifier</key>
  				<string>com.todesktop.230313mzl4w4u92.J6B5723A-6539-4F31-8A4E-3CC96E51F48C</string>
  				<key>PayloadType</key>
  				<string>com.todesktop.230313mzl4w4u92</string>
  				<key>PayloadUUID</key>
  				<string>J6B5723A-6539-4F31-8A4E-3CC96E51F48C</string>
  				<key>PayloadVersion</key>
  				<integer>1</integer>
  				<key>AllowedExtensions</key>
  				<string>{"anysphere":true}</string>
  				<key>AllowedTeamId</key>
  				<string>1,2</string>
  			</dict>
  		</array>
  		<key>PayloadDescription</key>
  		<string>This profile manages Cursor.</string>
  		<key>PayloadDisplayName</key>
  		<string>Cursor</string>
  		<key>PayloadIdentifier</key>
  		<string>com.todesktop.230313mzl4w4u92</string>
  		<key>PayloadOrganization</key>
  		<string>Anysphere</string>
  		<key>PayloadType</key>
  		<string>Configuration</string>
  		<key>PayloadUUID</key>
  		<string>F2C1A7B3-9D4E-4B2C-8E1F-7A6C5D4B3E2F</string>
  		<key>PayloadVersion</key>
  		<integer>1</integer>
  		<key>TargetDeviceType</key>
  		<integer>5</integer>
  	</dict>
  </plist>
  ```
</Accordion>

<div id="string-policies">
  ### Dize ilkeleri
</div>

Aşağıdaki örnek, `AllowedExtensions` ilkesinin yapılandırılmasını gösterir. Örnek dosyada ilke değeri başlangıçta boştur (hiçbir uzantıya izin verilmez).

```
<key>AllowedExtensions</key>
<string></string>
```

İlkeni tanımlayan uygun JSON dizgesini `<string>` etiketlerinin arasına ekle.

```
<key>AllowedExtensions</key>
<string>{"anysphere": true, "github": true}</string>
```

`AllowedTeamId` policy'si için takım kimliklerinin (ID) virgülle ayrılmış listesini ekle:

```
<key>AllowedTeamId</key>
<string>1,3,7</string>
```

**Önemli:** Sağlanan `.mobileconfig` dosyası, Cursor’ın o sürümünde bulunan **tüm** ilkeleri uygular. Gerekmeyen ilkeleri sil.

Örnek `.mobileconfig` içindeki bir ilkeyi düzenlemez veya kaldırmazsan, o ilke varsayılan (kısıtlayıcı) değeriyle zorunlu kılınır.

Bir yapılandırma profilini elle yüklemek için Finder’da `.mobileconfig` profilini çift tıkla ve ardından Sistem Ayarları’nda **Genel** > **Aygıt Yönetimi** altında etkinleştir. Profili Sistem Ayarları’ndan kaldırmak, ilke(leri) Cursor’dan da kaldırır.

Yapılandırma profilleri hakkında daha fazla bilgi için Apple’ın belgelerine bak.

<div id="additional-policies">
  ## Ek politikalar
</div>

Amaç, mevcut Cursor ayarlarını politikalar olarak öne çıkarmak ve adlandırma ile davranışın tutarlı olması için bu ayarları yakından izlemek. Daha fazla politika eklenmesine yönelik taleplerin varsa, lütfen Cursor’un GitHub deposunda bir issue aç. Ekip, söz konusu davranış için zaten karşılık gelen bir ayar olup olmadığını ya da istenen davranışı kontrol etmek üzere yeni bir ayar oluşturulması gerekip gerekmediğini belirleyecek.

<div id="frequently-asked-questions">
  ## Sık sorulan sorular
</div>

<div id="does-cursor-support-configuration-profiles-on-linux">
  ### Cursor, Linux'ta yapılandırma profillerini destekliyor mu?
</div>

Linux desteği yol haritasında yok. Linux'ta yapılandırma profilleriyle ilgileniyorsan, Cursor GitHub deposunda bir issue açıp senaryonla ilgili ayrıntıları paylaş.

---

← Previous: [Kontrol Paneli](./kontrol-paneli.md) | [Index](./index.md) | Next: [Üyeler ve Roller](./yeler-ve-roller.md) →