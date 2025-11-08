---
title: "Arka Plan Aracıları"
source: "https://docs.cursor.com/tr/background-agent"
language: "tr"
language_name: "Turkish"
---

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

---

← Previous: [Araçlar](./aralar.md) | [Index](./index.md) | Next: [Takip Ekle](./takip-ekle.md) →