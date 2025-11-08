---
title: "Pintasan Keyboard"
source: "https://docs.cursor.com/id/configuration/kbd"
language: "id"
language_name: "Indonesian"
---

# Pintasan Keyboard
Source: https://docs.cursor.com/id/configuration/kbd

Pintasan keyboard dan pemetaan tombol di Cursor

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

Ikhtisar pintasan keyboard di Cursor. Lihat semua pintasan keyboard dengan menekan <Kbd>Cmd R</Kbd> lalu <Kbd>Cmd S</Kbd> atau dengan membuka command palette <Kbd>Cmd Shift P</Kbd> dan mencari `Keyboard Shortcuts`.

Pelajari lebih lanjut tentang pintasan keyboard di Cursor dengan [Key Bindings for VS Code](https://code.visualstudio.com/docs/getstarted/keybindings) sebagai acuan dasar untuk keybinding Cursor.

Semua keybinding di Cursor, termasuk fitur khusus Cursor, bisa diubah di pengaturan Keyboard Shortcuts.

<div id="general">
  ## Umum
</div>

<div className="full-width-table equal-table-columns">
  | Pintasan               | Aksi                                            |
  | ---------------------- | ----------------------------------------------- |
  | <Kbd>Cmd I</Kbd>       | Alihkan Panel Samping (kecuali terikat ke mode) |
  | <Kbd>Cmd L</Kbd>       | Alihkan Panel Samping (kecuali terikat ke mode) |
  | <Kbd>Cmd E</Kbd>       | Panel kontrol Background Agent                  |
  | <Kbd>Cmd .</Kbd>       | Menu Mode                                       |
  | <Kbd>Cmd /</Kbd>       | Berpindah di antara model AI                    |
  | <Kbd>Cmd Shift J</Kbd> | Pengaturan Cursor                               |
  | <Kbd>Cmd ,</Kbd>       | Pengaturan umum                                 |
  | <Kbd>Cmd Shift P</Kbd> | Palet perintah                                  |
</div>

<div id="chat">
  ## Chat
</div>

Shortcut untuk kotak input chat.

<div className="full-width-table equal-table-columns">
  | Shortcut                                             | Aksi                                        |
  | ---------------------------------------------------- | ------------------------------------------- |
  | <Kbd>Return</Kbd>                                    | Nudge (default)                             |
  | <Kbd>Ctrl Return</Kbd>                               | Antrikan pesan                              |
  | <Kbd>Cmd Return</Kbd> when typing                    | Paksa kirim pesan                           |
  | <Kbd>Cmd Shift Backspace</Kbd>                       | Batalkan pembuatan                          |
  | <Kbd>Cmd Shift L</Kbd> with code selected            | Tambahkan kode yang dipilih sebagai konteks |
  | <Kbd>Cmd V</Kbd> with code or log in clipboard       | Tambahkan isi clipboard sebagai konteks     |
  | <Kbd>Cmd Shift V</Kbd> with code or log in clipboard | Tambahkan isi clipboard ke kotak input      |
  | <Kbd>Cmd Return</Kbd> with suggested changes         | Terima semua perubahan                      |
  | <Kbd>Cmd Backspace</Kbd>                             | Tolak semua perubahan                       |
  | <Kbd>Tab</Kbd>                                       | Pindah ke pesan berikutnya                  |
  | <Kbd>Shift Tab</Kbd>                                 | Pindah ke pesan sebelumnya                  |
  | <Kbd>Cmd Opt /</Kbd>                                 | Ganti model                                 |
  | <Kbd>Cmd N</Kbd> / <Kbd>Cmd R</Kbd>                  | Chat baru                                   |
  | <Kbd>Cmd T</Kbd>                                     | Tab chat baru                               |
  | <Kbd>Cmd \[</Kbd>                                    | Chat sebelumnya                             |
  | <Kbd>Cmd ]</Kbd>                                     | Chat berikutnya                             |
  | <Kbd>Cmd W</Kbd>                                     | Tutup chat                                  |
  | <Kbd>Escape</Kbd>                                    | Lepas fokus bidang                          |
</div>

<div id="inline-edit">
  ## Edit Inline
</div>

<div className="full-width-table equal-table-columns">
  | Pintasan                       | Aksi                    |
  | ------------------------------ | ----------------------- |
  | <Kbd>Cmd K</Kbd>               | Buka                    |
  | <Kbd>Cmd Shift K</Kbd>         | Alihkan fokus input     |
  | <Kbd>Return</Kbd>              | Kirim                   |
  | <Kbd>Cmd Shift Backspace</Kbd> | Batalkan                |
  | <Kbd>Opt Return</Kbd>          | Ajukan pertanyaan cepat |
</div>

## Pemilihan Kode & Konteks

<div className="full-width-table equal-table-columns">
  | Pintasan                                             | Aksi                                                  |
  | ---------------------------------------------------- | ----------------------------------------------------- |
  | <Kbd>@</Kbd>                                         | [Simbol @](/id/context/@-symbols/)                    |
  | <Kbd>#</Kbd>                                         | File                                                  |
  | <Kbd>/</Kbd>                                         | Perintah pintasan                                     |
  | <Kbd>Cmd Shift L</Kbd>                               | Tambahkan pilihan ke Chat                             |
  | <Kbd>Cmd Shift K</Kbd>                               | Tambahkan pilihan ke Edit                             |
  | <Kbd>Cmd L</Kbd>                                     | Tambahkan pilihan ke chat baru                        |
  | <Kbd>Cmd M</Kbd>                                     | Ganti strategi pembacaan file                         |
  | <Kbd>Cmd →</Kbd>                                     | Terima kata berikutnya dari saran                     |
  | <Kbd>Cmd Return</Kbd>                                | Cari codebase di chat                                 |
  | Pilih kode, <Kbd>Cmd C</Kbd>, <Kbd>Cmd V</Kbd>       | Tambahkan kode referensi yang disalin sebagai konteks |
  | Pilih kode, <Kbd>Cmd C</Kbd>, <Kbd>Cmd Shift V</Kbd> | Tambahkan kode yang disalin sebagai konteks teks      |
</div>

<div id="tab">
  ## Tab
</div>

<div className="full-width-table equal-table-columns">
  | Pintasan         | Aksi                    |
  | ---------------- | ----------------------- |
  | <Kbd>Tab</Kbd>   | Terima saran            |
  | <Kbd>Cmd →</Kbd> | Terima kata selanjutnya |
</div>

<div id="terminal">
  ## Terminal
</div>

<div className="full-width-table equal-table-columns">
  | Shortcut              | Aksi                          |
  | --------------------- | ----------------------------- |
  | <Kbd>Cmd K</Kbd>      | Buka bar prompt terminal      |
  | <Kbd>Cmd Return</Kbd> | Jalankan perintah yang dibuat |
  | <Kbd>Escape</Kbd>     | Terima perintah               |
</div>

---

← Previous: [Menggunakan Agent di CLI](./menggunakan-agent-di-cli.md) | [Index](./index.md) | Next: [Perintah Shell](./perintah-shell.md) →