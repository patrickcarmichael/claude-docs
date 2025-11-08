---
title: "Data Science"
source: "https://docs.cursor.com/id/guides/advanced/datascience"
language: "id"
language_name: "Indonesian"
---

# Data Science
Source: https://docs.cursor.com/id/guides/advanced/datascience

Pelajari cara menyiapkan Cursor untuk workflow data science mencakup Python, R, dan SQL dengan notebook, environment remote, dan analisis bertenaga AI

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

Cursor menyediakan alat terintegrasi untuk pengembangan data science melalui lingkungan yang dapat direplikasi, dukungan notebook, dan bantuan kode berbasis AI. Panduan ini membahas pola penyiapan penting untuk alur kerja Python, R, dan SQL.

<div id="notebook-development">
  ## Pengembangan notebook
</div>

<Note>
  Untuk dukungan notebook lengkap, unduh ekstensi Jupyter (id: ms-toolsai.jupyter) yang dipublikasikan oleh ms-toolsai.
</Note>

Cursor mendukung file `.ipynb` dan `.py` dengan eksekusi sel terintegrasi. Tab, Inline Edit, dan Agent
berfungsi di dalam notebook, sama seperti di file kode lainnya.

Kemampuan utama:

* **Eksekusi sel inline** menjalankan kode langsung di dalam antarmuka editor
* **Tab, Inline Edit, dan Agent** semuanya memahami pustaka data science termasuk pandas, NumPy, scikit-learn, dan perintah SQL magic

<div id="database-integration">
  ## Integrasi database
</div>

Database bisa diintegrasikan dengan Cursor lewat dua mekanisme utama: server MCP dan ekstensi.

* **Server MCP** bikin agent lo bisa terhubung ke database lo
* **Ekstensi** ngintegrasiin IDE lo secara lebih luas dengan database lo

<div id="via-mcp">
  ### Lewat MCP
</div>

Server MCP memungkinkan agent lo buat ngejalanin kueri langsung ke database lo. Ini bikin agent lo bisa milih buat ngekueri database lo, nulis kueri yang sesuai, ngejalanin perintah, dan nganalisis output, semuanya sebagai bagian dari task yang lagi berjalan.

Misalnya, lo bisa nyambungin database Postgres ke instance Cursor lo dengan nambahin [konfigurasi MCP](https://github.com/modelcontextprotocol/servers-archived/tree/main/src/postgres) berikut ke Cursor:

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

Untuk info lebih lanjut tentang MCP, lihat [dokumentasi MCP](/id/tools/mcp) kami.

<Frame>
  <video autoPlay loop muted playsInline controls width="100%">
    <source src="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/advanced/datascience/postgres-mcp.mp4?fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=334439f58b7d88b16d97134cf9c147aa" type="video/mp4" data-path="images/guides/advanced/datascience/postgres-mcp.mp4" />

    Browser lo nggak mendukung tag video.
  </video>
</Frame>

<div id="via-extensions">
  ### Via Extensions
</div>

Install ekstensi khusus database (PostgreSQL, BigQuery, SQLite, Snowflake) buat ngejalanin query langsung dari editor. Ini ngilangin context switching antar alat dan bikin AI bisa bantu ngeoptimalin query.

```sql  theme={null}
-- Cursor ngasih saran buat indeks, window function, dan optimasi kueri
SELECT
    user_id,
    event_type,
    COUNT(*) as jumlah_event,
    RANK() OVER (PARTITION BY user_id ORDER BY COUNT(*) DESC) as peringkat_frekuensi
FROM events
WHERE created_at >= NOW() - INTERVAL '7 hari'
GROUP BY user_id, event_type;
```

Gunakan Agents untuk menganalisis query yang lambat, ngasih saran peningkatan performa, atau ngehasilin kode visualisasi buat hasil query. Cursor paham konteks SQL dan bisa ngerekomendasiin tipe chart yang pas berdasarkan struktur data lo.

<Frame>
  <img src="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/advanced/datascience/snowflake-extension.png?fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=7c14c60dc3c0523fb565c9462ac49029" alt="Snowflake Extension" data-og-width="2324" width="2324" data-og-height="1602" height="1602" data-path="images/guides/advanced/datascience/snowflake-extension.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/advanced/datascience/snowflake-extension.png?w=280&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=a8f316c0a5e756aed89423082dfa11d8 280w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/advanced/datascience/snowflake-extension.png?w=560&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=a8a66623964651cac9182159d880a511 560w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/advanced/datascience/snowflake-extension.png?w=840&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=2dc2566fa81d26a920d681178cb1d209 840w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/advanced/datascience/snowflake-extension.png?w=1100&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=52c3a74cea69f812e869c2bc25457462 1100w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/advanced/datascience/snowflake-extension.png?w=1650&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=d3322864e752c413fb3bfb2b686136f3 1650w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/advanced/datascience/snowflake-extension.png?w=2500&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=9ee01c8736f8eb78a04aab6340c4eaae 2500w" />
</Frame>

<div id="data-visualization">
  ## Visualisasi data
</div>

Bantuan AI dari Cursor mencakup pustaka visualisasi data seperti Matplotlib, Plotly, dan Seaborn. Agen bisa ngasilin kode buat visualisasi data, bantu lo eksplor data dengan cepat dan mudah, sambil bikin artefak yang bisa direplikasi dan dibagikan.

```python  theme={null}
import plotly.express as px
import pandas as pd

---

← Previous: [Quickstart](./quickstart.md) | [Index](./index.md) | Next: [Basis Kode Skala Besar](./basis-kode-skala-besar.md) →