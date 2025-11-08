---
title: "Dokümantasyonla Çalışma"
source: "https://docs.cursor.com/tr/guides/advanced/working-with-documentation"
language: "tr"
language_name: "Turkish"
---

# Dokümantasyonla Çalışma
Source: https://docs.cursor.com/tr/guides/advanced/working-with-documentation

Cursor'da istemler, harici kaynaklar ve dahili bağlam aracılığıyla dokümantasyondan etkili şekilde nasıl yararlanılır

export const ChatInput = ({content = []}) => {
  const renderContent = () => {
    return content.map((item, index) => {
      if (item.type === 'mention') {
        return <span key={index} className="mention bg-blue-500/20 px-1 py-0.5 rounded-sm">
                        {item.text}
                    </span>;
      }
      return item.text;
    });
  };
  return <>
            <div className="flex flex-col items-stretch border border-neutral-500 rounded-lg p-3 gap-2 bg-neutral-800 relative transition-all duration-100 ease-in-out hover:border-neutral-500">
                <div className="flex flex-col gap-1">
                    <div className="flex flex-col gap-1 outline-none overflow-hidden">
                        <div className="flex-1 flex items-center gap-2">
                            <div className="w-full box-border max-h-10 overflow-hidden">
                                <div className="flex items-center gap-2 w-full flex-nowrap">
                                    <div className="cursor-pointer flex items-center justify-center p-1 h-5 w-5 rounded border border-neutral-600 outline-none flex-shrink-0 hover:bg-neutral-700 bg-neutral-750">
                                        <span className="text-neutral-400 text-sm font-semibold">@</span>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                <div className="relative pt-0">
                    <div className="min-h-6 w-full max-h-60">
                        <div className="relative overflow-y-hidden w-full">
                            <div className="w-full flex flex-wrap overflow-hidden min-h-6">
                                <div className="inline-block w-full min-h-full">
                                    <div className="w-full overflow-visible h-full min-h-6">
                                        <div className="grid relative grid-cols-1 w-full">

                                            <div className="leading-6 text-sm text-neutral-200 bg-transparent block break-words p-0 whitespace-pre-wrap font-medium min-h-6">
                                                {content.length > 0 ? renderContent() : <span className="text-neutral-500">Plan, search, build anything</span>}
                                            </div>

                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>

                    <div className="flex items-center justify-between gap-3 flex-shrink-0 mt-6">
                        <div className="flex-1 w-full h-full flex items-center flex-col gap-1">
                            <div className="flex items-center justify-between gap-2 flex-shrink-0 w-full">
                                <div className="flex items-center justify-between w-full">
                                    <div className="flex items-center gap-3 flex-shrink min-w-0">
                                        <div className="flex gap-1 text-xs items-center min-w-0 max-w-full px-1.5 py-0.5 flex-shrink-0 cursor-pointer bg-neutral-700 hover:bg-neutral-600 rounded-full">
                                            <div className="flex items-center gap-1 min-w-0 max-w-full overflow-hidden">
                                                <div className="text-xs flex-shrink-0 w-3 h-3 flex items-center justify-center text-neutral-400">
                                                    ∞
                                                </div>
                                                <div className="min-w-0 max-w-full overflow-hidden text-ellipsis whitespace-nowrap flex items-center gap-1 font-medium">
                                                    <span className="text-neutral-300">Agent</span>
                                                    <span className="text-neutral-500 text-[10px]">⌘I</span>
                                                </div>
                                                <Icon icon="chevron-down" size={6} color="currentColor" />
                                            </div>
                                        </div>

                                        <div className="flex gap-2 text-xs items-center cursor-pointer min-w-0 max-w-full px-0 py-1 opacity-90 rounded hover:text-neutral-200">
                                            <div className="flex items-center gap-2 min-w-0 max-w-full overflow-x-hidden">
                                                <div className="min-w-0 text-ellipsis whitespace-nowrap text-neutral-300 flex items-center gap-2 overflow-hidden">
                                                    <div className="overflow-hidden inline-flex gap-2 items-center">
                                                        <span className="whitespace-nowrap overflow-x-hidden text-ellipsis text-xs">
                                                            Auto
                                                        </span>
                                                    </div>
                                                </div>
                                                <Icon icon="chevron-down" size={8} color="currentColor" />
                                            </div>
                                        </div>
                                    </div>

                                    <div className="flex items-center gap-3 justify-end">
                                        <button className="bg-white/80 border-none text-neutral-500 flex w-5 h-5 items-center justify-center hover:text-neutral-400 hover:bg-white/90 rounded-full disabled:opacity-50" disabled={content.length === 0 || !content.some(item => item.text.trim())}>
                                            <span className="text-sm">↑</span>
                                        </button>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </>;
};

