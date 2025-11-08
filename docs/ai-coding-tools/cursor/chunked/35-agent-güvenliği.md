# Agent Güvenliği

**Navigation:** [← Previous](./34-модели.md) | [Index](./index.md) | [Next →](./36-kod-incelemesi.md)

---

# Agent Güvenliği
Source: https://docs.cursor.com/tr/account/agent-security

Cursor Agent kullanımı için güvenlik değerlendirmeleri

Prompt injection, AI halüsinasyonları ve diğer sorunlar, yapay zekanın beklenmedik ve potansiyel olarak kötü niyetli davranmasına yol açabilir. Prompt injection sorununu daha temel bir düzeyde çözmek için çalışmaya devam ederken, Cursor ürünlerindeki birincil korumamız, bir agent’ın yapabileceklerine konulan koruma sınırlarıdır; buna varsayılan olarak hassas işlemler için manuel onay gerektirilmesi de dahildir. Bu belgenin amacı, bu koruma sınırlarını ve kullanıcıların bunlardan ne bekleyebileceğini açıklamaktır.

Aşağıda yer alan tüm kontrol ve davranışlar varsayılan ve önerilen ayarlarımızdır.

<div id="first-party-tool-calls">
  ## Birinci taraf araç çağrıları
</div>

Cursor, ajanın kullanıcılarımıza kod yazmada yardımcı olmasını sağlayan yerleşik araçlarla birlikte gelir. Bunlara dosya okuma, düzenleme, terminal komutları çalıştırma, dokümantasyon için web’de arama ve diğerleri dahildir.

Okuma araçları onay gerektirmez (ör. dosya okuma, kod genelinde arama). Ajanın belirli dosyalara hiç erişmesini engellemek için [.cursorignore](/tr/context/ignore-files) kullanabilirsin; bunun dışında okumalar genellikle onaysız olarak serbesttir. Hassas verilerin dışa sızması riskini taşıyan eylemler içinse açık onay isteriz.

Geçerli çalışma alanındaki dosyaları değiştirmek, bazı istisnalar dışında açık onay gerektirmez. Bir ajan dosyalarda değişiklik yaptığında bunlar anında diske kaydedilir. Dosyaların içeriğini istediğin zaman geri alabilmek için Cursor’ı sürüm kontrollü çalışma alanlarında çalıştırmanı öneririz. IDE/CLI yapılandırmamızı değiştiren dosyalarda, örneğin editörün çalışma alanı ayar dosyasında değişiklik yapmadan önce açık onay isteriz. Ancak, dosya değiştiğinde otomatik yeniden yükleme yapan kullanıcılar, ajanın dosyalarda yaptığı değişikliklerin, sen gözden geçiremeden otomatik yürütmeyi tetikleyebileceğinin farkında olmalı.

Ajanlar tarafından önerilen herhangi bir terminal komutu varsayılan olarak onay gerektirir. Ajan çalıştırmadan önce her komutu gözden geçirmeni öneririz. Riski kabul ediyorsan, ajanın tüm komutları onay olmadan çalıştırmasını etkinleştirmeyi seçebilirsin. Cursor’da bir [allowlist](/tr/agent/tools) özelliği sunuyoruz, ancak bunu bir güvenlik kontrolü olarak görmüyoruz. Bazı kullanıcılar belirli komutlara izin vermeyi seçiyor; bu “best-effort” bir sistemdir ve baypas edilebilir. Herhangi bir yapılandırılmış allowlist’i baypas eden “Run Everything” seçeneğini önermiyoruz.

<div id="third-party-tool-calls">
  ## Üçüncü taraf araç çağrıları
</div>

Cursor, [MCP](/tr/context/mcp) üzerinden harici araçları bağlamanı sağlar. Tüm üçüncü taraf MCP bağlantılarının, kullanıcı tarafından açıkça onaylanması gerekir. Bir kullanıcı bir MCP’yi onayladıktan sonra, varsayılan olarak her harici MCP entegrasyonu için Agent Mode’da önerilen her araç çağrısı, çalıştırılmadan önce açıkça onaylanmalıdır.

<div id="network-requests">
  ## Ağ istekleri
</div>

Ağ istekleri, bir saldırgan tarafından veri sızdırmak için kullanılabilir. Şu anda çok sınırlı bir ana makine kümesi (örn. GitHub), açıkça talep edilen bağlantı alma ve seçili sağlayıcılarla web aramasını destekleme dışında, ağ isteği yapan herhangi bir birinci taraf aracı desteklemiyoruz. Keyfi aracının ağ istekleri varsayılan ayarlarla engellenir.

<div id="workspace-trust">
  ## Workspace trust
</div>

