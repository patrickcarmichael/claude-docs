---
title: "Perencanaan"
source: "https://docs.cursor.com/id/agent/planning"
language: "id"
language_name: "Indonesian"
---

# Perencanaan
Source: https://docs.cursor.com/id/agent/planning

Cara Agent merencanakan dan mengelola tugas kompleks dengan to-do dan antrean

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

Agent bisa merencanakan terlebih dulu dan mengelola tugas kompleks dengan daftar tugas yang terstruktur serta antrian pesan, sehingga tugas berjangka panjang lebih mudah dipahami dan dipantau.

<div id="agent-to-dos">
  ## To-do Agent
</div>

Agent bisa memecah tugas panjang menjadi langkah-langkah yang mudah dikelola dengan dependensi, sehingga terbentuk rencana terstruktur yang terus diperbarui seiring progres kerja.

<video autoPlay loop muted playsInline controls>
  <source src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/agent/planning/agent-todo.mp4?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=b0285913832a3ef123fe149516ee37ea" type="video/mp4" data-path="images/agent/planning/agent-todo.mp4" />
</video>

<div id="how-it-works">
  ### Cara kerja
</div>

* Agent otomatis membuat daftar to-do untuk tugas kompleks
* Tiap item bisa punya dependensi pada tugas lain
* Daftar diperbarui secara real-time seiring progres berjalan
* Tugas yang selesai ditandai otomatis

<div id="visibility">
  ### Visibilitas
</div>

* To-do muncul di antarmuka chat
* Kalau [integrasi Slack](/id/slack) disetel, to-do juga keliatan di sana
* Kamu bisa melihat rincian pemecahan tugas lengkap kapan aja

<Tip>
  Biar perencanaannya lebih bagus, jelasin tujuan akhirnya dengan jelas. Agent bakal bikin
  pemecahan tugas yang lebih akurat kalau paham cakupan penuh.
</Tip>

<Note>Perencanaan dan to-do saat ini belum didukung di mode otomatis.</Note>

<div id="queued-messages">
  ## Pesan dalam antrean
</div>

Antre pesan lanjutan sementara Agent ngerjain tugas saat ini. Instruksi lo nunggu di antrean dan jalan otomatis begitu siap.

<video autoPlay loop muted playsInline controls>
  <source src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/agent/planning/agent-queue.mp4?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=4cdd6a7d1e12c67e520bc3ba67a42e0d" type="video/mp4" data-path="images/agent/planning/agent-queue.mp4" />
</video>

<div id="using-the-queue">
  ### Menggunakan antrean
</div>

1. Sambil Agent bekerja, ketik instruksi berikutnya
2. Tekan <Kbd>Ctrl+Enter</Kbd> buat nambahkannya ke antrean
3. Pesan muncul berurutan di bawah tugas aktif
4. Ubah urutan pesan yang diantrikan dengan klik panah
5. Agent bakal memprosesnya satu per satu setelah selesai

<div id="override-the-queue">
  ### Mengabaikan antrean
</div>

Buat masukin pesan lo ke antrean alih-alih pakai pengiriman default, gunakan <Kbd>Ctrl+Enter</Kbd>. Buat ngirim pesan langsung tanpa diantrikan, gunakan <Kbd>Cmd+Enter</Kbd>. Ini bakal “memaksa” pesan lo dikirim, ngelewatin antrean supaya langsung dieksekusi.

<div id="default-messaging">
  ## Pesan default
</div>

Secara default, pesan dikirim secepat mungkin, biasanya muncul tepat setelah Agent selesai menjalankan pemanggilan tool. Ini bikin pengalaman jadi paling responsif.

<div id="how-default-messaging-works">
  ### Cara kerja pesan default
</div>

* Pesan lo bakal digabung ke pesan user terbaru di chat
* Pesan biasanya menempel ke hasil tool dan langsung dikirim begitu siap
* Ini bikin alur percakapan lebih natural tanpa mengganggu kerja Agent saat ini
* Secara default, ini kejadian saat lo menekan Enter sementara Agent lagi bekerja

---

← Previous: [Ikhtisar](./ikhtisar.md) | [Index](./index.md) | Next: [Diffs & Review](./diffs-review.md) →