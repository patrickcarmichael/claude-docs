---
title: "Araçlar"
source: "https://docs.cursor.com/tr/agent/tools"
language: "tr"
language_name: "Turkish"
---

# Araçlar
Source: https://docs.cursor.com/tr/agent/tools

Kod arama, düzenleme ve çalıştırma için ajanlara sunulan araçlar

[Agent](/tr/agent/overview) içindeki modlarda kullanılabilen tüm araçların listesi; kendi [özel modlarını](/tr/agent/modes#custom) oluştururken bunları etkinleştirip devre dışı bırakabilirsin.

<Note>
  Bir görev sırasında Agent’ın yapabileceği araç çağrılarının sayısında bir sınır yok. İsteğini tamamlamak için gerektiği kadar araç kullanmaya devam edecek.
</Note>

<div id="search">
  ## Arama
</div>

Kod tabanında ve web'de ilgili bilgiyi bulmak için kullanılan araçlar.

<AccordionGroup>
  <Accordion title="Read File" icon="file-lines">
    Bir dosyadan en fazla 250 satır (maks modda 750) okur.
  </Accordion>

  <Accordion title="List Directory" icon="folder-open">
    Dosya içeriklerini okumadan bir dizinin yapısını okur.
  </Accordion>

  <Accordion title="Codebase" icon="database">
    [indekslenmiş
    kod tabanında](/tr/context/codebase-indexing) semantik aramalar yapar.
  </Accordion>

  <Accordion title="Grep" icon="magnifying-glass">
    Dosyalar içinde tam anahtar kelimeleri veya desenleri arar.
  </Accordion>

  <Accordion title="Search Files" icon="file-magnifying-glass">
    Bulanık eşleştirme kullanarak dosyaları ada göre bulur.
  </Accordion>

  <Accordion title="Web" icon="globe">
    Arama sorguları üretir ve web aramaları yapar.
  </Accordion>

  <Accordion title="Fetch Rules" icon="gavel">
    Türe ve açıklamaya göre belirli [kuralları](/tr/context/rules) getirir.
  </Accordion>
</AccordionGroup>

<div id="edit">
  ## Düzenle
</div>

Dosyalarında ve kod tabanında belirli düzenlemeler yapmana yardımcı olan araçlar.

<AccordionGroup>
  <Accordion title="Düzenle & Yeniden Uygula" icon="pencil">
    Dosyalara düzenleme öner ve bunları otomatik olarak [uygula](/tr/agent/apply).
  </Accordion>

  <Accordion title="Dosyayı Sil" icon="trash">
    Dosyaları kendi kendine sil (ayarlar bölümünde devre dışı bırakılabilir).
  </Accordion>
</AccordionGroup>

<div id="run">
  ## Çalıştır
</div>

Chat terminalinle etkileşime geçebilir.

<AccordionGroup>
  <Accordion title="Terminal" icon="terminal">
    Terminal komutlarını çalıştır ve çıktıyı izle.
  </Accordion>
</AccordionGroup>

<Note>Varsayılan olarak, Cursor mevcut ilk terminal profilini kullanır.</Note>

Tercih ettiğin terminal profilini ayarlamak için:

1. Komut Paletini aç (`Cmd/Ctrl+Shift+P`)
2. "Terminal: Select Default Profile" ara
3. İstediğin profili seç

<div id="mcp">
  ## MCP
</div>

Sohbet, veritabanları veya üçüncü taraf API’ler gibi harici hizmetlerle etkileşim kurmak için yapılandırılmış MCP sunucularını kullanabilir.

<AccordionGroup>
  <Accordion title="MCP Sunucularını Aç/Kapat" icon="server">
    Kullanılabilir MCP sunucularını aç/kapat. Otomatik çalıştırma yapılandırmasına uyar.
  </Accordion>
</AccordionGroup>

[Model Context Protocol](/tr/context/model-context-protocol) hakkında daha fazlasını öğren ve [MCP dizini](/tr/tools)nde mevcut sunucuları keşfet.

<div id="advanced-options">
  ## Gelişmiş seçenekler
</div>

<AccordionGroup>
  <Accordion title="Auto-apply Edits" icon="check">
    Düzenlemeleri manuel onay olmadan otomatik uygula.
  </Accordion>

  <Accordion title="Auto-run" icon="play">
    Terminal komutlarını otomatik çalıştır ve düzenlemeleri kabul et. Test paketlerini (test suite) çalıştırmak ve değişiklikleri doğrulamak için kullanışlıdır.

    <Frame>
      <img src="https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=3135722076a5aa636d27dbedec665bae" data-og-width="1624" width="1624" data-og-height="1012" height="1012" data-path="images/agent/auto-run.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=280&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=9f2e2bed8f634201adc51ccb2bd96cd2 280w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=560&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=51704cac2f270a04856fffbeaccf9700 560w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=840&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=01a5034975497a8dff4f41dca0d19f2e 840w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=1100&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=5f19026a0c6e5fb28c935ce795edb706 1100w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=1650&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=a108fc86f8ee7c0db6e5b7ab80ede738 1650w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=2500&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=9ce5f45879c29049640bb5a1494db11e 2500w" />
    </Frame>
  </Accordion>

  <Accordion title="Guardrails" icon="shield">
    Hangi araçların otomatik çalıştırılabileceğini belirtmek için izin listelerini yapılandır. İzin listeleri, izin verilen işlemleri açıkça tanımlayarak daha iyi güvenlik sağlar.
  </Accordion>

  <Accordion title="Auto-fix Errors" icon="wrench">
    Agent tarafından karşılaşıldığında linter hatalarını ve uyarılarını otomatik olarak gider.
  </Accordion>
</AccordionGroup>

---

← Previous: [Terminal](./terminal.md) | [Index](./index.md) | Next: [Arka Plan Aracıları](./arka-plan-araclar.md) →