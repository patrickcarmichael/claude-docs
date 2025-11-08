---
title: "Bağlamla Çalışmak"
source: "https://docs.cursor.com/tr/guides/working-with-context"
language: "tr"
language_name: "Turkish"
---

# Bağlamla Çalışmak
Source: https://docs.cursor.com/tr/guides/working-with-context

Cursor'da bağlamla nasıl çalışılır

Önce, bağlam penceresi nedir? Ve Cursor’la verimli kod yazmayla nasıl ilişkili?

Biraz geniş açıdan bakarsak, büyük dil modeli (LLM), devasa veri kümelerinden kalıpları öğrenerek metin tahmin edip üreten bir yapay zeka modelidir. Girdini anlayıp daha önce gördüklerine dayanarak kod veya metin önererek Cursor gibi araçlara güç verir.

Token’lar bu modellerin giriş ve çıkışlarıdır. Bir LLM’nin tek tek işlediği, genellikle bir kelime parçası olan metin parçacıklarıdır. Modeller tüm cümleleri bir kerede okumaz; önceki token’lara bakarak bir sonrakini tahmin eder.

Bir metnin nasıl token’lara bölündüğünü görmek için [şu araç gibi bir tokenizer](https://tiktokenizer.vercel.app/) kullanabilirsin.

<img src="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/working-with-context/tokenizer.png?fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=29ce8eb4d2c29f254b3757304859d196" alt="Tokenizer" data-og-width="2048" width="2048" data-og-height="1259" height="1259" data-path="images/guides/working-with-context/tokenizer.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/working-with-context/tokenizer.png?w=280&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=4320774dd92cd5ac7c009a20df3c4a63 280w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/working-with-context/tokenizer.png?w=560&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=1a9f636c945c3b6a7d0b7a99408addb6 560w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/working-with-context/tokenizer.png?w=840&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=15c8d4e2cc11dd79179de20312e177cc 840w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/working-with-context/tokenizer.png?w=1100&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=551647ef3c0fa17f5b6bc0c998b9bd2e 1100w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/working-with-context/tokenizer.png?w=1650&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=b1be1180c2a9b94b7230e02d7b9be2ad 1650w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/working-with-context/tokenizer.png?w=2500&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=1af46c0197c8c23e6dbe913c44d90f08 2500w" />

<div id="what-is-context">
  # Bağlam nedir?
</div>

Cursor’da bir kod önerisi üretirken “bağlam”, modele sağlanan ("girdi token"ları şeklinde) ve modelin ardından ("çıktı token"ları şeklinde) sonraki bilgiyi tahmin etmek için kullandığı bilgiyi ifade eder.

İki tür bağlam vardır:

1. **Niyet bağlamı**, kullanıcının modelden ne elde etmek istediğini tanımlar. Örneğin, bir sistem istemi genellikle kullanıcının modelin nasıl davranmasını istediğine dair üst düzey talimatlar olarak kullanılır. Cursor’da yapılan "prompting"in çoğu niyet bağlamıdır. “Şu düğmeyi maviden yeşile çevir” ifade edilmiş niyete bir örnektir; yönlendiricidir.
2. **Durum bağlamı**, mevcut durumun kendisini açıklar. Cursor’a hata mesajları, konsol log’ları, görseller ve kod parçaları sağlamak durumla ilgili bağlam örnekleridir. Tanımlayıcıdır, yönerge vermez.

Bu iki bağlam türü birlikte, mevcut durumu ve istenen gelecekteki durumu tanımlayarak uyum içinde çalışır ve Cursor’ın işe yarar kod önerileri yapmasını sağlar.

```mermaid  theme={null}
flowchart LR
    A["Niyet (istediğin şey)"] --> C[Model]
    B["Durum (gerçek olan)"] --> C
    C -- Tahmin --> D["Eylem (yaptığı şey)"]
```

<div id="providing-context-in-cursor">
  # Cursor'da bağlam sağlama
</div>

Bir modele ne kadar ilgili bağlam sağlarsan, o kadar faydalı olur. Cursor’da yeterli bağlam verilmezse, model ilgili bilgi olmadan çözmeye çalışır. Bu genelde şunlarla sonuçlanır:

1. Modelin (ortada bir desen yokken) desen eşleştirmeye çalışıp halüsinasyon görmesi ve beklenmedik sonuçlar üretmesi. Bu, `claude-3.5-sonnet` gibi modellere yeterli bağlam verilmediğinde sık yaşanabilir.
2. Agent’ın kod tabanını arayarak, dosyaları okuyarak ve araçları çağırarak bağlamı kendi başına toplamaya çalışması. Güçlü muhakeme yeteneğine sahip bir model (örn. `claude-3.7-sonnet`) bu stratejiyle epey ilerleyebilir ve doğru başlangıç bağlamını vermek gidişatı belirler.

İyi haber şu ki Cursor, özünde bağlamsal farkındalıkla inşa edildi ve kullanıcıdan minimum müdahale gerektirecek şekilde tasarlandı. Cursor, modelin ilgili olduğunu tahmin ettiği kod tabanının parçalarını—mevcut dosya, diğer dosyalardaki semantik olarak benzer örüntüler ve oturumundan diğer bilgiler gibi—otomatik olarak içeri çeker.

Yine de çekilebilecek çok fazla bağlam var, o yüzden göreve ilgili olduğunu bildiğin bağlamı elle belirtmek, modelleri doğru yöne yönlendirmenin iyi bir yoludur.

<div id="symbol">
  ## @-sembolü
</div>

Açık bağlam vermenin en kolay yolu @-sembolünü kullanmak. Hangi dosyayı, klasörü, web sitesini ya da eklemek istediğin diğer bağlam parçasını özellikle bildiğinde harika. Ne kadar net olursan o kadar iyi. İşte bağlamı daha nokta atışı kullanmanın bir özeti:

| Sembol    | Örnek                | Kullanım durumu                                                                                                              | Dezavantaj                                                                        |
| --------- | -------------------- | ---------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| `@code`   | `@LRUCachedFunction` | Ürettiğin çıktıyla ilgili olan fonksiyonun, sabitin veya sembolün hangisi olduğunu biliyorsun                                | Kod tabanı hakkında çok fazla bilgi gerektirir                                    |
| `@file`   | `cache.ts`           | Hangi dosyanın okunması veya düzenlenmesi gerektiğini biliyorsun, ama dosyanın içinde tam olarak neresi olduğunu bilmiyorsun | Dosya boyutuna bağlı olarak eldeki görev için çok fazla ilgisiz bağlam içerebilir |
| `@folder` | `utils/`             | Bir klasördeki her şey veya dosyaların çoğu ilgili                                                                           | Eldeki görev için çok fazla ilgisiz bağlam içerebilir                             |

<img src="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/working-with-context/context-menu.png?fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=dd9cf0c3dc55465132421c7f4c63321a" alt="Context Menu" data-og-width="1956" width="1956" data-og-height="1266" height="1266" data-path="images/guides/working-with-context/context-menu.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/working-with-context/context-menu.png?w=280&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=bc3b241ff39cf6afd967f86dd8543dc6 280w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/working-with-context/context-menu.png?w=560&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=943522dab894b52ae922d0ba8d370f8e 560w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/working-with-context/context-menu.png?w=840&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=2fc3123a4388b5eab2b288e5c68301da 840w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/working-with-context/context-menu.png?w=1100&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=7ae7698ac325cab31376964994f7cecb 1100w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/working-with-context/context-menu.png?w=1650&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=04f2e442f95b59f2f11191b2f6f9222c 1650w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/working-with-context/context-menu.png?w=2500&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=d24a426d894174534501c6d0ddbbc5ba 2500w" />

<div id="rules">
  ## Kurallar
</div>

Kuralları, senin ya da ekibindeki diğer üyelerin erişebilmesini istediğin uzun vadeli bir bellek olarak düşün. İş akışları, biçimlendirme ve diğer teamüller de dahil olmak üzere alana özgü bağlamı yakalamak, kurallar yazmak için harika bir başlangıç noktasıdır.

Kurallar, `/Generate Cursor Rules` komutuyla mevcut konuşmalardan da oluşturulabilir. Eğer çok sayıda yönerge içeren uzun bir ileri-geri sohbet yaptıysan, muhtemelen daha sonra yeniden kullanmak isteyebileceğin bazı faydalı direktifler veya genel kurallar vardır.

<img src="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/working-with-context/rules.png?fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=7100fd32cff4f24b90910642cd96a31a" alt="Kurallar" data-og-width="2048" width="2048" data-og-height="1326" height="1326" data-path="images/guides/working-with-context/rules.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/working-with-context/rules.png?w=280&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=181822aa329fa5f575f502f91485411f 280w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/working-with-context/rules.png?w=560&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=e21ae2ff2794ad9a697cd87345670a9d 560w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/working-with-context/rules.png?w=840&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=c5a67c106c0846abb8c970feac85a463 840w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/working-with-context/rules.png?w=1100&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=84b6bcbea6d0950c2edf177a34e5398b 1100w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/working-with-context/rules.png?w=1650&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=682fca965fbaeac3e24b1aeadc22e5d1 1650w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/working-with-context/rules.png?w=2500&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=eb35dfa5784add7c1325429e797ed80f 2500w" />

<div id="mcp">
  ## MCP
</div>

[Model Context Protocol](https://modelcontextprotocol.io/introduction), Cursor’a eylemler gerçekleştirme ve harici bağlamı içeri alma yetenekleri kazandırabileceğin bir genişletilebilirlik katmanıdır.

Geliştirme kurulumuna bağlı olarak farklı türde sunuculardan yararlanmak isteyebilirsin, ancak özellikle faydalı olduğunu gördüğümüz iki kategori şunlar:

* **Dahili dokümantasyon**: ör. Notion, Confluence, Google Docs
* **Proje yönetimi**: ör. Linear, Jira

Bir API üzerinden bağlama erişmek ve eylemler gerçekleştirmek için mevcut araçların varsa, bunun için bir MCP sunucusu oluşturabilirsin. İşte [MCP sunucuları](https://modelcontextprotocol.io/tutorials/building-mcp-with-llms) oluşturma konusunda kısa bir rehber.

<img src="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/working-with-context/mcp.png?fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=220979c9c6d2d2df274f4e6569f36a65" alt="MCP" data-og-width="2048" width="2048" data-og-height="1326" height="1326" data-path="images/guides/working-with-context/mcp.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/working-with-context/mcp.png?w=280&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=109502940ebd0566ba4aae7973f4ee55 280w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/working-with-context/mcp.png?w=560&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=02b169068621a0260c13aaaebc85988f 560w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/working-with-context/mcp.png?w=840&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=5b78292cbc00f791ec4431130c289e2e 840w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/working-with-context/mcp.png?w=1100&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=2bb9323e56965bdfff44949847dae0ea 1100w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/working-with-context/mcp.png?w=1650&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=f0dc65099b6478a735e451cacdc3f2c3 1650w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/working-with-context/mcp.png?w=2500&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=b7865a098b75bccb25bb93d90e7232ac 2500w" />

<div id="self-gathering-context">
  ## Kendi kendine bağlam toplama
</div>

Birçok kullanıcının benimsediği güçlü bir kalıp, Agent’in daha fazla bağlam toplamak için çalıştırabileceği kısa ömürlü araçlar yazmasına izin vermek. Bu, kod çalıştırılmadan önce onu gözden aldığın insanın döngüde olduğu iş akışlarında özellikle etkili.

Örneğin, koduna hata ayıklama ifadeleri eklemek, kodu çalıştırmak ve modelin çıktıyı incelemesine izin vermek, statik olarak çıkaramayacağı dinamik bağlama erişmesini sağlar.

Python’da bunu Agent’i şu şekilde yönlendirerek yapabilirsin:

1. Kodun ilgili kısımlarına print("debugging: ...") ifadeleri ekle
2. Terminali kullanarak kodu veya testleri çalıştır

Agent terminal çıktısını okuyacak ve sırada ne yapılacağına karar verecek. Temel fikir, Agent’e yalnızca statik koda değil, gerçek çalışma zamanı davranışına erişim vermek.

<img src="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/working-with-context/self-gathering.png?fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=a90ba6d4d4f17148c95f3a4f0d6b382e" alt="Kendi Kendine Bağlam Toplama" data-og-width="2048" width="2048" data-og-height="1325" height="1325" data-path="images/guides/working-with-context/self-gathering.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/working-with-context/self-gathering.png?w=280&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=234f5240c4f4a74abeccd4d10d79df0b 280w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/working-with-context/self-gathering.png?w=560&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=dfa67903d8d44bbdcaa766533809fd21 560w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/working-with-context/self-gathering.png?w=840&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=ebe9b89eea9e2b942094e57105c79b94 840w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/working-with-context/self-gathering.png?w=1100&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=b4381b453dc4f852885f0229d189f131 1100w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/working-with-context/self-gathering.png?w=1650&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=c5981136bf7465465ac3cc0cc38c897e 1650w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/working-with-context/self-gathering.png?w=2500&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=132bc18e9994be819af3e24a22c7e814 2500w" />

<div id="takeaways">
  # Özetler
</div>

* Bağlam, etkili AI kodlamanın temelidir; niyet (ne istediğin) ve durumdan (ne mevcut) oluşur. İkisini de vermen, Cursor’ın doğru tahminler yapmasına yardımcı olur.
* Yalnızca otomatik bağlam toplamaya güvenmek yerine, Cursor’ı nokta atışı yönlendirmek için @-sembollerini (@code, @file, @folder) kullanarak cerrahi bağlam ver.
* Tekrarlanabilir bilgiyi ekip genelinde yeniden kullanılacak kurallara dök ve harici sistemlere bağlanmak için Model Context Protocol ile Cursor’ın yeteneklerini genişlet.
* Yetersiz bağlam halüsinasyonlara veya verimsizliğe yol açar; aşırı ve alakasız bağlam ise sinyali zayıflatır. En iyi sonuçlar için doğru dengeyi kur.

---

← Previous: [Web Geliştirme](./web-gelitirme.md) | [Index](./index.md) | Next: [Satır İçi Düzenleme](./satr-ii-dzenleme.md) →