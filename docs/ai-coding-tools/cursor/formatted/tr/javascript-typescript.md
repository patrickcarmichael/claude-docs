---
title: "JavaScript & TypeScript"
source: "https://docs.cursor.com/tr/guides/languages/javascript"
language: "tr"
language_name: "Turkish"
---

# JavaScript & TypeScript
Source: https://docs.cursor.com/tr/guides/languages/javascript

Framework desteğiyle JavaScript ve TypeScript geliştirme

Cursor’da JavaScript ve TypeScript geliştirmeye hoş geldin! Editör, eklenti ekosistemi sayesinde JS/TS geliştirme için olağanüstü destek sunuyor. Cursor’dan en iyi şekilde yararlanman için bilmen gerekenler:

<div id="essential-extensions">
  ## Temel Uzantılar
</div>

Cursor, tercih ettiğin herhangi bir uzantıyla harika çalışır; yine de yeni başlıyorsan şunları öneriyoruz:

* **ESLint** - Cursor’ın yapay zekâ destekli lint düzeltme özellikleri için gerekli
* **JavaScript and TypeScript Language Features** - Geliştirilmiş dil desteği ve IntelliSense
* **Path Intellisense** - Dosya yolları için akıllı otomatik tamamlama

<div id="cursor-features">
  ## Cursor Özellikleri
</div>

Cursor, mevcut JavaScript/TypeScript çalışma akışını şu özelliklerle güçlendirir:

* **Sekmeyle Tamamlama**: Proje yapını anlayan, bağlama duyarlı kod tamamlama
* **Otomatik İçe Aktarmalar**: Tab, bir kütüphaneyi kullanır kullanmaz onu otomatik olarak içe aktarır
* **Satır İçi Düzenleme**: Herhangi bir satırda `CMD+K` kullanarak kusursuz sözdizimiyle düzenle
* **Composer Yönlendirmesi**: Composer ile birden fazla dosyada kodunu planla ve düzenle

<div id="framework-intelligence-with-docs">
  ### @Docs ile Framework Zekâsı
</div>

Cursor’ın @Docs özelliği, yapay zekânın başvurabileceği özel dokümantasyon kaynakları ekleyerek JavaScript geliştirmeyi turbo besler. Daha doğru ve bağlamsal kod önerileri almak için MDN, Node.js veya favori framework’ünün dokümantasyonunu ekle.

<Card title="Learn more about @Docs" icon="book" href="/tr/context/@-symbols/@-docs">
  Cursor’da özel dokümantasyon kaynaklarını nasıl ekleyip yöneteceğini keşfet.
</Card>

<div id="automatic-linting-resolution">
  ### Otomatik Lint Çözümü
</div>

Cursor’ın öne çıkan özelliklerinden biri, linter uzantılarıyla kusursuz entegrasyonudur.
ESLint gibi bir linter kurduğundan emin ol ve 'Iterate on Lints' ayarını etkinleştir.

Ardından, Composer’da Agent modunu kullanırken, yapay zekâ sorguna yanıtlamaya çalışıp kodda değişiklik yaptıktan sonra, linter çıktısını otomatik olarak okuyacak ve o anda farkında olmadığı lint hatalarını düzeltmeye çalışacak.

<div id="framework-support">
  ## Framework Desteği
</div>

Cursor, tüm başlıca JavaScript framework’leri ve kütüphaneleriyle aşağıdaki gibi sorunsuz çalışır:

### React & Next.js

* Akıllı bileşen önerileriyle tam JSX/TSX desteği
* Next.js için server components ve API routes zekâsı
* Önerilen: [**React Developer Tools**](cursor:extension/msjsdiag.vscode-react-native) eklentisi

<div id="vuejs">
  ### Vue.js
</div>

* Volar entegrasyonuyla şablon sözdizimi desteği
* Bileşen otomatik tamamlama ve tür denetimi
* Önerilen: [**Vue Language Features**](cursor:extension/vue.volar)

<div id="angular">
  ### Angular
</div>

* Şablon doğrulama ve TypeScript decorator desteği
* Bileşen ve servis üretimi
* Önerilen: [**Angular Language Service**](cursor:extension/Angular.ng-template)

<div id="svelte">
  ### Svelte
</div>

* Bileşen sözdizimi vurgulama ve akıllı tamamlama
* Reaktif ifadeler ve store önerileri
* Önerilen: [**Svelte for VS Code**](cursor:extension/svelte.svelte-vscode)

<div id="backend-frameworks-expressnestjs">
  ### Backend Framework’leri (Express/NestJS)
</div>

* Route ve middleware zekâsı
* NestJS için TypeScript decorator desteği
* API test araçlarıyla entegrasyon

Unutma, Cursor’ın yapay zekâ özellikleri bu framework’lerin tümüyle uyumlu çalışır; kalıplarını ve en iyi uygulamalarını anlayarak ilgili öneriler sunar. Yapay zekâ, bileşen oluşturmadan karmaşık refaktoring görevlerine kadar her konuda, projenin mevcut kalıplarına saygı duyarak yardımcı olabilir.

---

← Previous: [Java](./java.md) | [Index](./index.md) | Next: [Python](./python.md) →