Cursor IDE, varsayılan olarak devre dışı olan standart [workspace trust](https://code.visualstudio.com/docs/editing/workspaces/workspace-trust) özelliğini destekliyor. Workspace trust, yeni bir workspace açtığında normal ya da kısıtlı mod arasında seçim yapman için bir bildirim gösterir. Kısıtlı mod, AI ve kullanıcılarımızın Cursor’da genelde kullandığı diğer özellikleri çalışmaz hâle getirir. Güvenmediğin repolarla çalışırken basit bir metin düzenleyici gibi başka araçları kullanmanı öneriyoruz.

Workspace trust, şu adımları izleyerek kullanıcı ayarlarında etkinleştirilebilir:

1. user settings.json dosyanı aç
2. Şu yapılandırmayı ekle:
   ```json  theme={null}
   "security.workspace.trust.enabled": true
   ```

Bu ayar, Mobile Device Management (MDM) çözümleri aracılığıyla kurum genelinde de zorunlu kılınabilir.

<div id="responsible-disclosure">
  ## Sorumlu açıklama
</div>

Cursor’da bir güvenlik açığı bulduğunu düşünüyorsan, GitHub Security sayfamızdaki kılavuzu takip et ve raporunu oradan gönder. GitHub’ı kullanamıyorsan, bize [security@cursor.com](mailto:security@cursor.com) adresinden de ulaşabilirsin.

Güvenlik açığı raporlarını 5 iş günü içinde aldığımızı teyit etmeyi ve onları mümkün olan en kısa sürede ele almayı taahhüt ediyoruz. Sonuçları GitHub Security sayfamızda güvenlik duyuruları olarak yayımlayacağız. Kritik olayları hem GitHub Security sayfasında hem de tüm kullanıcılara e-posta yoluyla duyuracağız.



# Faturalandırma
Source: https://docs.cursor.com/tr/account/billing

Cursor aboneliklerini, geri ödemeleri ve faturaları yönetme

<div id="how-do-i-access-billing-settings">
  ### Faturalandırma ayarlarına nasıl erişirim?
</div>

[Dashboard](https://cursor.com/dashboard) üzerinden dashboard’ında “Billing”e tıklayarak faturalandırma portalına eriş. Bu, tüm faturalandırma işlemleri için güvenli bir portal açar.

<div id="what-are-cursors-billing-cycles">
  ### Cursor’ın faturalandırma döngüleri nedir?
</div>

Faturalandırma döngüleri, aboneliğinin başladığı tarihten itibaren aylık veya yıllık olarak işler. Teams hesapları, yeni üyeler için orantılı (pro-rata) faturalandırmayla koltuk başına ücretlendirilir.

<div id="how-do-seats-work-for-teams-accounts">
  ### Teams hesaplarında koltuklar nasıl çalışır?
</div>

Teams hesapları koltuk başına ücretlendirir (her takım üyesi için bir koltuk). Üyeleri döngünün ortasında eklediğinde, yalnızca kalan süreleri için ücretlendirilirsin. Bir üye kredi kullandıysa ve kaldırıldıysa, koltuğu faturalandırma döngüsü bitene kadar dolu sayılır — orantılı geri ödeme yapılmaz. Takım yöneticileri koltukları dashboard üzerinden yönetebilir.

<div id="can-i-switch-between-monthly-and-annual-billing">
  ### Aylık ve yıllık faturalandırma arasında geçiş yapabilir miyim?
</div>

Evet! İşte nasıl:

**Pro plan**

1. Cursor [dashboard](https://cursor.com/dashboard)’a git
2. Sol kenar çubuğundan “Billing and Invoices”a tıklayarak faturalandırma sayfasına git
3. “Manage subscription”a tıkla
4. “Update subscription”a tıkla
5. “Yearly” veya “Monthly”yi seç, ardından “Continue”a tıkla

**Teams plan**

1. Cursor [dashboard](https://cursor.com/dashboard)’a git
2. Sol kenar çubuğundan “Billing and Invoices”a tıklayarak faturalandırma sayfasına git
3. Yıllık faturalandırmaya geçmek için “Upgrade Now” düğmesine tıkla

<Note>
  Yalnızca aylıktan yıllığa faturalandırmaya self-serve geçiş yapabilirsin. Yıllıktan aylığa geçmek için bizimle
  [hi@cursor.com](mailto:hi@cursor.com) üzerinden iletişime geç.
</Note>

<div id="where-can-i-find-my-invoices">
  ### Faturalarımı nerede bulabilirim?
</div>

Tüm faturalandırma geçmişini faturalandırma portalında bulabilirsin. Mevcut ve geçmiş faturaları görüntüleyip indirebilirsin.

<div id="can-i-get-invoices-automatically-emailed-to-me">
  ### Faturalar otomatik olarak e-postayla gönderilebilir mi?
</div>

Faturalar faturalandırma portalından manuel olarak indirilir. Otomatik fatura e-postaları üzerinde çalışıyoruz. Kullanıma sunulduğunda katılabileceksin.

<div id="how-do-i-update-my-billing-information">
  ### Faturalandırma bilgilerimi nasıl güncellerim?
</div>

Ödeme yöntemi, şirket adı, adres ve vergi bilgilerini faturalandırma portalı üzerinden güncelle. Güvenli işlemler için Stripe kullanıyoruz. Değişiklikler yalnızca gelecekteki faturaları etkiler; geçmiş faturaları değiştiremeyiz.

<div id="how-do-i-cancel-my-subscription">
  ### Aboneliğimi nasıl iptal ederim?
</div>

Billing and Invoices sayfasında “Manage Subscription”a, ardından “Cancel subscription” düğmesine tıklayarak aboneliğini iptal et. Erişimin, mevcut faturalandırma dönemin sona erene kadar devam eder.

<div id="im-having-other-billing-issues-how-can-i-get-help">
  ### Başka faturalandırma sorunları yaşıyorum. Nasıl yardım alabilirim?
</div>

Burada yer almayan faturalandırma soruları için, hesabına bağlı e-postadan [hi@cursor.com](mailto:hi@cursor.com) adresine yaz. Lütfen hesap bilgilerini ve konunu ekle.



# Fiyatlandırma
Source: https://docs.cursor.com/tr/account/pricing

Cursor’ın planları ve fiyatları

Cursor’ı ücretsiz deneyebilir ya da bireysel veya ekip planı satın alabilirsin.

<div id="individual">
  ## Bireysel
</div>

Tüm bireysel planlar şunları içerir:

* Sınırsız tab tamamlama
* Tüm modellerde genişletilmiş agent kullanım limitleri
* Bugbot’a erişim
* Background Agents’e erişim

Her plan, model çıkarımı [API fiyatlarına](/tr/models#model-pricing) göre ücretlendirilir:

* Pro, \$20 API agent kullanımı + ek bonus kullanım içerir
* Pro Plus, \$70 API agent kullanımı + ek bonus kullanım içerir
* Ultra, \$400 API agent kullanımı + ek bonus kullanım içerir

Garantili dahil kullanımın ötesinde ek bonus kapasite sağlamak için çok çalışıyoruz. Farklı modellerin API maliyetleri değiştiğinden, model seçimin hem token çıktısını hem de dahil kullanımının ne kadar hızlı tükeneceğini etkiler. Kullanımını ve token dökümlerini [panelinde](https://cursor.com/dashboard?tab=usage) görüntüleyebilirsin. Limit bildirimleri düzenli olarak editörde gösterilir.

<img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/usage-limits.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=c42b8ad6347f6fe9d075647dfece934c" alt="Kullanım limitleri" style={{ borderRadius: 16 }} data-og-width="666" width="666" data-og-height="394" height="394" data-path="images/account/usage-limits.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/usage-limits.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=e1ca3b5ab64a6ba6f3ad7d75b1ee72e2 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/usage-limits.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=d39dc254e7d059ac24310f26ea47dd5d 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/usage-limits.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=153472f14b4c10ec9a096b7a9db59888 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/usage-limits.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=0dc8b0cdb5c0677e45c1a082d0002880 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/usage-limits.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=cf4ac9875f5e587d16d4c6f1e7fdc057 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/usage-limits.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=13f21676cda8e4c2973bc3371892f4aa 2500w" />

<div id="how-much-usage-do-i-need">
  ### Ne kadar kullanıma ihtiyacım var?
</div>

Kullanım verilerimize göre aşağıdaki kullanım düzeylerini bekleyebilirsin:

* **Günlük Tab kullanıcıları**: Her zaman \$20 içinde kalır
* **Sınırlı Agent kullanıcıları**: Çoğu zaman dahilindeki \$20 içinde kalır
* **Günlük Agent kullanıcıları**: Genelde toplam kullanım $60–$100/ay
* **Power kullanıcıları (birden çok agent/otomasyon)**: Sıklıkla toplam kullanım \$200+/ay

Kullanım verilerimize göre, limitler bir “medyan kullanıcı” için kabaca şunlara denktir:

* Pro: \~225 Sonnet 4 isteği, \~550 Gemini isteği veya \~500 GPT 5 isteği
* Pro+: \~675 Sonnet 4 isteği, \~1.650 Gemini isteği veya \~1.500 GPT 5 isteği
* Ultra: \~4.500 Sonnet 4 isteği, \~11.000 Gemini isteği veya \~10.000 GPT 5 isteği

<div id="what-happens-when-i-reach-my-limit">
  ### Sınırıma ulaştığımda ne olur?
</div>

Dahil aylık kullanımını aştığında, editörde bilgilendirileceksin ve şunları tercih edebilirsin:

* **İsteğe bağlı kullanım ekle**: Kullanım kadar öde faturalandırmayla aynı API oranlarında Cursor’ı kullanmaya devam et
* **Planını yükselt**: Daha fazla dahil kullanım için daha yüksek bir katmana geç

İsteğe bağlı kullanım, dahil kullanımınla aynı oranlarda aylık olarak faturalandırılır. İsteklerin kalitesi veya hızı asla düşürülmez.

<div id="teams">
  ## Teams
</div>

İki takım planı var: Teams (\$40/kullanıcı/ay) ve Enterprise (Özel).

Teams planları şu ek özellikleri sunar:

* Gizlilik Modu zorlaması
* Kullanım istatistikleriyle Admin Panosu
* Merkezi takım faturalandırması
* SAML/OIDC SSO

Kendi kendine yönetmekten memnun olan herkes için Teams’i öneriyoruz. Öncelikli destek, havuzlu kullanım, faturalandırma, SCIM veya gelişmiş güvenlik kontrollerine ihtiyaç duyanlar için [Enterprise](/tr/contact-sales) öneriyoruz.

[Teams ücretlendirmesi](/tr/account/teams/pricing) hakkında daha fazla bilgi al.

<div id="auto">
  ## Auto
</div>

Auto'yu etkinleştirmek, Cursor’ın mevcut talebe göre en yüksek güvenilirliğe sahip ve o anki göreve en uygun premium modeli seçmesini sağlar. Bu özellik, çıktılarda performans düşüşünü tespit edebilir ve bunu gidermek için modeller arasında otomatik olarak geçiş yapabilir.

<Frame>
  <img src="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/models/model-picker.png?fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=9f039569ed0dc2ad7e02bb1b2e9cea71" data-og-width="2256" width="2256" data-og-height="1248" height="1248" data-path="images/models/model-picker.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/models/model-picker.png?w=280&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=49c6a091945972253eb6e819593e45f0 280w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/models/model-picker.png?w=560&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=f9bddfb2e130789d8d51a3d1a4eeba94 560w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/models/model-picker.png?w=840&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=db7273f399bb5decfed9d1b06f389df4 840w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/models/model-picker.png?w=1100&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=920fe98d4f99b5d7fddd47a14fb45699 1100w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/models/model-picker.png?w=1650&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=3b049686e5826263800b63299f4c19ca 1650w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/models/model-picker.png?w=2500&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=72ddd56b4d3ea9b2efa4001a155566fd 2500w" />
</Frame>

<Note>Auto’nun kalite ve genel performansına ciddi yatırımlar yaptık. 15 Eylül’den sonraki bir sonraki faturalandırma yenilemenden itibaren, Auto aşağıdaki API ücretlendirme oranlarıyla kullanım tüketir.</Note>

* **Girdi + Cache Yazma**: 1M token başına \$1.25
* **Çıktı**: 1M token başına \$6.00
* **Cache Okuma**: 1M token başına \$0.25

Hem editör hem de dashboard, Auto dahil kullanımını gösterir. Bir modeli doğrudan seçmeyi tercih edersen, kullanım o modelin liste API fiyatı üzerinden hesaplanır.

<div id="max-mode">
  ## Max Mode
</div>

Bazı modeller [Max Mode](/tr/models#max-mode) kullanabilir; bu, daha uzun akıl yürütme ve 1M tokene kadar daha büyük bağlam pencereleri sağlar. Çoğu kodlama işi Max Mode gerektirmese de, özellikle büyük dosyalar veya kod tabanlarıyla ilgili daha karmaşık sorgularda faydalı olabilir. Max Mode’u kullanmak daha fazla kullanım tüketecektir. Tüm isteklerini ve token dökümlerini [panelinde](https://cursor.com/dashboard?tab=usage) görebilirsin.

<div id="bugbot">
  ## Bugbot
</div>

Bugbot, Cursor aboneliklerinden ayrı bir üründür ve kendi fiyatlandırma planına sahiptir.

* **Pro** (40\$/ay): Ayda en fazla 200 PR için sınırsız inceleme, Cursor Ask’e sınırsız erişim, hataları düzeltmek için Cursor entegrasyonu ve Bugbot Rules erişimi
* **Teams** (kullanıcı başına 40\$/ay): Tüm PR’ler için sınırsız kod incelemesi, Cursor Ask’e sınırsız erişim, ekip genelinde havuzlanmış kullanım ve gelişmiş kurallar ile ayarlar
* **Enterprise** (Özel): Teams’in sunduklarının tümüne ek olarak gelişmiş analiz ve raporlama, öncelikli destek ve hesap yönetimi

[Bugbot fiyatlandırması](https://cursor.com/bugbot#pricing) hakkında daha fazla bilgi edin.

<div id="background-agent">
  ## Arka Plan Agenti
</div>

Arka Plan Agentleri, seçilen [model](/tr/models) için API fiyatlandırmasına göre ücretlendirilir. İlk kez kullanmaya başladığında Arka Plan Agentleri için bir harcama limiti belirlemen istenecek.

<Info>
  Arka Plan Agentleri için Sanal Makine (VM) hesaplama maliyeti gelecekte fiyatlandırılacak.
</Info>



# Admin API
Source: https://docs.cursor.com/tr/account/teams/admin-api

API aracılığıyla ekip metriklerine, kullanım verilerine ve harcama bilgilerine eriş

Admin API, üye bilgileri, kullanım metrikleri ve harcama detayları dahil olmak üzere ekibinin verilerine programatik olarak erişmeni sağlar. Özel panolar, izleme araçları oluştur ya da mevcut iş akışlarınla entegre et.

<Note>
  API ilk sürümünde. Yetenekleri geri bildirimlere göre genişletiyoruz — hangi endpoint’lere ihtiyacın olduğunu bize söyle!
</Note>

<div id="authentication">
  ## Kimlik doğrulama
</div>

Tüm API istekleri bir API anahtarıyla kimlik doğrulamayı gerektirir. API anahtarlarını yalnızca ekip yöneticileri oluşturabilir ve yönetebilir.

API anahtarları kuruluşa bağlıdır, tüm yöneticiler tarafından görüntülenebilir ve ilk oluşturanın hesap durumundan etkilenmez.

<div id="creating-an-api-key">
  ### Bir API Anahtarı Oluşturma
</div>

1. **cursor.com/dashboard** → **Settings** sekmesi → **Cursor Admin API Keys** bölümüne git
2. **Create New API Key**’e tıkla
3. Anahtarına açıklayıcı bir ad ver (ör. “Usage Dashboard Integration”)
4. Oluşturulan anahtarı hemen kopyala — bir daha gösterilmeyecek

Biçim: `key_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`

<div id="using-your-api-key">
  ### API Anahtarını Kullanma
</div>

API anahtarını temel kimlik doğrulamada kullanıcı adı olarak kullan:

**Temel kimlik doğrulamayla curl kullanma:**

```bash  theme={null}
curl https://api.cursor.com/{route} -u API_KEY:
```

**Ya da Authorization başlığını doğrudan ayarla:**

```bash  theme={null}
Authorization: Basic {base64_encode('API_KEY:')}
```

<div id="base-url">
  ## Temel URL
</div>

Tüm API uç noktaları şu adresi kullanır:

```
https://api.cursor.com
```

<div id="endpoints">
  ## Uç Noktalar
</div>

<div id="get-team-members">
  ### Ekip Üyelerini Getir
</div>

Tüm ekip üyelerini ve ayrıntılarını al.

```
GET /teams/members
```

#### Yanıt

Ekip üyesi nesnelerinden oluşan bir dizi döndürür:

```typescript  theme={null}
{
  teamMembers: {
    name: string;
    email: string;
    role: 'owner' | 'member' | 'free-owner';
  }[];
}
```

#### Örnek Yanıt

```json  theme={null}
{
  "teamMembers": [
    {
      "name": "Alex",
      "email": "developer@company.com",
      "role": "üye"
    },
    {
      "name": "Sam",
      "email": "admin@company.com",
      "role": "sahip"
    }
  ]
}

```

#### Örnek İstek

```bash  theme={null}
curl -X GET https://api.cursor.com/teams/members \
  -u API_ANAHTARIN:
```

<div id="get-daily-usage-data">
  ### Günlük Kullanım Verilerini Al
</div>

Belirli bir tarih aralığında ekibin için ayrıntılı günlük kullanım metriklerini getir. Kod düzenlemeleri, yapay zeka yardımı kullanımı ve kabul oranları hakkında içgörüler sunar.

```
POST /teams/daily-usage-data
```

#### İstek Gövdesi

<div className="full-width-table">
  | Parametre   | Tür    | Gerekli | Açıklama                                    |
  | :---------- | :----- | :------ | :------------------------------------------ |
  | `startDate` | number | Evet    | Epoch milisaniye cinsinden başlangıç tarihi |
  | `endDate`   | number | Evet    | Epoch milisaniye cinsinden bitiş tarihi     |
</div>

<Note>
  Tarih aralığı 90 günü geçemez. Daha uzun dönemler için birden fazla istek gönder.
</Note>

#### Yanıt

```typescript  theme={null}
{
  data: {
    date: number;
    isActive: boolean;
    totalLinesAdded: number;
    totalLinesDeleted: number;
    acceptedLinesAdded: number;
    acceptedLinesDeleted: number;
    totalApplies: number;
    totalAccepts: number;
    totalRejects: number;
    totalTabsShown: number;
    totalTabsAccepted: number;
    composerRequests: number;
    chatRequests: number;
    agentRequests: number;
    cmdkUsages: number;
    subscriptionIncludedReqs: number;
    apiKeyReqs: number;
    usageBasedReqs: number;
    bugbotUsages: number;
    mostUsedModel: string;
    applyMostUsedExtension?: string;
    tabMostUsedExtension?: string;
    clientVersion?: string;
    email?: string;
  }[];
  period: {
    startDate: number;
    endDate: number;
  };
}
```

<div id="response-fields">
  #### Yanıt Alanları
</div>

<div className="full-width-table">
  | Field                      | Description                                 |
  | :------------------------- | :------------------------------------------ |
  | `date`                     | Epoch milisaniye cinsinden tarih            |
  | `isActive`                 | Kullanıcı bu gün aktif mi                   |
  | `totalLinesAdded`          | Eklenen kod satırı                          |
  | `totalLinesDeleted`        | Silinen kod satırı                          |
  | `acceptedLinesAdded`       | Kabul edilen AI önerilerinden eklenen satır |
  | `acceptedLinesDeleted`     | Kabul edilen AI önerilerinden silinen satır |
  | `totalApplies`             | Apply işlemleri                             |
  | `totalAccepts`             | Kabul edilen öneriler                       |
  | `totalRejects`             | Reddedilen öneriler                         |
  | `totalTabsShown`           | Gösterilen sekme tamamlama sayısı           |
  | `totalTabsAccepted`        | Kabul edilen sekme tamamlama sayısı         |
  | `composerRequests`         | Composer istekleri                          |
  | `chatRequests`             | Sohbet istekleri                            |
  | `agentRequests`            | Agent istekleri                             |
  | `cmdkUsages`               | Komut paleti (Cmd+K) kullanımı              |
  | `subscriptionIncludedReqs` | Abonelik kapsamındaki istekler              |
  | `apiKeyReqs`               | API anahtarı istekleri                      |
  | `usageBasedReqs`           | Kullanım başına ödeme istekleri             |
  | `bugbotUsages`             | Hata bulma kullanımları                     |
  | `mostUsedModel`            | En sık kullanılan yapay zeka modeli         |
  | `applyMostUsedExtension`   | Apply için en çok kullanılan dosya uzantısı |
  | `tabMostUsedExtension`     | Sekme için en çok kullanılan dosya uzantısı |
  | `clientVersion`            | Cursor sürümü                               |
  | `email`                    | Kullanıcı e-postası                         |
</div>

#### Örnek Yanıt

```json  theme={null}
{
  "data": [
    {
      "date": 1710720000000,
      "isActive": true,
      "totalLinesAdded": 1543,
      "totalLinesDeleted": 892,
      "acceptedLinesAdded": 1102,
      "acceptedLinesDeleted": 645,
      "totalApplies": 87,
      "totalAccepts": 73,
      "totalRejects": 14,
      "totalTabsShown": 342,
      "totalTabsAccepted": 289,
      "composerRequests": 45,
      "chatRequests": 128,
      "agentRequests": 12,
      "cmdkUsages": 67,
      "subscriptionIncludedReqs": 180,
      "apiKeyReqs": 0,
      "usageBasedReqs": 5,
      "bugbotUsages": 3,
      "enCokKullanilanModel": "gpt-4",
      "applyEnCokKullanilanUzanti": ".tsx",
      "tabEnCokKullanilanUzanti": ".ts",
      "istemciSurumu": "0.25.1",
      "ePosta": "developer@company.com"
    },
    {
      "date": 1710806400000,
      "isActive": true,
      "totalLinesAdded": 2104,
      "totalLinesDeleted": 1203,
      "acceptedLinesAdded": 1876,
      "acceptedLinesDeleted": 987,
      "totalApplies": 102,
      "totalAccepts": 91,
      "totalRejects": 11,
      "totalTabsShown": 456,
      "totalTabsAccepted": 398,
      "composerRequests": 67,
      "chatRequests": 156,
      "agentRequests": 23,
      "cmdkUsages": 89,
      "subscriptionIncludedReqs": 320,
      "apiKeyReqs": 15,
      "usageBasedReqs": 0,
      "bugbotUsages": 5,
      "enCokKullanilanModel": "claude-3-opus",
      "applyEnCokKullanilanUzanti": ".py",
      "tabEnCokKullanilanUzanti": ".py",
      "istemciSurumu": "0.25.1",
      "ePosta": "developer@company.com"
    }
  ],
  "period": {
    "startDate": 1710720000000,
    "endDate": 1710892800000
  }
}
```

#### Örnek İstek

```bash  theme={null}
curl -X POST https://api.cursor.com/teams/daily-usage-data \
  -u API_ANAHTARIN: \
  -H "Content-Type: application/json" \
  -d '{
    "startDate": 1710720000000,
    "endDate": 1710892800000
  }'
```

<div id="get-spending-data">
  ### Harcama Verilerini Al
</div>

Geçerli takvim ayı için arama, sıralama ve sayfalama ile harcama bilgilerini getir.

```
POST /teams/spend
```

#### İstek Gövdesi

<div className="full-width-table">
  | Parametre       | Tür    | Gerekli | Açıklama                                                       |
  | :-------------- | :----- | :------ | :------------------------------------------------------------- |
  | `searchTerm`    | string | Hayır   | Kullanıcı adları ve e-postalarda ara                           |
  | `sortBy`        | string | Hayır   | Şuna göre sırala: `amount`, `date`, `user`. Varsayılan: `date` |
  | `sortDirection` | string | Hayır   | Sıralama yönü: `asc`, `desc`. Varsayılan: `desc`               |
  | `page`          | number | Hayır   | Sayfa numarası (1’den başlayarak). Varsayılan: `1`             |
  | `pageSize`      | number | Hayır   | Sayfa başına sonuç sayısı                                      |
</div>

#### Yanıt

```typescript  theme={null}
{
  teamMemberSpend: {
    spendCents: number;
    fastPremiumRequests: number;
    name: string;
    email: string;
    role: 'owner' | 'member' | 'free-owner';
    hardLimitOverrideDollars: number;
  }[];
  subscriptionCycleStart: number;
  totalMembers: number;
  totalPages: number;
}
```

<div id="response-fields">
  #### Yanıt Alanları
</div>

<div className="full-width-table">
  | Alan                       | Açıklama                                       |
  | :------------------------- | :--------------------------------------------- |
  | `spendCents`               | Toplam harcama (sent)                          |
  | `fastPremiumRequests`      | Hızlı premium model istekleri                  |
  | `name`                     | Üye adı                                        |
  | `email`                    | Üye e-postası                                  |
  | `role`                     | Ekipteki rol                                   |
  | `hardLimitOverrideDollars` | Özel harcama sınırı geçersiz kılma             |
  | `subscriptionCycleStart`   | Abonelik döngüsü başlangıcı (epoch milisaniye) |
  | `totalMembers`             | Toplam ekip üyesi sayısı                       |
  | `totalPages`               | Toplam sayfa sayısı                            |
</div>

#### Örnek Yanıt

```json  theme={null}
{
  "teamMemberSpend": [
    {
      "spendCents": 2450,
      "fastPremiumRequests": 1250,
      "name": "Alex",
      "email": "developer@company.com",
      "role": "member",
      "hardLimitOverrideDollars": 100
    },
    {
      "spendCents": 1875,
      "fastPremiumRequests": 980,
      "name": "Sam",
      "email": "admin@company.com",
      "role": "owner",
      "hardLimitOverrideDollars": 0
    },
  ],
  "subscriptionCycleStart": 1708992000000,
  "totalMembers": 15,
  "totalPages": 1
}
```

<div id="example-requests">
  #### Örnek istekler
</div>

**Temel harcama verileri:**

```bash  theme={null}
curl -X POST https://api.cursor.com/teams/spend \
  -u API_ANAHTARIN: \
  -H "İçerik Türü: application/json" \
  -d '{}'
```

**Belirli bir kullanıcıyı sayfalamayla ara:**

```bash  theme={null}
curl -X POST https://api.cursor.com/teams/spend \
  -u API_ANAHTARIN: \
  -H "İçerik-Tipi: application/json" \
  -d '{
    "searchTerm": "alex@company.com",
    "page": 2,
    "pageSize": 25
  }'
```

<div id="get-usage-events-data">
  ### Kullanım Olayları Verilerini Al
</div>

Takımın için kapsamlı filtreleme, arama ve sayfalama seçenekleriyle ayrıntılı kullanım olaylarını getir. Bu uç nokta, tekil API çağrıları, model kullanımı, token tüketimi ve maliyetler hakkında daha ayrıntılı içgörüler sunar.

```
POST /teams/filtered-usage-events
```

#### İstek Gövdesi

<div className="full-width-table">
  | Parametre   | Tip    | Gerekli | Açıklama                                       |
  | :---------- | :----- | :------ | :--------------------------------------------- |
  | `startDate` | number | Hayır   | Epoch milisaniye cinsinden başlangıç tarihi    |
  | `endDate`   | number | Hayır   | Epoch milisaniye cinsinden bitiş tarihi        |
  | `userId`    | number | Hayır   | Belirli kullanıcı kimliğine göre filtrele      |
  | `page`      | number | Hayır   | Sayfa numarası (1’den başlar). Varsayılan: `1` |
  | `pageSize`  | number | Hayır   | Sayfa başına sonuç sayısı. Varsayılan: `10`    |
  | `email`     | string | Hayır   | Kullanıcı e-posta adresine göre filtrele       |
</div>

#### Yanıt

```typescript  theme={null}
{
  totalUsageEventsCount: number;
  pagination: {
    numPages: number;
    currentPage: number;
    pageSize: number;
    hasNextPage: boolean;
    hasPreviousPage: boolean;
  };
  usageEvents: {
    zamanDamgasi: string;
    model: string;
    tur: string;
    maxMode: boolean;
    istekMaliyetleri: number;
    isTokenBasedCall: boolean;
    belirteçKullanimi?: {
      girisBelirtecleri: number;
      cikisBelirtecleri: number;
      önbellekYazmaBelirtecleri: number;
      önbellekOkumaBelirtecleri: number;
      toplamSent: number;
    };
    isFreeBugbot: boolean;
    kullaniciEpostasi: string;
  }[];
  period: {
    baslangicTarihi: number;
    bitisTarihi: number;
  };
}
```

<div id="response-fields-explained">
  #### Yanıt Alanlarının Açıklaması
</div>

<div className="full-width-table">
  | Alan                    | Açıklama                                                           |
  | :---------------------- | :----------------------------------------------------------------- |
  | `totalUsageEventsCount` | Sorguyla eşleşen kullanım olaylarının toplam sayısı                |
  | `pagination`            | Sonuçlar arasında gezinmeye yönelik sayfalama üst verisi           |
  | `timestamp`             | Olay zaman damgası (epoch milisaniyeler)                           |
  | `model`                 | İstek için kullanılan yapay zeka modeli                            |
  | `kind`                  | Kullanım kategorisi (ör. "Usage-based", "Included in Business")    |
  | `maxMode`               | Maks modun etkin olup olmadığı                                     |
  | `requestsCosts`         | İstek birimleri cinsinden maliyet                                  |
  | `isTokenBasedCall`      | Olay kullanım bazlı olarak ücretlendirildiğinde true               |
  | `tokenUsage`            | Ayrıntılı token kullanımı (isTokenBasedCall true olduğunda mevcut) |
  | `isFreeBugbot`          | Bunun ücretsiz bugbot kullanımı olup olmadığı                      |
  | `userEmail`             | İsteği yapan kullanıcının e-posta adresi                           |
  | `period`                | Sorgulanan verinin tarih aralığı                                   |
</div>

#### Örnek Yanıt

```json  theme={null}
{
  "totalUsageEventsCount": 113,
  "pagination": {
    "numPages": 12,
    "currentPage": 1,
    "pageSize": 10,
    "hasNextPage": true,
    "hasPreviousPage": false
  },
  "usageEvents": [
    {
      "timestamp": "1750979225854",
      "model": "claude-4-opus",
      "kind": "Kullanıma göre",
      "maxMode": true,
      "requestsCosts": 5,
      "isTokenBasedCall": true,
      "tokenUsage": {
        "inputTokens": 126,
        "outputTokens": 450,
        "cacheWriteTokens": 6112,
        "cacheReadTokens": 11964,
        "totalCents": 20.18232
      },
      "isFreeBugbot": false,
      "userEmail": "developer@company.com"
    },
    {
      "timestamp": "1750979173824",
      "model": "claude-4-opus",
      "kind": "Kullanıma göre",
      "maxMode": true,
      "requestsCosts": 10,
      "isTokenBasedCall": true,
      "tokenUsage": {
        "inputTokens": 5805,
        "outputTokens": 311,
        "cacheWriteTokens": 11964,
        "cacheReadTokens": 0,
        "totalCents": 40.16699999999999
      },
      "isFreeBugbot": false,
      "userEmail": "developer@company.com"
    },
    {
      "timestamp": "1750978339901",
      "model": "claude-4-sonnet-thinking",
      "kind": "Business’a dahil",
      "maxMode": true,
      "requestsCosts": 1.4,
      "isTokenBasedCall": false,
      "isFreeBugbot": false
      "userEmail": "admin@company.com"
    }
  ],
  "period": {
    "startDate": 1748411762359,
    "endDate": 1751003762359
  }
}
```

#### Örnek İstekler

**Varsayılan sayfalamayla tüm kullanım etkinliklerini getir:**

```bash  theme={null}
curl -X POST https://api.cursor.com/teams/filtered-usage-events \
  -u YOUR_API_KEY: \
  -H "Content-Type: application/json" \
  -d '{}'
```

**Tarih aralığına ve belirli bir kullanıcıya göre filtrele:**

```bash  theme={null}
curl -X POST https://api.cursor.com/teams/filtered-usage-events \
  -u YOUR_API_KEY: \
  -H "İçerik-Türü: application/json" \
  -d '{
    "startDate": 1748411762359,
    "endDate": 1751003762359,
    "email": "developer@company.com",
    "page": 1,
    "pageSize": 25
  }'
```

**Özel sayfalama ile belirli bir kullanıcının kullanım etkinliklerini al:**

```bash  theme={null}
curl -X POST https://api.cursor.com/teams/filtered-usage-events \
  -u API_ANAHTARIN: \
  -H "İçerik Türü: application/json" \
  -d '{
    "userId": 12345,
    "page": 2,
    "pageSize": 50
  }'
```

<div id="set-user-spend-limit">
  ### Kullanıcı Harcama Limitini Ayarla
</div>

Tek tek ekip üyeleri için harcama limitleri belirle. Böylece ekibindeki her kullanıcının AI kullanımı için ne kadar harcayabileceğini kontrol edebilirsin.

```
POST /teams/user-spend-limit
```

<Note>
  **Oran sınırlaması:** ekip başına dakikada 60 istek
</Note>

#### İstek Gövdesi

<div className="full-width-table">
  | Parametre           | Tür    | Gerekli | Açıklama                                                         |
  | :------------------ | :----- | :------ | :--------------------------------------------------------------- |
  | `userEmail`         | string | Evet    | Ekip üyesinin e-posta adresi                                     |
  | `spendLimitDollars` | number | Evet    | Dolar cinsinden harcama limiti (yalnızca tam sayı, ondalık yok). |
</div>

<Note>
  * Kullanıcı zaten senin ekibinin bir üyesi olmalı
  * Yalnızca tam sayı değerleri kabul edilir (ondalık tutar kabul edilmez)
  * `spendLimitDollars` değerini 0 olarak ayarlamak limiti \$0 yapar
</Note>

#### Yanıt

Başarı ya da başarısızlığı belirten standart bir yanıt döndürür:

```typescript  theme={null}
{
  outcome: 'başarılı' | 'hata';
  message: string;
}
```

<div id="example-responses">
  #### Örnek Yanıtlar
</div>

**Limit başarıyla belirlendi:**

```json  theme={null}
{
  "outcome": "başarılı",
  "message": "developer@company.com kullanıcısının harcama limiti $100 olarak ayarlandı"
}
```

**Hata yanıtı:**

```json  theme={null}
{
  "outcome": "error",
  "message": "Geçersiz e-posta formatı"
}
```

#### Örnek İstekler

**Harcama limiti belirle:**

```bash  theme={null}
curl -X POST https://api.cursor.com/teams/user-spend-limit \
  -u API_ANAHTARIN: \
  -H "Content-Type: application/json" \
  -d '{
    "userEmail": "developer@company.com",
    "spendLimitDollars": 100
  }'
```

<div id="repo-blocklists-api">
  ### Repo Blocklists API
</div>

Takımın için dosya veya dizinlerin dizine alınmasını ya da bağlam olarak kullanılmasını önlemek üzere depolar ve eşleşme kalıpları ekle.

<div id="get-team-repo-blocklists">
  #### Takım Depo Engelleme Listelerini Al
</div>

Takımın için yapılandırılmış tüm depo engelleme listelerini al.

```
GET /settings/repo-blocklists/repos
```

<div id="response">
  ##### Yanıt
</div>

Bir dizi depo engelleme listesi (blocklist) nesnesi döndürür:

```typescript  theme={null}
{
  repos: {
    id: string;
    url: string;
    patterns: string[];
  }[];
}
```

<div id="example-response">
  ##### Örnek Yanıt
</div>

```json  theme={null}
{
  "repos": [
    {
      "id": "repo_123",
      "url": "https://github.com/company/sensitive-repo",
      "patterns": ["*.env", "config/*", "secrets/**"]
    },
    {
      "id": "repo_456",
      "url": "https://github.com/company/internal-tools",
      "patterns": ["*"]
    }
  ]
}
```

<div id="example-request">
  ##### Örnek İstek
</div>

```bash  theme={null}
curl -X GET https://api.cursor.com/settings/repo-blocklists/repos \
  -u API_ANAHTARIN:
```

<div id="upsert-repo-blocklists">
  #### Repo Engelleme Listelerini (Blocklist) Yükselt/İçer
</div>

Sağlanan repolar için mevcut repo engelleme listelerini (blocklist) yenisiyle değiştir.
*Not: Bu uç nokta yalnızca sağlanan repoların desenlerini (pattern) geçersiz kılar. Diğer tüm repolar etkilenmeden kalır.*

```
POST /settings/repo-blocklists/repos/upsert
```

<div id="request-body">
  ##### İstek Gövdesi
</div>

| Parametre | Tür   | Gerekli | Açıklama                                     |
| --------- | ----- | ------- | -------------------------------------------- |
| repos     | array | Evet    | Depo engel listesi nesnelerinden oluşan dizi |

Her depo nesnesi şunları içermelidir:

| Alan     | Tür       | Gerekli | Açıklama                                                            |
| -------- | --------- | ------- | ------------------------------------------------------------------- |
| url      | string    | Evet    | Engel listesine eklenecek depo URL’si                               |
| patterns | string\[] | Evet    | Engellenecek dosya kalıplarının dizisi (glob kalıpları desteklenir) |

<div id="response">
  ##### Yanıt
</div>

Güncellenmiş depo engel listelerinin listesini döndürür:

```typescript  theme={null}
{
  repos: {
    id: string;
    url: string;
    patterns: string[];
  }[];
}
```

<div id="example-request">
  ##### Örnek İstek
</div>

```bash  theme={null}
curl -X POST https://api.cursor.com/settings/repo-blocklists/repos/upsert \
  -u YOUR_API_KEY: \
  -H "Content-Type: application/json" \
  -d '{
    "repos": [
      {
        "url": "https://github.com/company/sensitive-repo",
        "patterns": ["*.env", "config/*", "secrets/**"]
      },
      {
        "url": "https://github.com/company/internal-tools", 
        "patterns": ["*"]
      }
    ]
  }'
```

<div id="delete-repo-blocklist">
  #### Depo Engelleme Listesinden Kaldır
</div>

Engelleme listesinden belirli bir depoyu kaldır.

```
DELETE /settings/repo-blocklists/repos/:repoId
```

<div id="parameters">
  ##### Parametreler
</div>

| Parametre | Tür    | Gerekli | Açıklama                                            |
| --------- | ------ | ------- | --------------------------------------------------- |
| repoId    | string | Evet    | Silinecek depo engel listesinin (blocklist) kimliği |

<div id="response">
  ##### Yanıt
</div>

Başarıyla silindiğinde 204 No Content döndürür.

<div id="example-request">
  ##### Örnek İstek
</div>

```bash  theme={null}
curl -X DELETE https://api.cursor.com/settings/repo-blocklists/repos/repo_123 \
  -u YOUR_API_KEY:
```

<div id="pattern-examples">
  #### Kalıp Örnekleri
</div>

Yaygın blocklist kalıpları:

* `*` - Tüm depoyu engelle
* `*.env` - Tüm .env dosyalarını engelle
* `config/*` - config dizinindeki tüm dosyaları engelle
* `**/*.secret` - Herhangi bir alt dizindeki tüm .secret dosyalarını engelle
* `src/api/keys.ts` - Belirli bir dosyayı engelle



# AI Kod Takip API'si
Source: https://docs.cursor.com/tr/account/teams/ai-code-tracking-api

Ekibinin depoları için yapay zekâ tarafından üretilen kod analizlerine eriş

Ekibinin depoları için yapay zekâ tarafından üretilen kod analizlerine eriş. Buna commit başına yapay zekâ kullanımı ve ayrıntılı düzeyde kabul edilen yapay zekâ değişiklikleri de dâhil.

<Note>
  API ilk sürümünde. Geri bildirimlere göre yetenekleri genişletiyoruz — hangi endpoint'lere ihtiyaç duyduğunu bize söyle!
</Note>

* **Kullanılabilirlik**: Yalnızca kurumsal ekipler için
* **Durum**: Alfa (yanıt yapı ve alanları değişebilir)

<div id="authentication">
  ## Kimlik Doğrulama
</div>

Tüm API istekleri, bir API anahtarıyla kimlik doğrulaması gerektirir. Bu API, diğer uç noktalarla aynı Admin API kimlik doğrulamasını kullanır.

Ayrıntılı kimlik doğrulama yönergeleri için bkz. [Admin API kimlik doğrulama](/tr/account/teams/admin-api#authentication).

<div id="base-url">
  ## Temel URL
</div>

Tüm API uç noktaları şu adresi kullanır:

```
https://api.cursor.com
```

<div id="rate-limits">
  ## Oran Sınırları
</div>

* Her ekip için, her uç nokta için dakikada 5 istek

<div id="query-parameters">
  ## Sorgu Parametreleri
</div>

Aşağıdaki tüm uç noktalar, aynı sorgu parametrelerini sorgu dizesiyle kabul eder:

<div className="full-width-table">
  | Parametre   | Tür    | Gerekli | Açıklama                                                                                                                                                                                             |                                                                                                         |
  | :---------- | :----- | :------ | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
  | `startDate` | string | date    | Hayır                                                                                                                                                                                                | ISO tarih dizesi, birebir "now" veya "7d" gibi göreli günler (şu an - 7 gün). Varsayılan: şu an - 7 gün |
  | `endDate`   | string | date    | Hayır                                                                                                                                                                                                | ISO tarih dizesi, birebir "now" veya "0d" gibi göreli günler. Varsayılan: şu an                         |
  | `page`      | number | Hayır   | Sayfa numarası (1 tabanlı). Varsayılan: 1                                                                                                                                                            |                                                                                                         |
  | `pageSize`  | number | Hayır   | Sayfa başına sonuç sayısı. Varsayılan: 100, Maks: 1000                                                                                                                                               |                                                                                                         |
  | `user`      | string | Hayır   | Tek bir kullanıcıya göre isteğe bağlı filtre. E-posta (örn. [developer@company.com](mailto:developer@company.com)), kodlanmış kimlik (örn. user\_abc123...) veya sayısal kimlik (örn. 42) kabul eder |                                                                                                         |
</div>

<Note>
  Yanıtlarda userId, user\_ önekiyle kodlanmış harici bir kimlik olarak döner. Bu, API kullanımı için kararlıdır.
</Note>

<div id="semantics-and-how-metrics-are-computed">
  ## Anlambilim ve Metriklerin Nasıl Hesaplandığı
</div>

* **Kaynaklar**: "TAB", kabul edilen satır içi tamamlamaları temsil eder; "COMPOSER", Composer’dan kabul edilen diff’leri temsil eder
* **Satır metrikleri**: tabLinesAdded/Deleted ve composerLinesAdded/Deleted ayrı ayrı sayılır; nonAiLinesAdded/Deleted, max(0, totalLines - AI lines) olarak türetilir
* **Gizlilik modu**: İstemcide etkinleştirilirse, bazı meta veriler (örn. fileName) atlanabilir
* **Dal bilgisi**: isPrimaryBranch, geçerli dal repo’nun varsayılan dalına eşitse true olur; repo bilgisi yoksa undefined olabilir

Commit’lerin ve değişikliklerin nasıl algılanıp raporlandığını anlamak için o dosyayı inceleyebilirsin.

<div id="endpoints">
  ## Uç Noktalar
</div>

<div id="get-ai-commit-metrics-json-paginated">
  ### AI Commit Metriklerini Getir (JSON, sayfalı)
</div>

Commit başına, satırları TAB, COMPOSER ve AI dışı kaynaklara atfeden toplu metrikleri al.

```
GET /analytics/ai-code/commits
```

<div id="response">
  #### Yanıt
</div>

```typescript  theme={null}
{
  items: AiCommitMetric[];
  totalCount: number;
  page: number;
  pageSize: number;
}
```

<div id="aicommitmetric-fields">
  #### AiCommitMetric Alanları
</div>

<div className="full-width-table">
  | Alan                   | Tür     | Açıklama                                        |                                              |
  | :--------------------- | :------ | :---------------------------------------------- | -------------------------------------------- |
  | `commitHash`           | string  | Git commit karma değeri                         |                                              |
  | `userId`               | string  | Kodlanmış kullanıcı kimliği (örn. user\_abc123) |                                              |
  | `userEmail`            | string  | Kullanıcının e‑posta adresi                     |                                              |
  | `repoName`             | string  | null                                            | Depo adı                                     |
  | `branchName`           | string  | null                                            | Dal adı                                      |
  | `isPrimaryBranch`      | boolean | null                                            | Birincil dal olup olmadığı                   |
  | `totalLinesAdded`      | number  | Commit’te eklenen toplam satır                  |                                              |
  | `totalLinesDeleted`    | number  | Commit’te silinen toplam satır                  |                                              |
  | `tabLinesAdded`        | number  | TAB tamamlamalarıyla eklenen satırlar           |                                              |
  | `tabLinesDeleted`      | number  | TAB tamamlamalarıyla silinen satırlar           |                                              |
  | `composerLinesAdded`   | number  | Composer ile eklenen satırlar                   |                                              |
  | `composerLinesDeleted` | number  | Composer ile silinen satırlar                   |                                              |
  | `nonAiLinesAdded`      | number  | null                                            | Yapay zekâ kaynaklı olmayan eklenen satırlar |
  | `nonAiLinesDeleted`    | number  | null                                            | Yapay zekâ kaynaklı olmayan silinen satırlar |
  | `message`              | string  | null                                            | Commit mesajı                                |
  | `commitTs`             | string  | null                                            | Commit zaman damgası (ISO biçimi)            |
  | `createdAt`            | string  | Alım zaman damgası (ISO biçimi)                 |                                              |
</div>

<div id="example-response">
  #### Örnek Yanıt
</div>

```json  theme={null}
{
  "items": [
    {
      "commitHash": "a1b2c3d4",
      "userId": "user_3k9x8q...",
      "userEmail": "developer@company.com",
      "repoName": "company/repo",
      "branchName": "main",
      "isPrimaryBranch": true,
      "totalLinesAdded": 120,
      "totalLinesDeleted": 30,
      "tabLinesAdded": 50,
      "tabLinesDeleted": 10,
      "composerLinesAdded": 40,
      "composerLinesDeleted": 5,
      "nonAiLinesAdded": 30,
      "nonAiLinesDeleted": 15,
      "message": "Refactor: analytics istemcisini ayır"
      "commitTs": "2025-07-30T14:12:03.000Z",
      "createdAt": "2025-07-30T14:12:30.000Z"
    }
  ],
  "totalCount": 42,
  "page": 1,
  "pageSize": 100
}
```

<div id="example-requests">
  #### Örnek İstekler
</div>

**Basit istek:**

```bash  theme={null}
curl -X GET "https://api.cursor.com/analytics/ai-code/commits?startDate=7d&endDate=now&page=1&pageSize=100" \
  -u API_ANAHTARIN:
```

**Kullanıcıya göre filtrele (e‑posta):**

```bash  theme={null}
curl -X GET "https://api.cursor.com/analytics/ai-code/commits?startDate=2025-06-01T00:00:00Z&endDate=now&user=developer@company.com" \
  -u API_ANAHTARIN:
```

<div id="download-ai-commit-metrics-csv-streaming">
  ### AI Commit Metrics’i indir (CSV, akış)
</div>

Büyük hacimli veri çıkarımları için commit metriklerini CSV formatında indir.

```
GET /analytics/ai-code/commits.csv
```

<div id="response">
  #### Yanıt
</div>

Üstbilgiler:

* Content-Type: text/csv; charset=utf-8

<div id="csv-columns">
  #### CSV Sütunları
</div>

<div className="full-width-table">
  | Sütun                    | Tür     | Açıklama                           |
  | :----------------------- | :------ | :--------------------------------- |
  | `commit_hash`            | string  | Git commit özeti (hash)            |
  | `user_id`                | string  | Kodlanmış kullanıcı kimliği        |
  | `user_email`             | string  | Kullanıcının e‑posta adresi        |
  | `repo_name`              | string  | Depo adı                           |
  | `branch_name`            | string  | Dal adı                            |
  | `is_primary_branch`      | boolean | Birincil dal olup olmadığı         |
  | `total_lines_added`      | number  | Commit’te eklenen toplam satır     |
  | `total_lines_deleted`    | number  | Commit’te silinen toplam satır     |
  | `tab_lines_added`        | number  | TAB tamamlamalarıyla eklenen satır |
  | `tab_lines_deleted`      | number  | TAB tamamlamalarıyla silinen satır |
  | `composer_lines_added`   | number  | Composer ile eklenen satır         |
  | `composer_lines_deleted` | number  | Composer ile silinen satır         |
  | `non_ai_lines_added`     | number  | Yapay zekâ dışı eklenen satır      |
  | `non_ai_lines_deleted`   | number  | Yapay zekâ dışı silinen satır      |
  | `message`                | string  | Commit mesajı                      |
  | `commit_ts`              | string  | Commit zaman damgası (ISO biçimi)  |
  | `created_at`             | string  | Alım zaman damgası (ISO biçimi)    |
</div>

<div id="sample-csv-output">
  #### Örnek CSV Çıktısı
</div>

```csv  theme={null}
commit_hash,user_id,user_email,repo_name,branch_name,is_primary_branch,total_lines_added,total_lines_deleted,tab_lines_added,tab_lines_deleted,composer_lines_added,composer_lines_deleted,non_ai_lines_added,non_ai_lines_deleted,message,commit_ts,created_at
a1b2c3d4,user_3k9x8q...,developer@company.com,company/repo,main,true,120,30,50,10,40,5,30,15,"Refactor: analytics istemcisini ayır",2025-07-30T14:12:03.000Z,2025-07-30T14:12:30.000Z
e5f6g7h8,user_3k9x8q...,developer@company.com,company/repo,feature-branch,false,85,15,30,5,25,3,30,7,"Hata işleme ekle",2025-07-30T13:45:21.000Z,2025-07-30T13:45:45.000Z
```

<div id="example-request">
  #### Örnek İstek
</div>

```bash  theme={null}
curl -L "https://api.cursor.com/analytics/ai-code/commits.csv?startDate=2025-07-01T00:00:00Z&endDate=now&user=user_3k9x8q..." \
  -u YOUR_API_KEY: \
  -o commits.csv
```

<div id="get-ai-code-change-metrics-json-paginated">
  ### AI Kod Değişikliği Metriğini Al (JSON, sayfalı)
</div>

Deterministik changeId ile gruplanmış, ayrıntılı olarak kabul edilmiş AI değişikliklerini al. Commit’lerden bağımsız kabul edilmiş AI olaylarını analiz etmek için işe yarar.

```
GET /analytics/ai-code/changes
```

<div id="response">
  #### Yanıt
</div>

```typescript  theme={null}
{
  items: AiCodeChangeMetric[];
  totalCount: number;
  page: number;
  pageSize: number;
}
```

<div id="aicodechangemetric-fields">
  #### AiCodeChangeMetric Alanları
</div>

<div className="full-width-table">
  | Alan                | Tür    | Açıklama                                                   |                           |
  | :------------------ | :----- | :--------------------------------------------------------- | ------------------------- |
  | `changeId`          | string | Değişikliğe ait deterministik kimlik                       |                           |
  | `userId`            | string | Kodlanmış kullanıcı kimliği (ör. user\_abc123)             |                           |
  | `userEmail`         | string | Kullanıcının e-posta adresi                                |                           |
  | `source`            | "TAB"  | "COMPOSER"                                                 | AI değişikliğinin kaynağı |
  | `model`             | string | null                                                       | Kullanılan AI modeli      |
  | `totalLinesAdded`   | number | Eklenen toplam satır                                       |                           |
  | `totalLinesDeleted` | number | Silinen toplam satır                                       |                           |
  | `createdAt`         | string | İçeri aktarma zaman damgası (ISO biçimi)                   |                           |
  | `metadata`          | Array  | Dosya üst verileri (gizlilik modunda fileName atlanabilir) |                           |
</div>

<div id="example-response">
  #### Örnek Yanıt
</div>

```json  theme={null}
{
  "items": [
    {
      "changeId": "749356201",
      "userId": "user_3k9x8q...",
      "userEmail": "developer@company.com",
      "source": "COMPOSER",
      "model": null,
      "totalLinesAdded": 18,
      "totalLinesDeleted": 4,
      "createdAt": "2025-07-30T15:10:12.000Z",
        { "fileName": "src/analytics/report.ts", "fileExtension": "ts", "linesAdded": 12, "linesDeleted": 3 },
        { "fileName": "src/analytics/ui.tsx", "fileExtension": "tsx", "linesAdded": 6, "linesDeleted": 1 }
        { "fileName": "src/analytics/ui.tsx", "fileExtension": "tsx", "linesAdded": 6, "linesDeleted": 1 }
      ]
    }
  ],
  "totalCount": 128,
  "page": 1,
  "pageSize": 200
}
```

<div id="example-requests">
  #### Örnek İstekler
</div>

**Basit istek:**

```bash  theme={null}
curl -X GET "https://api.cursor.com/analytics/ai-code/changes?startDate=14d&endDate=now&page=1&pageSize=200" \
  -u API_ANAHTARIN:
```

**Kullanıcıya göre filtrele (kodlanmış kimlik):**

```bash  theme={null}
curl -X GET "https://api.cursor.com/analytics/ai-code/changes?user=user_3k9x8q..." \
  -u API_ANAHTARIN:
```

**Kullanıcıya göre filtrele (e-posta):**

```bash  theme={null}
curl -X GET "https://api.cursor.com/analytics/ai-code/changes?user=developer@company.com" \
  -u YOUR_API_KEY:
```

<div id="download-ai-code-change-metrics-csv-streaming">
  ### AI Kod Değişikliği Metriklerini İndir (CSV, akış)
</div>

Büyük veri çıkarımları için değişiklik metriklerini CSV formatında indir.

```
GET /analytics/ai-code/changes.csv
```

<div id="response">
  #### Yanıt
</div>

Başlıklar:

* Content-Type: text/csv; charset=utf-8

<div id="csv-columns">
  #### CSV Sütunları
</div>

<div className="full-width-table">
  | Sütun                 | Tür    | Açıklama                                               |
  | :-------------------- | :----- | :----------------------------------------------------- |
  | `change_id`           | string | Değişiklik için deterministik kimlik                   |
  | `user_id`             | string | Kodlanmış kullanıcı kimliği                            |
  | `user_email`          | string | Kullanıcının e-posta adresi                            |
  | `source`              | string | AI değişikliğinin kaynağı (TAB veya COMPOSER)          |
  | `model`               | string | Kullanılan AI modeli                                   |
  | `total_lines_added`   | number | Eklenen toplam satır sayısı                            |
  | `total_lines_deleted` | number | Silinen toplam satır sayısı                            |
  | `created_at`          | string | Alım zaman damgası (ISO biçimi)                        |
  | `metadata_json`       | string | JSON olarak dizgeleştirilmiş metadata girdileri dizisi |
</div>

<div id="notes">
  #### Notlar
</div>

* metadata\_json, JSON olarak dizgeleştirilmiş metadata girdileri dizisidir (gizlilik modunda fileName atlanabilir)
* CSV’yi işlerken tırnak içindeki alanları ayrıştırdığından emin ol

<div id="sample-csv-output">
  #### Örnek CSV Çıktısı
</div>

```csv  theme={null}
change_id,user_id,user_email,kaynak,model,toplam_eklenen_satır,toplam_silinen_satır,oluşturulma_tarihi,metadata_json
749356201,user_3k9x8q...,developer@company.com,COMPOSER,gpt-4o,18,4,2025-07-30T15:10:12.000Z,"[{""fileName"":""src/analytics/report.ts"",""fileExtension"":""ts"",""linesAdded"":12,""linesDeleted"":3},{""fileName"":""src/analytics/ui.tsx"",""fileExtension"":""tsx"",""linesAdded"":6,""linesDeleted"":1}]"
749356202,user_3k9x8q...,developer@company.com,TAB,,8,2,2025-07-30T15:08:45.000Z,"[{""fileName"":""src/utils/helpers.ts"",""fileExtension"":""ts"",""linesAdded"":8,""linesDeleted"":2}]"
```

<div id="example-request">
  #### Örnek İstek
</div>

```bash  theme={null}
curl -L "https://api.cursor.com/analytics/ai-code/changes.csv?startDate=30d&endDate=now" \
  -u YOUR_API_KEY: \
  -o changes.csv
```

<div id="tips">
  ## İpuçları
</div>

* Tüm endpoint’ler genelinde tek bir kullanıcıyı hızlıca filtrelemek için `user` parametresini kullan
* Büyük veri çıkarımları için CSV endpoint’lerini tercih et — sunucu tarafında 10.000 kayıttan oluşan sayfalar halinde akış (stream) olarak iletilir
* Varsayılan branch çözülemediyse `isPrimaryBranch` tanımsız olabilir
* `commitTs` commit zaman damgasıdır; `createdAt` sunucularımızda işlenme (ingestion) zamanıdır
* İstemcide gizlilik modu etkinse bazı alanlar bulunmayabilir

<div id="changelog">
  ## Değişiklik Günlüğü
</div>

* **Alfa sürümü**: Commit ve değişiklikler için başlangıç uç noktaları. Geri bildirimlere göre yanıt biçimleri değişebilir



# Analytics
Source: https://docs.cursor.com/tr/account/teams/analytics

Takım kullanımını ve etkinlik metriklerini takip et

Takım adminleri metrikleri [dashboard](/tr/account/teams/dashboard) üzerinden takip edebilir.

<Frame>
  <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/analytics.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=a8a4a0ca334e5f5acac55307b2ebeadf" data-og-width="3456" width="3456" data-og-height="1944" height="1944" data-path="images/account/team/analytics.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/analytics.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=73c11df8fcb2862e5c1fd551e6399159 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/analytics.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=c3eaa0d4faa7d6fdf5e3c79dfd11fb5a 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/analytics.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=e9ee5fc554ae46e9d0e2cf53c19e652d 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/analytics.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=5f0afded72e0b02142c5a85e448f2d4e 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/analytics.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=3a6dec2a182ac88d7de75f7a42b1f5ff 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/analytics.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=7a8ac7dafe559da435f3f4974b04df52 2500w" />
</Frame>

<div id="total-usage">
  ### Total Usage
</div>

Takım genelinde toplam sekmeler ve premium istekler dahil olmak üzere toplu metrikleri görüntüle. 30 günden küçük takımlar için metrikler, oluşturulduğu tarihten itibaren kullanımı yansıtır ve takım üyelerinin katılmadan önceki etkinliklerini de içerir.

<div id="per-active-user">
  ### Per Active User
</div>

Aktif kullanıcı başına ortalama metrikleri gör: kabul edilen sekmeler, kod satırları ve premium istekler.

<div id="user-activity">
  ### User Activity
</div>

Haftalık ve aylık aktif kullanıcıları takip et.

<div id="analytics-report-headers">
  ## Analitik Rapor Başlıkları
</div>

Kontrol panelinden analitik verileri dışa aktardığında, rapor kullanıcı davranışı ve özellik kullanımı hakkında ayrıntılı metrikler içerir. İşte her başlığın anlamı:

<div id="user-information">
  ### Kullanıcı Bilgileri
</div>

<ResponseField name="Date" type="ISO 8601 timestamp">
  Analitik verilerinin kaydedildiği tarih (örn. 2024-01-15T04:30:00.000Z)
</ResponseField>

<ResponseField name="User ID" type="string">
  Sistemindeki her kullanıcı için benzersiz tanımlayıcı
</ResponseField>

<ResponseField name="Email" type="string">
  Kullanıcının hesabıyla ilişkili e‑posta adresi
</ResponseField>

<ResponseField name="Is Active" type="boolean">
  Kullanıcının bu tarihte aktif olup olmadığını belirtir
</ResponseField>

<div id="ai-generated-code-metrics">
  ### AI Tarafından Üretilen Kod Metrikleri
</div>

<ResponseField name="Chat Suggested Lines Added" type="number">
  AI sohbet özelliği tarafından önerilen toplam eklenen kod satırı
</ResponseField>

<ResponseField name="Chat Suggested Lines Deleted" type="number">
  AI sohbet tarafından silinmesi önerilen toplam kod satırı
</ResponseField>

<ResponseField name="Chat Accepted Lines Added" type="number">
  Kullanıcının kabul edip koduna eklediği AI önerili satırlar
</ResponseField>

<ResponseField name="Chat Accepted Lines Deleted" type="number">
  Kullanıcının kabul ettiği AI önerili silmeler
</ResponseField>

<div id="feature-usage-metrics">
  ### Özellik Kullanım Metrikleri
</div>

<ResponseField name="Chat Total Applies" type="number">
  Bir kullanıcının sohbette AI tarafından üretilen değişiklikleri uygulama sayısı
</ResponseField>

<ResponseField name="Chat Total Accepts" type="number">
  Bir kullanıcının AI önerilerini kabul etme sayısı
</ResponseField>

<ResponseField name="Chat Total Rejects" type="number">
  Bir kullanıcının AI önerilerini reddetme sayısı
</ResponseField>

<ResponseField name="Chat Tabs Shown" type="number">
  AI öneri sekmelerinin kullanıcıya gösterilme sayısı
</ResponseField>

<ResponseField name="Tabs Accepted" type="number">
  Kullanıcı tarafından kabul edilen AI öneri sekmeleri
</ResponseField>

<div id="request-type-metrics">
  ### İstek Türü Metrikleri
</div>

<ResponseField name="Edit Requests" type="number">
  composer/edit özelliğiyle yapılan istekler (Cmd+K satır içi düzenlemeler)
</ResponseField>

<ResponseField name="Ask Requests" type="number">
  Kullanıcıların AI’ye soru sorduğu sohbet istekleri
</ResponseField>

<ResponseField name="Agent Requests" type="number">
  AI ajanlarına yapılan istekler (uzmanlaşmış AI asistanları)
</ResponseField>

<ResponseField name="Cmd+K Usages" type="number">
  Cmd+K (veya Ctrl+K) komut paletinin kullanılma sayısı
</ResponseField>

<div id="subscription-and-api-metrics">
  ### Abonelik ve API Metrikleri
</div>

<ResponseField name="Subscription Included Reqs" type="number">
  Kullanıcının abonelik planı kapsamında karşılanan AI istekleri
</ResponseField>

<ResponseField name="API Key Reqs" type="number">
  Programatik erişim için API anahtarları kullanılarak yapılan istekler
</ResponseField>

<ResponseField name="Usage-Based Reqs" type="number">
  Kullanıma dayalı faturalamaya dahil olan istekler
</ResponseField>

<div id="additional-features">
  ### Ek Özellikler
</div>

<ResponseField name="Bugbot Usages" type="number">
  Hata tespit/düzeltme AI özelliğinin kullanılma sayısı
</ResponseField>

<div id="configuration-information">
  ### Yapılandırma Bilgileri
</div>

<ResponseField name="Most Used Model" type="string">
  Kullanıcının en sık kullandığı AI modeli (örn. GPT-4, Claude)
</ResponseField>

<ResponseField name="Most Used Apply Extension" type="string">
  AI önerilerini uygularken en sık kullanılan dosya uzantısı (örn. .ts,
  .py, .java)
</ResponseField>

<ResponseField name="Most Used Tab Extension" type="string">
  Sekme tamamlama özellikleriyle en sık kullanılan dosya uzantısı
</ResponseField>

<ResponseField name="Client Version" type="string">
  Kullanılan Cursor editörünün sürümü
</ResponseField>

<div id="calculated-metrics">
  ### Hesaplanmış Metrikler
</div>

Rapor ayrıca AI kod katkısını anlamaya yardımcı olan işlenmiş veriler de içerir:

* Total Lines Added/Deleted: Tüm kod değişikliklerinin ham sayımı
* Accepted Lines Added/Deleted: AI önerilerinden kaynaklanıp kabul edilen satırlar
* Composer Requests: Satır içi composer özelliğiyle yapılan istekler
* Chat Requests: Sohbet arayüzü üzerinden yapılan istekler

<Note>
  Tüm sayısal değerler yoksa varsayılan olarak 0, boolean değerler false ve string değerler boş string olarak kabul edilir. Metrikler kullanıcı başına günlük düzeyde toplanır.
</Note>



# Analytics V2
Source: https://docs.cursor.com/tr/account/teams/analyticsV2

Gelişmiş ekip kullanımı ve etkinlik metrikleri takibi

Analytics altyapımızın V2 sürümü üzerinde çalışıyoruz. Bu, çeşitli metrikleri nasıl izlediğimizi yeniden düzenlemeyi içeriyor.

**1 Eylül 2025** itibarıyla ve **Cursor 1.5** kullananlar için analytics V2 altyapımıza geçecek. Önceki sürümler, aşağıdakiler de dahil olmak üzere çeşitli metrikleri eksik sayıyordu:

* Toplam Kabul Edilen Kod Satırı
* Toplam Önerilen Kod Satırı
* Toplam Kabul Edilen Sekmeler

Analytics’e yatırım yapmaya ve bu alanda yeni özellikler yayınlamaya devam ederken bizi takipte kal.



# Kontrol Paneli
Source: https://docs.cursor.com/tr/account/teams/dashboard

Faturalandırmayı, kullanımı ve ekip ayarlarını kontrol panelinden yönet

Kontrol paneli, faturalandırmaya erişmeni, kullanım bazlı fiyatlandırmayı kurmanı ve ekibini yönetmeni sağlar.

<div id="overview">
  ## Genel Bakış
</div>

Ekibinin aktivitesinin, kullanım istatistiklerinin ve son değişikliklerin hızlı bir özetini al. Genel bakış sayfası, çalışma alanına dair anlık içgörüler sunar.

<Frame>
  <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/dashboard.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=48ee98a4d9b168b93c26a03c1af74ddd" data-og-width="3456" width="3456" data-og-height="1944" height="1944" data-path="images/account/team/dashboard.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/dashboard.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=2ac6f157659354866eaa03b38cd1eb90 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/dashboard.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=8e9e84e894a3faf2846e3aae5deb9a2b 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/dashboard.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=e1034c739d961ccc69c17ba947edda90 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/dashboard.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=dbeed5506f7ae3fc4fabc7d248d69e64 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/dashboard.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=afac07ce763fccf7eded7248fb990745 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/dashboard.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=c4ed8c8161c3f2a964371a237134b1ae 2500w" />
</Frame>

<div id="settings">
  ## Ayarlar
</div>

<Frame>
  <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/settings.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=5edb18df1ddc2d20e69abdd83140a509" data-og-width="1390" width="1390" data-og-height="913" height="913" data-path="images/account/team/settings.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/settings.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=4d4c8f244231868bf4111f05b1f46c93 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/settings.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=582ddf5415a973010e3bcbeeb13d4f64 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/settings.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=74a5d5f4644b701adc25b6d847f5752e 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/settings.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=9250830c64e8c3490c3ca6f7b6f65eec 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/settings.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=7ce96a620ac6d447e79abd901b5c6cdc 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/settings.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=6d24738577e0ffd837d87f8926339215 2500w" />
</Frame>

Tüm takım için tercihleri ve güvenlik ayarlarını yapılandır. Ayarlar sayfasında şunlar bulunur:

<div id="teams-enterprise-settings">
  ## Takım ve Kurumsal Ayarlar
</div>

<AccordionGroup>
  <Accordion title="Gizlilik Ayarları">
    Takımının veri paylaşımı tercihlerini kontrol et. Yapay zeka sağlayıcılarıyla (OpenAI, Anthropic, Google Vertex AI, xAI Grok) sıfır veri saklama politikalarını yapılandır ve takım genelinde gizlilik uygulamasını yönet.
  </Accordion>

  {" "}

  <Accordion title="Kullanıma Dayalı Fiyatlandırma Ayarları">
    Kullanıma dayalı fiyatlandırmayı etkinleştir ve harcama limitlerini belirle. Aylık takım
    harcama limitlerini ve isteğe bağlı kişi başı limitleri yapılandır. Bu ayarları yalnızca yöneticilerin
    değiştirip değiştiremeyeceğini kontrol et.
  </Accordion>

  {" "}

  <Accordion title="Bedrock IAM Rolü">
    Güvenli bulut entegrasyonu için AWS Bedrock IAM rollerini yapılandır.
  </Accordion>

  {" "}

  <Accordion title="Tek Oturum Açma (SSO)">
    Kurumsal takımlar için SSO kimlik doğrulamasını kurarak kullanıcı erişimini kolaylaştır
    ve güvenliği artır.
  </Accordion>

  {" "}

  <Accordion title="Cursor Yönetici API Anahtarları">
    Cursor'ın yönetici özelliklerine programatik erişim için API anahtarları oluştur ve yönet.
  </Accordion>

  {" "}

  <Accordion title="Aktif Oturumlar">
    Takım genelindeki aktif kullanıcı oturumlarını izle ve yönet.
  </Accordion>

  <Accordion title="Davet Kodu Yönetimi">
    Yeni takım üyeleri eklemek için davet kodları oluştur ve yönet.
  </Accordion>

  <Accordion title="API Uç Noktaları">
    Cursor'ın REST API uç noktalarına programatik entegrasyon için eriş. Tüm API uç noktaları Team ve Enterprise planlarında kullanılabilir, yalnızca [AI Code Tracking API](/tr/docs/account/teams/ai-code-tracking-api) için Enterprise üyeliği gerekir.
  </Accordion>
</AccordionGroup>

<div id="enterprise-only-settings">
  ## Yalnızca Enterprise Ayarları
</div>

<AccordionGroup>
  {" "}

  <Accordion title="Model Erişim Kontrolü">
    Hangi AI modellerinin ekip üyelerine açık olacağını kontrol et. Maliyetleri yönetmek ve organizasyon genelinde uygun kullanımı sağlamak için belirli modellere veya model katmanlarına kısıtlamalar ayarla.
  </Accordion>

  {" "}

  <Accordion title="Otomatik Çalıştırma Yapılandırması (0.49+)">
    Cursor 0.49 ve üzeri sürümler için otomatik komut yürütme ayarlarını yapılandır. Hangi komutların otomatik çalıştırılabileceğini kontrol et ve kod yürütme için güvenlik politikaları belirle.
  </Accordion>

  <Accordion title="Depo Engelleme Listesi">
    Güvenlik veya uyumluluk nedenleriyle belirli depolara erişimi engelle.
  </Accordion>

  {" "}

  <Accordion title="MCP Yapılandırması (0.51+)">
    Cursor 0.51 ve üzeri sürümler için Model Context Protocol ayarlarını yapılandır. Modellerin geliştirme ortamından bağlama nasıl erişip onu nasıl işleyeceğini yönet.
  </Accordion>

  {" "}

  <Accordion title="Cursor Ignore Yapılandırması (0.50+)">
    Cursor 0.50 ve üzeri sürümlerde dosya ve dizinler için yok sayma kalıplarını ayarla. Hangi dosya ve dizinlerin AI analizinden ve önerilerinden hariç tutulacağını kontrol et.
  </Accordion>

  <Accordion title=".cursor Dizin Koruması (0.51+)">
    .cursor dizinini 0.51 ve üzeri sürümlerde yetkisiz erişime karşı koru. Hassas yapılandırma ve önbellek dosyalarının güvende kalmasını sağla.
  </Accordion>

  <Accordion title="AI Kod Takip API'si">
    Ekibinin depoları için ayrıntılı AI kaynaklı kod analizlerine eriş. REST API uç noktaları üzerinden commit başına AI kullanım metriklerini ve ayrıntılı, kabul edilen AI değişikliklerini al. Enterprise plan gerektirir. Daha fazla bilgi için [buraya](/tr/account/teams/ai-code-tracking-api) bak.
  </Accordion>
</AccordionGroup>

<Note>
  **SCIM** (System for Cross-domain Identity Management) provizyonu ayrıca Enterprise planlarda mevcut. Kurulum talimatları için [SCIM dokümantasyonumuza](/tr/account/teams/scim) bak.
</Note>

<div id="members">
  ## Üyeler
</div>

Ekip üyelerini yönet, yeni kullanıcılar davet et ve erişim izinlerini kontrol et. Role dayalı izinler ayarla ve üye etkinliğini takip et.

<Frame>
  <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/members.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=4ac43692626733caf2da4b53e4cd9055" data-og-width="1390" width="1390" data-og-height="591" height="591" data-path="images/account/team/members.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/members.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=a2a24d3282df1e875d73fd2bf29b9c04 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/members.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=1abe9715816149f577a5d9c9e2f3545d 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/members.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=ccc84260c5139119e5b16ad6c214af72 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/members.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=5fe34e422fa9540004c25a61570029c3 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/members.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=dee7c3ade8ef46b5ead5dbe2bfd2a6be 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/members.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=9a42bce921a799886b8e3e0a389b8589 2500w" />
</Frame>

<div id="integrations">
  ## Entegrasyonlar
</div>

<Frame>
  <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/integrations.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=187b9e77d6b99c77caec81e1b3063417" data-og-width="1390" width="1390" data-og-height="592" height="592" data-path="images/account/team/integrations.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/integrations.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=470d5697ff2bfb9db2ae745b2c33cce6 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/integrations.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=e1e7d589f1f208ecdba9840629897968 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/integrations.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=2285e05c99c3a6ace609b51770475a3e 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/integrations.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=7c44649c5e8cd0f2a3791a3085252eca 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/integrations.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=0cf7111171c8019f7a59adc79cb9639d 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/integrations.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=8423a209b4e1c753045dca1514cbfbad 2500w" />
</Frame>

{" "}

Cursor’ı favori araç ve hizmetlerinle bağla. Sürüm kontrol sistemleri, proje yönetim araçları ve diğer geliştirici hizmetleriyle entegrasyonları yapılandır.

<div id="background-agents">
  ## Arka Plan Ajanları
</div>

<Frame>
  <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/integrations.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=187b9e77d6b99c77caec81e1b3063417" data-og-width="1390" width="1390" data-og-height="592" height="592" data-path="images/account/team/integrations.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/integrations.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=470d5697ff2bfb9db2ae745b2c33cce6 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/integrations.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=e1e7d589f1f208ecdba9840629897968 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/integrations.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=2285e05c99c3a6ace609b51770475a3e 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/integrations.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=7c44649c5e8cd0f2a3791a3085252eca 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/integrations.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=0cf7111171c8019f7a59adc79cb9639d 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/integrations.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=8423a209b4e1c753045dca1514cbfbad 2500w" />
</Frame>

{" "}

Çalışma alanında çalışan arka plan ajanlarını izle ve yönet. Ajan durumunu, günlükleri ve kaynak kullanımını görüntüle.

<div id="bugbot">
  ## Bugbot
</div>

Otomatik hata tespiti ve düzeltme özelliklerine eriş. Bugbot, kod tabanındaki yaygın sorunları otomatik olarak belirleyip çözmene yardımcı olur.

<Frame>
  <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/bugbot.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=20d841dfc7837445103a933dab18b470" alt="Bugbot kod incelemesi" data-og-width="1390" width="1390" data-og-height="913" height="913" data-path="images/account/team/bugbot.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/bugbot.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=975f5e3f9f9a0334c8a5bcc12faf72be 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/bugbot.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=17099f8bbe0701750d0ba212879d8a93 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/bugbot.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=041c82a4c3bada0524527609dfc134a4 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/bugbot.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=90ac57ea38768ace4b9404476fafdf32 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/bugbot.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=5785673a93f899ccca7b70e7a3752ef7 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/bugbot.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=a1a1dc51872967e392e10d6b85c31a04 2500w" />
</Frame>

<div id="active-directory-management">
  ## Active Directory Yönetimi
</div>

Kurumsal ekipler için, Active Directory entegrasyonuyla kullanıcı kimlik doğrulamasını ve erişimi yönet. SSO’yu ve kullanıcı provizyonunu yapılandır.

<div id="usage">
  ## Kullanım
</div>

AI istekleri, model kullanımı ve kaynak tüketimi de dahil ayrıntılı kullanım metriklerini izle. Kullanımı ekip üyeleri ve projeler genelinde takip et.

<Frame>
  <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/usage.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=8744e41430d162199d85ca8e966c91cd" data-og-width="1390" width="1390" data-og-height="913" height="913" data-path="images/account/team/usage.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/usage.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=bc43eaaeca3c2a531a56243037a7a53f 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/usage.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=34700d63fabf072e9906aab74f79f7d9 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/usage.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=7f2bcdb271d6b30e333374c798638989 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/usage.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=424bd0eeda69200668f8f0b86dc360bf 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/usage.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=f0e716c72f01a3297a53a5b63d191ef4 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/usage.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=ffa574322508a07cc5ab867b331b6d35 2500w" />
</Frame>

<div id="billing-invoices">
  ## Faturalandırma ve Faturalar
</div>

Aboneliğini yönet, ödeme yöntemlerini güncelle ve faturalandırma geçmişine eriş. Faturaları indir ve kullanım bazlı fiyatlandırma ayarlarını yönet.

<Frame>
  <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/billing.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=d76d20a7fafc6ed2135f2f9c78ec6c2d" data-og-width="1390" width="1390" data-og-height="913" height="913" data-path="images/account/team/billing.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/billing.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=45501f34dd144ecd74e982fe5f8f8364 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/billing.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=19860b61e083a8550cb3caa16bdb1ba0 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/billing.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=7005bae381a362b39980a49113ca367c 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/billing.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=e47c9ee55e3699ba46429b0ac0563b5b 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/billing.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=039106fd5ff42f2e343b2b853614e7e7 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/billing.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=e598f83559985558f5825a3da25bb554 2500w" />
</Frame>



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



# Başlarken
Source: https://docs.cursor.com/tr/account/teams/setup

Bir Cursor ekibi oluştur ve kur

<div id="cursor-for-teams">
  ## Ekipler için Cursor
</div>

Cursor hem bireysel hem de ekip kullanımı için uygundur. Teams planı, kurumlara yönelik şu araçları sunar: SSO, ekip yönetimi, erişim kontrolleri ve kullanım analizleri.

<div id="creating-a-team">
  ## Bir Takım Oluşturma
</div>

Şu adımları izleyerek bir takım oluştur:

<Steps>
  <Step title="Teams planını ayarla">
    Bir takım oluşturmak için şu adımları izle:

    1. **Yeni kullanıcılar için**: Yeni bir hesap ve takım oluşturmak için [cursor.com/team/new-team](https://cursor.com/team/new-team) adresine git
    2. **Mevcut kullanıcılar için**: [dashboard](/tr/account/dashboard) sayfana git ve "Upgrade to Teams"e tıkla
  </Step>

  <Step title="Takım bilgilerini gir">
    Bir takım adı ve faturalama döngüsü seç

    <Frame>
      <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/new-team.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=3b9df20d032b544dcbc0343d9ddf056f" data-og-width="3456" width="3456" data-og-height="2158" height="2158" data-path="images/account/team/new-team.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/new-team.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=b81f3241069a8a0fb9278b6a2e246057 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/new-team.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=c26976bf06297d36ec9224ec1496a630 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/new-team.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=fed5c7c95914ff47cfceae81f1441208 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/new-team.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=0dc5986368419ef54f45803547741cfe 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/new-team.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=4eb38a9618399ddadbf7596b185d2732 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/new-team.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=1c7d720a1e20d2aa23463a1b9001d545 2500w" />
    </Frame>
  </Step>

  <Step title="Üyeleri davet et">
    Takım üyelerini davet et. Kullanıcı sayıları oransal olarak hesaplanır — sadece kullanıcıların üye olduğu süre için ödeme yaparsın.

    <Frame>
      <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/invite-members.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=bbd84dd96a7003415c2d2f038b1aaa77" style={{ paddingLeft: 16, paddingRight: 16, backgroundColor: '#0c0c0c' }} data-og-width="880" width="880" data-og-height="422" height="422" data-path="images/account/invite-members.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/invite-members.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=988e36ee874f704dfaae1b0a69ed2f84 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/invite-members.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=c0f85aacd3be59e11b1bfd05f9e5d6cd 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/invite-members.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=411456e375f8c406ad2972965e0b549e 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/invite-members.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=57ae04799be300a7e61464490344146f 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/invite-members.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=2faa0cf8ed56865c19916e33fde97900 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/invite-members.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=0bdb5040f44338e748246b4f1ddf2ddf 2500w" />
    </Frame>
  </Step>

  <Step title="SSO'yu etkinleştir (opsiyonel)">
    Güvenlik ve otomatik onboarding için [SSO](/tr/account/teams/sso)'yu etkinleştir.

    <Frame>
      <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=76608c26daf1f9ab2bbc2c4ccb156c0e" data-og-width="802" width="802" data-og-height="440" height="440" data-path="images/account/sso-settings.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=334dc1fc107338d19ec7b0052e7ea0e4 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=543b3d868c19960a5fb4c526d9895bd3 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=a06655178ba10f6a72919e9f7d598191 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=e280fc911306fe8d3b8e90b7221b0c11 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=ffd8f2c0168e2ac4f95431062b226021 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=1c17e4eac666b663d676ce874f1c4ba5 2500w" />
    </Frame>
  </Step>
</Steps>

<div id="faq">
  ## SSS
</div>

<AccordionGroup>
  <Accordion title="Ekibim Zscaler / proxy / VPN kullanıyor, Cursor çalışır mı?">
    Cursor varsayılan olarak HTTP/2 kullanır. Bazı proxy’ler ve VPN’ler bunu engelleyebilir.

    Bunun yerine HTTP/1.1 kullanmak için ayarlardan HTTP/1.1 geri dönüşünü etkinleştir.
  </Accordion>

  <Accordion title="Şirketim için lisansları nasıl satın alabilirim?">
    Cursor, koltuk yerine aktif kullanıcı başına ücretlendirir. Kullanıcıları istediğin zaman ekleyip kaldırabilirsin — yeni üyeler kalan süreleri için orantılı ücretlendirilir. Kaldırılan bir kullanıcı herhangi bir kredi kullandıysa, koltuğu fatura dönemi sonuna kadar dolu kalır.

    Yenileme tarihin aynı kalır.
  </Accordion>

  <Accordion title="Cursor’ı kullanmıyorken bir ekibi nasıl kurabilirim?">
    Lisans olmadan yönetebilmek için kendini [Unpaid Admin](/tr/account/teams/members) olarak ayarla.

    <Warning>
      Ekiplerin en az bir ücretli üyeye ihtiyacı var. Kurulumu yapabilir, bir üyeyi davet edebilir, sonra faturalandırmadan önce rolünü değiştirebilirsin.
    </Warning>
  </Accordion>

  <Accordion title="Cursor’ı şirketimin MDM’ine nasıl ekleyebilirim?">
    Tüm platformlar için indirme bağlantıları [cursor.com/downloads](https://cursor.com/downloads) adresinde.

    MDM yönergeleri:

    * [Omnissa Workspace ONE](https://docs.omnissa.com/bundle/MobileApplicationManagementVSaaS/page/DeployInternalApplications.html) (eski adıyla VMware)
    * [Microsoft Intune (Windows)](https://learn.microsoft.com/en-us/mem/intune-service/apps/apps-win32-app-management)
    * [Microsoft Intune (Mac)](https://learn.microsoft.com/en-us/mem/intune-service/apps/lob-apps-macos-dmg)
    * [Kandji MDM](https://support.kandji.io/kb/custom-apps-overview)
  </Accordion>
</AccordionGroup>



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



# Güncelleme Erişimi
Source: https://docs.cursor.com/tr/account/update-access

Güncellemeleri ne sıklıkla almak istediğini seç

export const Kbd = ({children, tooltip, os}) => {
  const keysInput = typeof children === 'string' && children.trim() !== '' ? children : null;
  if (!keysInput) {
    return null;
  }
  const isModifier = key => {
    const modifiers = ['⌘', '⇧', '⌥', '⌃', '⏎', '⌫', '⌦', '⎋', '⇥', '⌁', '←', '→', '↑', '↓', 'Ctrl', 'Shift', 'Alt', 'Cmd', 'Opt', 'Return', 'Backspace', 'Delete', 'Escape', 'Tab', 'Space', 'Enter', 'Esc', 'ArrowLeft', 'ArrowRight', 'ArrowUp', 'ArrowDown', 'Left', 'Right', 'Up', 'Down'];
    return modifiers.includes(key.trim());
  };
  const capitalizeFirstLetter = string => {
    return string.charAt(0).toUpperCase() + string.slice(1);
  };
  const isMac = os ? os.toLowerCase() === 'mac' || os.toLowerCase() === 'macos' : typeof navigator !== 'undefined' && (navigator.platform.toUpperCase().indexOf('MAC') >= 0 || navigator.userAgent.toUpperCase().indexOf('MAC') >= 0);
  const convertToSymbols = shortcut => {
    if (isMac) {
      return shortcut.replace(/⌘|Cmd|CMD/gi, '⌘').replace(/⌥|Opt|OPT/gi, '⌥').replace(/⌃|Ctrl/gi, '⌃').replace(/⇧|Shift/gi, '⇧').replace(/⏎|Return/gi, '⏎').replace(/⌫|Backspace/gi, '⌫').replace(/⌦|Delete/gi, '⌦').replace(/␛|Escape/gi, '␛').replace(/⇥|Tab/gi, '⇥').replace(/⌁|Space/gi, '⌁').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, '←').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, '→').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, '↑').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, '↓');
    } else {
      const converted = shortcut.replace(/⌘|Cmd|CMD/gi, 'Ctrl').replace(/⌥|Opt|OPT/gi, 'Alt').replace(/⌃|Ctrl/gi, 'Ctrl').replace(/⇧|Shift/gi, 'Shift').replace(/⏎|Return/gi, 'Enter').replace(/⌫|Backspace/gi, 'Backspace').replace(/⌦|Delete/gi, 'Delete').replace(/⎋|Escape/gi, 'Esc').replace(/⇥|Tab/gi, 'Tab').replace(/⌁|Space/gi, 'Space').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, 'Arrow-Left').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, 'Arrow-Right').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, 'Arrow-Up').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, 'Arrow-Down');
      const keyList = converted.split(/[\+\s]+/).filter(key => key.trim());
      return keyList.join('+');
    }
  };
  const convertToReadableText = shortcut => {
    const converted = shortcut.replace(/⌘|Cmd|CMD/gi, 'Cmd').replace(/⌥|Opt|OPT/gi, 'Opt').replace(/⌃|Ctrl/gi, 'Ctrl').replace(/⇧|Shift/gi, 'Shift').replace(/⏎|Return/gi, 'Return').replace(/⌫|Backspace/gi, 'Backspace').replace(/⌦|Delete/gi, 'Delete').replace(/⎋|Escape/gi, 'Escape').replace(/⇥|Tab/gi, 'Tab').replace(/⌁|Space/gi, 'Space').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, 'Arrow-Left').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, 'Arrow-Right').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, 'Arrow-Up').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, 'Arrow-Down');
    const keyList = converted.split(/[\+\s]+/).filter(key => key.trim());
    return keyList.map(key => {
      const trimmedKey = key.trim();
      return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
    }).join('+');
  };
  const displayShortcut = convertToSymbols(keysInput);
  const tooltipText = isMac ? tooltip ? `${convertToReadableText(keysInput)}: ${tooltip}` : convertToReadableText(keysInput) : tooltip || null;
  const processedKeys = isMac ? displayShortcut.split(/[\+\s]+/).filter(key => key.trim()).map(key => {
    const trimmedKey = key.trim();
    return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
  }).join('') : displayShortcut.split('+').map(key => {
    const trimmedKey = key.trim();
    return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
  }).join('+');
  return tooltipText ? <Tooltip tip={tooltipText}>
      <kbd>
        {processedKeys}
      </kbd>
    </Tooltip> : <kbd>
      {processedKeys}
    </kbd>;
};

Cursor'ın iki güncelleme kanalı var.

<Tabs>
  <Tab title="Default">
    Test edilmiş sürümlerle varsayılan güncelleme kanalı.

    * Kararlı sürümler
    * Ön sürüm testlerinden gelen hata düzeltmeleri
    * Tüm kullanıcılar için varsayılan
    * Ekip kullanıcıları için tek seçenek

    <Note>
      Ekip ve kurumsal hesaplar Default modunu kullanır.
    </Note>
  </Tab>

  <Tab title="Early Access">
    Yeni özellikler içeren ön sürüm sürümleri.

    <Warning>
      Early Access derlemeleri hatalar veya kararlılık sorunları içerebilir.
    </Warning>

    * Geliştirme aşamasındaki özelliklere erişim
    * Hata içerebilir
    * Ekip hesapları için kullanılamaz
  </Tab>
</Tabs>

<div id="change-update-channel">
  ## Güncelleme kanalını değiştir
</div>

1. **Ayarları aç**: <Kbd>Cmd+Shift+J</Kbd> tuşlarına bas
2. **Beta'ya git**: Kenar çubuğundan Beta'yı seç
3. **Kanalı seç**: Default veya Early Access'i seç

<Frame>
  <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/early-access.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=36c55c2deb93bc734b6ee0099a0d184c" data-og-width="1798" width="1798" data-og-height="442" height="442" data-path="images/account/early-access.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/early-access.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=624bfea7b3643f55afaa85b38b1c56e1 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/early-access.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=f32c8e59596f024223735b4f929949e0 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/early-access.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=bd8c4bf3265ab802b6188aa81a620244 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/early-access.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=e8600f42cc363c61377f158972187e01 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/early-access.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=32c83b2109587d299959c2d46ce67353 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/early-access.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=b2c4032824d39c62a7cbada5578b1a98 2500w" />
</Frame>

Early Access sorunlarını [Forum](https://forum.cursor.com) üzerinden bildir.



# Uygula
Source: https://docs.cursor.com/tr/agent/apply

Apply ile sohbetteki kod önerilerini nasıl uygular, kabul eder ya da reddedersin öğren

<div id="how-apply-works">
  ## Apply nasıl çalışır
</div>

Apply, sohbetin ürettiği kodu alıp dosyalarına entegre eden, Cursor’a özel bir modeldir. Sohbet içindeki kod bloklarını işler ve değişiklikleri kod tabanına uygular.

Apply kendi başına kod üretmez. Kodu sohbet modeli üretir, Apply ise entegrasyonunu mevcut dosyalara üstlenir. Birden fazla dosya ve büyük kod tabanları genelinde değişiklikleri işleyebilir.

<div id="apply-code-blocks">
  ## Kod bloklarını uygulama
</div>

Bir kod bloğu önerisini uygulamak için kod bloğunun sağ üst köşesindeki oynat düğmesine bas.

<Frame>
  <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/apply.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=634492fa2f63b4f6eada08b2a1ded47e" data-og-width="1032" width="1032" data-og-height="410" height="410" data-path="images/chat/apply.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/apply.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=7dbc88cfe20429c73e627a289b17c964 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/apply.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=721e2d51bdb16dbb817e19d96d93c9d9 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/apply.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=8faea188ca903e58d347ddfec2c9bf6e 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/apply.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=f3bc38701cab63602b54374dfaa9e024 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/apply.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=fddad51f5b12c32493e2370ed326712d 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/apply.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=1584d431007b33a595905e23b5e1b453 2500w" />
</Frame>



# Checkpoints
Source: https://docs.cursor.com/tr/agent/chat/checkpoints

Agent değişikliklerinden sonra önceki durumları kaydet ve geri yükle

Checkpoints, Agent'in kod tabanında yaptığı değişikliklerin otomatik anlık görüntüleridir. Gerekirse Agent’in yaptığı değişiklikleri geri almanı sağlar.

<Frame>
  <video src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/restore-checkpoint.mp4?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=7cededf7892f15a6342a81953ea0aa38" autoPlay loop muted playsInline controls data-path="images/chat/restore-checkpoint.mp4" />
</Frame>

<div id="restoring-checkpoints">
  ## Checkpoint’leri geri yükleme
</div>

Geri yüklemenin iki yolu var:

1. **Girdi kutusundan**: Önceki isteklerde `Restore Checkpoint` düğmesine tıkla
2. **Mesajdan**: Bir mesajın üzerine geldiğinde + düğmesine tıkla

<Warning>
  Checkpoint’ler sürüm kontrolü değildir. Kalıcı geçmiş için Git kullan.
</Warning>

<div id="how-they-work">
  ## Nasıl çalışır
</div>

* Yerelde saklanır, Git’ten ayrı
* Yalnızca Agent değişikliklerini izler (manuel düzenlemeleri değil)
* Otomatik olarak temizlenir

<Note>
  Manuel düzenlemeler izlenmez. Checkpoint’leri sadece Agent değişiklikleri için kullan.
</Note>

<div id="faq">
  ## SSS
</div>

<AccordionGroup>
  <Accordion title="Kontrol noktaları Git'i etkiler mi?">
    Hayır. Git geçmişinden bağımsızdır.
  </Accordion>

  {" "}

  <Accordion title="Ne kadar süre saklanır?">
    Geçerli oturum ve yakın geçmiş için. Otomatik olarak temizlenir.
  </Accordion>

  <Accordion title="Bunları elle oluşturabilir miyim?">
    Hayır. Cursor bunları otomatik olarak oluşturur.
  </Accordion>
</AccordionGroup>

{" "}



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



# Compact
Source: https://docs.cursor.com/tr/agent/chat/compact

Kompakt mod arayüzüyle sohbette yerden tasarruf et

Kompakt mod, görsel karmaşayı azaltarak ve sohbetler için kullanılabilir alanı en üst düzeye çıkararak yalın bir sohbet arayüzü sunar.

<div id="overview">
  ## Genel Bakış
</div>

Etkinleştirildiğinde, kompakt mod sohbet arayüzünü şöyle dönüştürür:

* Daha temiz, minimalist bir görünüm için **simgeleri gizler**
* Görsel karmaşayı azaltmak için **diff’leri otomatik olarak daraltır**
* Sohbet alanını en üst düzeye çıkarmak için **girdiyi otomatik olarak daraltır**

Bu ayar özellikle daha küçük ekranlarda çalışırken ya da odaklı, dikkat dağıtmayan bir sohbet deneyimi tercih ettiğinde işine yarar.

<div id="before-and-after">
  ## Önce ve Sonra
</div>

<div id="default-mode">
  ### Varsayılan mod
</div>

<Frame>
  <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/compact/off.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=e0f8b97ecd5201be396fcd09cec54de6" alt="Tüm simgelerin ve genişletilmiş öğelerin göründüğü varsayılan moddaki sohbet arayüzü" data-og-width="2048" width="2048" data-og-height="2350" height="2350" data-path="images/chat/compact/off.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/compact/off.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=9395c8d1f324033631508dc9cdfd6f3e 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/compact/off.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=5d8025ef65ad2fc9fe8c30e5c4fcda32 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/compact/off.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=28050b27b683af948bc1ed939f31786c 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/compact/off.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=dc443705188da9d3368acefd917cc890 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/compact/off.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=be6603e2cedb7e88e7c20d797b18599c 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/compact/off.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=3afe563c9cd4576623adce5dcaaccddf 2500w" />
</Frame>

<div id="compact-mode">
  ### Kompakt mod
</div>

<Frame>
  <img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/compact/on.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=e9f068889026827422b2a9d943b55ded" alt="Simgelerin gizlendiği ve öğelerin daraltıldığı kompakt moddaki sohbet arayüzü" data-og-width="2048" width="2048" data-og-height="2350" height="2350" data-path="images/chat/compact/on.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/compact/on.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=44e86a79eb893b4de6c57c65487bbe9a 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/compact/on.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=539b71c72ed2fb3508e3aec0624429c1 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/compact/on.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=2c0da715a5daf93e94dbf2a5eefbb7eb 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/compact/on.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=b5bddca39109779c9d91bb6bc8bb42e9 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/compact/on.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=8bb334bb055e49d4d51cd137d2396db0 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/compact/on.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=70730d151a24440eeb6dc31e18189c7d 2500w" />
</Frame>

<div id="enabling-compact-mode">
  ## Compact Mode’u etkinleştirme
</div>

Compact Mode’u etkinleştirmek için:

1. Cursor Settings’i aç
2. **Chat** ayarlarına git
3. **Compact Mode** anahtarını aç

Arayüz anında sadeleştirilmiş görünüme geçecek ve sohbetlerine odaklanman için daha fazla alan sunacak.



# Çoğalt
Source: https://docs.cursor.com/tr/agent/chat/duplicate

Bir konuşmanın herhangi bir noktasından dallar oluştur

Geçerli konuşmanı kaybetmeden alternatif çözümleri keşfetmek için sohbetleri çoğalt ya da çatalla.

<Frame>
  <video src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/duplicate-chat.mp4?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=29fdb23214ba3e2c5b94ccefc01f7615" autoPlay loop muted playsInline controls data-path="images/chat/duplicate-chat.mp4" />
</Frame>

<div id="how-to-duplicate">
  ## Nasıl kopyalanır
</div>

1. Ayrılmak istediğin yeri bul
2. Mesajdaki üç noktaya tıkla
3. "Duplicate Chat" seçeneğini seç

<div id="what-happens">
  ## Ne olur
</div>

* O ana kadarki bağlam korunur
* Orijinal konuşma değişmeden kalır
* Her iki sohbetin geçmişi ayrı ayrı tutulur



# Dışa Aktar
Source: https://docs.cursor.com/tr/agent/chat/export

Sohbetleri markdown formatına dışa aktar

Paylaşmak veya dokümantasyon için Agent sohbetlerini markdown dosyaları olarak dışa aktar.

<Frame>
  <video src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/export-chat.mp4?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=c6aa9d23a6a80ffae5864cd494907961" autoPlay loop muted playsInline controls data-path="images/chat/export-chat.mp4" />
</Frame>

<div id="whats-exported">
  ## Neler dışa aktarılır
</div>

* Tüm mesajlar ve yanıtlar
* Sözdizimi vurgulamalı kod blokları
* Dosya başvuruları ve bağlam
* Kronolojik sohbet akışı

<div id="how-to-export">
  ## Nasıl dışa aktarılır
</div>

1. Dışa aktaracağın sohbete git
2. Bağlam menüsüne tıkla → "Sohbeti Dışa Aktar"
3. Dosyayı yerel olarak kaydet

<Warning>
  Dışa aktarımları hassas veriler için gözden geçir: API anahtarları, dahili URL'ler, tescilli kod,
  kişisel bilgiler
</Warning>



# Geçmiş
Source: https://docs.cursor.com/tr/agent/chat/history

Sohbetleri görüntüle ve yönet

export const Kbd = ({children, tooltip, os}) => {
  const keysInput = typeof children === 'string' && children.trim() !== '' ? children : null;
  if (!keysInput) {
    return null;
  }
  const isModifier = key => {
    const modifiers = ['⌘', '⇧', '⌥', '⌃', '⏎', '⌫', '⌦', '⎋', '⇥', '⌁', '←', '→', '↑', '↓', 'Ctrl', 'Shift', 'Alt', 'Cmd', 'Opt', 'Return', 'Backspace', 'Delete', 'Escape', 'Tab', 'Space', 'Enter', 'Esc', 'ArrowLeft', 'ArrowRight', 'ArrowUp', 'ArrowDown', 'Left', 'Right', 'Up', 'Down'];
    return modifiers.includes(key.trim());
  };
  const capitalizeFirstLetter = string => {
    return string.charAt(0).toUpperCase() + string.slice(1);
  };
  const isMac = os ? os.toLowerCase() === 'mac' || os.toLowerCase() === 'macos' : typeof navigator !== 'undefined' && (navigator.platform.toUpperCase().indexOf('MAC') >= 0 || navigator.userAgent.toUpperCase().indexOf('MAC') >= 0);
  const convertToSymbols = shortcut => {
    if (isMac) {
      return shortcut.replace(/⌘|Cmd|CMD/gi, '⌘').replace(/⌥|Opt|OPT/gi, '⌥').replace(/⌃|Ctrl/gi, '⌃').replace(/⇧|Shift/gi, '⇧').replace(/⏎|Return/gi, '⏎').replace(/⌫|Backspace/gi, '⌫').replace(/⌦|Delete/gi, '⌦').replace(/␛|Escape/gi, '␛').replace(/⇥|Tab/gi, '⇥').replace(/⌁|Space/gi, '⌁').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, '←').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, '→').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, '↑').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, '↓');
    } else {
      const converted = shortcut.replace(/⌘|Cmd|CMD/gi, 'Ctrl').replace(/⌥|Opt|OPT/gi, 'Alt').replace(/⌃|Ctrl/gi, 'Ctrl').replace(/⇧|Shift/gi, 'Shift').replace(/⏎|Return/gi, 'Enter').replace(/⌫|Backspace/gi, 'Backspace').replace(/⌦|Delete/gi, 'Delete').replace(/⎋|Escape/gi, 'Esc').replace(/⇥|Tab/gi, 'Tab').replace(/⌁|Space/gi, 'Space').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, 'Arrow-Left').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, 'Arrow-Right').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, 'Arrow-Up').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, 'Arrow-Down');
      const keyList = converted.split(/[\+\s]+/).filter(key => key.trim());
      return keyList.join('+');
    }
  };
  const convertToReadableText = shortcut => {
    const converted = shortcut.replace(/⌘|Cmd|CMD/gi, 'Cmd').replace(/⌥|Opt|OPT/gi, 'Opt').replace(/⌃|Ctrl/gi, 'Ctrl').replace(/⇧|Shift/gi, 'Shift').replace(/⏎|Return/gi, 'Return').replace(/⌫|Backspace/gi, 'Backspace').replace(/⌦|Delete/gi, 'Delete').replace(/⎋|Escape/gi, 'Escape').replace(/⇥|Tab/gi, 'Tab').replace(/⌁|Space/gi, 'Space').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, 'Arrow-Left').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, 'Arrow-Right').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, 'Arrow-Up').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, 'Arrow-Down');
    const keyList = converted.split(/[\+\s]+/).filter(key => key.trim());
    return keyList.map(key => {
      const trimmedKey = key.trim();
      return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
    }).join('+');
  };
  const displayShortcut = convertToSymbols(keysInput);
  const tooltipText = isMac ? tooltip ? `${convertToReadableText(keysInput)}: ${tooltip}` : convertToReadableText(keysInput) : tooltip || null;
  const processedKeys = isMac ? displayShortcut.split(/[\+\s]+/).filter(key => key.trim()).map(key => {
    const trimmedKey = key.trim();
    return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
  }).join('') : displayShortcut.split('+').map(key => {
    const trimmedKey = key.trim();
    return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
  }).join('+');
  return tooltipText ? <Tooltip tip={tooltipText}>
      <kbd>
        {processedKeys}
      </kbd>
    </Tooltip> : <kbd>
      {processedKeys}
    </kbd>;
};

