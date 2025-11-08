---
title: "Kod Tabanı İndeksleme"
source: "https://docs.cursor.com/tr/context/codebase-indexing"
language: "tr"
language_name: "Turkish"
---

# Kod Tabanı İndeksleme
Source: https://docs.cursor.com/tr/context/codebase-indexing

Cursor'ın kod tabanını daha iyi anlamak için nasıl öğrendiği

Cursor, her dosya için gömme vektörleri (embeddings) hesaplayarak kod tabanını indeksler. Bu, kodunla ilgili AI tarafından üretilen yanıtları iyileştirir. Bir projeyi açtığında Cursor otomatik olarak indekslemeye başlar. Yeni dosyalar artımlı olarak indekslenir.
İndeksleme durumunu şuradan kontrol et: `Cursor Settings` > `Indexing & Docs`

<Frame>
  <img src="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/codebase-indexing.png?fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=47c946c1a46c8047feda127ef84faa9d" alt="Kod tabanı indeksleme ilerleme göstergesi" data-og-width="2048" width="2048" data-og-height="1183" height="1183" data-path="images/get-started/codebase-indexing.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/codebase-indexing.png?w=280&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=3d628d1692d4cc512f4a81ece7e4a2c5 280w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/codebase-indexing.png?w=560&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=d5e20a24a9f38c97eb83249cd063ae41 560w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/codebase-indexing.png?w=840&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=ea26f1d9bf65ae5093333d15035ec96d 840w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/codebase-indexing.png?w=1100&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=1d532fe92021c50bee36b97e541419df 1100w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/codebase-indexing.png?w=1650&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=01c4cfe42a58ac06f6ac18e6e565782e 1650w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/codebase-indexing.png?w=2500&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=41d02dff523bfa3a33c6d4e86e79732a 2500w" />
</Frame>

<div id="configuration">
  ## Yapılandırma
</div>

Cursor, [yoksayma dosyaları](/tr/context/ignore-files) içindekiler (ör. `.gitignore`, `.cursorignore`) dışında tüm dosyaları indeksler.

`Show Settings`'e tıkla ve şunları yap:

* Yeni depolar için otomatik indekslemeyi etkinleştir
* Hangi dosyaların yoksayılacağını yapılandır

<Tip>
  [Büyük içerik dosyalarını yoksaymak](/tr/context/ignore-files) yanıt
  doğruluğunu artırır.
</Tip>

<div id="view-indexed-files">
  ### İndekslenen dosyaları görüntüle
</div>

İndekslenen dosya yollarını görmek için: `Cursor Settings` > `Indexing & Docs` > `View included files`

Bu, tüm indekslenen dosyaları listeleyen bir `.txt` dosyası açar.

<div id="multi-root-workspaces">
  ## Çok köklü çalışma alanları
</div>

Cursor, birden fazla kod tabanıyla çalışmana olanak tanıyan [çok köklü çalışma alanları](https://code.visualstudio.com/docs/editor/workspaces#_multiroot-workspaces) desteğini sunar:

* Tüm kod tabanları otomatik olarak dizine eklenir
* Her kod tabanının bağlamı AI tarafından kullanılabilir
* `.cursor/rules` tüm klasörlerde çalışır

<div id="pr-search">
  ## PR araması
</div>

PR araması, geçmiş değişiklikleri aranabilir ve AI aracılığıyla erişilebilir hale getirerek kod tabanının evrimini anlamana yardımcı olur.

<div id="how-it-works">
  ### Nasıl çalışır
</div>

Cursor, depo geçmişinden **birleşmiş tüm PR'leri otomatik olarak indeksler**. Özetler, yakın zamandaki değişiklikleri önceliklendiren akıllı filtreleme ile semantik arama sonuçlarında görünür.

Agent, `@[PR number]`, `@[commit hash]` veya `@[branch name]` kullanarak bağlama **PR’leri, commit’leri, issue’ları veya branch’leri** getirebilir. Bağlandığında GitHub yorumlarını ve Bugbot incelemelerini de içerir.

**Platform desteği** GitHub, GitHub Enterprise ve Bitbucket'ı kapsar. GitLab şu anda desteklenmiyor.

<Note>
  GitHub Enterprise kullanıcıları: Fetch aracı, VSCode kimlik doğrulama sınırlamaları nedeniyle
  git komutlarına geri döner.
</Note>

<div id="using-pr-search">
  ### PR aramasını kullanma
</div>

"Diğer PR’lerde servisler nasıl uygulanmış?" gibi sorular sor ve Agent, deponun geçmişine dayanarak kapsamlı yanıtlar sağlamak için ilgili PR’leri otomatik olarak bağlama getirir.

<div id="faq">
  ## SSS
</div>

<AccordionGroup>
  <Accordion title="İndekslenen tüm kod tabanlarını nerede görebilirim?">
    Henüz genel bir liste yok. Her projeyi tek tek Cursor’da açıp Codebase Indexing ayarlarını kontrol et.
  </Accordion>

  <Accordion title="İndekslenen tüm kod tabanlarını nasıl silerim?">
    Tüm indekslenen kod tabanlarını kaldırmak için Settings’ten Cursor hesabını sil.
    Yoksa, her projenin Codebase Indexing
    ayarlarından kod tabanlarını tek tek sil.
  </Accordion>

  <Accordion title="İndekslenen kod tabanları ne kadar süre saklanır?">
    İndekslenen kod tabanları, 6 hafta boyunca etkinlik olmazsa silinir. Projeyi
    yeniden açman yeniden indekslemeyi tetikler.
  </Accordion>

  <Accordion title="Kaynak kodum Cursor sunucularında saklanıyor mu?">
    Hayır. Cursor, dosya adlarını veya kaynak kodu saklamadan embedding’ler oluşturur. Dosya adları bulanıklaştırılır ve kod parçaları şifrelenir.

    Agent kod tabanında arama yaptığında, Cursor embedding’leri sunucudan alır ve parçaların şifresini çözer.
  </Accordion>
</AccordionGroup>

---

← Previous: [/command](./command.md) | [Index](./index.md) | Next: [Dosyaları yoksay](./dosyalar-yoksay.md) →