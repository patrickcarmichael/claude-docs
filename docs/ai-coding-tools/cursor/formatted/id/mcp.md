---
title: "MCP"
source: "https://docs.cursor.com/id/cli/mcp"
language: "id"
language_name: "Indonesian"
---

# MCP
Source: https://docs.cursor.com/id/cli/mcp

Gunakan server MCP dengan cursor-agent untuk terhubung ke alat eksternal dan sumber data

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
  ## Ikhtisar
</div>

CLI Cursor mendukung server [Model Context Protocol (MCP)](/id/context/mcp), yang bikin lo bisa nyambungin tool eksternal dan sumber data ke `cursor-agent`. **MCP di CLI pakai konfigurasi yang sama kayak editor** — server MCP apa pun yang udah lo set bakal jalan mulus di keduanya.

<Card title="Pelajari tentang MCP" icon="link" href="/id/context/mcp">
  Baru kenal MCP? Baca panduan lengkap soal konfigurasi, autentikasi, dan server yang tersedia
</Card>

<div id="cli-commands">
  ## Perintah CLI
</div>

Gunakan perintah `cursor-agent mcp` buat ngelola server MCP:

<div id="list-configured-servers">
  ### Daftar server yang tersetup
</div>

Lihat semua server MCP yang tersetup dan statusnya saat ini:

```bash  theme={null}
cursor-agent mcp list
```

Ini menampilkan:

* Nama server dan pengenal
* Status koneksi (terhubung/terputus)
* Sumber konfigurasi (proyek atau global)
* Metode transport (stdio, HTTP, SSE)

<div id="list-available-tools">
  ### Lihat daftar tool yang tersedia
</div>

Lihat tool yang disediakan oleh server MCP tertentu:

```bash  theme={null}
cursor-agent mcp list-tools <identifier>
```

Ini menampilkan:

* Nama dan deskripsi tool
* Parameter wajib dan opsional
* Jenis parameter dan batasannya

<div id="login-to-mcp-server">
  ### Login ke server MCP
</div>

Lakukan autentikasi ke server MCP yang dikonfigurasi di `mcp.json`:

```bash  theme={null}
cursor-agent mcp login <identifier>
```

<div id="disable-mcp-server">
  ### Nonaktifkan server MCP
</div>

Hapus server MCP dari daftar lokal yang disetujui:

```bash  theme={null}
cursor-agent mcp disable <identifier>
```

<div id="using-mcp-with-agent">
  ## Menggunakan MCP bareng Agent
</div>

Begitu lo udah ngonfigurasi server MCP (lihat [panduan MCP utama](/id/context/mcp) buat setup), `cursor-agent` bakal otomatis nemuin dan make tools yang tersedia kalau relevan sama permintaan lo.

```bash  theme={null}

---

← Previous: [Instalasi](./instalasi.md) | [Index](./index.md) | Next: [Cursor CLI](./cursor-cli.md) →