Geçmiş panelinden önceki Agent sohbetlerine eriş.

<Frame>
  <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/chat-history.jpeg?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=d9ec96fad0c8c2fb132bbf5ce8ea35f7" alt="Chat History" data-og-width="2048" width="2048" data-og-height="1317" height="1317" data-path="images/chat/chat-history.jpeg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/chat-history.jpeg?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=a3ad71e9891c3c9642f4288953a78e97 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/chat-history.jpeg?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=76139a177ebfeb0c55add7fb955f9000 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/chat-history.jpeg?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=1af22180859c017542777ab36b434b7a 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/chat-history.jpeg?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=751e7fa0888e5790f841432ef7521337 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/chat-history.jpeg?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=86b447c18601a9d44af8866d0042719e 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/chat-history.jpeg?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=88c84a8fb1b764ad3070e3211f539408 2500w" />
</Frame>

<div id="opening-history">
  ## Geçmişi açma
</div>

* Agent yan panelinde geçmiş simgesine tıkla
* Sohbet geçmişini açmak için <Kbd tooltip="Open chat history">Opt Cmd '</Kbd> tuşlarına bas

<div id="managing-chats">
  ## Sohbetleri yönetme
</div>

* **Başlıkları düzenle**: Yeniden adlandırmak için tıkla
* **Sil**: Gereksiz sohbetleri kaldır
* **Aç**: Tüm konuşmayı görmek için tıkla

