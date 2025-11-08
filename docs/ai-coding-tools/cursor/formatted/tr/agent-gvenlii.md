---
title: "Agent Güvenliği"
source: "https://docs.cursor.com/tr/account/agent-security"
language: "tr"
language_name: "Turkish"
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

---

← Previous: [Index](./index.md) | [Index](./index.md) | Next: [Faturalandırma](./faturalandrma.md) →