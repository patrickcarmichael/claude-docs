---
title: "CLI’de Agent Kullanımı"
source: "https://docs.cursor.com/tr/cli/using"
language: "tr"
language_name: "Turkish"
---

# CLI’de Agent Kullanımı
Source: https://docs.cursor.com/tr/cli/using

Cursor CLI ile etkili şekilde prompt yaz, gözden geçir ve yinele

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

<div id="prompting">
  ## Komut Yazımı
</div>

En iyi sonuçlar için niyetini net belirtmen önerilir. Örneğin, "hiç kod yazma" şeklinde bir komut kullanarak agent'ın hiçbir dosyayı düzenlememesini garanti edebilirsin. Bu, genelde bir şeyi hayata geçirmeden önce görevleri planlarken işe yarar.

Agent şu anda dosya işlemleri, arama ve kabuk komutlarını çalıştırma için araçlara sahip. IDE agent'ına benzer şekilde daha fazla araç ekleniyor.

<div id="mcp">
  ## MCP
</div>

Agent, genişletilmiş işlevsellik ve entegrasyonlar için [MCP (Model Context Protocol)](/tr/tools/mcp) destekler. CLI, `mcp.json` yapılandırma dosyanı otomatik olarak algılar ve buna uyar; böylece IDE’de yapılandırdığın aynı MCP sunucuları ve araçları etkinleştirilir.

<div id="rules">
  ## Kurallar
</div>

CLI agent, IDE ile aynı [kural sistemini](/tr/context/rules) destekler. Ajana bağlam ve yönlendirme sağlamak için `.cursor/rules` dizininde kurallar oluşturabilirsin. Bu kurallar yapılandırmalarına göre otomatik olarak yüklenir ve uygulanır; böylece projenin farklı bölümleri ya da belirli dosya türleri için ajanın davranışını özelleştirebilirsin.

<Note>
  CLI ayrıca proje kökünde (varsa) `AGENTS.md` ve `CLAUDE.md` dosyalarını da okur ve bunları `.cursor/rules` ile birlikte kurallar olarak uygular.
</Note>

<div id="working-with-agent">
  ## Agent ile çalışma
</div>

<div id="navigation">
  ### Gezinme
</div>

Önceki mesajlara yukarı ok (<Kbd>ArrowUp</Kbd>) ile erişebilir, aralarında dolaşabilirsin.

<div id="review">
  ### İnceleme
</div>

Değişiklikleri <Kbd>Cmd+R</Kbd> ile gözden geçir. Takip talimatı eklemek için <Kbd>i</Kbd>’ye bas. Kaydırmak için <Kbd>ArrowUp</Kbd>/<Kbd>ArrowDown</Kbd>, dosyalar arasında geçiş yapmak için <Kbd>ArrowLeft</Kbd>/<Kbd>ArrowRight</Kbd> kullan.

<div id="selecting-context">
  ### Bağlam seçme
</div>

Bağlama dahil etmek için dosya ve klasörleri <Kbd>@</Kbd> ile seç. Bağlam penceresinde yer açmak için `/compress` komutunu çalıştır. Ayrıntılar için [Özetleme](/tr/agent/chat/summarization) sayfasına bak.

<div id="history">
  ## Geçmiş
</div>

Önceki bağlamı yüklemek için mevcut bir ileti dizisinden `--resume [thread id]` ile devam et.

En son sohbeti sürdürmek için `cursor-agent resume` kullan.

Ayrıca önceki sohbetlerin listesini görmek için `cursor-agent ls` komutunu çalıştırabilirsin.

<div id="command-approval">
  ## Komut onayı
</div>

Terminal komutlarını çalıştırmadan önce CLI, yürütmeyi onaylamanı (<Kbd>y</Kbd>) ya da reddetmeni (<Kbd>n</Kbd>) isteyecek.

<div id="non-interactive-mode">
  ## Etkileşimsiz mod
</div>

Agent’i etkileşimsiz modda çalıştırmak için `-p` veya `--print` kullan. Bu, yanıtı konsola yazdırır.

Etkileşimsiz modda, Agent’i etkileşime girmeden çağırabilirsin. Böylece onu betiklere, CI hatlarına vb. entegre edebilirsin.

Çıktının biçimini kontrol etmek için bunu `--output-format` ile birleştirebilirsin. Örneğin, betiklerde ayrıştırması daha kolay olan yapılandırılmış çıktı için `--output-format json`, düz metin çıktısı için `--output-format text` kullan.

<Note>
  Cursor’ın etkileşimsiz modda tam yazma yetkisi vardır.
</Note>

---

← Previous: [Shell Modu](./shell-modu.md) | [Index](./index.md) | Next: [Klavye Kısayolları](./klavye-ksayollar.md) →