Sohbet geçmişi, makinenizdeki bir SQLite veritabanında yerel olarak saklanır.

<Note>
  Sohbetleri saklamak için [markdown olarak dışa aktar](/tr/agent/chats/export).
</Note>

## Arka Plan Agent'ları

Arka plan agent sohbetleri normal geçmişte görünmez; bunun yerine uzak bir veritabanında saklanır. Görüntülemek için <Kbd tooltip="Arka plan agent kontrol panelini aç">Cmd E</Kbd> kullan.

<div id="referencing-past-chats">
  ## Geçmiş sohbetlere referans verme
</div>

Önceki konuşmalardaki bağlamı mevcut sohbetine eklemek için [@Past Chats](/tr/context/@-symbols/@-past-chats)’i kullan.



# Özetleme
Source: https://docs.cursor.com/tr/agent/chat/summarization

Sohbette uzun konuşmalar için bağlam yönetimi

<div id="message-summarization">
  ## Mesaj özetleme
</div>

Sohbetler uzadıkça, Cursor sohbetlerini verimli tutmak için bağlamı otomatik olarak özetleyip yönetir. Bağlam menüsünü nasıl kullanacağını ve dosyaların modelin bağlam pencerelerine sığması için nasıl yoğunlaştırıldığını öğren.

<div id="using-the-summarize-command">
  ### /summarize komutunu kullanma
