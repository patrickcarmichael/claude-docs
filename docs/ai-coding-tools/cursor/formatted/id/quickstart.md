---
title: "Quickstart"
source: "https://docs.cursor.com/id/get-started/quickstart"
language: "id"
language_name: "Indonesian"
---

# Quickstart
Source: https://docs.cursor.com/id/get-started/quickstart

Mulai dengan Cursor dalam 5 menit

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

Quickstart ini bakal ngebimbing lo lewat sebuah proyek yang pakai fitur inti Cursor. Di akhir, lo bakal familiar dengan Tab, Inline Edit, dan Agent.

<div id="open-a-project-in-cursor">
  ## Buka proyek di Cursor
</div>

Pakai proyek yang sudah ada atau clone contoh dari kami:

<Tabs>
  <Tab title="Clone example project">
    1. Pastikan git sudah terpasang
    2. Clone proyek contoh:

    ```bash  theme={null}
    git clone git@github.com:voxelize/voxelize.git && \
    cd voxelize && \
    cursor .
    ```
  </Tab>

  <Tab title="Use existing project">
    1. Buka Cursor
    2. Buka folder proyek dengan <Kbd>Cmd O</Kbd> atau `cursor <path-to-project>`
  </Tab>
</Tabs>

Kita bakal demo pakai proyek contoh, tapi lo bisa pakai proyek apa pun yang lo punya secara lokal.

<div id="autocomplete-with-tab">
  ## Autocomplete dengan [Tab](/id/kbd#tab)
</div>

Tab adalah model autocomplete yang kami latih sendiri. Ini cara yang pas buat mulai pakai coding berbantuan AI kalau kamu belum terbiasa. Dengan Tab, kamu bisa:

* Melengkapi **banyak baris dan blok** kode
* Melompat **di dalam** dan **antar** file ke saran autocomplete berikutnya

1. Mulai mengetik awal sebuah fungsi:
   ```javascript  theme={null}
   function calculate
   ```
2. Saran Tab muncul otomatis
3. Tekan Tab untuk menerima saran
4. Cursor menyarankan parameter dan body fungsi

<div id="inline-edit-a-selection">
  ## [Inline Edit](/id/inline-edit) pada sebuah pilihan
</div>

1. Pilih fungsi yang baru aja kamu buat
2. Tekan <Kbd>Cmd K</Kbd>
3. Ketik "make this function calculate fibonacci numbers"
4. Tekan <Kbd>Return</Kbd> untuk menerapkan perubahan
5. Cursor menambahkan import dan dokumentasi

<div id="chat-with-agent">
  ## Ngobrol dengan [Agent](/id/agent)
</div>

1. Buka panel Chat (<Kbd>Cmd I</Kbd>)
2. Tanyain: "Add tests for this function and run them"
3. Agent bakal bikin file test, nulis test case, dan ngejalaninnya buat lo

<div id="bonus">
  ## Bonus
</div>

Fitur lanjutan:

<AccordionGroup>
  <Accordion title="Serahkan pekerjaan ke Background Agent">
    1. Buka panel kontrol Background Agent (<Kbd>Cmd E</Kbd>)
    2. Tanyakan: "Find and fix a bug in this project"
    3. [Background Agent](/id/background-agent) akan:
       * Membuat Virtual Machine (VM) remote
       * Menjelajahi proyek lo
       * Mendeteksi bug
       * Mengusulkan perbaikan

    Tinjau dan terapkan perubahan.
  </Accordion>

  {" "}

  <Accordion title="Tulis rule">
    1. Buka command palette (<Kbd>Cmd Shift P</Kbd>) 2. Cari: "New Cursor
       Rule" 3. Kasih nama (mis., `style-guide`) 4. Pilih Rule Type "Always" 5. Tentukan
       gaya lo: `Prefer using camelCase for variable names`
  </Accordion>

  <Accordion title="Siapkan server MCP">
    1. Kunjungi [direktori MCP](https://docs.cursor.com/tools) kami
    2. Pilih tool
    3. Klik "Install"

    Server juga bisa diinstal secara manual:

    1. Buka Cursor Settings (<Kbd>Cmd Shift J</Kbd>)
    2. Masuk ke "Tools & Integrations"
    3. Klik "New MCP Server"
  </Accordion>
</AccordionGroup>

<div id="next-steps">
  ## Langkah berikutnya
</div>

Jelajahi panduan ini untuk belajar lebih lanjut:

<CardGroup cols={2}>
  <Card title="Working with Context" href="/id/guides/working-with-context">
    Kasih konteks yang efektif biar hasilnya lebih bagus
  </Card>

  <Card title="Selecting Models" href="/id/guides/selecting-models">
    Pilih model yang pas buat tugas lo
  </Card>
</CardGroup>

Pelajari semua [konsep Cursor](/id/get-started/concepts) dan mulai berkarya!

---

← Previous: [Instalasi](./instalasi.md) | [Index](./index.md) | Next: [Data Science](./data-science.md) →