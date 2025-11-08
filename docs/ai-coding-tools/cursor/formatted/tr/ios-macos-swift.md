---
title: "iOS & macOS (Swift)"
source: "https://docs.cursor.com/tr/guides/languages/swift"
language: "tr"
language_name: "Turkish"
---

# iOS & macOS (Swift)
Source: https://docs.cursor.com/tr/guides/languages/swift

Swift geliştirme için Cursor’ı Xcode’la entegre et

Cursor’da Swift geliştirmeye hoş geldin! iOS uygulamaları, macOS uygulamaları ya da sunucu tarafı Swift projeleri geliştiriyor ol, yanındayız. Bu rehber, temellerden başlayıp daha gelişmiş özelliklere geçerek Cursor’da Swift ortamını kurmana yardımcı olacak.

<div id="basic-workflow">
  ## Temel Çalışma Akışı
</div>

Cursor’ı Swift ile kullanmanın en kolay yolu, onu birincil kod editörün olarak kullanıp uygulamalarını derlemek ve çalıştırmak için Xcode’dan yararlanmaya devam etmek. Şu gibi harika özellikler elde edersin:

* Akıllı kod tamamlama
* Yapay zekâ destekli kodlama desteği (herhangi bir satırda [CMD+K](/tr/inline-edit/overview) dene)
* [@Docs](/tr/context/@-symbols/@-docs) ile belgelere hızlı erişim
* Sözdizimi vurgulama
* Temel kod gezinme

Uygulamanı derlemen veya çalıştırman gerektiğinde sadece Xcode’a geç. Bu çalışma akışı, hata ayıklama ve dağıtım için alışık olduğun Xcode araçlarını kullanırken Cursor’ın yapay zekâ yeteneklerinden yararlanmak isteyen geliştiriciler için ideal.

<div id="hot-reloading">
  ### Hot Reloading
</div>

Xcode çalışma alanları veya projeleri kullanırken (Xcode’da bir klasörü doğrudan açmak yerine), Xcode bazen Cursor’da ya da genel olarak Xcode dışında yapılan dosya değişikliklerini görmezden gelebilir.

Bunu çözmek için klasörü Xcode’da açabilsen de, Swift geliştirme çalışma akışın için bir projeye ihtiyaç duyabilirsin.

Buna harika bir çözüm, Swift için bir hot reloading kütüphanesi olan ve uygulamanın değişiklikler yapılır yapılmaz gerçek zamanlı olarak “hot reload” edip güncellenmesini sağlayan [Inject](https://github.com/krzysztofzablocki/Inject)’i kullanmak. Bu yaklaşım, Xcode çalışma alanı/proje sorunlarının yan etkilerinden etkilenmez ve Cursor’da yaptığın değişikliklerin uygulamanda anında görünmesini sağlar.

<CardGroup cols={1}>
  <Card title="Inject - Swift için Hot Reloading" horizontal icon="fire" href="https://github.com/krzysztofzablocki/Inject">
    Inject hakkında daha fazla bilgi edin ve Swift projelerinde nasıl kullanacağını öğren.
  </Card>
</CardGroup>

<div id="advanced-swift-development">
  ## İleri Seviye Swift Geliştirme
</div>

<Note>
  Bu bölüm, [Thomas
  Ricouard](https://x.com/Dimillian) ve iOS geliştirme için Cursor kullanımıyla ilgili
  [makalesinden](https://dimillian.medium.com/how-to-use-cursor-for-ios-development-54b912c23941)
  büyük ölçüde ilham alınarak hazırlandı. Daha fazla ayrıntı için makalesine göz at ve daha fazla Swift içeriği için onu takip et.
</Note>

Aynı anda yalnızca tek bir editörü açık tutmak ve Xcode’la Cursor arasında gidip gelmekten kaçınmak istiyorsan, Cursor’ı doğrudan Xcode’un temel derleme sistemine entegre etmek için [Sweetpad](https://sweetpad.hyzyla.dev/) gibi bir uzantı kullanabilirsin.

Sweetpad, Xcode’un özelliklerinden ödün vermeden Swift projelerini doğrudan Cursor’da derlemeni, çalıştırmanı ve hata ayıklamanı sağlayan güçlü bir uzantıdır.

Sweetpad ile başlamadan önce, Mac’inde Xcode kurulu olmalı — Swift geliştirmenin temeli bu. Xcode’u [Mac App Store](https://apps.apple.com/us/app/xcode/id497799835) üzerinden indirebilirsin. Xcode’u kurduktan sonra Cursor’daki geliştirme deneyimini birkaç önemli araçla güçlendirelim.

Terminalini aç ve şunu çalıştır:

```bash  theme={null}

---

← Previous: [Python](./python.md) | [Index](./index.md) | Next: [JetBrains](./jetbrains.md) →