</div>

Sohbette `/summarize` komutunu kullanarak özetlemeyi manuel olarak tetikleyebilirsin. Bu komut, konuşmalar çok uzadığında bağlamı yönetmene yardımcı olur; böylece önemli bilgileri kaybetmeden verimli şekilde çalışmaya devam edebilirsin.

<Info>
  Cursor'da bağlamın nasıl çalıştığını daha ayrıntılı öğrenmek için [Working with
  Context](/tr/guides/working-with-context) rehberimize göz at.
</Info>

<div id="how-summarization-works">
  ### Özetleme nasıl çalışır
</div>

Sohbet uzadıkça, modelin bağlam penceresi sınırını aşabilir:

<Frame>
  <div className="font-mono text-xs w-full bg-neutral-100 p-4 rounded-lg">
    <div className="relative">
      <div className="bg-white px-3 py-2 mb-2 rounded border border-dashed border-neutral-400 w-full">
        <div className="text-xs text-neutral-700 font-medium">User</div>
      </div>

      <div className="bg-white px-3 py-2 mb-2 rounded border border-dashed border-neutral-400 w-full">
        <div className="text-xs text-neutral-700 font-medium">Cursor</div>
      </div>

      <div className="bg-white px-3 py-2 mb-2 rounded border border-dashed border-neutral-400 w-full">
        <div className="text-xs text-neutral-700 font-medium">User</div>
      </div>

      <div className="relative my-4">
        <div className="absolute top-0 left-1/2 transform -translate-x-1/2 -translate-y-1/2 text-center text-xs text-black bg-neutral-100 px-2">Bağlam penceresi sınırı</div>

        <div className="w-full h-px bg-black" />
      </div>

      <div className="bg-white px-3 py-2 mb-2 rounded border border-neutral-400 w-full">
        <div className="text-xs text-neutral-700 font-medium">Cursor</div>
      </div>

      <div className="bg-white px-3 py-2 mb-2 rounded border border-neutral-400 w-full">
        <div className="text-xs text-neutral-700 font-medium">User</div>
      </div>

      <div className="bg-white px-3 py-2 mb-2 rounded border border-neutral-400 w-full">
        <div className="text-xs text-neutral-700 font-medium">Cursor</div>
      </div>
    </div>
  </div>
</Frame>

Bunu aşmak için Cursor, yeni mesajlara yer açmak amacıyla eski mesajları özetler.

<Frame>
  <div className="font-mono text-xs w-full bg-neutral-100 p-4 rounded-lg">
    <div className="relative">
      <div className="relative my-4">
        <div className="absolute top-0 left-1/2 transform -translate-x-1/2 -translate-y-1/2 text-center text-xs text-black bg-neutral-100 px-2">
          Bağlam penceresi sınırı
        </div>

        <div className="w-full h-px bg-black" />
      </div>

      <div className="bg-neutral-100 px-3 py-2 mb-2 rounded border border-dashed border-neutral-400 w-full">
        <div className="text-xs text-neutral-700 font-medium">
          Özetlenen Mesajlar
        </div>
      </div>

      <div className="bg-white px-3 py-2 mb-2 rounded border border-neutral-400 w-full">
        <div className="text-xs text-neutral-700 font-medium">Cursor</div>
      </div>

      <div className="bg-white px-3 py-2 mb-2 rounded border border-neutral-400 w-full">
        <div className="text-xs text-neutral-700 font-medium">User</div>
      </div>

      <div className="bg-white px-3 py-2 mb-2 rounded border border-neutral-400 w-full">
        <div className="text-xs text-neutral-700 font-medium">Cursor</div>
      </div>
    </div>
  </div>
</Frame>

<div id="file-folder-condensation">
  ## Dosya ve klasör yoğunlaştırma
</div>

Sohbet özetleme uzun konuşmaları ele alırken, Cursor büyük dosya ve klasörleri yönetmek için farklı bir strateji kullanır: **akıllı yoğunlaştırma**. Sohbetine dosya eklediğinde, Cursor bunları boyutlarına ve kullanılabilir bağlam alanına göre sunmanın en iyi yolunu belirler.

Bir dosya/klasörün alabileceği farklı durumlar şunlardır:

<div id="condensed">
  ### Özetlenmiş
</div>

Dosya veya klasörler bağlam penceresine sığmayacak kadar büyük olduğunda, Cursor bunları otomatik olarak özetler. Özetleme, modele işlev imzaları, sınıflar ve yöntemler gibi temel yapısal öğeleri gösterir. Bu özet görünümden model, gerekirse belirli dosyaları genişletmeyi seçebilir. Bu yaklaşım, mevcut bağlam penceresinin etkin kullanımını en üst düzeye çıkarır.

<Frame>
  <img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/context-management/condensed.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=0c3a07b6fef6402945138f7ee38b44c1" alt="Bağlam menüsü" data-og-width="1226" width="1226" data-og-height="793" height="793" data-path="images/context/context-management/condensed.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/context-management/condensed.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=4cc08626f9cfce1d186cdd6aa96c7d09 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/context-management/condensed.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=fa49ce9605bdb0186c98712f4c0a32cc 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/context-management/condensed.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=84874b2f40bff0a2cd54796865469914 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/context-management/condensed.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=050290a85c154e92f9298883afcdf892 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/context-management/condensed.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=f953aa28f11926b2d6fdf734cf928402 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/context-management/condensed.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=50aa9973ccf2027814860f3d97a2b031 2500w" />
</Frame>

<div id="significantly-condensed">
  ### Önemli ölçüde kısaltıldı
</div>

Bir dosya adı "Önemli ölçüde kısaltıldı" etiketini taşıyorsa, dosya tam hâliyle, hatta kısaltılmış biçimde bile dahil edilemeyecek kadar büyüktü. Modele yalnızca dosya adı gösterilecek.

<div id="not-included">
  ### Kapsama alınmadı
</div>

Bir dosya veya klasörün yanında bir uyarı simgesi belirdiğinde, öğe, yoğunlaştırılmış biçimde bile bağlam penceresine sığmayacak kadar büyük demektir. Bu, kod tabanının hangi kısımlarının modele erişilebilir olduğunu anlamana yardımcı olur.

<Frame>
  <img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/context-management/not-included.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=06df9854c74c257d1ceb7d18b1864ceb" alt="Context menu" data-og-width="1090" width="1090" data-og-height="346" height="346" data-path="images/context/context-management/not-included.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/context-management/not-included.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=072e75878f27a151f1310007d0e5e534 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/context-management/not-included.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=c6f3f71351ddf8e367096651b455bf9d 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/context-management/not-included.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=c407f7870412007549f8eb2871f9ca12 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/context-management/not-included.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=b0d17023b5734c8d7584c56f5419bd1a 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/context-management/not-included.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=f1bedff398cee6c957fe62877f7d2012 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/context-management/not-included.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=8b00fbaff658c384f69bfddf3f3a4cfe 2500w" />
</Frame>



# Sekmeler
Source: https://docs.cursor.com/tr/agent/chat/tabs

Birden fazla Agent sohbetini aynı anda yürüt

export const Kbd = ({children, tooltip, os}) => {
  const keysInput = typeof children === 'string' && children.trim() !== '' ? children : null;
  if (!keysInput) {
    return null;
  }
  const isModifier = key => {
    const modifiers = ['⌘', '⇧', '⌥', '⌃', '⏎', '⌫', '⌦', '⎋', '⇥', '⌁', '←', '→', '↑', '↓', 'Ctrl', 'Shift', 'Alt', 'Cmd', 'Opt', 'Return', 'Backspace', 'Delete', 'Escape', 'Tab', 'Space', 'Enter', 'Esc', 'ArrowLeft', 'ArrowRight', 'ArrowUp', 'ArrowDown', 'Left', 'Right', 'Up', 'Down'];
    return modifiers.includes(key.trim());
  };
  const capitalizeFirstLetter = string => {
    return string.charAt(0).toUpperCase() + string.slice(1);
  };
  const isMac = os ? os.toLowerCase() === 'mac' || os.toLowerCase() === 'macos' : typeof navigator !== 'undefined' && (navigator.platform.toUpperCase().indexOf('MAC') >= 0 || navigator.userAgent.toUpperCase().indexOf('MAC') >= 0);
  const convertToSymbols = shortcut => {
    if (isMac) {
      return shortcut.replace(/⌘|Cmd|CMD/gi, '⌘').replace(/⌥|Opt|OPT/gi, '⌥').replace(/⌃|Ctrl/gi, '⌃').replace(/⇧|Shift/gi, '⇧').replace(/⏎|Return/gi, '⏎').replace(/⌫|Backspace/gi, '⌫').replace(/⌦|Delete/gi, '⌦').replace(/␛|Escape/gi, '␛').replace(/⇥|Tab/gi, '⇥').replace(/⌁|Space/gi, '⌁').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, '←').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, '→').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, '↑').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, '↓');
    } else {
      const converted = shortcut.replace(/⌘|Cmd|CMD/gi, 'Ctrl').replace(/⌥|Opt|OPT/gi, 'Alt').replace(/⌃|Ctrl/gi, 'Ctrl').replace(/⇧|Shift/gi, 'Shift').replace(/⏎|Return/gi, 'Enter').replace(/⌫|Backspace/gi, 'Backspace').replace(/⌦|Delete/gi, 'Delete').replace(/⎋|Escape/gi, 'Esc').replace(/⇥|Tab/gi, 'Tab').replace(/⌁|Space/gi, 'Space').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, 'Arrow-Left').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, 'Arrow-Right').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, 'Arrow-Up').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, 'Arrow-Down');
      const keyList = converted.split(/[\+\s]+/).filter(key => key.trim());
      return keyList.join('+');
    }
  };
  const convertToReadableText = shortcut => {
    const converted = shortcut.replace(/⌘|Cmd|CMD/gi, 'Cmd').replace(/⌥|Opt|OPT/gi, 'Opt').replace(/⌃|Ctrl/gi, 'Ctrl').replace(/⇧|Shift/gi, 'Shift').replace(/⏎|Return/gi, 'Return').replace(/⌫|Backspace/gi, 'Backspace').replace(/⌦|Delete/gi, 'Delete').replace(/⎋|Escape/gi, 'Escape').replace(/⇥|Tab/gi, 'Tab').replace(/⌁|Space/gi, 'Space').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, 'Arrow-Left').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, 'Arrow-Right').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, 'Arrow-Up').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, 'Arrow-Down');
    const keyList = converted.split(/[\+\s]+/).filter(key => key.trim());
    return keyList.map(key => {
      const trimmedKey = key.trim();
      return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
    }).join('+');
  };
  const displayShortcut = convertToSymbols(keysInput);
  const tooltipText = isMac ? tooltip ? `${convertToReadableText(keysInput)}: ${tooltip}` : convertToReadableText(keysInput) : tooltip || null;
  const processedKeys = isMac ? displayShortcut.split(/[\+\s]+/).filter(key => key.trim()).map(key => {
    const trimmedKey = key.trim();
    return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
  }).join('') : displayShortcut.split('+').map(key => {
    const trimmedKey = key.trim();
    return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
  }).join('+');
  return tooltipText ? <Tooltip tip={tooltipText}>
      <kbd>
        {processedKeys}
      </kbd>
    </Tooltip> : <kbd>
      {processedKeys}
    </kbd>;
};

<Frame>
  <video src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/chat-tabs.mp4?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=57fd5305279dc0a3139055b353ce4b7a" autoPlay loop muted playsInline controls data-path="images/chat/chat-tabs.mp4" />
</Frame>

<div id="overview">
  ## Genel Bakış
</div>

Yeni sekmeler oluşturmak için <Kbd>Cmd+T</Kbd> tuşlarına bas. Her sekme kendi konuşma geçmişini, bağlamını ve model seçimini ayrı ayrı tutar.

<Tip>
  Paralel iş akışları için [Background Agents](/tr/background-agents)'ı deneyebilirsin
</Tip>

<div id="managing-tabs">
  ## Sekmeleri yönetme
</div>

* <Kbd>Cmd+T</Kbd> ile yeni sekmeler oluştur. Her sekme yeni bir konuşmayla başlar ve kendi bağlamını korur.

* Sekmeler arasında başlıklarına tıklayarak ya da <Kbd>Ctrl+Tab</Kbd> ile aralarında dolaşarak geçiş yap.

* Sekme başlıkları ilk mesajdan sonra otomatik oluşturulur, ancak sekme başlığına sağ tıklayarak yeniden adlandırabilirsin.

<Tip>
  Her sekmede tek bir görev yürüt, net bir başlangıç açıklaması ver ve çalışma alanını düzenli tutmak için tamamlanan
  sekmeleri kapat.
</Tip>

<div id="conflicts">
  ### Çakışmalar
</div>

Cursor, birden fazla sekmenin aynı dosyaları düzenlemesini engeller. Çakışmaları çözmen için uyarı alırsın.

<div id="reference-other-chats">
  ## Diğer sohbetlere başvur
</div>

Diğer sekmelerden veya önceki oturumlardan bağlam eklemek için [@Past Chats](/tr/context/@-symbols/@-past-chats) kullan.



# Modlar
Source: https://docs.cursor.com/tr/agent/modes

Görevine uygun modu seç — otonom kodlamadan odaklı düzenlemelere

