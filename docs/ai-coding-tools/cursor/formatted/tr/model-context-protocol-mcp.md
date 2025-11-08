---
title: "Model Context Protocol (MCP)"
source: "https://docs.cursor.com/tr/context/mcp"
language: "tr"
language_name: "Turkish"
---

# Model Context Protocol (MCP)
Source: https://docs.cursor.com/tr/context/mcp

MCP ile harici araçları ve veri kaynaklarını Cursor’a bağla

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
  ## MCP nedir?
</div>

[Model Context Protocol (MCP)](https://modelcontextprotocol.io/introduction), Cursor’ın dış araçlara ve veri kaynaklarına bağlanmasına olanak tanır.

<Frame>
  <video src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/mcp/simple-mcp-call.mp4?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=08c642babc501c939ecbec9ef5124ce7" autoPlay loop muted playsInline controls data-path="images/context/mcp/simple-mcp-call.mp4" />
</Frame>

<div id="why-use-mcp">
  ### Neden MCP kullanmalı?
</div>

MCP, Cursor’ı harici sistemlere ve verilere bağlar. Proje yapını tekrar tekrar açıklamak yerine, doğrudan araçlarınla entegre ol.

`stdout`’a yazdırabilen ya da bir HTTP endpoint’i sunabilen herhangi bir dille MCP sunucuları yaz — Python, JavaScript, Go vb.

<div id="how-it-works">
  ### Nasıl çalışır
</div>

MCP sunucuları, protokol üzerinden yeteneklerini sunarak Cursor’ı harici araçlara veya veri kaynaklarına bağlar.

Cursor üç aktarım yöntemini destekler:

<div className="full-width-table">
  | Aktarım                                                          | Çalışma ortamı | Dağıtım             | Kullanıcılar         | Girdi                     | Kimlik doğrulama |
  | :--------------------------------------------------------------- | :------------- | :------------------ | :------------------- | :------------------------ | :--------------- |
  | **<span className="whitespace-nowrap">`stdio`</span>**           | Yerel          | Cursor yönetir      | Tek kullanıcı        | Kabuk komutu              | Manuel           |
  | **<span className="whitespace-nowrap">`SSE`</span>**             | Yerel/Uzak     | Sunucu olarak dağıt | Birden çok kullanıcı | Bir SSE uç noktasına URL  | OAuth            |
  | **<span className="whitespace-nowrap">`Streamable HTTP`</span>** | Yerel/Uzak     | Sunucu olarak dağıt | Birden çok kullanıcı | Bir HTTP uç noktasına URL | OAuth            |
</div>

<div id="protocol-support">
  ### Protokol desteği
</div>

Cursor, şu MCP protokol yeteneklerini destekler:

<div className="full-width-table">
  | Özellik         | Destek        | Açıklama                                                                                            |
  | :-------------- | :------------ | :-------------------------------------------------------------------------------------------------- |
  | **Tools**       | Destekleniyor | Yapay zeka modelinin çalıştıracağı işlevler                                                         |
  | **Prompts**     | Destekleniyor | Kullanıcılar için şablon mesajlar ve iş akışları                                                    |
  | **Resources**   | Destekleniyor | Okunup referans verilebilen yapılandırılmış veri kaynakları                                         |
  | **Roots**       | Destekleniyor | Çalışma alanını belirlemek için sunucu tarafından başlatılan URI veya dosya sistemi sınır sorguları |
  | **Elicitation** | Destekleniyor | Kullanıcılardan ek bilgi almak için sunucu tarafından başlatılan talepler                           |
</div>

<div id="installing-mcp-servers">
  ## MCP sunucularını yükleme
</div>

<div id="one-click-installation">
  ### Tek tıkla kurulum
</div>

Koleksiyonumuzdan MCP sunucularını yükle ve OAuth ile oturum açıp doğrula.

<Columns cols={2}>
  <Card title="MCP Araçlarına Göz At" icon="table" horizontal href="/tr/tools">
    Kullanılabilir MCP sunucularına göz at
  </Card>

  <Card title="Cursor’a Ekle Butonu" icon="plus" horizontal href="/tr/deeplinks">
    “Cursor’a Ekle” butonu oluştur
  </Card>
</Columns>

<div id="using-mcpjson">
  ### `mcp.json` kullanımı
</div>

Özel MCP sunucularını bir JSON dosyasıyla yapılandır:

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
  // HTTP veya SSE kullanan MCP sunucusu — bir sunucuda çalışır
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
  ### STDIO sunucu yapılandırması
</div>

STDIO sunucuları (yerel komut satırı sunucuları) için `mcp.json` dosyanda şu alanları yapılandır:

<div className="full-width-table">
  | Field       | Required | Description                                                                                     | Examples                                  |
  | :---------- | :------- | :---------------------------------------------------------------------------------------------- | :---------------------------------------- |
  | **type**    | Evet     | Sunucu bağlantı türü                                                                            | `"stdio"`                                 |
  | **command** | Evet     | Sunucu çalıştırılabilirini başlatacak komut. Sistem PATH’inde bulunmalı ya da tam yol içermeli. | `"npx"`, `"node"`, `"python"`, `"docker"` |
  | **args**    | Hayır    | Komuta iletilecek argümanlar dizisi                                                             | `["server.py", "--port", "3000"]`         |
  | **env**     | Hayır    | Sunucu için ortam değişkenleri                                                                  | `{"API_KEY": "${input:api-key}"}`         |
  | **envFile** | Hayır    | Ek değişkenleri yüklemek için ortam dosyasının yolu                                             | `".env"`, `"${workspaceFolder}/.env"`     |
</div>

### Extension API'yi kullanma

Programatik MCP sunucusu kaydı için Cursor, `mcp.json` dosyalarını değiştirmeden dinamik yapılandırmaya olanak tanıyan bir Extension API sunar. Bu, özellikle kurumsal ortamlar ve otomatik kurulum iş akışları için kullanışlıdır.

<Card title="MCP Extension API Referansı" icon="code" href="/tr/context/mcp-extension-api">
  `vscode.cursor.mcp.registerServer()` kullanarak MCP sunucularını programatik olarak nasıl kaydedebileceğini öğren
</Card>

<div id="configuration-locations">
  ### Yapılandırma konumları
</div>

<CardGroup cols={2}>
  <Card title="Proje Yapılandırması" icon="folder-tree">
    Projene özel araçlar için projende `.cursor/mcp.json` oluştur.
  </Card>

  <Card title="Genel Yapılandırma" icon="globe">
    Her yerden kullanılabilen araçlar için ana dizininde `~/.cursor/mcp.json` oluştur.
  </Card>
</CardGroup>

<div id="config-interpolation">
  ### Yapılandırma interpolasyonu
</div>

`mcp.json` değerlerinde değişken kullan. Cursor şu alanlardaki değişkenleri çözümler: `command`, `args`, `env`, `url` ve `headers`.

Desteklenen sözdizimi:

* `${env:NAME}` ortam değişkenleri
* `${userHome}` ana klasörünün yolu
* `${workspaceFolder}` proje kökü (`.cursor/mcp.json` dosyasını içeren klasör)
* `${workspaceFolderBasename}` proje kökünün adı
* `${pathSeparator}` ve `${/}` işletim sistemi yol ayırıcıları

Örnekler

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
  ### Kimlik doğrulama
</div>

MCP sunucuları kimlik doğrulama için ortam değişkenlerini kullanır. API anahtarlarını ve access token’ları config üzerinden ilet.

Cursor, bunu gerektiren sunucular için OAuth’u destekler.

<div id="using-mcp-in-chat">
  ## Sohbette MCP kullanma
</div>

Composer Agent, uygun olduğunda `Available Tools` altında listelenen MCP araçlarını otomatik olarak kullanır. Belirli bir aracı adıyla iste ya da neye ihtiyacın olduğunu anlat. Araçları ayarlardan etkinleştirip devre dışı bırakabilirsin.

<div id="toggling-tools">
  ### Araçları açma/kapama
</div>

MCP araçlarını doğrudan sohbet arayüzünden etkinleştir veya devre dışı bırak. Araçlar listesindeki araç adına tıklayarak açıp kapatabilirsin. Devre dışı bırakılan araçlar bağlama yüklenmez ve Agent tarafından kullanılamaz.

<Frame>
  <video src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/mcp/tool-toggle.mp4?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=0fa3060f593cae3e5fb7c7d2f041a715" autoPlay loop muted playsInline controls data-path="images/context/mcp/tool-toggle.mp4" />
</Frame>

<div id="tool-approval">
  ### Araç onayı
</div>

Agent, varsayılan olarak MCP araçlarını kullanmadan önce onay ister. Argümanları görmek için araç adının yanındaki oka tıkla.

<Frame><img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/mcp/tool-confirm.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=bf9b19d5f23abc65914f712185b3ec72" alt="" data-og-width="1212" width="1212" data-og-height="902" height="902" data-path="images/context/mcp/tool-confirm.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/mcp/tool-confirm.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=e3f900fad0b8f2a469460c70fa1dd1dc 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/mcp/tool-confirm.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=de2f90138de39d75d70c5800f13be93a 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/mcp/tool-confirm.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=b9c616ce7a4080ea4088a0fdd0050c7c 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/mcp/tool-confirm.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=3f783e62a7a31957b8988edb97c139f9 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/mcp/tool-confirm.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=10bf2c1dbfd5c2a03aa95334f53cd571 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/mcp/tool-confirm.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=231c0e3cd60df5ad12455d5e8ef308d2 2500w" /></Frame>

<div id="auto-run">
  #### Otomatik çalıştırma
</div>

Agent’in MCP araçlarını senden onay istemeden kullanabilmesi için otomatik çalıştırmayı etkinleştir. Terminal komutları gibi çalışır. Otomatik çalıştırma ayarları hakkında daha fazla bilgiyi [buradan](/tr/agent/tools#auto-run) edinebilirsin.

<div id="tool-response">
  ### Araç yanıtı
</div>

Cursor, sohbette argümanlar ve yanıtların açılabilir görünümleriyle yanıtı gösterir:

<Frame><img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/mcp/tool-call.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=30af3f35869e9a78781f455bdbc0e3b5" alt="" data-og-width="1212" width="1212" data-og-height="952" height="952" data-path="images/context/mcp/tool-call.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/mcp/tool-call.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=8821ac7bad00ad54a18abc614c2e3d5c 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/mcp/tool-call.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=d9d55f089ad53a89da99b8ddd524f6de 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/mcp/tool-call.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=a107d68a1fb05ed43851548b34fb4496 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/mcp/tool-call.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=b409b4941c2fd783043770fad0bd6390 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/mcp/tool-call.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=2a331b5e2bb9be0b9659393157454c2e 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/mcp/tool-call.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=585b769dfa2a5114b111eb901a969845 2500w" /></Frame>

<div id="images-as-context">
  ### Bağlam olarak görseller
</div>

MCP sunucuları görseller döndürebilir — ekran görüntüleri, diyagramlar vb. Bunları base64 kodlu dizeler olarak döndür:

```js  theme={null}
const RED_CIRCLE_BASE64 = "/9j/4AAQSkZJRgABAgEASABIAAD/2w...";
// ^ okunabilirlik için tam base64 kısaltıldı

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

Uygulama ayrıntıları için şu [örnek sunucuya](https://github.com/msfeldstein/mcp-test-servers/blob/main/src/image-server.js) bak. Cursor, dönen görselleri sohbete ekler. Model görselleri destekliyorsa onları analiz eder.

<div id="security-considerations">
  ## Güvenlik hususları
</div>

MCP sunucularını kurarken şu güvenlik uygulamalarını göz önünde bulundur:

* **Kaynağı doğrula**: MCP sunucularını yalnızca güvenilir geliştiricilerden ve depolardan kur
* **İzinleri incele**: Sunucunun hangi verilere ve API’lere erişeceğini kontrol et
* **API anahtarlarını sınırla**: Yalnızca minimum gerekli izinlere sahip kısıtlı API anahtarları kullan
* **Kodu denetle**: Kritik entegrasyonlar için sunucunun kaynak kodunu incele

MCP sunucularının harici hizmetlere erişebileceğini ve senin adına kod çalıştırabileceğini unutma. Kurmadan önce bir sunucunun ne yaptığını mutlaka anla.

<div id="real-world-examples">
  ## Gerçek dünya örnekleri
</div>

MCP’nin gerçek hayattaki kullanımına dair pratik örnekler için, Linear, Figma ve tarayıcı araçlarını geliştirme iş akışına entegre etmeyi gösteren [Web Development guide](/tr/guides/tutorials/web-development) sayfasına göz at.

<div id="faq">
  ## SSS
</div>

<AccordionGroup>
  <Accordion title="MCP sunucularının amacı nedir?">
    MCP sunucuları Cursor'ı Google Drive, Notion ve diğer hizmetler gibi harici araçlara bağlayarak dokümanları ve gereksinimleri kodlama iş akışına dahil eder.
  </Accordion>

  {" "}

  <Accordion title="MCP sunucu sorunlarını nasıl debug ederim?">
    MCP loglarını görüntülemek için: 1. Cursor'da Output panelini aç (<Kbd>Cmd+Shift+U</Kbd>)
    2\. Dropdown'dan "MCP Logs" seç 3. Bağlantı hatalarını, kimlik doğrulama sorunlarını veya sunucu çökmelerini kontrol et Loglar sunucu başlatma, araç çağrıları ve hata mesajlarını gösterir.
  </Accordion>

  {" "}

  <Accordion title="Bir MCP sunucusunu geçici olarak devre dışı bırakabilir miyim?">
    Evet! Sunucuları kaldırmadan açıp kapatabilirsin: 1. Ayarları aç (
    <Kbd>Cmd+Shift+J</Kbd>) 2. Features → Model Context Protocol'e git 3. Herhangi bir sunucunun yanındaki toggle'a tıklayarak etkinleştir/devre dışı bırak Devre dışı bırakılan sunucular yüklenmez veya chat'te görünmez. Bu, sorun giderme veya araç karmaşasını azaltmak için kullanışlıdır.
  </Accordion>

  {" "}

  <Accordion title="Bir MCP sunucusu çökerse veya zaman aşımına uğrarsa ne olur?">
    Bir MCP sunucusu başarısız olursa: - Cursor chat'te bir hata mesajı gösterir - Araç çağrısı başarısız olarak işaretlenir - İşlemi yeniden deneyebilir veya ayrıntılar için logları kontrol edebilirsin - Diğer MCP sunucuları normal şekilde çalışmaya devam eder Cursor, bir sunucunun diğerlerini etkilemesini önlemek için sunucu başarısızlıklarını izole eder.
  </Accordion>

  {" "}

  <Accordion title="Bir MCP sunucusunu nasıl güncellerim?">
    npm tabanlı sunucular için: 1. Sunucuyu ayarlardan kaldır 2. npm cache'ini temizle:
    `npm cache clean --force` 3. En son sürümü almak için sunucuyu yeniden ekle Özel sunucular için, yerel dosyalarını güncelle ve Cursor'ı yeniden başlat.
  </Accordion>

  <Accordion title="MCP sunucularını hassas verilerle kullanabilir miyim?">
    Evet, ancak güvenlik best practice'lerini takip et: - Gizli bilgiler için environment variable'ları kullan, asla hardcode etme - Hassas sunucuları `stdio`
    transport ile yerel olarak çalıştır - API key izinlerini gerekli minimum ile sınırla - Hassas sistemlere bağlanmadan önce sunucu kodunu incele - Sunucuları izole edilmiş ortamlarda çalıştırmayı düşün
  </Accordion>
</AccordionGroup>

---

← Previous: [Dosyaları yoksay](./dosyalar-yoksay.md) | [Index](./index.md) | Next: [Anılar](./anlar.md) →