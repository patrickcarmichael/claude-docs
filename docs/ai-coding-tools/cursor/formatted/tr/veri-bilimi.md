---
title: "Veri Bilimi"
source: "https://docs.cursor.com/tr/guides/advanced/datascience"
language: "tr"
language_name: "Turkish"
---

# Veri Bilimi
Source: https://docs.cursor.com/tr/guides/advanced/datascience

Python, R ve SQL için defterler, uzak ortamlar ve yapay zekâ destekli analizle veri bilimi iş akışlarına uygun şekilde Cursor’ı nasıl kuracağını öğren

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

Cursor, tekrarlanabilir ortamlar, notebook desteği ve yapay zekâ destekli kod yardımıyla veri bilimi geliştirme için entegre araçlar sunar. Bu kılavuz, Python, R ve SQL iş akışları için temel kurulum örüntülerini kapsar.

<div id="notebook-development">
  ## Notebook geliştirme
</div>

<Note>
  Tam notebook desteği için, ms-toolsai tarafından yayımlanan Jupyter (id: ms-toolsai.jupyter) uzantısını indir.
</Note>

Cursor, entegre hücre çalıştırma ile hem `.ipynb` hem de `.py` dosyalarını destekler. Tab, Inline Edit ve Agent’lar,
diğer kod dosyalarında olduğu gibi notebook’larda da çalışır.

Temel yetenekler:

* **Satır içi hücre çalıştırma**, kodu doğrudan editör arayüzünde çalıştırır
* **Tab, Inline Edit ve Agent**; pandas, NumPy, scikit-learn ve SQL magic komutları dahil olmak üzere veri bilimi kütüphanelerini anlar

<div id="database-integration">
  ## Veritabanı entegrasyonu
</div>

Veritabanları, Cursor’a iki ana mekanizma üzerinden entegre edilebilir: MCP sunucuları ve uzantılar.

* **MCP Sunucuları**, agent’larının veritabanlarına bağlanmasını sağlar
* **Uzantılar**, IDE’ni veritabanlarınla entegre eder

<div id="via-mcp">
  ### MCP aracılığıyla
</div>

MCP sunucuları, agent’ının sorguları doğrudan veritabanına karşı çalıştırmasına izin verir. Bu sayede agent’ın, veritabanını sorgulamayı seçebilir, uygun sorguyu yazabilir, komutu çalıştırabilir ve çıktıları analiz edebilir; tüm bunları devam eden bir görevin parçası olarak yapar.

Örneğin, aşağıdaki [MCP config](https://github.com/modelcontextprotocol/servers-archived/tree/main/src/postgres)’i Cursor’a ekleyerek bir Postgres veritabanını Cursor kurulumuna bağlayabilirsin:

```json  theme={null}
{
  "mcpServers": {
    "postgres": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-postgres",
        "postgresql://localhost/mydb"
      ]
    }
  }
}
```

MCP hakkında daha fazlası için [MCP dokümantasyonumuza](/tr/tools/mcp) göz at.

<Frame>
  <video autoPlay loop muted playsInline controls width="100%">
    <source src="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/advanced/datascience/postgres-mcp.mp4?fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=334439f58b7d88b16d97134cf9c147aa" type="video/mp4" data-path="images/guides/advanced/datascience/postgres-mcp.mp4" />

    Tarayıcın video etiketini desteklemiyor.
  </video>
</Frame>

<div id="via-extensions">
  ### Uzantılarla
</div>

Sorguları doğrudan editörden çalıştırmak için veritabanına özel uzantıları (PostgreSQL, BigQuery, SQLite, Snowflake) yükle. Bu, araçlar arasında bağlam değiştirmeyi ortadan kaldırır ve sorgu optimizasyonu için yapay zekâ desteğini etkinleştirir.

```sql  theme={null}
-- Cursor, dizinler, pencere işlevleri ve sorgu optimizasyonu için öneriler sunar
SELECT
    user_id,
    event_type,
    COUNT(*) as event_count,
    RANK() OVER (PARTITION BY user_id ORDER BY COUNT(*) DESC) as frequency_rank
FROM events
WHERE created_at >= NOW() - INTERVAL '7 days'
GROUP BY user_id, event_type;
```

Yavaş sorguları analiz etmek, performans iyileştirmeleri önermek ya da sorgu sonuçları için görselleştirme kodu üretmek için Agents kullan. Cursor SQL bağlamını anlar ve veri yapına göre uygun grafik türlerini önerebilir.

<Frame>
  <img src="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/advanced/datascience/snowflake-extension.png?fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=7c14c60dc3c0523fb565c9462ac49029" alt="Snowflake Extension" data-og-width="2324" width="2324" data-og-height="1602" height="1602" data-path="images/guides/advanced/datascience/snowflake-extension.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/advanced/datascience/snowflake-extension.png?w=280&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=a8f316c0a5e756aed89423082dfa11d8 280w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/advanced/datascience/snowflake-extension.png?w=560&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=a8a66623964651cac9182159d880a511 560w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/advanced/datascience/snowflake-extension.png?w=840&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=2dc2566fa81d26a920d681178cb1d209 840w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/advanced/datascience/snowflake-extension.png?w=1100&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=52c3a74cea69f812e869c2bc25457462 1100w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/advanced/datascience/snowflake-extension.png?w=1650&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=d3322864e752c413fb3bfb2b686136f3 1650w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/advanced/datascience/snowflake-extension.png?w=2500&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=9ee01c8736f8eb78a04aab6340c4eaae 2500w" />
</Frame>

<div id="data-visualization">
  ## Veri görselleştirme
</div>

Cursor'ın yapay zeka desteği, Matplotlib, Plotly ve Seaborn gibi veri görselleştirme kütüphanelerini de kapsar. Aracı, veri görselleştirme için kod üretebilir; böylece verileri hızlı ve kolayca keşfetmene yardımcı olurken, yeniden üretilebilir ve paylaşılabilir bir çıktı oluşturur.

```python  theme={null}
import plotly.express as px
import pandas as pd

---

← Previous: [Hızlı Başlangıç](./hzl-balang.md) | [Index](./index.md) | Next: [Large Codebases](./large-codebases.md) →