export const Kbd = ({children, tooltip, os}) => {
  const keysInput = typeof children === 'string' && children.trim() !== '' ? children : null;
  if (!keysInput) {
    return null;
  }
  const isModifier = key => {
    const modifiers = ['⌘', '⇧', '⌥', '⌃', '⏎', '⌫', '⌦', '⎋', '⇥', '⌁', '←', '→', '↑', '↓', 'Ctrl', 'Shift', 'Alt', 'Cmd', 'Opt', 'Return', 'Backspace', 'Delete', 'Escape', 'Tab', 'Space', 'Enter', 'Esc', 'ArrowLeft', 'ArrowRight', 'ArrowUp', 'ArrowDown', 'Left', 'Right', 'Up', 'Down'];
    return modifiers.includes(key.trim());
  };
  const capitalizeFirstLetter = string => {
    return string.charAt(0).toUpperCase() + string.slice(1);
  };
  const isMac = os ? os.toLowerCase() === 'mac' || os.toLowerCase() === 'macos' : typeof navigator !== 'undefined' && (navigator.platform.toUpperCase().indexOf('MAC') >= 0 || navigator.userAgent.toUpperCase().indexOf('MAC') >= 0);
  const convertToSymbols = shortcut => {
    if (isMac) {
      return shortcut.replace(/⌘|Cmd|CMD/gi, '⌘').replace(/⌥|Opt|OPT/gi, '⌥').replace(/⌃|Ctrl/gi, '⌃').replace(/⇧|Shift/gi, '⇧').replace(/⏎|Return/gi, '⏎').replace(/⌫|Backspace/gi, '⌫').replace(/⌦|Delete/gi, '⌦').replace(/␛|Escape/gi, '␛').replace(/⇥|Tab/gi, '⇥').replace(/⌁|Space/gi, '⌁').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, '←').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, '→').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, '↑').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, '↓');
    } else {
      const converted = shortcut.replace(/⌘|Cmd|CMD/gi, 'Ctrl').replace(/⌥|Opt|OPT/gi, 'Alt').replace(/⌃|Ctrl/gi, 'Ctrl').replace(/⇧|Shift/gi, 'Shift').replace(/⏎|Return/gi, 'Enter').replace(/⌫|Backspace/gi, 'Backspace').replace(/⌦|Delete/gi, 'Delete').replace(/⎋|Escape/gi, 'Esc').replace(/⇥|Tab/gi, 'Tab').replace(/⌁|Space/gi, 'Space').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, 'Arrow-Left').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, 'Arrow-Right').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, 'Arrow-Up').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, 'Arrow-Down');
      const keyList = converted.split(/[\+\s]+/).filter(key => key.trim());
      return keyList.join('+');
    }
  };
  const convertToReadableText = shortcut => {
    const converted = shortcut.replace(/⌘|Cmd|CMD/gi, 'Cmd').replace(/⌥|Opt|OPT/gi, 'Opt').replace(/⌃|Ctrl/gi, 'Ctrl').replace(/⇧|Shift/gi, 'Shift').replace(/⏎|Return/gi, 'Return').replace(/⌫|Backspace/gi, 'Backspace').replace(/⌦|Delete/gi, 'Delete').replace(/⎋|Escape/gi, 'Escape').replace(/⇥|Tab/gi, 'Tab').replace(/⌁|Space/gi, 'Space').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, 'Arrow-Left').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, 'Arrow-Right').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, 'Arrow-Up').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, 'Arrow-Down');
    const keyList = converted.split(/[\+\s]+/).filter(key => key.trim());
    return keyList.map(key => {
      const trimmedKey = key.trim();
      return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
    }).join('+');
  };
  const displayShortcut = convertToSymbols(keysInput);
  const tooltipText = isMac ? tooltip ? `${convertToReadableText(keysInput)}: ${tooltip}` : convertToReadableText(keysInput) : tooltip || null;
  const processedKeys = isMac ? displayShortcut.split(/[\+\s]+/).filter(key => key.trim()).map(key => {
    const trimmedKey = key.trim();
    return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
  }).join('') : displayShortcut.split('+').map(key => {
    const trimmedKey = key.trim();
    return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
  }).join('+');
  return tooltipText ? <Tooltip tip={tooltipText}>
      <kbd>
        {processedKeys}
      </kbd>
    </Tooltip> : <kbd>
      {processedKeys}
    </kbd>;
};

Agent, belirli görevler için optimize edilmiş farklı modlar sunar. Her mod, iş akışı ihtiyaçlarına uygun olacak şekilde etkinleştirilen farklı yeteneklere ve araçlara sahiptir.

<div className="full-width-table">
  | Mod                   | Kullanım amacı                   | Yetenekler                                 | Araçlar                 |
  | :-------------------- | :------------------------------- | :----------------------------------------- | :---------------------- |
  | **[Agent](#agent)**   | Karmaşık özellikler, refactoring | Otonom keşif, çok dosyalı düzenlemeler     | Tüm araçlar etkin       |
  | **[Ask](#ask)**       | Öğrenme, planlama, sorular       | Salt okunur keşif, otomatik değişiklik yok | Yalnızca arama araçları |
  | **[Custom](#custom)** | Özelleşmiş iş akışları           | Kullanıcı tanımlı yetenekler               | Yapılandırılabilir      |
</div>

<div id="agent">
  ## Agent
</div>

Karmaşık kodlama görevleri için varsayılan mod. Agent, isteklerini tamamlamak için kod tabanını kendi kendine keşfeder, birden fazla dosyayı düzenler, komutlar çalıştırır ve hataları düzeltir.

<Frame>
  <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/agent.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=9cd06dd9f59e019b3d76aa0fd9f934ba" data-og-width="3600" width="3600" data-og-height="2025" height="2025" data-path="images/chat/agent.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/agent.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=d979435c61e2112ebcb784f16a49327f 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/agent.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=1a88e2085ffe80f02daea9a523887282 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/agent.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=de98a8bf766c3f35a6187e87190e30f9 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/agent.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=8648638c4240b718e0512a6ec2274171 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/agent.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=45b9898d65f5b425d276eaa44d4e1940 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/agent.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=30fef2b190d453ee0166e554a4005bd1 2500w" />
</Frame>

<div id="ask">
  ## Ask
</div>

Öğrenme ve keşif için salt okunur mod. Ask, kod tabanında arama yapar ve hiçbir değişiklik yapmadan yanıtlar verir — kodu değiştirmeden önce anlamak için ideal.

<Frame>
  <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/ask.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=15e531cb84f0a18228723870fd84fa4f" data-og-width="3600" width="3600" data-og-height="2025" height="2025" data-path="images/chat/ask.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/ask.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=592ac5a681910a075ae88dec89bee25d 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/ask.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=74b98cce3b5bb83c79d0566cd3c65c34 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/ask.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=c4d80f50e20e7ca28db5a3ee71718979 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/ask.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=a4a6e017fd64149cf68d997114bbf6b6 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/ask.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=7354479ecd644b86ddbcb9fe1131f100 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/ask.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=274125e614eadd17522e0dacfcc6a38e 2500w" />
</Frame>

<div id="custom">
  ## Özel
</div>

Belirli araç kombinasyonları ve yönergelerle kendi modlarını oluştur. Yetenekleri karıştırıp eşleştirerek iş akışına uydur.

<Note>
  Özel modlar beta aşamasında. `Cursor Settings` → `Chat` → `Custom
      Modes` yolundan etkinleştir
</Note>

<div id="examples">
  ### Örnekler
</div>

<AccordionGroup>
  <Accordion title="Learn">
    **Tools:** All Search\
    **Instructions:** Kavramları kapsamlı biçimde açıklamaya odaklan ve netleştirici sorular sor
  </Accordion>

  {" "}

  <Accordion title="Refactor">
    **Tools:** Edit & Reapply **Instructions:** Yeni işlev eklemeden kod yapısını iyileştir
  </Accordion>

  {" "}

  <Accordion title="Plan">
    **Tools:** Codebase, Read file, Terminal **Instructions:** `plan.md` içinde ayrıntılı uygulama planları oluştur
  </Accordion>

  <Accordion title="Debug">
    **Tools:** All Search, Terminal, Edit & Reapply\
    **Instructions:** Düzeltmeler önermeden önce sorunları kapsamlı şekilde araştır
  </Accordion>
</AccordionGroup>

<div id="switching-modes">
  ## Modlar arasında geçiş
</div>

* Agent’ta mod seçici açılır menüsünü kullan
* Hızlı geçiş için <Kbd>Cmd+.</Kbd> tuşlarına bas
* Klavye kısayollarını [ayarlar](#settings) bölümünden belirle

<div id="settings">
  ## Ayarlar
</div>

Tüm modlar ortak yapılandırma seçeneklerini paylaşır:

<div className="full-width-table">
  | Ayar               | Açıklama                                      |
  | :----------------- | :-------------------------------------------- |
  | Model              | Hangi yapay zeka modelini kullanacağını seç   |
  | Klavye kısayolları | Modlar arasında geçiş için kısayolları ayarla |
</div>

Moda özel ayarlar:

<div className="full-width-table">
  | Mod        | Ayarlar                              | Açıklama                                              |
  | :--------- | :----------------------------------- | :---------------------------------------------------- |
  | **Agent**  | Otomatik çalıştır ve otomatik düzelt | Komutları otomatik çalıştır ve hataları düzelt        |
  | **Ask**    | Kod tabanında ara                    | İlgili dosyaları otomatik olarak bul                  |
  | **Custom** | Araç seçimi ve yönergeler            | [tools](/tr/agent/tools) ve özel istemleri yapılandır |
</div>



# Genel Bakış
Source: https://docs.cursor.com/tr/agent/overview

Otonom kodlama görevleri, terminal komutları ve kod düzenleme için asistan

export const Kbd = ({children, tooltip, os}) => {
  const keysInput = typeof children === 'string' && children.trim() !== '' ? children : null;
  if (!keysInput) {
    return null;
  }
  const isModifier = key => {
    const modifiers = ['⌘', '⇧', '⌥', '⌃', '⏎', '⌫', '⌦', '⎋', '⇥', '⌁', '←', '→', '↑', '↓', 'Ctrl', 'Shift', 'Alt', 'Cmd', 'Opt', 'Return', 'Backspace', 'Delete', 'Escape', 'Tab', 'Space', 'Enter', 'Esc', 'ArrowLeft', 'ArrowRight', 'ArrowUp', 'ArrowDown', 'Left', 'Right', 'Up', 'Down'];
    return modifiers.includes(key.trim());
  };
  const capitalizeFirstLetter = string => {
    return string.charAt(0).toUpperCase() + string.slice(1);
  };
  const isMac = os ? os.toLowerCase() === 'mac' || os.toLowerCase() === 'macos' : typeof navigator !== 'undefined' && (navigator.platform.toUpperCase().indexOf('MAC') >= 0 || navigator.userAgent.toUpperCase().indexOf('MAC') >= 0);
  const convertToSymbols = shortcut => {
    if (isMac) {
      return shortcut.replace(/⌘|Cmd|CMD/gi, '⌘').replace(/⌥|Opt|OPT/gi, '⌥').replace(/⌃|Ctrl/gi, '⌃').replace(/⇧|Shift/gi, '⇧').replace(/⏎|Return/gi, '⏎').replace(/⌫|Backspace/gi, '⌫').replace(/⌦|Delete/gi, '⌦').replace(/␛|Escape/gi, '␛').replace(/⇥|Tab/gi, '⇥').replace(/⌁|Space/gi, '⌁').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, '←').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, '→').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, '↑').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, '↓');
    } else {
      const converted = shortcut.replace(/⌘|Cmd|CMD/gi, 'Ctrl').replace(/⌥|Opt|OPT/gi, 'Alt').replace(/⌃|Ctrl/gi, 'Ctrl').replace(/⇧|Shift/gi, 'Shift').replace(/⏎|Return/gi, 'Enter').replace(/⌫|Backspace/gi, 'Backspace').replace(/⌦|Delete/gi, 'Delete').replace(/⎋|Escape/gi, 'Esc').replace(/⇥|Tab/gi, 'Tab').replace(/⌁|Space/gi, 'Space').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, 'Arrow-Left').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, 'Arrow-Right').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, 'Arrow-Up').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, 'Arrow-Down');
      const keyList = converted.split(/[\+\s]+/).filter(key => key.trim());
      return keyList.join('+');
    }
  };
  const convertToReadableText = shortcut => {
    const converted = shortcut.replace(/⌘|Cmd|CMD/gi, 'Cmd').replace(/⌥|Opt|OPT/gi, 'Opt').replace(/⌃|Ctrl/gi, 'Ctrl').replace(/⇧|Shift/gi, 'Shift').replace(/⏎|Return/gi, 'Return').replace(/⌫|Backspace/gi, 'Backspace').replace(/⌦|Delete/gi, 'Delete').replace(/⎋|Escape/gi, 'Escape').replace(/⇥|Tab/gi, 'Tab').replace(/⌁|Space/gi, 'Space').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, 'Arrow-Left').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, 'Arrow-Right').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, 'Arrow-Up').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, 'Arrow-Down');
    const keyList = converted.split(/[\+\s]+/).filter(key => key.trim());
    return keyList.map(key => {
      const trimmedKey = key.trim();
      return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
    }).join('+');
  };
  const displayShortcut = convertToSymbols(keysInput);
  const tooltipText = isMac ? tooltip ? `${convertToReadableText(keysInput)}: ${tooltip}` : convertToReadableText(keysInput) : tooltip || null;
  const processedKeys = isMac ? displayShortcut.split(/[\+\s]+/).filter(key => key.trim()).map(key => {
    const trimmedKey = key.trim();
    return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
  }).join('') : displayShortcut.split('+').map(key => {
    const trimmedKey = key.trim();
    return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
  }).join('+');
  return tooltipText ? <Tooltip tip={tooltipText}>
      <kbd>
        {processedKeys}
      </kbd>
    </Tooltip> : <kbd>
      {processedKeys}
    </kbd>;
};

Agent, Cursor’ın karmaşık kodlama görevlerini kendi başına tamamlayabilen, terminal komutları çalıştırabilen ve kod düzenleyebilen asistanı. Yan panelden <Kbd>Cmd+I</Kbd> ile eriş.

<Frame caption="Yan panelde Agent">
  <video src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/overview.mp4?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=b17d6a1225b4992ea19978b6a6c259e1" autoPlay loop muted playsInline data-path="images/chat/overview.mp4" />
</Frame>

<div className="mt-24 flex flex-col gap-12">
  <Columns className="gap-4">
    <div>
      <h2 className="text-lg font-medium mb-2">
        <a href="/tr/agent/modes" className="hover:text-primary transition-colors">
          Modlar
        </a>
      </h2>

      <p className="text-sm">
        Agent, Ask arasında seçim yap ya da özel modlar oluştur. Her mod,
        iş akışına uyan farklı yetenekler ve araçlar sunar.
      </p>
    </div>

    <Frame>
      <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/agent.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=9cd06dd9f59e019b3d76aa0fd9f934ba" alt="Agent modları" data-og-width="3600" width="3600" data-og-height="2025" height="2025" data-path="images/chat/agent.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/agent.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=d979435c61e2112ebcb784f16a49327f 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/agent.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=1a88e2085ffe80f02daea9a523887282 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/agent.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=de98a8bf766c3f35a6187e87190e30f9 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/agent.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=8648638c4240b718e0512a6ec2274171 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/agent.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=45b9898d65f5b425d276eaa44d4e1940 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/agent.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=30fef2b190d453ee0166e554a4005bd1 2500w" />
    </Frame>
  </Columns>

  <Columns className="gap-4">
    <div>
      <h3 className="text-lg font-medium mb-2">
        <a href="/tr/agent/tools" className="hover:text-primary transition-colors">
          Araçlar
        </a>
      </h3>

      <p className="text-sm">
        Agent, arama yapma, düzenleme ve komut çalıştırma için araçlar kullanır. Anlamsal kod tabanı
        aramadan terminalde çalıştırmaya kadar bu araçlar, görevleri
        kendi başına tamamlamasını sağlar.
      </p>
    </div>

    <div>
      <Frame>
        <img src="https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=3135722076a5aa636d27dbedec665bae" alt="Agent tools" data-og-width="1624" width="1624" data-og-height="1012" height="1012" data-path="images/agent/auto-run.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=280&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=9f2e2bed8f634201adc51ccb2bd96cd2 280w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=560&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=51704cac2f270a04856fffbeaccf9700 560w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=840&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=01a5034975497a8dff4f41dca0d19f2e 840w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=1100&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=5f19026a0c6e5fb28c935ce795edb706 1100w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=1650&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=a108fc86f8ee7c0db6e5b7ab80ede738 1650w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=2500&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=9ce5f45879c29049640bb5a1494db11e 2500w" />
      </Frame>
    </div>
  </Columns>

  <Columns className="gap-4">
    <div>
      <h3 className="text-lg font-medium mb-2">
        <a href="/tr/agent/apply" className="hover:text-primary transition-colors">
          Değişiklikleri Uygula
        </a>
      </h3>

      <p className="text-sm">
        Yapay zekânın önerdiği kod bloklarını kod tabanına entegre et. Apply,
        hassasiyeti korurken geniş kapsamlı değişiklikleri verimli şekilde uygular.
      </p>
    </div>

    <div>
      <Frame>
        <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/apply.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=634492fa2f63b4f6eada08b2a1ded47e" alt="Değişiklikleri uygula" data-og-width="1032" width="1032" data-og-height="410" height="410" data-path="images/chat/apply.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/apply.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=7dbc88cfe20429c73e627a289b17c964 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/apply.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=721e2d51bdb16dbb817e19d96d93c9d9 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/apply.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=8faea188ca903e58d347ddfec2c9bf6e 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/apply.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=f3bc38701cab63602b54374dfaa9e024 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/apply.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=fddad51f5b12c32493e2370ed326712d 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/apply.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=1584d431007b33a595905e23b5e1b453 2500w" />
      </Frame>
    </div>
  </Columns>

  <Columns className="gap-4">
    <div>
      <h3 className="text-lg font-medium mb-2">
        <a href="/tr/agent/review" className="hover:text-primary transition-colors">
          Farkları Gözden Geçir
        </a>
      </h3>

      <p className="text-sm">
        Kabul etmeden önce değişiklikleri gözden geçir. İnceleme arayüzü, ekleme ve silmeleri renk kodlu satırlarla göstererek değişiklikler üzerinde kontrol sağlar.
      </p>
    </div>

    <div>
      <Frame>
        <video src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/review/review-bar.mp4?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=5dca0fe7aba3c79e6760cb264821a617" autoPlay loop muted playsInline controls data-path="images/chat/review/review-bar.mp4" />
      </Frame>
    </div>
  </Columns>

  <Columns className="gap-4">
    <div>
      <h3 className="text-lg font-medium mb-2">
        <a href="/tr/agent/chats/tabs" className="hover:text-primary transition-colors">
          Sohbet Sekmeleri
        </a>
      </h3>

      <p className="text-sm">
        <Kbd>Cmd+T</Kbd> ile aynı anda birden fazla sohbeti çalıştır. Her sekme
        kendi bağlamını, geçmişini ve model seçimini korur.
      </p>
    </div>

    <div>
      <Frame>
        <video src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/chat-tabs.mp4?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=57fd5305279dc0a3139055b353ce4b7a" autoPlay loop muted playsInline controls data-path="images/chat/chat-tabs.mp4" />
      </Frame>
    </div>
  </Columns>

  <Columns className="gap-4">
    <div>
      <h3 className="text-lg font-medium mb-2">
        <a href="/tr/agent/chats/checkpoints" className="hover:text-primary transition-colors">
          Kontrol Noktaları
        </a>
      </h3>

      <p className="text-sm">
        Otomatik anlık görüntüler Agent'ın yaptığı değişiklikleri takip eder. Değişiklikler beklediğin gibi çalışmadığında ya da farklı yaklaşımlar denemek istediğinde önceki durumlara geri dön.
      </p>
    </div>

    <div>
      <Frame>
        <video src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/restore-checkpoint.mp4?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=7cededf7892f15a6342a81953ea0aa38" autoPlay loop muted playsInline controls data-path="images/chat/restore-checkpoint.mp4" />
      </Frame>
    </div>
  </Columns>

  <Columns className="gap-4">
    <div>
      <h3 className="text-lg font-medium mb-2">
        <a href="/tr/agent/terminal" className="hover:text-primary transition-colors">
          Terminal Entegrasyonu
        </a>
      </h3>

      <p className="text-sm">
        Agent terminal komutlarını çalıştırır, çıktıyı izler ve çok adımlı
        süreçleri yönetir. Güvenilir iş akışları için otomatik çalıştırmayı yapılandırabilir ya da güvenlik için
        onay gerektirebilirsin.
      </p>
    </div>

    <div>
      <Frame>
        <img src="https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=3135722076a5aa636d27dbedec665bae" alt="Terminal entegrasyonu" data-og-width="1624" width="1624" data-og-height="1012" height="1012" data-path="images/agent/auto-run.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=280&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=9f2e2bed8f634201adc51ccb2bd96cd2 280w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=560&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=51704cac2f270a04856fffbeaccf9700 560w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=840&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=01a5034975497a8dff4f41dca0d19f2e 840w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=1100&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=5f19026a0c6e5fb28c935ce795edb706 1100w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=1650&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=a108fc86f8ee7c0db6e5b7ab80ede738 1650w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=2500&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=9ce5f45879c29049640bb5a1494db11e 2500w" />
      </Frame>
    </div>
  </Columns>

  <Columns className="gap-4">
    <div>
      <h3 className="text-lg font-medium mb-2">
        <a href="/tr/agent/chats/history" className="hover:text-primary transition-colors">
          Sohbet Geçmişi
        </a>
      </h3>

      <p className="text-sm">
        <Kbd>Opt Cmd '</Kbd> ile geçmiş konuşmalarına eriş. Önceki
        sohbetleri gözden geçir, kodlama oturumlarını takip et ve önceki
        konuşmalardaki bağlama başvur.
      </p>
    </div>

    <div>
      <Frame>
        <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/chat-history.jpeg?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=d9ec96fad0c8c2fb132bbf5ce8ea35f7" alt="Sohbet geçmişi" data-og-width="2048" width="2048" data-og-height="1317" height="1317" data-path="images/chat/chat-history.jpeg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/chat-history.jpeg?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=a3ad71e9891c3c9642f4288953a78e97 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/chat-history.jpeg?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=76139a177ebfeb0c55add7fb955f9000 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/chat-history.jpeg?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=1af22180859c017542777ab36b434b7a 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/chat-history.jpeg?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=751e7fa0888e5790f841432ef7521337 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/chat-history.jpeg?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=86b447c18601a9d44af8866d0042719e 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/chat-history.jpeg?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=88c84a8fb1b764ad3070e3211f539408 2500w" />
      </Frame>
    </div>
  </Columns>

  <Columns className="gap-4">
    <div>
      <h3 className="text-lg font-medium mb-2">
        <a href="/tr/agent/chats/export" className="hover:text-primary transition-colors">
          Sohbetleri Dışa Aktar
        </a>
      </h3>

      <p className="text-sm">
        Konuşmaları Markdown formatında dışa aktar. Çözümleri ekip
        üyeleriyle paylaş, kararları belgele veya kodlama
        oturumlarından bilgi tabanları oluştur.
      </p>
    </div>

    <div>
      <Frame>
        <video src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/export-chat.mp4?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=c6aa9d23a6a80ffae5864cd494907961" autoPlay loop muted playsInline controls data-path="images/chat/export-chat.mp4" />
      </Frame>
    </div>
  </Columns>

  <Columns className="gap-4">
    <div>
      <h3 className="text-lg font-medium mb-2">
        <a href="/tr/context/rules" className="hover:text-primary transition-colors">
          Kurallar
        </a>
      </h3>

      <p className="text-sm">
        Agent’ın davranışları için özel yönergeler tanımla. Kurallar, kodlama standartlarını korumayı, kalıpları dayatmayı ve Agent’ın projene nasıl yardımcı olacağını kişiselleştirmeyi sağlar.
      </p>
    </div>

    <div>
      <Frame>
        <img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rules-applied.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=e637bab83cfd5dcc8a3b15ed6fd9fc15" alt="Agent kuralları" data-og-width="1198" width="1198" data-og-height="674" height="674" data-path="images/context/rules/rules-applied.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rules-applied.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=78e3c392987c6f95a02fc106753c5f98 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rules-applied.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=9d3a8b76ba99ada5ca302cba9fb63810 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rules-applied.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=f5ab7fb374a1a4c5fe2f50e2e50d233a 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rules-applied.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=5d25394a29c1da4172a3e673ee384c07 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rules-applied.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=0fc125bd3c2a93551674252c0523d3ec 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rules-applied.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=c576ea053ee18c30d2781c6bdd394a70 2500w" />
      </Frame>
    </div>
  </Columns>
