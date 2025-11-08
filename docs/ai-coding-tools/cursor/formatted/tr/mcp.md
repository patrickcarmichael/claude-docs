---
title: "MCP"
source: "https://docs.cursor.com/tr/cli/mcp"
language: "tr"
language_name: "Turkish"
---

# MCP
Source: https://docs.cursor.com/tr/cli/mcp

MCP sunucularını cursor-agent ile kullanarak harici araçlara ve veri kaynaklarına bağlan

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

<div id="overview">
  ## Genel Bakış
</div>

Cursor CLI, `cursor-agent`e harici araçlar ve veri kaynaklarını bağlamanı sağlayan [Model Context Protocol (MCP)](/tr/context/mcp) sunucularını destekler. **CLI’deki MCP, düzenleyiciyle aynı yapılandırmayı kullanır** — yapılandırdığın tüm MCP sunucuları her ikisinde de sorunsuz çalışır.

<Card title="MCP hakkında bilgi edin" icon="link" href="/tr/context/mcp">
  MCP’ye yeni misin? Yapılandırma, kimlik doğrulama ve mevcut sunuculara dair kapsamlı kılavuzu oku
</Card>

<div id="cli-commands">
  ## CLI komutları
</div>

MCP sunucularını yönetmek için `cursor-agent mcp` komutunu kullan:

<div id="list-configured-servers">
  ### Yapılandırılmış sunucuları listele
</div>

Yapılandırılmış tüm MCP sunucularını ve mevcut durumlarını görüntüle:

```bash  theme={null}
cursor-agent mcp list
```

Bu şunları gösterir:

* Sunucu adları ve tanımlayıcıları
* Bağlantı durumu (bağlı/bağlantı kesik)
* Yapılandırma kaynağı (proje veya genel)
* Taşıma yöntemi (stdio, HTTP, SSE)

<div id="list-available-tools">
  ### Kullanılabilir araçları listele
</div>

Belirli bir MCP sunucusunun sunduğu araçları görüntüle:

```bash  theme={null}
cursor-agent mcp list-tools <kimlik>
```

Bu şunları gösterir:

* Araç adları ve açıklamaları
* Zorunlu ve isteğe bağlı parametreler
* Parametre türleri ve kısıtlamaları

<div id="login-to-mcp-server">
  ### MCP sunucusuna giriş yap
</div>

`mcp.json` içinde yapılandırılmış bir MCP sunucusunda kimlik doğrula:

```bash  theme={null}
cursor-agent mcp login <kimlik>
```

<div id="disable-mcp-server">
  ### MCP sunucusunu devre dışı bırak
</div>

Yerel onaylı listeden bir MCP sunucusunu kaldır:

```bash  theme={null}
cursor-agent mcp disable <tanımlayıcı>
```

<div id="using-mcp-with-agent">
  ## Agent ile MCP kullanma
</div>

MCP sunucularını yapılandırdıktan sonra (kurulum için [ana MCP kılavuzuna](/tr/context/mcp) bak), `cursor-agent` isteklerinle ilgili olduğunda uygun araçları otomatik olarak bulur ve kullanır.

```bash  theme={null}

---

← Previous: [Kurulum](./kurulum.md) | [Index](./index.md) | Next: [Cursor CLI](./cursor-cli.md) →