<div id="why-documentation-matters">
  # Belgelendirme neden önemlidir
</div>

Belgelendirme güncel ve doğru bağlam sağlar. Olmadan modeller eski ya da eksik eğitim verilerini kullanır. Belgelendirme, modellerin şunları anlamasına yardımcı olur:

* Güncel API’ler ve parametreler
* En iyi uygulamalar
* Organizasyon gelenekleri
* Alan terminolojisi

Ve çok daha fazlası. Bağlam değiştirmeden belgelendirmeyi doğrudan Cursor’da nasıl kullanacağını öğrenmek için okumaya devam et.

<div id="model-knowledge-cutoff">
  ## Model bilgi kesim tarihi
</div>

Büyük dil modelleri, "bilgi kesim tarihi" denilen belirli bir zamana kadar olan verilerle eğitilir. Bu şu anlama gelir:

* En son kütüphane güncellemeleri yansımamış olabilir
* Yeni çatı (framework) veya araçlar bilinmeyebilir
* Kesim tarihinden sonra yapılan API değişiklikleri atlanır
* En iyi uygulamalar eğitimden bu yana değişmiş olabilir

Örneğin, bir modelin bilgi kesim tarihi 2024’ün başıysa, 2024’ün sonlarında çıkan özelliklerden, popüler çatı (framework)lar için bile haberdar olmaz.

<div id="which-tool-should-i-use">
  # Hangi aracı kullanmalıyım?
</div>

Dokümantasyon ihtiyaçların için en iyi yaklaşımı hızlıca belirlemek için bu karar ağacını kullan:

```mermaid  theme={null}
flowchart TD
    A[Hangi bilgiye ihtiyacın var?] --> B[Herkese açık framework’ler/kütüphaneler]
    A --> C[Yakın dönem topluluk bilgisi/sorun giderme]
    A --> D[Dahili şirket bilgileri]
    
    B --> E[Resmî dokümantasyon gerekiyor mu?]
    E -->|Evet| F[@Docs kullan<br/>API referansları, kılavuzlar, en iyi uygulamalar]
    E -->|Hayır| G[@Web kullan<br/>Topluluk eğitimleri, karşılaştırmalar]
    
    C --> H[@Web kullan<br/>Güncel paylaşımlar, GitHub issue’ları]
    
    D --> I[Mevcut MCP entegrasyonları var mı?]
    I -->|Evet| J[Mevcut MCP’yi kullan<br/>Confluence, Google Drive, vb.]
    I -->|Hayır| K[Özel MCP oluştur<br/>Dahili API’ler, mülkiyet sistemleri]
    
    style F fill:#e1f5fe
    style G fill:#e8f5e8  
    style H fill:#e8f5e8
    style J fill:#fff3e0
    style K fill:#fce4ec
```

<div id="mental-model">
  ## Zihinsel model
</div>

<div className="full-width-table">
  | Araç        | Zihinsel model                             |
  | ----------- | ------------------------------------------ |
  | **`@Docs`** | Resmi dokümantasyonda gezinip okumak gibi  |
  | **`@Web`**  | İnternette çözüm aramak gibi               |
  | **MCP**     | Kendi dahili dokümantasyonuna erişmek gibi |
</div>

<div id="public-documentation">
  # Public documentation
</div>

Harici dokümantasyon, modellerin sınırlı ya da güncelliğini yitirmiş bilgiye sahip olabileceği, herkese açık bilgileri kapsar. Cursor, bu bilgilere erişmek için iki ana yol sunar.

<div id="using-docs">
  ## @Docs'u kullanma
</div>

`@Docs`, Cursor'ı popüler araç ve framework'lerin resmi dokümantasyonuna bağlar. Şu konularda güncel ve yetkili bilgiye ihtiyaç duyduğunda kullan:

* **API referansları**: Fonksiyon imzaları, parametreler, dönüş tipleri
* **Başlangıç rehberleri**: Kurulum, yapılandırma, temel kullanım
* **En iyi uygulamalar**: Kaynaktan önerilen kalıplar
* **Framework'e özel hata ayıklama**: Resmi sorun giderme rehberleri