</div>



# Planlama
Source: https://docs.cursor.com/tr/agent/planning

Agent, yapılacak listeleri ve kuyruklama ile karmaşık görevleri nasıl planlar ve yönetir

export const Kbd = ({children, tooltip, os}) => {
  const keysInput = typeof children === 'string' && children.trim() !== '' ? children : null;
  if (!keysInput) {
    return null;
  }
  const isModifier = key => {
    const modifiers = ['⌘', '⇧', '⌥', '⌃', '⏎', '⌫', '⌦', '⎋', '⇥', '⌁', '←', '→', '↑', '↓', 'Ctrl', 'Shift', 'Alt', 'Cmd', 'Opt', 'Return', 'Backspace', 'Delete', 'Escape', 'Tab', 'Space', 'Enter', 'Esc', 'ArrowLeft', 'ArrowRight', 'ArrowUp', 'ArrowDown', 'Left', 'Right', 'Up', 'Down'];
    return modifiers.includes(key.trim());
  };
  const capitalizeFirstLetter = string => {
    return string.charAt(0).toUpperCase() + string.slice(1);
  };
  const isMac = os ? os.toLowerCase() === 'mac' || os.toLowerCase() === 'macos' : typeof navigator !== 'undefined' && (navigator.platform.toUpperCase().indexOf('MAC') >= 0 || navigator.userAgent.toUpperCase().indexOf('MAC') >= 0);
  const convertToSymbols = shortcut => {
    if (isMac) {
      return shortcut.replace(/⌘|Cmd|CMD/gi, '⌘').replace(/⌥|Opt|OPT/gi, '⌥').replace(/⌃|Ctrl/gi, '⌃').replace(/⇧|Shift/gi, '⇧').replace(/⏎|Return/gi, '⏎').replace(/⌫|Backspace/gi, '⌫').replace(/⌦|Delete/gi, '⌦').replace(/␛|Escape/gi, '␛').replace(/⇥|Tab/gi, '⇥').replace(/⌁|Space/gi, '⌁').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, '←').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, '→').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, '↑').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, '↓');
    } else {
      const converted = shortcut.replace(/⌘|Cmd|CMD/gi, 'Ctrl').replace(/⌥|Opt|OPT/gi, 'Alt').replace(/⌃|Ctrl/gi, 'Ctrl').replace(/⇧|Shift/gi, 'Shift').replace(/⏎|Return/gi, 'Enter').replace(/⌫|Backspace/gi, 'Backspace').replace(/⌦|Delete/gi, 'Delete').replace(/⎋|Escape/gi, 'Esc').replace(/⇥|Tab/gi, 'Tab').replace(/⌁|Space/gi, 'Space').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, 'Arrow-Left').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, 'Arrow-Right').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, 'Arrow-Up').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, 'Arrow-Down');
      const keyList = converted.split(/[\+\s]+/).filter(key => key.trim());
      return keyList.join('+');
    }
  };
  const convertToReadableText = shortcut => {
    const converted = shortcut.replace(/⌘|Cmd|CMD/gi, 'Cmd').replace(/⌥|Opt|OPT/gi, 'Opt').replace(/⌃|Ctrl/gi, 'Ctrl').replace(/⇧|Shift/gi, 'Shift').replace(/⏎|Return/gi, 'Return').replace(/⌫|Backspace/gi, 'Backspace').replace(/⌦|Delete/gi, 'Delete').replace(/⎋|Escape/gi, 'Escape').replace(/⇥|Tab/gi, 'Tab').replace(/⌁|Space/gi, 'Space').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, 'Arrow-Left').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, 'Arrow-Right').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, 'Arrow-Up').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, 'Arrow-Down');
    const keyList = converted.split(/[\+\s]+/).filter(key => key.trim());
    return keyList.map(key => {
      const trimmedKey = key.trim();
      return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
    }).join('+');
  };
  const displayShortcut = convertToSymbols(keysInput);
  const tooltipText = isMac ? tooltip ? `${convertToReadableText(keysInput)}: ${tooltip}` : convertToReadableText(keysInput) : tooltip || null;
  const processedKeys = isMac ? displayShortcut.split(/[\+\s]+/).filter(key => key.trim()).map(key => {
    const trimmedKey = key.trim();
    return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
  }).join('') : displayShortcut.split('+').map(key => {
    const trimmedKey = key.trim();
    return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
  }).join('+');
  return tooltipText ? <Tooltip tip={tooltipText}>
      <kbd>
        {processedKeys}
      </kbd>
    </Tooltip> : <kbd>
      {processedKeys}
    </kbd>;
};

Agent, yapılandırılmış yapılacak listeleri ve mesaj kuyruğa alma sayesinde önceden plan yapıp karmaşık görevleri yönetebilir; böylece uzun soluklu görevleri anlamak ve takip etmek kolaylaşır.

<div id="agent-to-dos">
  ## Agent yapılacaklar
</div>

Agent, daha uzun görevleri bağımlılıkları olan yönetilebilir adımlara ayırarak, iş ilerledikçe güncellenen yapılandırılmış bir plan oluşturur.

<video autoPlay loop muted playsInline controls>
  <source src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/agent/planning/agent-todo.mp4?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=b0285913832a3ef123fe149516ee37ea" type="video/mp4" data-path="images/agent/planning/agent-todo.mp4" />
</video>

<div id="how-it-works">
  ### Nasıl çalışır
</div>

* Agent karmaşık görevler için otomatik olarak yapılacaklar listeleri oluşturur
* Her öğe diğer görevlere bağımlılıklar içerebilir
* Liste, iş ilerledikçe gerçek zamanlı olarak güncellenir
* Tamamlanan görevler otomatik olarak işaretlenir

<div id="visibility">
  ### Görünürlük
</div>

* Yapılacaklar sohbet arayüzünde görünür
* [Slack entegrasyonu](/tr/slack) kuruluysa, yapılacaklar orada da görünür
* İstediğin zaman tam görev dökümünü görebilirsin

<Tip>
  Daha iyi planlama için nihai hedefini net şekilde anlat. Agent, kapsamın tamamını
  anladığında daha doğru görev dökümleri oluşturur.
</Tip>

<Note>Planlama ve yapılacaklar şu anda otomatik mod için desteklenmiyor.</Note>

<div id="queued-messages">
  ## Kuyruğa alınan mesajlar
</div>

Agent mevcut görev üzerinde çalışırken takip mesajlarını kuyruğa al. Talimatların sırada bekler ve hazır olduğunda otomatik olarak yürütülür.

<video autoPlay loop muted playsInline controls>
  <source src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/agent/planning/agent-queue.mp4?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=4cdd6a7d1e12c67e520bc3ba67a42e0d" type="video/mp4" data-path="images/agent/planning/agent-queue.mp4" />
</video>

<div id="using-the-queue">
  ### Kuyruğu kullanma
</div>

1. Agent çalışırken bir sonraki talimatını yaz
2. Kuyruğa eklemek için <Kbd>Ctrl+Enter</Kbd> tuşuna bas
3. Mesajlar, etkin görevin altında sırayla görünür
4. Ok simgesine tıklayarak kuyruğa alınan mesajların sırasını değiştir
5. Agent, bitirdikten sonra onları sırayla işler

<div id="override-the-queue">
  ### Kuyruğu geçersiz kılma
</div>

Varsayılan mesajlaşma yerine mesajını kuyruğa almak için <Kbd>Ctrl+Enter</Kbd> kullan. Kuyruğa almadan mesajı anında göndermek için <Kbd>Cmd+Enter</Kbd> kullan. Bu, mesajını “zorla gönderir” ve kuyruğu atlayarak hemen çalıştırır.

<div id="default-messaging">
  ## Varsayılan mesajlaşma
</div>

Mesajlar varsayılan olarak mümkün olduğunca hızlı gönderilir; genellikle Agent bir araç çağrısını tamamlar tamamlamaz görünür. Bu, en hızlı tepki veren deneyimi sağlar.

<div id="how-default-messaging-works">
  ### Varsayılan mesajlaşma nasıl çalışır
</div>

* Mesajın, sohbetteki en son kullanıcı mesajına eklenir
* Mesajlar genellikle araç sonuçlarına iliştirilir ve hazır olur olmaz gönderilir
* Bu, Agent’ın mevcut işini bölmeden daha doğal bir sohbet akışı sağlar
* Varsayılan olarak, Agent çalışırken Enter’a bastığında bu gerçekleşir



# Diff’ler & İnceleme
Source: https://docs.cursor.com/tr/agent/review

AI ajanının oluşturduğu kod değişikliklerini incele ve yönet

Agent kod değişiklikleri oluşturduğunda, eklemeleri ve silmeleri renk kodlu satırlarla gösteren bir inceleme arayüzünde sunulur. Bu, kod tabanına hangi değişiklikleri uygulayacağını incelemene ve kontrol etmene olanak tanır.

İnceleme arayüzü, kod değişikliklerini tanıdık bir diff formatında gösterir:

<div id="diffs">
  ## Farklar
</div>

<div className="full-width-table">
  | Tür               | Anlam                          | Örnek                                                                                                 |
  | :---------------- | :----------------------------- | :---------------------------------------------------------------------------------------------------- |
  | **Added lines**   | Yeni eklenen kod satırları     | <code className="bg-green-100 text-green-800 px-2 py-1 rounded">+ const newVariable = 'hello';</code> |
  | **Deleted lines** | Silinen kod satırları          | <code className="bg-red-100 text-red-800 px-2 py-1 rounded">- const oldVariable = 'goodbye';</code>   |
  | **Context lines** | Değişmeyen çevreleyen satırlar | <code className="bg-gray-100 text-gray-600 px-2 py-1 rounded"> function example() {}</code>           |
</div>

<div id="review">
  ## İnceleme
</div>

Oluşturma tamamlandıktan sonra, devam etmeden önce tüm değişiklikleri gözden geçirmen için bir istem göreceksin. Bu, nelerin değiştirileceğine dair genel bir bakış sunar.

<Frame>
  <img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/review/input-review.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=10633167c76c24c1e69748ef93dc3888" alt="Girdi inceleme arayüzü" data-og-width="2095" width="2095" data-og-height="1178" height="1178" data-path="images/chat/review/input-review.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/review/input-review.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=f462337898ca48f71cd2b570b140d30d 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/review/input-review.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=07c91dfc92110cce444da8bbf3d0b3b5 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/review/input-review.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=492522862dabae6243fa8d33f6fd77f2 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/review/input-review.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=c897e19ce7f508bad4e24fcf8efb2512 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/review/input-review.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=3956c2d2c5c9156181b19e262e301b5b 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/review/input-review.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=907f90b1db432128964a7f4e59523bb6 2500w" />
</Frame>

<div id="file-by-file">
  ### Dosya dosya
</div>

Ekranın altında kayan bir inceleme çubuğu belirir ve şunları yapmana olanak tanır:

* Geçerli dosyadaki değişiklikleri **kabul et** veya **reddet**
* Bekleyen değişiklikleri olan **sonraki dosyaya** git
  <Frame>
    <video src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/review/review-bar.mp4?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=5dca0fe7aba3c79e6760cb264821a617" autoPlay loop muted playsInline controls data-path="images/chat/review/review-bar.mp4">
      Tarayıcın video etiketini desteklemiyor.
    </video>
  </Frame>

<div id="selective-acceptance">
  ### Seçimli kabul
</div>

Daha ince ayarlı kontrol için:

* Çoğu değişikliği kabul etmek için: istemediğin satırları reddet, ardından **Tümünü kabul et**’e tıkla
* Çoğu değişikliği reddetmek için: istediğin satırları kabul et, ardından **Tümünü reddet**’e tıkla

<div id="review-changes">
  ## Değişiklikleri gözden geçir
</div>

Agent yanıtının sonunda, yapılan değişikliklerin tüm diff’ini görmek için **Değişiklikleri gözden geçir** düğmesine tıkla.

<Frame>
  <video src="https://www.cursor.com/changelog/049/review-ui.mp4" autoPlay loop muted playsInline controls />
</Frame>



# Terminal
Source: https://docs.cursor.com/tr/agent/terminal

Aracın işlemlerinin bir parçası olarak terminal komutlarını otomatik çalıştır

Agent, geçmişi korunarak Cursor’un yerel terminalinde komutları çalıştırır. Komutları kesmek için Atla’ya tıklayıp <kbd>Ctrl+C</kbd> gönder.

<div id="troubleshooting">
  ## Sorun Giderme
</div>

<Info>
  Bazı shell temaları (örneğin Powerlevel9k/Powerlevel10k) satır içi terminal çıktısını
  etkileyebilir. Komut çıktın kesilmiş ya da yanlış biçimlendirilmiş görünüyorsa,
  temayı devre dışı bırak ya da Agent çalışırken daha basit bir prompt’a geç.
</Info>

<div id="disable-heavy-prompts-for-agent-sessions">
  ### Agent oturumları için ağır prompt’ları devre dışı bırak
</div>

Agent’ın çalıştığını algılamak ve süslü prompt/tema başlatmayı atlamak için shell yapılandırmanda `CURSOR_AGENT` ortam değişkenini kullan.

```zsh  theme={null}

# ~/.zshrc — Cursor Agent çalıştığında Powerlevel10k'i devre dışı bırak
if [[ -n "$CURSOR_AGENT" ]]; then
  # Daha iyi uyumluluk için temayı başlatmayı atla
else
  [[ -r ~/.p10k.zsh ]] && source ~/.p10k.zsh
fi
```

```bash  theme={null}

# ~/.bashrc — Agent oturumlarında basit bir isteme geri dön
if [[ -n "$CURSOR_AGENT" ]]; then
  PS1='\u@\h \W \$ '
fi
```



# Araçlar
Source: https://docs.cursor.com/tr/agent/tools

Kod arama, düzenleme ve çalıştırma için ajanlara sunulan araçlar

[Agent](/tr/agent/overview) içindeki modlarda kullanılabilen tüm araçların listesi; kendi [özel modlarını](/tr/agent/modes#custom) oluştururken bunları etkinleştirip devre dışı bırakabilirsin.

<Note>
  Bir görev sırasında Agent’ın yapabileceği araç çağrılarının sayısında bir sınır yok. İsteğini tamamlamak için gerektiği kadar araç kullanmaya devam edecek.
</Note>

<div id="search">
  ## Arama
</div>

Kod tabanında ve web'de ilgili bilgiyi bulmak için kullanılan araçlar.

<AccordionGroup>
  <Accordion title="Read File" icon="file-lines">
    Bir dosyadan en fazla 250 satır (maks modda 750) okur.
  </Accordion>

  <Accordion title="List Directory" icon="folder-open">
    Dosya içeriklerini okumadan bir dizinin yapısını okur.
  </Accordion>

  <Accordion title="Codebase" icon="database">
    [indekslenmiş
    kod tabanında](/tr/context/codebase-indexing) semantik aramalar yapar.
  </Accordion>

  <Accordion title="Grep" icon="magnifying-glass">
    Dosyalar içinde tam anahtar kelimeleri veya desenleri arar.
  </Accordion>

  <Accordion title="Search Files" icon="file-magnifying-glass">
    Bulanık eşleştirme kullanarak dosyaları ada göre bulur.
  </Accordion>

  <Accordion title="Web" icon="globe">
    Arama sorguları üretir ve web aramaları yapar.
  </Accordion>

  <Accordion title="Fetch Rules" icon="gavel">
    Türe ve açıklamaya göre belirli [kuralları](/tr/context/rules) getirir.
  </Accordion>
</AccordionGroup>

<div id="edit">
  ## Düzenle
</div>

Dosyalarında ve kod tabanında belirli düzenlemeler yapmana yardımcı olan araçlar.

<AccordionGroup>
  <Accordion title="Düzenle & Yeniden Uygula" icon="pencil">
    Dosyalara düzenleme öner ve bunları otomatik olarak [uygula](/tr/agent/apply).
  </Accordion>

  <Accordion title="Dosyayı Sil" icon="trash">
    Dosyaları kendi kendine sil (ayarlar bölümünde devre dışı bırakılabilir).
  </Accordion>
</AccordionGroup>

<div id="run">
  ## Çalıştır
</div>

Chat terminalinle etkileşime geçebilir.

<AccordionGroup>
  <Accordion title="Terminal" icon="terminal">
    Terminal komutlarını çalıştır ve çıktıyı izle.
  </Accordion>
</AccordionGroup>

<Note>Varsayılan olarak, Cursor mevcut ilk terminal profilini kullanır.</Note>

Tercih ettiğin terminal profilini ayarlamak için:

1. Komut Paletini aç (`Cmd/Ctrl+Shift+P`)
2. "Terminal: Select Default Profile" ara
3. İstediğin profili seç

<div id="mcp">
  ## MCP
</div>

Sohbet, veritabanları veya üçüncü taraf API’ler gibi harici hizmetlerle etkileşim kurmak için yapılandırılmış MCP sunucularını kullanabilir.

<AccordionGroup>
  <Accordion title="MCP Sunucularını Aç/Kapat" icon="server">
    Kullanılabilir MCP sunucularını aç/kapat. Otomatik çalıştırma yapılandırmasına uyar.
  </Accordion>
</AccordionGroup>

[Model Context Protocol](/tr/context/model-context-protocol) hakkında daha fazlasını öğren ve [MCP dizini](/tr/tools)nde mevcut sunucuları keşfet.

<div id="advanced-options">
  ## Gelişmiş seçenekler
</div>

<AccordionGroup>
  <Accordion title="Auto-apply Edits" icon="check">
    Düzenlemeleri manuel onay olmadan otomatik uygula.
  </Accordion>

  <Accordion title="Auto-run" icon="play">
    Terminal komutlarını otomatik çalıştır ve düzenlemeleri kabul et. Test paketlerini (test suite) çalıştırmak ve değişiklikleri doğrulamak için kullanışlıdır.

    <Frame>
      <img src="https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=3135722076a5aa636d27dbedec665bae" data-og-width="1624" width="1624" data-og-height="1012" height="1012" data-path="images/agent/auto-run.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=280&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=9f2e2bed8f634201adc51ccb2bd96cd2 280w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=560&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=51704cac2f270a04856fffbeaccf9700 560w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=840&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=01a5034975497a8dff4f41dca0d19f2e 840w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=1100&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=5f19026a0c6e5fb28c935ce795edb706 1100w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=1650&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=a108fc86f8ee7c0db6e5b7ab80ede738 1650w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=2500&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=9ce5f45879c29049640bb5a1494db11e 2500w" />
    </Frame>
  </Accordion>

  <Accordion title="Guardrails" icon="shield">
    Hangi araçların otomatik çalıştırılabileceğini belirtmek için izin listelerini yapılandır. İzin listeleri, izin verilen işlemleri açıkça tanımlayarak daha iyi güvenlik sağlar.
  </Accordion>

  <Accordion title="Auto-fix Errors" icon="wrench">
    Agent tarafından karşılaşıldığında linter hatalarını ve uyarılarını otomatik olarak gider.
  </Accordion>
</AccordionGroup>



# Arka Plan Aracıları
Source: https://docs.cursor.com/tr/background-agent

Cursor'da asenkron uzaktan aracıları

export const Kbd = ({children, tooltip, os}) => {
  const keysInput = typeof children === 'string' && children.trim() !== '' ? children : null;
  if (!keysInput) {
    return null;
  }
  const isModifier = key => {
    const modifiers = ['⌘', '⇧', '⌥', '⌃', '⏎', '⌫', '⌦', '⎋', '⇥', '⌁', '←', '→', '↑', '↓', 'Ctrl', 'Shift', 'Alt', 'Cmd', 'Opt', 'Return', 'Backspace', 'Delete', 'Escape', 'Tab', 'Space', 'Enter', 'Esc', 'ArrowLeft', 'ArrowRight', 'ArrowUp', 'ArrowDown', 'Left', 'Right', 'Up', 'Down'];
    return modifiers.includes(key.trim());
  };
  const capitalizeFirstLetter = string => {
    return string.charAt(0).toUpperCase() + string.slice(1);
  };
  const isMac = os ? os.toLowerCase() === 'mac' || os.toLowerCase() === 'macos' : typeof navigator !== 'undefined' && (navigator.platform.toUpperCase().indexOf('MAC') >= 0 || navigator.userAgent.toUpperCase().indexOf('MAC') >= 0);
  const convertToSymbols = shortcut => {
    if (isMac) {
      return shortcut.replace(/⌘|Cmd|CMD/gi, '⌘').replace(/⌥|Opt|OPT/gi, '⌥').replace(/⌃|Ctrl/gi, '⌃').replace(/⇧|Shift/gi, '⇧').replace(/⏎|Return/gi, '⏎').replace(/⌫|Backspace/gi, '⌫').replace(/⌦|Delete/gi, '⌦').replace(/␛|Escape/gi, '␛').replace(/⇥|Tab/gi, '⇥').replace(/⌁|Space/gi, '⌁').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, '←').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, '→').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, '↑').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, '↓');
    } else {
      const converted = shortcut.replace(/⌘|Cmd|CMD/gi, 'Ctrl').replace(/⌥|Opt|OPT/gi, 'Alt').replace(/⌃|Ctrl/gi, 'Ctrl').replace(/⇧|Shift/gi, 'Shift').replace(/⏎|Return/gi, 'Enter').replace(/⌫|Backspace/gi, 'Backspace').replace(/⌦|Delete/gi, 'Delete').replace(/⎋|Escape/gi, 'Esc').replace(/⇥|Tab/gi, 'Tab').replace(/⌁|Space/gi, 'Space').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, 'Arrow-Left').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, 'Arrow-Right').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, 'Arrow-Up').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, 'Arrow-Down');
      const keyList = converted.split(/[\+\s]+/).filter(key => key.trim());
      return keyList.join('+');
    }
  };
  const convertToReadableText = shortcut => {
    const converted = shortcut.replace(/⌘|Cmd|CMD/gi, 'Cmd').replace(/⌥|Opt|OPT/gi, 'Opt').replace(/⌃|Ctrl/gi, 'Ctrl').replace(/⇧|Shift/gi, 'Shift').replace(/⏎|Return/gi, 'Return').replace(/⌫|Backspace/gi, 'Backspace').replace(/⌦|Delete/gi, 'Delete').replace(/⎋|Escape/gi, 'Escape').replace(/⇥|Tab/gi, 'Tab').replace(/⌁|Space/gi, 'Space').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, 'Arrow-Left').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, 'Arrow-Right').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, 'Arrow-Up').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, 'Arrow-Down');
    const keyList = converted.split(/[\+\s]+/).filter(key => key.trim());
    return keyList.map(key => {
      const trimmedKey = key.trim();
      return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
    }).join('+');
  };
  const displayShortcut = convertToSymbols(keysInput);
  const tooltipText = isMac ? tooltip ? `${convertToReadableText(keysInput)}: ${tooltip}` : convertToReadableText(keysInput) : tooltip || null;
  const processedKeys = isMac ? displayShortcut.split(/[\+\s]+/).filter(key => key.trim()).map(key => {
    const trimmedKey = key.trim();
    return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
  }).join('') : displayShortcut.split('+').map(key => {
    const trimmedKey = key.trim();
    return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
  }).join('+');
  return tooltipText ? <Tooltip tip={tooltipText}>
      <kbd>
        {processedKeys}
      </kbd>
    </Tooltip> : <kbd>
      {processedKeys}
    </kbd>;
};

Background agents ile, uzak bir ortamda kod düzenleyip çalıştıran asenkron ajanlar başlat. Durumlarını görüntüle, takip mesajları gönder ya da istediğin zaman kontrolü devral.

<div id="how-to-use">
  ## Nasıl Kullanılır
</div>

Arka plan ajanlarına iki şekilde erişebilirsin:

1. **Background Agent Sidebar**: Hesabınla ilişkili tüm arka plan ajanlarını görüntülemek, mevcut ajanları aramak ve yenilerini başlatmak için yerel Cursor kenar çubuğundaki background agent sekmesini kullan.
2. **Background Agent Mode**: Arayüzde background agent modunu tetiklemek için <Kbd tooltip="Trigger background agent mode">Cmd E</Kbd> tuşlarına bas.

Bir istem gönderdikten sonra, durumunu görmek ve makineye girmek için listeden ajanını seç.

<Note>
  <p className="!mb-0">
    Arka plan ajanları birkaç gün seviyesinde veri saklama gerektirir.
  </p>
</Note>

<div id="setup">
  ## Kurulum
</div>

Arka plan ajanları varsayılan olarak izole bir Ubuntu tabanlı makinede çalışır. Ajanların internet erişimi vardır ve paketleri yükleyebilir.

<div id="github-connection">
  #### GitHub bağlantısı
</div>

Arka plan ajanları repoyu GitHub’dan klonlar, ayrı bir branch’te çalışır ve kolay devretme için repoya push’lar.

