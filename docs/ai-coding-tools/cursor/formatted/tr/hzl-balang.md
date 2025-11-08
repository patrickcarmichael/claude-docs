---
title: "Hızlı Başlangıç"
source: "https://docs.cursor.com/tr/get-started/quickstart"
language: "tr"
language_name: "Turkish"
---

# Hızlı Başlangıç
Source: https://docs.cursor.com/tr/get-started/quickstart

Cursor’la 5 dakikada başlayın

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

Bu hızlı başlangıç, Cursor’ın temel özelliklerini kullanan bir projeyi adım adım gösterecek. Sonunda Tab, Inline Edit ve Agent’a aşina olacaksın.

## Cursor'da bir proje aç

Mevcut bir projeyi kullan ya da örneğimizi klonla:

<Tabs>
  <Tab title="Örnek projeyi klonla">
    1. Git'in kurulu olduğundan emin ol
    2. Örnek projeyi klonla:

    ```bash  theme={null}
    git clone git@github.com:voxelize/voxelize.git && \
    cd voxelize && \
    cursor .
    ```
  </Tab>

  <Tab title="Mevcut projeyi kullan">
    1. Cursor'ı aç
    2. <Kbd>Cmd O</Kbd> ile ya da `cursor <path-to-project>` komutuyla bir proje klasörü aç
  </Tab>
</Tabs>

Örnek projeyi kullanarak göstereceğiz, ama yerelde sahip olduğun herhangi bir projeyi de kullanabilirsin.

<div id="autocomplete-with-tab">
  ## [Tab](/tr/kbd#tab) ile otomatik tamamlama
</div>

Tab, dahili olarak eğittiğimiz otomatik tamamlama modeli. Buna alışık değilsen AI destekli kodlamaya ısınmanın harika bir yolu. Tab ile şunları yapabilirsin:

* Kodun **birden çok satırını ve bloğunu** otomatik tamamla
* Sonraki otomatik tamamlama önerisine **dosya içinde** ve **dosyalar arasında** atla

1. Bir fonksiyonun başlangıcını yazmaya başla:
   ```javascript  theme={null}
   function calculate
   ```
2. Tab önerileri otomatik olarak görünür
3. Öneriyi kabul etmek için Tab tuşuna bas
4. Cursor parametreleri ve fonksiyon gövdelerini önerir

<div id="inline-edit-a-selection">
  ## [Inline Edit](/tr/inline-edit) ile bir seçimi düzenle
</div>

1. Az önce oluşturduğun fonksiyonu seç
2. <Kbd>Cmd K</Kbd> tuşlarına bas
3. "bu fonksiyon Fibonacci sayıları hesaplasın" yaz
4. Değişiklikleri uygulamak için <Kbd>Return</Kbd> tuşuna bas
5. Cursor gerekli importları ve dokümantasyonu ekler

<div id="chat-with-agent">
  ## [Agent](/tr/agent) ile sohbet et
</div>

1. Chat panelini aç (<Kbd>Cmd I</Kbd>)
2. Şunu sor: "Bu fonksiyon için testler ekle ve çalıştır"
3. Agent senin için bir test dosyası oluşturacak, test senaryoları yazacak ve onları çalıştıracak

<div id="bonus">
  ## Bonus
</div>

Gelişmiş özellikler:

<AccordionGroup>
  <Accordion title="Çalışmayı Background Agent’a devret">
    1. Background Agent kontrol panelini aç (<Kbd>Cmd E</Kbd>)
    2. Şunu sor: "Bu projede bir bug bul ve düzelt"
    3. [Background Agent](/tr/background-agent) şunları yapar:
       * Uzak bir Sanal Makine (VM) oluşturur
       * Projeni inceler
       * Hataları tespit eder
       * Düzeltmeler önerir

    Değişiklikleri gözden geçir ve uygula.
  </Accordion>

  {" "}

  <Accordion title="Kural yaz">
    1. Komut paletini aç (<Kbd>Cmd Shift P</Kbd>) 2. Şunu ara: "New Cursor
       Rule" 3. Ad ver (örn. `style-guide`) 4. Kural Türü olarak "Always" seç 5. Stilini
       tanımla: `Değişken adları için camelCase kullanmayı tercih et`
  </Accordion>

  <Accordion title="MCP sunucusu kur">
    1. [MCP dizinimizi](https://docs.cursor.com/tools) ziyaret et
    2. Bir araç seç
    3. "Install"a tıkla

    Sunucular manuel olarak da kurulabilir:

    1. Cursor Ayarlarını aç (<Kbd>Cmd Shift J</Kbd>)
    2. "Tools & Integrations" bölümüne git
    3. "New MCP Server"a tıkla
  </Accordion>
</AccordionGroup>

<div id="next-steps">
  ## Sonraki adımlar
</div>

Daha fazlasını öğrenmek için bu kılavuzlara göz at:

<CardGroup cols={2}>
  <Card title="Working with Context" href="/tr/guides/working-with-context">
    Daha iyi sonuçlar için etkili bağlam ver
  </Card>

  <Card title="Selecting Models" href="/tr/guides/selecting-models">
    Görevin için doğru modeli seç
  </Card>
</CardGroup>

Tüm [Cursor kavramlarını](/tr/get-started/concepts) öğren ve üretmeye başla!

---

← Previous: [Kurulum](./kurulum.md) | [Index](./index.md) | Next: [Veri Bilimi](./veri-bilimi.md) →