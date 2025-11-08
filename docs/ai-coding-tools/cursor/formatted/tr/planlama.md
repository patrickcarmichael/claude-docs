---
title: "Planlama"
source: "https://docs.cursor.com/tr/agent/planning"
language: "tr"
language_name: "Turkish"
---

# Planlama
Source: https://docs.cursor.com/tr/agent/planning

Agent, yapılacak listeleri ve kuyruklama ile karmaşık görevleri nasıl planlar ve yönetir

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

Agent, yapılandırılmış yapılacak listeleri ve mesaj kuyruğa alma sayesinde önceden plan yapıp karmaşık görevleri yönetebilir; böylece uzun soluklu görevleri anlamak ve takip etmek kolaylaşır.

<div id="agent-to-dos">
  ## Agent yapılacaklar
</div>

Agent, daha uzun görevleri bağımlılıkları olan yönetilebilir adımlara ayırarak, iş ilerledikçe güncellenen yapılandırılmış bir plan oluşturur.

<video autoPlay loop muted playsInline controls>
  <source src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/agent/planning/agent-todo.mp4?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=b0285913832a3ef123fe149516ee37ea" type="video/mp4" data-path="images/agent/planning/agent-todo.mp4" />
</video>

<div id="how-it-works">
  ### Nasıl çalışır
</div>

* Agent karmaşık görevler için otomatik olarak yapılacaklar listeleri oluşturur
* Her öğe diğer görevlere bağımlılıklar içerebilir
* Liste, iş ilerledikçe gerçek zamanlı olarak güncellenir
* Tamamlanan görevler otomatik olarak işaretlenir

<div id="visibility">
  ### Görünürlük
</div>

* Yapılacaklar sohbet arayüzünde görünür
* [Slack entegrasyonu](/tr/slack) kuruluysa, yapılacaklar orada da görünür
* İstediğin zaman tam görev dökümünü görebilirsin

<Tip>
  Daha iyi planlama için nihai hedefini net şekilde anlat. Agent, kapsamın tamamını
  anladığında daha doğru görev dökümleri oluşturur.
</Tip>

<Note>Planlama ve yapılacaklar şu anda otomatik mod için desteklenmiyor.</Note>

<div id="queued-messages">
  ## Kuyruğa alınan mesajlar
</div>

Agent mevcut görev üzerinde çalışırken takip mesajlarını kuyruğa al. Talimatların sırada bekler ve hazır olduğunda otomatik olarak yürütülür.

<video autoPlay loop muted playsInline controls>
  <source src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/agent/planning/agent-queue.mp4?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=4cdd6a7d1e12c67e520bc3ba67a42e0d" type="video/mp4" data-path="images/agent/planning/agent-queue.mp4" />
</video>

<div id="using-the-queue">
  ### Kuyruğu kullanma
</div>

1. Agent çalışırken bir sonraki talimatını yaz
2. Kuyruğa eklemek için <Kbd>Ctrl+Enter</Kbd> tuşuna bas
3. Mesajlar, etkin görevin altında sırayla görünür
4. Ok simgesine tıklayarak kuyruğa alınan mesajların sırasını değiştir
5. Agent, bitirdikten sonra onları sırayla işler

<div id="override-the-queue">
  ### Kuyruğu geçersiz kılma
</div>

Varsayılan mesajlaşma yerine mesajını kuyruğa almak için <Kbd>Ctrl+Enter</Kbd> kullan. Kuyruğa almadan mesajı anında göndermek için <Kbd>Cmd+Enter</Kbd> kullan. Bu, mesajını “zorla gönderir” ve kuyruğu atlayarak hemen çalıştırır.

<div id="default-messaging">
  ## Varsayılan mesajlaşma
</div>

Mesajlar varsayılan olarak mümkün olduğunca hızlı gönderilir; genellikle Agent bir araç çağrısını tamamlar tamamlamaz görünür. Bu, en hızlı tepki veren deneyimi sağlar.

<div id="how-default-messaging-works">
  ### Varsayılan mesajlaşma nasıl çalışır
</div>

* Mesajın, sohbetteki en son kullanıcı mesajına eklenir
* Mesajlar genellikle araç sonuçlarına iliştirilir ve hazır olur olmaz gönderilir
* Bu, Agent’ın mevcut işini bölmeden daha doğal bir sohbet akışı sağlar
* Varsayılan olarak, Agent çalışırken Enter’a bastığında bu gerçekleşir

---

← Previous: [Genel Bakış](./genel-bak.md) | [Index](./index.md) | Next: [Diff’ler & İnceleme](./diffler-inceleme.md) →