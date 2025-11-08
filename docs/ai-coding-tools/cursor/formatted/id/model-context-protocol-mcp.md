---
title: "Model Context Protocol (MCP)"
source: "https://docs.cursor.com/id/context/mcp"
language: "id"
language_name: "Indonesian"
---

# Model Context Protocol (MCP)
Source: https://docs.cursor.com/id/context/mcp

Hubungkan alat eksternal dan sumber data ke Cursor menggunakan MCP

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

<div id="what-is-mcp">
  ## Apa itu MCP?
</div>

[Model Context Protocol (MCP)](https://modelcontextprotocol.io/introduction) memungkinkan Cursor terhubung ke alat eksternal dan sumber data.

<Frame>
  <video src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/mcp/simple-mcp-call.mp4?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=08c642babc501c939ecbec9ef5124ce7" autoPlay loop muted playsInline controls data-path="images/context/mcp/simple-mcp-call.mp4" />
</Frame>

<div id="why-use-mcp">
  ### Kenapa pakai MCP?
</div>

MCP menghubungkan Cursor ke sistem dan data eksternal. Daripada ngejelasin struktur proyek berulang kali, integrasiin langsung sama tool yang dipakai.

Tulis server MCP pakai bahasa apa pun yang bisa nge-print ke `stdout` atau nyediain endpoint HTTP — Python, JavaScript, Go, dll.

<div id="how-it-works">
  ### Cara kerjanya
</div>

Server MCP mengekspos kemampuan melalui protokol, menghubungkan Cursor ke alat atau sumber data eksternal.

Cursor mendukung tiga metode transport:

<div className="full-width-table">
  | Transport                                                        | Lingkungan eksekusi | Deployment              | Pengguna        | Input                | Auth   |
  | :--------------------------------------------------------------- | :------------------ | :---------------------- | :-------------- | :------------------- | :----- |
  | **<span className="whitespace-nowrap">`stdio`</span>**           | Lokal               | Dikelola oleh Cursor    | Satu pengguna   | Perintah shell       | Manual |
  | **<span className="whitespace-nowrap">`SSE`</span>**             | Lokal/Jarak jauh    | Dideploy sebagai server | Banyak pengguna | URL ke endpoint SSE  | OAuth  |
  | **<span className="whitespace-nowrap">`Streamable HTTP`</span>** | Lokal/Jarak jauh    | Dideploy sebagai server | Banyak pengguna | URL ke endpoint HTTP | OAuth  |
</div>

<div id="protocol-support">
  ### Dukungan protokol
</div>

Cursor mendukung kapabilitas protokol MCP berikut:

<div className="full-width-table">
  | Fitur           | Dukungan | Deskripsi                                                                              |
  | :-------------- | :------- | :------------------------------------------------------------------------------------- |
  | **Tools**       | Didukung | Fungsi yang dieksekusi oleh model AI                                                   |
  | **Prompts**     | Didukung | Pesan dan alur kerja bertemplate untuk pengguna                                        |
  | **Resources**   | Didukung | Sumber data terstruktur yang dapat dibaca dan dirujuk                                  |
  | **Roots**       | Didukung | Kueri yang diprakarsai server ke batas URI atau sistem berkas tempat operasi dilakukan |
  | **Elicitation** | Didukung | Permintaan yang diprakarsai server untuk informasi tambahan dari pengguna              |
</div>

<div id="installing-mcp-servers">
  ## Menginstal server MCP
</div>

<div id="one-click-installation">
  ### Instal sekali klik
</div>

Instal server MCP dari koleksi kami dan lakukan autentikasi dengan OAuth.

<Columns cols={2}>
  <Card title="Browse MCP Tools" icon="table" horizontal href="/id/tools">
    Jelajahi server MCP yang tersedia
  </Card>

  <Card title="Add to Cursor Button" icon="plus" horizontal href="/id/deeplinks">
    Bikin tombol "Add to Cursor"
  </Card>
</Columns>

<div id="using-mcpjson">
  ### Menggunakan `mcp.json`
</div>

Konfigurasikan server MCP kustom dengan file JSON:

<CodeGroup>
  ```json CLI Server - Node.js theme={null}
  {
    "mcpServers": {
      "server-name": {
        "command": "npx",
        "args": ["-y", "mcp-server"],
        "env": {
          "API_KEY": "value"
        }
      }
    }
  }
  ```

  ```json CLI Server - Python theme={null}
  {
    "mcpServers": {
      "server-name": {
        "command": "python",
        "args": ["mcp-server.py"],
        "env": {
          "API_KEY": "value"
        }
      }
    }
  }
  ```

  ```json Remote Server theme={null}
  // Server MCP menggunakan HTTP atau SSE - berjalan di server
  {
    "mcpServers": {
      "server-name": {
        "url": "http://localhost:3000/mcp",
        "headers": {
          "API_KEY": "value"
        }
      }
    }
  }
  ```
</CodeGroup>

<div id="stdio-server-configuration">
  ### Konfigurasi server STDIO
</div>

Untuk server STDIO (server command line lokal), atur field berikut di `mcp.json`:

<div className="full-width-table">
  | Field       | Wajib | Deskripsi                                                                                     | Contoh                                    |
  | :---------- | :---- | :-------------------------------------------------------------------------------------------- | :---------------------------------------- |
  | **type**    | Ya    | Jenis koneksi server                                                                          | `"stdio"`                                 |
  | **command** | Ya    | Perintah untuk menjalankan executable server. Harus ada di system path atau pakai path penuh. | `"npx"`, `"node"`, `"python"`, `"docker"` |
  | **args**    | Nggak | Array argumen yang dikirim ke perintah                                                        | `["server.py", "--port", "3000"]`         |
  | **env**     | Nggak | Variabel environment untuk server                                                             | `{"API_KEY": "${input:api-key}"}`         |
  | **envFile** | Nggak | Path ke file environment untuk memuat lebih banyak variabel                                   | `".env"`, `"${workspaceFolder}/.env"`     |
</div>

<div id="using-the-extension-api">
  ### Menggunakan Extension API
</div>

Buat pendaftaran server MCP secara terprogram, Cursor nyediain Extension API yang memungkinkan konfigurasi dinamis tanpa perlu ngubah file `mcp.json`. Ini khususnya berguna buat lingkungan enterprise dan workflow setup otomatis.

<Card title="Referensi MCP Extension API" icon="code" href="/id/context/mcp-extension-api">
  Pelajari cara nge-register server MCP secara terprogram pakai `vscode.cursor.mcp.registerServer()`
</Card>

<div id="configuration-locations">
  ### Lokasi konfigurasi
</div>

<CardGroup cols={2}>
  <Card title="Konfigurasi Proyek" icon="folder-tree">
    Bikin `.cursor/mcp.json` di proyek lo buat alat yang khusus proyek.
  </Card>

  <Card title="Konfigurasi Global" icon="globe">
    Bikin `~/.cursor/mcp.json` di direktori home lo buat alat yang tersedia di mana-mana.
  </Card>
</CardGroup>

<div id="config-interpolation">
  ### Interpolasi konfigurasi
</div>

Gunakan variabel dalam nilai `mcp.json`. Cursor me-resolve variabel di bidang berikut: `command`, `args`, `env`, `url`, dan `headers`.

Sintaks yang didukung:

* `${env:NAME}` variabel environment
* `${userHome}` jalur ke folder home kamu
* `${workspaceFolder}` root proyek (folder yang berisi `.cursor/mcp.json`)
* `${workspaceFolderBasename}` nama root proyek
* `${pathSeparator}` dan `${/}` pemisah jalur OS

Contoh

```json  theme={null}
{
  "mcpServers": {
    "local-server": {
      "command": "python",
      "args": ["${workspaceFolder}/tools/mcp_server.py"],
      "env": {
        "API_KEY": "${env:API_KEY}"
      }
    }
  }
}
```

```json  theme={null}
{
  "mcpServers": {
    "remote-server": {
      "url": "https://api.example.com/mcp",
      "headers": {
        "Authorization": "Bearer ${env:MY_SERVICE_TOKEN}"
      }
    }
  }
}
```

<div id="authentication">
  ### Autentikasi
</div>

Server MCP menggunakan variabel lingkungan untuk autentikasi. Lewatkan kunci API dan token lewat konfigurasi.

Cursor mendukung OAuth untuk server yang memerlukannya.

<div id="using-mcp-in-chat">
  ## Menggunakan MCP di chat
</div>

Composer Agent otomatis pakai tool MCP yang tercantum di `Available Tools` saat relevan. Minta tool tertentu berdasarkan nama atau jelasin apa yang lo butuhin. Aktifin atau nonaktifin tool dari Settings.

<div id="toggling-tools">
  ### Mengaktifkan/nonaktifkan tool
</div>

Aktifkan atau nonaktifkan tool MCP langsung dari antarmuka chat. Klik nama tool di daftar tool untuk menyalakan atau mematikannya. Tool yang dinonaktifkan nggak akan dimuat ke konteks atau tersedia buat Agent.

<Frame>
  <video src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/mcp/tool-toggle.mp4?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=0fa3060f593cae3e5fb7c7d2f041a715" autoPlay loop muted playsInline controls data-path="images/context/mcp/tool-toggle.mp4" />
</Frame>

<div id="tool-approval">
  ### Persetujuan tool
</div>

Secara default, Agent bakal minta persetujuan sebelum pakai tool MCP. Klik panah di sebelah nama tool buat lihat argumen.

<Frame><img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/mcp/tool-confirm.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=bf9b19d5f23abc65914f712185b3ec72" alt="" data-og-width="1212" width="1212" data-og-height="902" height="902" data-path="images/context/mcp/tool-confirm.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/mcp/tool-confirm.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=e3f900fad0b8f2a469460c70fa1dd1dc 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/mcp/tool-confirm.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=de2f90138de39d75d70c5800f13be93a 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/mcp/tool-confirm.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=b9c616ce7a4080ea4088a0fdd0050c7c 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/mcp/tool-confirm.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=3f783e62a7a31957b8988edb97c139f9 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/mcp/tool-confirm.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=10bf2c1dbfd5c2a03aa95334f53cd571 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/mcp/tool-confirm.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=231c0e3cd60df5ad12455d5e8ef308d2 2500w" /></Frame>

<div id="auto-run">
  #### Auto-run
</div>

Aktifkan auto-run biar Agent bisa pakai tool MCP tanpa perlu konfirmasi. Cara kerjanya mirip perintah terminal. Baca selengkapnya tentang pengaturan Auto-run [di sini](/id/agent/tools#auto-run).

<div id="tool-response">
  ### Respons tool
</div>

Cursor menampilkan respons di chat dengan tampilan argumen dan respons yang bisa diperluas:

<Frame><img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/mcp/tool-call.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=30af3f35869e9a78781f455bdbc0e3b5" alt="" data-og-width="1212" width="1212" data-og-height="952" height="952" data-path="images/context/mcp/tool-call.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/mcp/tool-call.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=8821ac7bad00ad54a18abc614c2e3d5c 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/mcp/tool-call.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=d9d55f089ad53a89da99b8ddd524f6de 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/mcp/tool-call.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=a107d68a1fb05ed43851548b34fb4496 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/mcp/tool-call.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=b409b4941c2fd783043770fad0bd6390 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/mcp/tool-call.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=2a331b5e2bb9be0b9659393157454c2e 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/mcp/tool-call.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=585b769dfa2a5114b111eb901a969845 2500w" /></Frame>

<div id="images-as-context">
  ### Gambar sebagai konteks
</div>

Server MCP bisa mengembalikan gambar—screenshot, diagram, dan sebagainya. Kembalikan gambar sebagai string yang dienkode base64:

```js  theme={null}
const RED_CIRCLE_BASE64 = "/9j/4AAQSkZJRgABAgEASABIAAD/2w...";
// ^ seluruh base64 dipangkas untuk keterbacaan

server.tool("generate_image", async (params) => {
  return {
    content: [
      {
        type: "image",
        data: RED_CIRCLE_BASE64,
        mimeType: "image/jpeg",
      },
    ],
  };
});
```

Lihat [server contoh](https://github.com/msfeldstein/mcp-test-servers/blob/main/src/image-server.js) ini untuk detail implementasi. Cursor menautkan gambar yang dikembalikan ke obrolan. Kalau model mendukung gambar, model bakal menganalisisnya.

<div id="security-considerations">
  ## Pertimbangan keamanan
</div>

Saat menginstal server MCP, pertimbangkan praktik keamanan berikut:

* **Verifikasi sumber**: Hanya pasang server MCP dari pengembang dan repositori tepercaya
* **Tinjau perizinan**: Periksa data dan API apa yang akan diakses server
* **Batasi kunci API**: Gunakan kunci API dengan batasan dan izin minimum yang dibutuhkan
* **Audit kode**: Untuk integrasi yang krusial, tinjau kode sumber server

Ingat, server MCP bisa mengakses layanan eksternal dan mengeksekusi kode atas namamu. Selalu pahami apa yang dilakukan server sebelum menginstalnya.

<div id="real-world-examples">
  ## Contoh dunia nyata
</div>

Untuk contoh praktis MCP yang benar-benar digunakan, lihat [panduan Web Development](/id/guides/tutorials/web-development) yang menunjukkan cara mengintegrasikan Linear, Figma, dan alat peramban ke dalam workflow pengembangan lo.

<div id="faq">
  ## FAQ
</div>

<AccordionGroup>
  <Accordion title="Apa gunanya server MCP?">
    Server MCP menghubungkan Cursor ke tool eksternal seperti Google Drive, Notion,
    dan layanan lain untuk memasukkan dokumen dan requirement ke alur kerja pengkodean Anda.
  </Accordion>

  {" "}

  <Accordion title="Gimana cara debug masalah server MCP?">
    Lihat log MCP dengan: 1. Buka panel Output di Cursor (<Kbd>Cmd+Shift+U</Kbd>) 2.
    Pilih "MCP Logs" dari dropdown 3. Cek error koneksi, masalah autentikasi, atau server
    crash. Log menampilkan inisialisasi server, pemanggilan tool, dan pesan error.
  </Accordion>

  {" "}

  <Accordion title="Bisa nggak gue nonaktifin server MCP sementara?">
    Bisa! Toggle server on/off tanpa menghapusnya: 1. Buka Settings (<Kbd>Cmd+Shift+J</Kbd>) 2.
    Masuk ke Features → Model Context Protocol 3. Klik toggle di samping server mana pun untuk
    mengaktifkan/menonaktifkan. Server yang dinonaktifkan tidak akan dimuat atau muncul di chat.
    Ini berguna untuk troubleshooting atau mengurangi clutter tool.
  </Accordion>

  {" "}

  <Accordion title="Apa yang terjadi kalau server MCP crash atau timeout?">
    Jika server MCP gagal: Cursor menampilkan pesan error di chat. Pemanggilan tool ditandai gagal.
    Anda bisa mencoba ulang operasi atau memeriksa log untuk detailnya. Server MCP lain tetap bekerja normal.
    Cursor mengisolasi kegagalan server agar satu server tidak memengaruhi yang lain.
  </Accordion>

  {" "}

  <Accordion title="Gimana cara update server MCP?">
    Untuk server berbasis npm: 1. Hapus server dari settings 2. Bersihkan cache npm:
    `npm cache clean --force` 3. Tambahkan kembali server untuk mendapatkan versi terbaru. Untuk server kustom,
    perbarui file lokal Anda dan restart Cursor.
  </Accordion>

  <Accordion title="Bisa nggak pakai server MCP dengan data sensitif?">
    Bisa, tapi ikuti praktik keamanan terbaik: gunakan environment variables untuk
    secret dan jangan pernah hardcode; jalankan server sensitif secara lokal dengan transport `stdio`;
    batasi izin API key seminimal mungkin; tinjau kode server sebelum menyambungkan ke sistem sensitif;
    pertimbangkan menjalankan server di lingkungan terisolasi.
  </Accordion>
</AccordionGroup>

---

← Previous: [Mengabaikan file](./mengabaikan-file.md) | [Index](./index.md) | Next: [Memories](./memories.md) →