<ChatInput
  content={[
{ type: 'mention', text: '@Docs Next.js' },
{ type: 'text', text: ' Catch-all rotalarla dinamik yönlendirmeyi nasıl kurarım?' }
]}
/>

<div id="using-web">
  ## @Web'i kullanma
</div>

`@Web`, güncel bilgiler, blog yazıları ve topluluk tartışmaları için canlı internette arama yapar. Şunlara ihtiyacın olduğunda kullan:

* **Güncel eğitimler**: Topluluk kaynaklı içerikler ve örnekler
* **Karşılaştırmalar**: Farklı yaklaşımları karşılaştıran yazılar
* **En son güncellemeler**: Çok yeni güncellemeler veya duyurular
* **Birden fazla bakış açısı**: Sorunlara farklı yaklaşımlar

<ChatInput
  content={[
{ type: 'mention', text: '@Web' },
{ type: 'text', text: ' React 19 için en yeni performans optimizasyonları' }
]}
/>

<div id="internal-documentation">
  # İç dokümantasyon
</div>

İç dokümantasyon, AI modellerinin eğitim sırasında hiç görmediği, organizasyonuna özgü bilgileri içerir. Şunları kapsayabilir:

* **Dahili API'ler**: Özel servisler ve mikroservisler
* **Şirket standartları**: Kodlama kuralları, mimari desenler
* **Mülkiyet sistemler**: Özel araçlar, veritabanları, iş akışları
* **Alan bilgisi**: İş mantığı, uyumluluk gereksinimleri

<div id="accessing-internal-docs-with-mcp">
  ## MCP ile dahili dökümanlara erişim
</div>

Model Context Protocol (MCP), özel dökümanlarını ve sistemlerini Cursor’a getirmenin standart bir yolunu sağlar. MCP, Cursor ile dahili kaynakların arasında ince bir katman olarak çalışır.

**MCP neden önemli:**

* Modeller dahili uygulamalarını/alışkanlıklarını tahmin edemez
* Özel servisler için API dökümantasyonu herkese açık değildir
* İş mantığı ve alan bilgisi organizasyonuna özeldir
* Uyum ve güvenlik gereksinimleri şirkete göre değişir

<div id="common-mcp-integrations">
  ### Yaygın MCP entegrasyonları
</div>

| Entegrasyon      | Erişim                                  | Örnekler                                                                                                                   |
| ---------------- | --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| **Confluence**   | Şirket Confluence alanları              | Mimari dökümantasyon, dahili servisler için API spesifikasyonları, kod standartları ve yönergeler, süreç dökümantasyonu    |
| **Google Drive** | Paylaşılan belgeler ve klasörler        | Spesifikasyon dokümanları, toplantı notları ve karar kayıtları, tasarım dokümanları ve gereksinimler, ekip bilgi tabanları |
| **Notion**       | Çalışma alanı veritabanları ve sayfalar | Proje dökümantasyonu, ekip vikileri, bilgi tabanları, ürün gereksinimleri, teknik spesifikasyonlar                         |
| **Custom**       | Dahili sistemler ve veritabanları       | Tescilli API’ler, legacy dökümantasyon sistemleri, özel bilgi tabanları, uzmanlaşmış araçlar ve iş akışları                |

<div id="custom-solutions">
  #### Özel çözümler
</div>

Benzersiz ihtiyaçlar için, şunları yapabilen özel MCP sunucuları geliştirebilirsin:

* Dahili web sitelerini veya portalları taramak
* Tescilli veritabanlarına bağlanmak
* Özel dökümantasyon sistemlerine erişmek
* Dahili vikilerden veya bilgi tabanlarından veri çekmek

<Tip>Özel bir MCP sunucusu geliştirirsen, Cursor’ın dökümantasyonu güncellemesi için araçlar da expose edebilirsin</Tip>

Dahili dökümanları taramak için örnek özel MCP sunucusu:

