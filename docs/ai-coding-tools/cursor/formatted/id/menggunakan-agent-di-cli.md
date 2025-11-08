---
title: "Menggunakan Agent di CLI"
source: "https://docs.cursor.com/id/cli/using"
language: "id"
language_name: "Indonesian"
---

# Menggunakan Agent di CLI
Source: https://docs.cursor.com/id/cli/using

Meminta, meninjau, dan beriterasi secara efektif dengan Cursor CLI

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
  ## Prompting
</div>

Ngasih tahu intent dengan jelas itu disarankan biar hasilnya maksimal. Misalnya, lo bisa pakai prompt "do not write any code" buat memastikan agent nggak bakal ngedit file apa pun. Ini biasanya membantu waktu ngerencanain task sebelum ngejalaninnya.

Agent saat ini punya tools buat operasi file, pencarian, dan ngejalanin perintah shell. Lebih banyak tools bakal ditambahin, mirip kayak agent di IDE.

<div id="mcp">
  ## MCP
</div>

Agent mendukung [MCP (Model Context Protocol)](/id/tools/mcp) untuk fungsionalitas dan integrasi yang lebih luas. CLI bakal otomatis mendeteksi dan mengikuti file konfigurasi `mcp.json` lo, jadi server dan tool MCP yang sama kayak yang udah lo set di IDE bakal aktif juga.

<div id="rules">
  ## Rules
</div>

Agen CLI mendukung [sistem rules](/id/context/rules) yang sama seperti di IDE. Kamu bisa bikin rules di direktori `.cursor/rules` buat ngasih konteks dan panduan ke agen. Rules ini bakal otomatis dimuat dan diterapkan sesuai konfigurasinya, jadi kamu bisa ngustom perilaku agen buat bagian-bagian tertentu di proyekmu atau tipe file tertentu.

<Note>
  CLI juga baca `AGENTS.md` dan `CLAUDE.md` di root proyek (kalau ada) dan nerapinnya sebagai rules bareng `.cursor/rules`.
</Note>

<div id="working-with-agent">
  ## Bekerja dengan Agent
</div>

<div id="navigation">
  ### Navigasi
</div>

Pesan sebelumnya bisa diakses pakai panah atas (<Kbd>ArrowUp</Kbd>) dan kamu bisa menelusurinya satu per satu.

<div id="review">
  ### Review
</div>

Review perubahan dengan <Kbd>Cmd+R</Kbd>. Tekan <Kbd>i</Kbd> buat nambah instruksi lanjutan. Pakai <Kbd>ArrowUp</Kbd>/<Kbd>ArrowDown</Kbd> buat nge-scroll, dan <Kbd>ArrowLeft</Kbd>/<Kbd>ArrowRight</Kbd> buat pindah file.

<div id="selecting-context">
  ### Memilih konteks
</div>

Pilih file dan folder buat disertakan ke konteks dengan <Kbd>@</Kbd>. Bebasin ruang di jendela konteks dengan menjalankan `/compress`. Lihat [Summarization](/id/agent/chat/summarization) buat detailnya.

<div id="history">
  ## Riwayat
</div>

Lanjutkan dari thread yang sudah ada dengan `--resume [thread id]` untuk memuat konteks sebelumnya.

Untuk melanjutkan percakapan terbaru, gunakan `cursor-agent resume`.

Kamu juga bisa menjalankan `cursor-agent ls` untuk melihat daftar percakapan sebelumnya.

<div id="command-approval">
  ## Persetujuan perintah
</div>

Sebelum ngejalanin perintah di terminal, CLI bakal minta lo buat nyetujuin (<Kbd>y</Kbd>) atau nolak (<Kbd>n</Kbd>) eksekusinya.

<div id="non-interactive-mode">
  ## Mode non-interaktif
</div>

Gunakan `-p` atau `--print` buat jalanin Agent dalam mode non-interaktif. Ini bakal nge-print respons ke konsol.

Dengan mode non-interaktif, lo bisa manggil Agent tanpa interaksi. Ini bikin lo bisa ngintegrasiin Agent ke skrip, pipeline CI, dll.

Lo bisa nggabungin ini dengan `--output-format` buat ngontrol format output. Misalnya, pakai `--output-format json` buat output terstruktur yang lebih gampang di-parse di skrip, atau `--output-format text` buat output teks polos.

<Note>
  Cursor punya akses tulis penuh dalam mode non-interaktif.
</Note>

---

← Previous: [Mode Shell](./mode-shell.md) | [Index](./index.md) | Next: [Pintasan Keyboard](./pintasan-keyboard.md) →