---
title: "Mode Shell"
source: "https://docs.cursor.com/id/cli/shell-mode"
language: "id"
language_name: "Indonesian"
---

# Mode Shell
Source: https://docs.cursor.com/id/cli/shell-mode

Jalanin perintah shell langsung dari CLI tanpa ninggalin percakapan

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

Shell Mode ngejalanin perintah shell langsung dari CLI tanpa keluar dari percakapan. Pakai buat perintah cepat yang non-interaktif dengan safety check, dan output-nya bakal ditampilin di percakapan.

<Frame>
  <video src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/cli/shell-mode/cli-shell-mode.mp4?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=5194392f1189eb1eba340d731e86bd5f" autoPlay loop muted playsInline controls data-path="images/cli/shell-mode/cli-shell-mode.mp4" />
</Frame>

<div id="command-execution">
  ## Eksekusi perintah
</div>

Perintah dijalankan di shell login lo (`$SHELL`) dengan direktori kerja dan environment milik CLI. Rangkaikan perintah buat dijalankan di direktori lain:

```bash  theme={null}
cd subdir && npm test
```

<div id="output">
  ## Output
</div>

<product_visual type="screenshot">
  Output perintah menampilkan header dengan kode keluar (exit code), tampilan stdout/stderr, dan kontrol pemendekan
</product_visual>

Output yang besar dipendekkan secara otomatis, dan proses yang berjalan lama akan di-timeout untuk menjaga performa.

<div id="limitations">
  ## Keterbatasan
</div>

* Perintah akan timeout setelah 30 detik
* Proses jangka panjang, server, dan prompt interaktif tidak didukung
* Gunakan perintah singkat yang non-interaktif untuk hasil terbaik

<div id="permissions">
  ## Permissions
</div>

Perintah bakal diperiksa berdasarkan permissions dan pengaturan tim kamu sebelum dijalankan. Lihat [Permissions](/id/cli/reference/permissions) untuk konfigurasi mendetail.

<product_visual type="screenshot">
  Banner keputusan yang menampilkan opsi persetujuan: Run, Reject/Propose, Add to allowlist, dan Auto-run
</product_visual>

Kebijakan admin bisa memblokir perintah tertentu, dan perintah dengan redirection nggak bisa dimasukkan ke allowlist secara inline.

<div id="usage-guidelines">
  ## Pedoman penggunaan
</div>

Shell Mode cocok untuk pengecekan status, build cepat, operasi file, dan inspeksi environment.

Hindari server yang berjalan lama, aplikasi interaktif, dan perintah yang memerlukan input.

Setiap perintah berjalan secara independen — pakai `cd <dir> && ...` untuk menjalankan perintah di direktori lain.

<div id="troubleshooting">
  ## Pemecahan masalah
</div>

* Kalau perintah ngegantung, batalin dengan <Kbd>Ctrl+C</Kbd> dan tambahin flag non-interaktif
* Kalau diminta izin, setujui sekali atau tambahin ke allowlist pakai <Kbd>Tab</Kbd>
* Kalau output kepotong, pakai <Kbd>Ctrl+O</Kbd> buat nge-expand
* Buat jalanin di direktori lain, pakai `cd <dir> && ...` soalnya perubahan nggak ke-save
* Shell Mode dukung zsh dan bash sesuai variabel `$SHELL` kamu

<div id="faq">
  ## FAQ
</div>

<AccordionGroup>
  <Accordion title="Apakah `cd` bertahan antar run?">
    Nggak. Tiap perintah jalan sendiri. Pakai `cd <dir> && ...` buat jalanin perintah di direktori yang beda.
  </Accordion>

  <Accordion title="Bisa nggak aku ubah timeout?">
    Nggak. Perintah dibatasi 30 detik dan ini nggak bisa dikonfigurasi.
  </Accordion>

  <Accordion title="Izin dikonfigurasinya di mana?">
    Izin dikelola lewat konfigurasi CLI dan tim. Pakai decision banner buat nambahin perintah ke allowlist.
  </Accordion>

  <Accordion title="Gimana cara keluar dari Shell Mode?">
    Tekan <Kbd>Escape</Kbd> waktu input kosong, <Kbd>Backspace</Kbd>/<Kbd>Delete</Kbd> pas input kosong, atau <Kbd>Ctrl+C</Kbd> buat nge-clear dan keluar.
  </Accordion>
</AccordionGroup>

---

← Previous: [Perintah slash](./perintah-slash.md) | [Index](./index.md) | Next: [Menggunakan Agent di CLI](./menggunakan-agent-di-cli.md) →