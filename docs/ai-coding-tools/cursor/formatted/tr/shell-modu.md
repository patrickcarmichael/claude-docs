---
title: "Shell Modu"
source: "https://docs.cursor.com/tr/cli/shell-mode"
language: "tr"
language_name: "Turkish"
---

# Shell Modu
Source: https://docs.cursor.com/tr/cli/shell-mode

Sohbetten çıkmadan CLI üzerinden doğrudan shell komutları çalıştır

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

Shell Mode, sohbetten çıkmadan komut satırından doğrudan shell komutları çalıştırır. Güvenlik kontrolleriyle birlikte çıktısı sohbette gösterilen hızlı, etkileşimsiz komutlar için kullan.

<Frame>
  <video src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/cli/shell-mode/cli-shell-mode.mp4?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=5194392f1189eb1eba340d731e86bd5f" autoPlay loop muted playsInline controls data-path="images/cli/shell-mode/cli-shell-mode.mp4" />
</Frame>

<div id="command-execution">
  ## Komut yürütme
</div>

Komutlar, oturum açtığın kabukta (`$SHELL`), CLI’nin çalışma dizini ve ortamıyla çalıştırılır. Başka dizinlerde çalıştırmak için komutları zincirle:

```bash  theme={null}
cd subdir && npm test
```

<div id="output">
  ## Çıktı
</div>

<product_visual type="screenshot">
  Komut çıktısı; çıkış kodunu gösteren başlık, stdout/stderr görüntüleme ve kırpma denetimlerini gösteriyor
</product_visual>

Büyük çıktılar otomatik olarak kırpılır ve uzun süre çalışan işlemler performansı korumak için zaman aşımına uğratılır.

<div id="limitations">
  ## Sınırlamalar
</div>

* Komutlar 30 saniye sonra zaman aşımına uğrar
* Uzun süre çalışan işlemler, sunucular ve etkileşimli istemler desteklenmez
* En iyi sonuçlar için kısa, etkileşime girmeyen komutlar kullan

<div id="permissions">
  ## İzinler
</div>

Komutlar, çalıştırılmadan önce izinlerin ve takım ayarlarınla karşılaştırılarak kontrol edilir. Ayrıntılı yapılandırma için [Permissions](/tr/cli/reference/permissions) sayfasına bak.

<product_visual type="screenshot">
  Onay seçeneklerini gösteren karar bandı: Run, Reject/Propose, Add to allowlist ve Auto-run
</product_visual>

Yönetici ilkeleri bazı komutları engelleyebilir ve yönlendirme içeren komutlar satır içinde allowlist’e eklenemez.

<div id="usage-guidelines">
  ## Kullanım yönergeleri
</div>

Shell Mode, durum kontrolleri, hızlı derlemeler, dosya işlemleri ve ortam incelemesi için iyi çalışır.

Uzun süre çalışan sunuculardan, etkileşimli uygulamalardan ve girdi gerektiren komutlardan kaçın.

Her komut bağımsız çalışır — başka dizinlerde komut çalıştırmak için `cd <dir> && ...` kullan.

<div id="troubleshooting">
  ## Sorun Giderme
</div>

* Bir komut takılırsa, <Kbd>Ctrl+C</Kbd> ile iptal et ve etkileşimsiz bayraklar ekle
* İzin istendiğinde, bir kez onayla ya da <Kbd>Tab</Kbd> ile allowlist’e ekle
* Kırpılmış çıktıyı genişletmek için <Kbd>Ctrl+O</Kbd> kullan
* Farklı dizinlerde çalıştırmak için, değişiklikler kalmadığından `cd <dir> && ...` kullan
* Shell Mode, `$SHELL` değişkenine göre zsh ve bash’i destekler

<div id="faq">
  ## SSS
</div>

<AccordionGroup>
  <Accordion title="`cd` oturumlar arasında kalıcı mı?">
    Hayır. Her komut bağımsız çalışır. Farklı dizinlerde komutları çalıştırmak için `cd <dir> && ...` kullan.
  </Accordion>

  <Accordion title="Zaman aşımını değiştirebilir miyim?">
    Hayır. Komutlar 30 saniyeyle sınırlıdır ve bu ayar değiştirilemez.
  </Accordion>

  <Accordion title="İzinler nerede yapılandırılıyor?">
    İzinler CLI ve ekip yapılandırması üzerinden yönetilir. İzin verilecek komutları eklemek için karar bandını kullan.
  </Accordion>

  <Accordion title="Shell Mode'dan nasıl çıkarım?">
    Girdi boşken <Kbd>Escape</Kbd>'e bas, girdi boşken <Kbd>Backspace</Kbd>/<Kbd>Delete</Kbd> tuşlarını kullan, ya da temizleyip çıkmak için <Kbd>Ctrl+C</Kbd> bas.
  </Accordion>
</AccordionGroup>

---

← Previous: [Slash komutları](./slash-komutlar.md) | [Index](./index.md) | Next: [CLI’de Agent Kullanımı](./clide-agent-kullanm.md) →