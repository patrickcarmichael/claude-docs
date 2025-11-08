---
title: "Klavye Kısayolları"
source: "https://docs.cursor.com/tr/configuration/kbd"
language: "tr"
language_name: "Turkish"
---

# Klavye Kısayolları
Source: https://docs.cursor.com/tr/configuration/kbd

Cursor'da klavye kısayolları ve tuş bağları

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

Cursor’daki klavye kısayollarına genel bakış. Tüm kısayolları görmek için <Kbd>Cmd R</Kbd> ardından <Kbd>Cmd S</Kbd>’ye bas veya komut paletini <Kbd>Cmd Shift P</Kbd> ile açıp `Keyboard Shortcuts` arat.

Cursor’daki klavye kısayolları hakkında daha fazla bilgi için, Cursor’ın tuş eşlemeleri için temel olarak [VS Code için Key Bindings](https://code.visualstudio.com/docs/getstarted/keybindings) dokümanını kullan.

Cursor’a özgü özellikler de dahil tüm Cursor tuş eşlemelerini, Keyboard Shortcuts ayarlarında yeniden eşleyebilirsin.

<div id="general">
  ## Genel
</div>

<div className="full-width-table equal-table-columns">
  | Kısayol                | Eylem                                          |
  | ---------------------- | ---------------------------------------------- |
  | <Kbd>Cmd I</Kbd>       | Kenar paneli aç/kapat (bir moda bağlı değilse) |
  | <Kbd>Cmd L</Kbd>       | Kenar paneli aç/kapat (bir moda bağlı değilse) |
  | <Kbd>Cmd E</Kbd>       | Arka plan ajanı kontrol paneli                 |
  | <Kbd>Cmd .</Kbd>       | Mod menüsü                                     |
  | <Kbd>Cmd /</Kbd>       | Yapay zeka modelleri arasında geçiş yap        |
  | <Kbd>Cmd Shift J</Kbd> | Cursor ayarları                                |
  | <Kbd>Cmd ,</Kbd>       | Genel ayarlar                                  |
  | <Kbd>Cmd Shift P</Kbd> | Komut paleti                                   |
</div>

<div id="chat">
  ## Sohbet
</div>

Sohbet giriş kutusu için kısayollar.

<div className="full-width-table equal-table-columns">
  | Kısayol                                             | Eylem                          |
  | --------------------------------------------------- | ------------------------------ |
  | <Kbd>Return</Kbd>                                   | Hafif it (varsayılan)          |
  | <Kbd>Ctrl Return</Kbd>                              | Mesajı kuyruğa al              |
  | <Kbd>Cmd Return</Kbd> yazarken                      | Mesajı zorla gönder            |
  | <Kbd>Cmd Shift Backspace</Kbd>                      | Oluşturmayı iptal et           |
  | <Kbd>Cmd Shift L</Kbd> kod seçiliyken               | Seçili kodu bağlam olarak ekle |
  | <Kbd>Cmd V</Kbd> panoda kod veya log varken         | Panoyu bağlam olarak ekle      |
  | <Kbd>Cmd Shift V</Kbd> panoda kod veya log varken   | Panodakini giriş kutusuna ekle |
  | <Kbd>Cmd Return</Kbd> önerilen değişiklikler varken | Tüm değişiklikleri kabul et    |
  | <Kbd>Cmd Backspace</Kbd>                            | Tüm değişiklikleri reddet      |
  | <Kbd>Tab</Kbd>                                      | Sonraki mesaja geç             |
  | <Kbd>Shift Tab</Kbd>                                | Önceki mesaja geç              |
  | <Kbd>Cmd Opt /</Kbd>                                | Modeli değiştir                |
  | <Kbd>Cmd N</Kbd> / <Kbd>Cmd R</Kbd>                 | Yeni sohbet                    |
  | <Kbd>Cmd T</Kbd>                                    | Yeni sohbet sekmesi            |
  | <Kbd>Cmd \[</Kbd>                                   | Önceki sohbet                  |
  | <Kbd>Cmd ]</Kbd>                                    | Sonraki sohbet                 |
  | <Kbd>Cmd W</Kbd>                                    | Sohbeti kapat                  |
  | <Kbd>Escape</Kbd>                                   | Alanın odağını kaldır          |
</div>

<div id="inline-edit">
  ## Satır İçi Düzenleme
</div>

<div className="full-width-table equal-table-columns">
  | Kısayol                        | İşlem                   |
  | ------------------------------ | ----------------------- |
  | <Kbd>Cmd K</Kbd>               | Aç                      |
  | <Kbd>Cmd Shift K</Kbd>         | Odak arasında geçiş yap |
  | <Kbd>Return</Kbd>              | Gönder                  |
  | <Kbd>Cmd Shift Backspace</Kbd> | İptal et                |
  | <Kbd>Opt Return</Kbd>          | Hızlı soru sor          |
</div>

<div id="code-selection-context">
  ## Kod Seçimi ve Bağlam
</div>

<div className="full-width-table equal-table-columns">
  | Kısayol                                            | Eylem                                         |
  | -------------------------------------------------- | --------------------------------------------- |
  | <Kbd>@</Kbd>                                       | [@-sembolleri](/tr/context/@-symbols/)        |
  | <Kbd>#</Kbd>                                       | Dosyalar                                      |
  | <Kbd>/</Kbd>                                       | Kısayol komutları                             |
  | <Kbd>Cmd Shift L</Kbd>                             | Seçimi Sohbet’e ekle                          |
  | <Kbd>Cmd Shift K</Kbd>                             | Seçimi Düzenle’ye ekle                        |
  | <Kbd>Cmd L</Kbd>                                   | Seçimi yeni sohbete ekle                      |
  | <Kbd>Cmd M</Kbd>                                   | Dosya okuma stratejilerini aç/kapat           |
  | <Kbd>Cmd →</Kbd>                                   | Önerinin bir sonraki kelimesini kabul et      |
  | <Kbd>Cmd Return</Kbd>                              | Sohbette kod tabanında ara                    |
  | Kodu seç, <Kbd>Cmd C</Kbd>, <Kbd>Cmd V</Kbd>       | Kopyalanan referans kodunu bağlam olarak ekle |
  | Kodu seç, <Kbd>Cmd C</Kbd>, <Kbd>Cmd Shift V</Kbd> | Kopyalanan kodu metin bağlamı olarak ekle     |
</div>

<div id="tab">
  ## Tab
</div>

<div className="full-width-table equal-table-columns">
  | Kısayol          | İşlem                     |
  | ---------------- | ------------------------- |
  | <Kbd>Tab</Kbd>   | Öneriyi kabul et          |
  | <Kbd>Cmd →</Kbd> | Sonraki kelimeyi kabul et |
</div>

<div id="terminal">
  ## Terminal
</div>

<div className="full-width-table equal-table-columns">
  | Kısayol               | İşlem                             |
  | --------------------- | --------------------------------- |
  | <Kbd>Cmd K</Kbd>      | Terminal komut istemi çubuğunu aç |
  | <Kbd>Cmd Return</Kbd> | Üretilen komutu çalıştır          |
  | <Kbd>Escape</Kbd>     | Komutu onayla                     |
</div>

---

← Previous: [CLI’de Agent Kullanımı](./clide-agent-kullanm.md) | [Index](./index.md) | Next: [Shell Komutları](./shell-komutlar.md) →