Repoya (ve bağımlı repolara ya da submodule’lere) okuma-yazma yetkisi ver. Gelecekte diğer sağlayıcıları (GitLab, Bitbucket, vb.) da destekleyeceğiz.

<div id="ip-allow-list-configuration">
  ##### IP Allow List Yapılandırması
</div>

Kuruluşun GitHub’ın IP allow list özelliğini kullanıyorsa, arka plan agent’ları için erişimi yapılandırman gerekir. İletişim bilgileri ve IP adresleri de dahil eksiksiz kurulum talimatları için [GitHub entegrasyon dökümantasyonuna](/tr/integrations/github#ip-allow-list-configuration) bak.

<div id="base-environment-setup">
  #### Temel Ortam Kurulumu
</div>

Gelişmiş senaryolar için ortamı kendin kur. Uzak makineye bağlı bir IDE instance’ı edin. Makinenin kurulumunu yap, araçları ve paketleri yükle, sonra bir snapshot al. Çalışma zamanı ayarlarını yapılandır:

* Install komutu, agent başlamadan önce çalışır ve runtime bağımlılıklarını yükler. Bu, `npm install` veya `bazel build` çalıştırmak olabilir.
* Terminals, agent çalışırken arka planda süreçler yürütür — bir web sunucusu başlatmak ya da protobuf dosyalarını derlemek gibi.

Daha da ileri senaryolar için makine kurulumunda bir Dockerfile kullan. Dockerfile, sistem düzeyinde bağımlılıkları ayarlamana olanak tanır: belirli derleyici sürümlerini, hata ayıklayıcıları yüklemek veya temel OS imajını değiştirmek. Tüm projeyi `COPY` etme — çalışma alanını biz yönetiyoruz ve doğru commit’i checkout ediyoruz. Yine de bağımlılık kurulumunu install script’inde yap.

Geliştirme ortamın için gereken tüm secrets’ları gir — veritabanımızda at-rest şifreli (KMS kullanarak) olarak saklanır ve arka plandaki agent ortamına sağlanır.

Makine kurulumu `.cursor/environment.json` içinde bulunur; repoya commit edebilirsin (önerilir) ya da özel olarak saklayabilirsin. Kurulum akışı, `environment.json` oluşturma sürecinde sana rehberlik eder.

<div id="maintenance-commands">
  #### Bakım Komutları
</div>

Yeni bir makine kurarken temel ortamdan başlarız, ardından `environment.json` içindeki `install` komutunu çalıştırırız. Bu komut, bir geliştiricinin dallar arasında geçiş yaparken çalıştıracağı komuttur — yeni bağımlılıkları kurar.

Çoğu kişi için `install` komutu `npm install` veya `bazel build`’dür.

Makinenin hızlı açılmasını sağlamak için, `install` komutu çalıştıktan sonra disk durumunu önbelleğe alırız. Birden fazla kez çalışacak şekilde tasarlayın. `install` komutundan yalnızca disk durumu kalıcıdır — burada başlatılan süreçler, agent başladığında çalışır durumda olmayacaktır.

<div id="startup-commands">
  #### Başlangıç Komutları
</div>

`install` çalıştırıldıktan sonra makine başlar, biz de `start` komutunu çalıştırır ve ardından varsa `terminals`’ı başlatırız. Bu, ajan çalışırken ayakta kalması gereken süreçleri başlatır.

`start` komutu çoğu zaman atlanabilir. Geliştirme ortamın docker’a bağlıysa kullan—`start` komutuna `sudo service docker start` ekle.

`terminals` uygulama kodu içindir. Bu terminaller, senin ve ajanın erişebileceği bir `tmux` oturumunda çalışır. Örneğin, birçok web sitesi reposu `npm run watch` komutunu bir terminal olarak ekler.

<div id="the-environmentjson-spec">
  #### `environment.json` Özellikleri
</div>

`environment.json` dosyası şu şekilde görünebilir:

```json  theme={null}
{
  "snapshot": "POPULATED_FROM_SETTINGS",
  "install": "npm install",
  "terminals": [
    {
      "name": "Next.js'i çalıştır"
      "command": "npm run dev"
    }
  ]
}
```

Resmî olarak, özellikler [burada tanımlanmıştır](https://www.cursor.com/schemas/environment.schema.json).

<div id="models">
  ## Modeller
</div>

Arka plan ajanlarında yalnızca [Max Mode](/tr/context/max-mode) ile uyumlu modeller kullanılabilir.

<div id="pricing">
  ## Fiyatlandırma
</div>

[Background Agent fiyatlandırması](/tr/account/pricing#background-agent) hakkında daha fazla bilgi edin.

<div id="security">
  ## Güvenlik
</div>

Background Agents, Privacy Mode’da kullanılabilir. Kodun üzerinde asla eğitim yapmıyoruz ve kodu yalnızca agent’ı çalıştırmak için tutuyoruz. [Privacy Mode hakkında daha fazla bilgi al](https://www.cursor.com/privacy-overview).

Bilmen gerekenler:

1. Düzenlemek istediğin repolar için GitHub uygulamamıza okuma-yazma yetkisi ver. Bunu repoyu klonlamak ve değişiklik yapmak için kullanıyoruz.
2. Kodun, AWS altyapımızda izole VM’ler içinde çalışır ve agent erişilebilir olduğu sürece VM disklerinde saklanır.
3. Agent’ın internet erişimi vardır.
4. Agent tüm terminal komutlarını otomatik olarak çalıştırır; bu da testler üzerinde yineleme yapmasını sağlar. Bu, her komut için kullanıcı onayı gerektiren foreground agent’tan farklıdır. Otomatik çalıştırma, veri sızdırma riski doğurur: saldırganlar prompt injection saldırılarıyla agent’ı kandırıp kodu kötü niyetli web sitelerine yükletmeye çalışabilir. [Arka plan agent’ları için prompt injection riskleri hakkında OpenAI’nin açıklamasına bak](https://platform.openai.com/docs/codex/agent-network#risks-of-agent-internet-access).
5. Privacy Mode kapalıysa, ürünü geliştirmek için prompt’ları ve dev environment’larını toplarız.
6. Bir background agent başlatırken Privacy Mode’u kapatır, agent çalışırken tekrar açarsan, agent tamamlanana kadar Privacy Mode kapalı kalmaya devam eder.

<div id="dashboard-settings">
  ## Dashboard ayarları
</div>

Workspace yöneticileri, Dashboard’daki Background Agents sekmesinden ek ayarları yapılandırabilir.

<div id="defaults-settings">
  ### Varsayılan Ayarları
</div>

* **Varsayılan model** – bir çalıştırmada model belirtilmediğinde kullanılan model. Max Mode’u destekleyen herhangi bir modeli seç.
* **Varsayılan depo** – boşsa, ajanlar kullanıcıya bir repo seçmesini sorar. Buraya bir repo girerek bu adımı atlayabilirsin.
* **Temel branch** – ajanların pull request oluştururken çatalladığı branch. Depodaki varsayılan branch’i kullanmak için boş bırak.

<div id="security-settings">
  ### Güvenlik Ayarları
</div>

Tüm güvenlik seçenekleri yönetici ayrıcalıkları gerektirir.

* **Kullanıcı kısıtlamaları** – *None* (tüm üyeler arka planda ajan başlatabilir) veya *Allow list* seç. *Allow list* olarak ayarlandığında, hangi ekip arkadaşlarının ajan oluşturabileceğini tam olarak belirlersin.
* **Ekip takipleri** – açıkken, çalışma alanındaki herkes başkası tarafından başlatılan bir ajana takip mesajı ekleyebilir. Bunu kapatarak takipleri yalnızca ajan sahibine ve yöneticilere kısıtlayabilirsin.
* **Ajan özetini göster** – Cursor’ın ajanın dosya diff görsellerini ve kod parçacıklarını gösterip göstermeyeceğini kontrol eder. Kenar çubuğunda dosya yollarını veya kodu göstermek istemiyorsan bunu devre dışı bırak.
* **Ajan özetini harici kanallarda göster** – önceki ayarı Slack’e veya bağladığın diğer harici kanallara genişletir.

Değişiklikler anında kaydedilir ve yeni ajanları hemen etkiler.



# Takip Ekle
Source: https://docs.cursor.com/tr/background-agent/api/add-followup

en/background-agent/api/openapi.yaml post /v0/agents/{id}/followup
Arka planda çalışan bir ajana ek bir komut gönder.




# Ajan Konuşması
Source: https://docs.cursor.com/tr/background-agent/api/agent-conversation

en/background-agent/api/openapi.yaml get /v0/agents/{id}/conversation
Arka plan ajanının konuşma geçmişini getir.

Arka plan ajanı silindiyse konuşmaya erişemezsin.



# Aracı Durumu
Source: https://docs.cursor.com/tr/background-agent/api/agent-status

en/background-agent/api/openapi.yaml get /v0/agents/{id}
Belirli bir arka plan aracının geçerli durumunu ve sonuçlarını al.




# API Anahtarı Bilgileri
Source: https://docs.cursor.com/tr/background-agent/api/api-key-info

en/background-agent/api/openapi.yaml get /v0/me
Kimlik doğrulamada kullanılan API anahtarına ait üst verileri getir.




# Bir Aracıyı Sil
Source: https://docs.cursor.com/tr/background-agent/api/delete-agent

en/background-agent/api/openapi.yaml delete /v0/agents/{id}
Bir arka plan aracısını ve ilişkili kaynaklarını kalıcı olarak sil.




# Bir Agent Başlat
Source: https://docs.cursor.com/tr/background-agent/api/launch-an-agent

en/background-agent/api/openapi.yaml post /v0/agents
Depoda çalışacak yeni bir arka plan agent'ı başlat.




# Aracıları Listele
Source: https://docs.cursor.com/tr/background-agent/api/list-agents

en/background-agent/api/openapi.yaml get /v0/agents
Kimliği doğrulanmış kullanıcı için tüm arka plan aracıların sayfalı listesini al.




# Modelleri Listele
Source: https://docs.cursor.com/tr/background-agent/api/list-models

en/background-agent/api/openapi.yaml get /v0/models
Arka plan ajanları için önerilen modellerin listesini al.

Oluşturma sırasında arka plan ajanın modelini belirtmek istiyorsan, önerilen modellerin listesini görmek için bu endpoint’i kullanabilirsin.

Bu durumda ayrıca bir "Auto" seçeneği bulundurmanı öneriyoruz. Bu seçenekle oluşturma endpoint’ine bir model adı vermezsin, en uygun modeli biz seçeriz.



# GitHub Depolarını Listele
Source: https://docs.cursor.com/tr/background-agent/api/list-repositories

en/background-agent/api/openapi.yaml get /v0/repositories
Kimliği doğrulanmış kullanıcının erişebildiği GitHub depolarının listesini al.

<Warning>
  **Bu endpoint’in hız limitleri çok katı.**

  İstekleri **kullanıcı başına 1/dakika** ve **kullanıcı başına 30/saat** ile sınırla.

  Birçok depoya erişimi olan kullanıcılar için bu isteğin yanıtı onlarca saniye sürebilir.

  Bu bilginin mevcut olmadığı durumları sorunsuzca ele aldığından emin ol.
</Warning>



# Genel Bakış
Source: https://docs.cursor.com/tr/background-agent/api/overview

Depolarında çalışan arka plan ajanlarını programatik olarak oluştur ve yönet

<div id="background-agents-api">
  # Background Agents API
</div>

<Badge variant="beta">Beta</Badge>

Background Agents API, depolarında otonom çalışan yapay zekâ destekli kodlama ajanlarını programatik olarak oluşturup yönetmeni sağlar.
API’yi kullanıcı geri bildirimlerine otomatik yanıt vermek, hataları düzeltmek, dokümanları güncellemek ve çok daha fazlası için kullanabilirsin!

<Info>
  Background Agents API şu anda beta aşamasında; bununla ilgili geri bildirimlerini çok isteriz!
</Info>

<div id="key-features">
  ## Temel özellikler
</div>

* **Otonom kod üretimi** - Prompt'unu anlayıp kod tabanında değişiklik yapabilen agent'lar oluştur
* **Depo entegrasyonu** - GitHub depolarıyla doğrudan çalış
* Takip prompt'ları - Çalışan agent'lara ek talimatlar ekle
* **Kullanıma göre fiyatlandırma** - Yalnızca kullandığın token'lar için öde
* **Ölçeklenebilir** - API anahtarı başına 256 aktif agent'a kadar destek

<div id="quick-start">
  ## Hızlı başlangıç
</div>

<div id="1-get-your-api-key">
  ### 1. API anahtarını al
</div>

API anahtarı oluşturmak için [Cursor Dashboard → Integrations](https://cursor.com/dashboard?tab=integrations) sayfasına **git**.

<div id="2-start-using-the-api">
  ### 2. API’yi kullanmaya başla
</div>

Tüm API uç noktaları şu temele göredir:

```
https://api.cursor.com
```

Uç noktaların ayrıntılı listesi için [API referansına](/tr/background-agent/api/launch-an-agent) göz at.

<div id="authentication">
  ## Kimlik Doğrulama
</div>

Tüm API isteği için Bearer belirteciyle kimlik doğrulaması gerekir:

```
Authorization: Bearer SENİN_API_ANAHTARIN
```

API anahtarları [Cursor Dashboard](https://cursor.com/dashboard?tab=integrations)’da oluşturulur. Anahtarlar hesabına özeldir ve ajanlar oluşturup yönetmene izin verir (plan sınırların ve depo erişimin doğrultusunda).

<div id="pricing">
  ## Fiyatlandırma
</div>

API şu anda beta aşamasında ve Background Agents ile aynı fiyatlandırmaya sahip. Hizmeti ölçeklendirdikçe fiyatlandırma değişebilir. [Background Agent fiyatlandırmasına](/tr/account/pricing#background-agent) göz at.

<div id="next-steps">
  ## Sonraki adımlar
</div>

* Ortamları, izinleri ve iş akışlarını anlamak için [Background Agents genel bakış](/tr/background-agent) ana belgesini oku.
* Background Agents'ı [web ve mobil](/tr/background-agent/web-and-mobile) üzerinden dene.
* [Discord #background-agent](https://discord.gg/jfgpZtYpmb) kanalında sohbete katıl ya da [background-agent-feedback@cursor.com](mailto:background-agent-feedback@cursor.com) adresine e‑posta gönder.



# Webhook’lar
Source: https://docs.cursor.com/tr/background-agent/api/webhooks

Arka plan aracısı durum değişiklikleri için gerçek zamanlı bildirimler al

<div id="webhooks">
  # Webhook'lar
</div>

Bir agent'i bir webhook URL'siyle oluşturduğunda, Cursor durum değişiklikleri hakkında seni bilgilendirmek için HTTP POST istekleri gönderir. Şu anda yalnızca `statusChange` olayları destekleniyor; özellikle bir agent `ERROR` veya `FINISHED` durumuna geçtiğinde.

<div id="webhook-verification">
  ## Webhook doğrulama
</div>

Webhook isteklerinin gerçekten Cursor’dan geldiğinden emin olmak için, her isteğe eklenen imzayı doğrula:

<div id="headers">
  ### Headers
</div>

Her webhook isteği aşağıdaki header’ları içerir:

* **`X-Webhook-Signature`** – `sha256=<hex_digest>` formatında HMAC-SHA256 imzasını içerir
* **`X-Webhook-ID`** – Bu teslimat için benzersiz bir tanımlayıcı (loglama için yararlı)
* **`X-Webhook-Event`** – Olay türü (şu anda yalnızca `statusChange`)
* **`User-Agent`** – Her zaman `Cursor-Agent-Webhook/1.0` olarak ayarlanır

<div id="signature-verification">
  ### İmza doğrulama
</div>

Webhook imzasını doğrulamak için beklenen imzayı hesapla ve alınan imzayla karşılaştır:

```javascript  theme={null}
const crypto = require('crypto');

function verifyWebhook(secret, rawBody, signature) {
  const expectedSignature = 'sha256=' + 
    crypto.createHmac('sha256', secret)
          .update(rawBody)
          .digest('hex');
  
  return signature === expectedSignature;
}
```

```python  theme={null}
import hmac
import hashlib

def webhooku_dogrula(gizli_anahtar, ham_govde, imza):
    beklenen_imza = 'sha256=' + hmac.new(
        gizli_anahtar.encode(),
        ham_govde,
        hashlib.sha256
    ).hexdigest()
    
    return imza == beklenen_imza
```

İmzayı hesaplarken her zaman pars edilmeden önceki ham istek gövdesini kullan.

<div id="payload-format">
  ## Yük biçimi
</div>

Webhook yükü, aşağıdaki yapıda JSON olarak gönderilir:

```json  theme={null}
{
  "event": "statusChange",
  "timestamp": "2024-01-15T10:30:00Z",
  "id": "bc_abc123",
  "status": "FINISHED",
  "source": {
    "repository": "https://github.com/your-org/your-repo",
    "ref": "main"
  },
  "target": {
    "url": "https://cursor.com/agents?id=bc_abc123",
    "branchName": "cursor/add-readme-1234",
    "prUrl": "https://github.com/your-org/your-repo/pull/1234"
  },
  "summary": "Kurulum talimatlarını içeren README.md eklendi"
}
```

Bazı alanların isteğe bağlı olduğunu ve yalnızca mevcut olduklarında dahil edileceğini unutma.

<div id="best-practices">
  ## En iyi uygulamalar
</div>

* **İmzaları doğrula** – İsteğin Cursor’dan geldiğinden emin olmak için webhook imzasını her zaman doğrula
* **Yeniden denemeleri ele al** – Uç noktan hata durum kodu döndürürse webhooks yeniden denenebilir
* **Hızlı yanıt ver** – Mümkün olan en kısa sürede 2xx durum kodu döndür
* **HTTPS kullan** – Üretimde webhook uç noktaları için her zaman HTTPS URL’leri kullan
* **Ham payload’ları sakla** – Hata ayıklama ve ilerideki doğrulamalar için ham webhook payload’ını sakla



# Web ve Mobil
Source: https://docs.cursor.com/tr/background-agent/web-and-mobile

Herhangi bir cihazdan kodlama agent'larını çalıştır; masaüstüne sorunsuz aktar

<div id="overview">
  ## Genel Bakış
</div>

Cursor’ın webdeki Agent özelliği, güçlü bir kodlama asistanını her cihaza getiriyor. İster yürürken telefondasın, ister web tarayıcında çalışıyorsun, artık arka planda çalışacak güçlü kodlama agent’larını başlatabilirsin.
İşleri bittiğinde, çalışmalarını Cursor içinde devral, değişiklikleri gözden geçirip birleştir ya da ekibinle iş birliği yapmak için bağlantılar paylaş.

Başlamak için [cursor.com/agents](https://cursor.com/agents).

<Frame><img src="https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/webagent/cursor-web-1.png?fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=79c7d14df82cfcae369bccb8a1431cf3" alt="Cursor web agent arayüzü" data-og-width="4095" width="4095" data-og-height="2048" height="2048" data-path="images/webagent/cursor-web-1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/webagent/cursor-web-1.png?w=280&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=099c28633151e6c20eebc7fe03b3d420 280w, https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/webagent/cursor-web-1.png?w=560&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=452e0216c7e270d760072032f1e2b36d 560w, https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/webagent/cursor-web-1.png?w=840&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=baaa4a73d4822b5daa293814dc201d37 840w, https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/webagent/cursor-web-1.png?w=1100&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=8c5255fbf16aa60924e78a8285afb95d 1100w, https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/webagent/cursor-web-1.png?w=1650&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=7cc5a04ff6b24ad4ce0cfb4a35a9919c 1650w, https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/webagent/cursor-web-1.png?w=2500&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=f5f1b15fa508e20f89a4089f81417774 2500w" /></Frame>

<div id="getting-started">
  ## Başlarken
</div>

<div id="quick-setup">
  ### Hızlı kurulum
</div>

1. **Web uygulamasını ziyaret et**: Herhangi bir cihazdan [cursor.com/agents](https://cursor.com/agents) adresine git
2. **Giriş yap**: Cursor hesabınla oturum aç
3. **GitHub’ı bağla**: Depolara erişmek için GitHub hesabını bağla
4. **İlk agent’ını çalıştır**: Bir görev yaz ve agent’ın işe koyulmasını izle

<div id="mobile-installation">
  ### Mobil kurulum
</div>

En iyi mobil deneyim için Cursor’ı Bir İlerlemeli Web Uygulaması (PWA) olarak yükle:

* **iOS**: Safari’de [cursor.com/agents](https://cursor.com/agents) adresini aç, paylaş düğmesine dokun, ardından “Ana Ekrana Ekle”
* **Android**: URL’yi Chrome’da aç, menüye dokun, ardından “Ana Ekrana Ekle” veya “Uygulamayı Yükle”

<Tip>
  PWA olarak yüklemek şu avantajlarla yerel bir deneyim sunar: - Tam ekran
  arayüz - Daha hızlı açılış - Ana ekranında uygulama simgesi
</Tip>

<div id="working-across-devices">
  ## Cihazlar arasında çalışma
</div>

Web ve Mobil Agent, masaüstü iş akışınla uyumlu olacak şekilde tasarlandı; ajanın işini IDE'nde sürdürmek için "Open in Cursor"a tıkla.

<Frame><img src="https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/webagent/cursor-web-2.png?fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=352140fd4bf3f3d98a1e1b9f4a995cad" alt="Gözden geçirme ve devretme" data-og-width="4095" width="4095" data-og-height="2048" height="2048" data-path="images/webagent/cursor-web-2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/webagent/cursor-web-2.png?w=280&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=eedd50318503fd3d3961b6da27a386d9 280w, https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/webagent/cursor-web-2.png?w=560&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=fd8c730cf62a0af6f873945a6a23b90b 560w, https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/webagent/cursor-web-2.png?w=840&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=ac537cc639471556f1afa0e09425ef30 840w, https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/webagent/cursor-web-2.png?w=1100&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=d512cddda6890c0749a7ad6396682def 1100w, https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/webagent/cursor-web-2.png?w=1650&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=e208297f414976bcfeea6850b39e8abb 1650w, https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/webagent/cursor-web-2.png?w=2500&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=54683ff7f25750fdc788e87c30bb6d6d 2500w" /></Frame>

<div id="team-collaboration">
  ### Takım iş birliği
</div>

* **Paylaşılan erişim**: Ajan çalıştırmalarında birlikte çalışmak için takım üyeleriyle bağlantılar paylaş.
* **Gözden geçirme süreci**: İş arkadaşların diff'leri inceleyip geri bildirim verebilir.
* **Pull request yönetimi**: Pull request'leri doğrudan web arayüzünden oluştur, gözden geçir ve birleştir.

<div id="slack-integration">
  ### Slack entegrasyonu
</div>

Slack’te `@Cursor`dan bahsederek ajanları doğrudan tetikle; web veya mobilden ajan başlatırken tamamlandığında Slack bildirimleri almayı da seçebilirsin.

<Card title="Slack’te Cursor kullan" icon="slack" href="/tr/slack">
  Slack entegrasyonunu kurma ve kullanma hakkında daha fazla bilgi edin,
  ajan tetikleme ve bildirim alma dahil.
</Card>

<div id="pricing">
  ## Fiyatlandırma
</div>

Web ve mobil ajanlar, Background Agents ile aynı fiyatlandırma modelini kullanır.

[Background Agent fiyatlandırması](/tr/account/pricing#background-agent) hakkında daha fazla bilgi edin.

<div id="troubleshooting">
  ## Sorun Giderme
</div>

<AccordionGroup>
  <Accordion title="Agent çalışmaları başlamıyor">
    * Giriş yaptığından ve GitHub hesabını bağladığından emin ol. - Gerekli
      depo izinlerine sahip olduğunu kontrol et. - Kullanım bazlı fiyatlandırma
      etkin olan bir Pro Denemesi veya ücretli planda olman gerekir. Kullanım
      bazlı fiyatlandırmayı etkinleştirmek için
      [Dashboard](https://www.cursor.com/dashboard?tab=settings) bölümünde Ayarlar sekmesine git.
  </Accordion>

  <Accordion title="Mobilde agent çalışmalarını göremiyorum">
    Sayfayı yenilemeyi veya tarayıcı önbelleğini temizlemeyi dene. Cihazlar
    arasında aynı hesabı kullandığından emin ol.
  </Accordion>

  <Accordion title="Slack entegrasyonu çalışmıyor">
    Çalışma alanı yöneticinin Cursor Slack uygulamasını yüklediğini ve gerekli
    izinlere sahip olduğunu doğrula.
  </Accordion>
</AccordionGroup>



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

**Navigation:** [← Previous](./34-модели.md) | [Index](./index.md) | [Next →](./36-kod-incelemesi.md)