<CodeGroup>
  ```javascript TypeScript theme={null}
  import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
  import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
  import { z } from "zod";
  import TurndownService from "turndown";

  // Dahili dökümanları taramak için bir MCP sunucusu oluştur
  const server = new McpServer({
    name: "internal-docs",
    version: "1.0.0"
  });

  const turndownService = new TurndownService();

  // Dahili dökümantasyonu taramak için tool ekle
  server.tool("get_doc",
    { url: z.string() },
    async ({ url }) => {
      try {
        const response = await fetch(url);
        const html = await response.text();
        
        // HTML’i markdown’a dönüştür
        const markdown = turndownService.turndown(html);
        
        return {
          content: [{ type: "text", text: markdown }]
        };
      } catch (error) {
        return {
          content: [{ type: "text", text: `Error scraping ${url}: ${error.message}` }]
        };
      }
    }
  );

  // stdin üzerinden mesaj almayı ve stdout üzerinden mesaj göndermeyi başlat
  const transport = new StdioServerTransport();
  await server.connect(transport);
  ```

  ```python Python theme={null}
  # server.py
  import os
  import asyncio
  from mcp.server.fastmcp import FastMCP
  import aiohttp
  from markdownify import markdownify as md

  # Dahili dökümanları taramak için bir MCP sunucusu oluştur
  mcp = FastMCP("internal-docs")

  @mcp.tool()
  async def get_doc(url: str) -> dict:
      """Bir URL’den dahili dökümantasyonu tara"""
      try:
          async with aiohttp.ClientSession() as session:
              async with session.get(url) as response:
                  html = await response.text()
          
          # HTML’i markdown’a dönüştür
          markdown = md(html)
          
          return {
              "content": [{"type": "text", "text": markdown}]
          }
      except Exception as error:
          return {
              "content": [{"type": "text", "text": f"Error scraping {url}: {str(error)}"}]
          }
  ```
</CodeGroup>

<div id="keeping-docs-up-to-date">
  # Dokümanları güncel tutmak
</div>

Dokümantasyon hızla eskir. Cursor, gerçek koduna ve geliştirme konuşmalarına dayanarak dokümantasyonu oluşturup güncelleyerek onu güncel ve faydalı tutmana yardımcı olur.

<div id="from-existing-code">
  ## Mevcut koddan
</div>

Cursor’ı kullanarak dokümantasyonu doğrudan kod tabanından oluştur:

<Tabs>
  <Tab title="API Documentation">
    <ChatInput
      content={[
    { type: 'text', text: 'Bu Express router için, tüm uç noktalar, parametreler ve yanıt formatları dahil olmak üzere API dokümantasyonu oluştur' }
  ]}
    />
  </Tab>

  <Tab title="JSDoc Comments">
    <ChatInput
      content={[
    { type: 'text', text: 'Bu sınıfa kapsamlı JSDoc açıklamaları ekle; tüm yöntemleri ve bunların parametrelerini belgele' }
  ]}
    />
  </Tab>

  <Tab title="README Creation">
    <ChatInput
      content={[
    { type: 'text', text: 'Kurulum yönergeleri, kullanım örnekleri ve API genel bakışını içeren bu proje için bir README oluştur' }
  ]}
    />
  </Tab>
</Tabs>

<div id="from-chat-sessions">
  ## Sohbet oturumlarından
</div>

Cursor’la yaptığın sohbetlerde, dokümantasyona dönüştürülebilecek değerli niyetler var.

<Tabs>
  <Tab title="Problem Solving">
    **Karmaşık bir sorun çözüldükten sonra:**

    <ChatInput
      content={[
    { type: 'text', text: 'Kimlik doğrulamayı kurma üzerine sohbetimizi ekip wikisi için adım adım bir rehbere özetle' }
  ]}
    />
  </Tab>

  <Tab title="Architecture">
    **Mimari kararların ardından:**

    <ChatInput
      content={[
    { type: 'text', text: 'Tartıştığımız ödünleri de dahil ederek bu veritabanı tasarımını neden seçtiğimizi açıklayan bir dokümantasyon hazırla' }
  ]}
    />
  </Tab>

  <Tab title="Debugging">
    **Hata ayıklama oturumlarından sonra:**

    <ChatInput
      content={[
    { type: 'text', text: 'Az önce düzelttiğimiz bu hataya dayanarak, belirtiler ve çözüm adımlarını içeren bir sorun giderme rehberi yaz' }
  ]}
    />
  </Tab>
</Tabs>

<div id="takeaways">
  ## Özet
</div>

* Belgeleri bağlam olarak kullanmak, Cursor’ı daha isabetli ve güncel yapar
* Resmi dokümantasyon için `@Docs`, topluluk bilgisi için `@Web` kullan
* MCP, Cursor ile dahili sistemlerin arasındaki boşluğu kapatır
* Bilgiyi güncel tutmak için koddan ve sohbetlerden dokümantasyon üret
* Kapsamlı bir anlayış için harici ve dahili dokümantasyon kaynaklarını birleştir

---

← Previous: [Large Codebases](./large-codebases.md) | [Index](./index.md) | Next: [Java](./java.md) →