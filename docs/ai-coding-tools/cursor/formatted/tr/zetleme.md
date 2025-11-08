---
title: "Özetleme"
source: "https://docs.cursor.com/tr/agent/chat/summarization"
language: "tr"
language_name: "Turkish"
---

# Özetleme
Source: https://docs.cursor.com/tr/agent/chat/summarization

Sohbette uzun konuşmalar için bağlam yönetimi

<div id="message-summarization">
  ## Mesaj özetleme
</div>

Sohbetler uzadıkça, Cursor sohbetlerini verimli tutmak için bağlamı otomatik olarak özetleyip yönetir. Bağlam menüsünü nasıl kullanacağını ve dosyaların modelin bağlam pencerelerine sığması için nasıl yoğunlaştırıldığını öğren.

<div id="using-the-summarize-command">
  ### /summarize komutunu kullanma
</div>

Sohbette `/summarize` komutunu kullanarak özetlemeyi manuel olarak tetikleyebilirsin. Bu komut, konuşmalar çok uzadığında bağlamı yönetmene yardımcı olur; böylece önemli bilgileri kaybetmeden verimli şekilde çalışmaya devam edebilirsin.

<Info>
  Cursor'da bağlamın nasıl çalıştığını daha ayrıntılı öğrenmek için [Working with
  Context](/tr/guides/working-with-context) rehberimize göz at.
</Info>

<div id="how-summarization-works">
  ### Özetleme nasıl çalışır
</div>

Sohbet uzadıkça, modelin bağlam penceresi sınırını aşabilir:

<Frame>
  <div className="font-mono text-xs w-full bg-neutral-100 p-4 rounded-lg">
    <div className="relative">
      <div className="bg-white px-3 py-2 mb-2 rounded border border-dashed border-neutral-400 w-full">
        <div className="text-xs text-neutral-700 font-medium">User</div>
      </div>

      <div className="bg-white px-3 py-2 mb-2 rounded border border-dashed border-neutral-400 w-full">
        <div className="text-xs text-neutral-700 font-medium">Cursor</div>
      </div>

      <div className="bg-white px-3 py-2 mb-2 rounded border border-dashed border-neutral-400 w-full">
        <div className="text-xs text-neutral-700 font-medium">User</div>
      </div>

      <div className="relative my-4">
        <div className="absolute top-0 left-1/2 transform -translate-x-1/2 -translate-y-1/2 text-center text-xs text-black bg-neutral-100 px-2">Bağlam penceresi sınırı</div>

        <div className="w-full h-px bg-black" />
      </div>

      <div className="bg-white px-3 py-2 mb-2 rounded border border-neutral-400 w-full">
        <div className="text-xs text-neutral-700 font-medium">Cursor</div>
      </div>

      <div className="bg-white px-3 py-2 mb-2 rounded border border-neutral-400 w-full">
        <div className="text-xs text-neutral-700 font-medium">User</div>
      </div>

      <div className="bg-white px-3 py-2 mb-2 rounded border border-neutral-400 w-full">
        <div className="text-xs text-neutral-700 font-medium">Cursor</div>
      </div>
    </div>
  </div>
</Frame>

Bunu aşmak için Cursor, yeni mesajlara yer açmak amacıyla eski mesajları özetler.

<Frame>
  <div className="font-mono text-xs w-full bg-neutral-100 p-4 rounded-lg">
    <div className="relative">
      <div className="relative my-4">
        <div className="absolute top-0 left-1/2 transform -translate-x-1/2 -translate-y-1/2 text-center text-xs text-black bg-neutral-100 px-2">
          Bağlam penceresi sınırı
        </div>

        <div className="w-full h-px bg-black" />
      </div>

      <div className="bg-neutral-100 px-3 py-2 mb-2 rounded border border-dashed border-neutral-400 w-full">
        <div className="text-xs text-neutral-700 font-medium">
          Özetlenen Mesajlar
        </div>
      </div>

      <div className="bg-white px-3 py-2 mb-2 rounded border border-neutral-400 w-full">
        <div className="text-xs text-neutral-700 font-medium">Cursor</div>
      </div>

      <div className="bg-white px-3 py-2 mb-2 rounded border border-neutral-400 w-full">
        <div className="text-xs text-neutral-700 font-medium">User</div>
      </div>

      <div className="bg-white px-3 py-2 mb-2 rounded border border-neutral-400 w-full">
        <div className="text-xs text-neutral-700 font-medium">Cursor</div>
      </div>
    </div>
  </div>
</Frame>

<div id="file-folder-condensation">
  ## Dosya ve klasör yoğunlaştırma
</div>

Sohbet özetleme uzun konuşmaları ele alırken, Cursor büyük dosya ve klasörleri yönetmek için farklı bir strateji kullanır: **akıllı yoğunlaştırma**. Sohbetine dosya eklediğinde, Cursor bunları boyutlarına ve kullanılabilir bağlam alanına göre sunmanın en iyi yolunu belirler.

Bir dosya/klasörün alabileceği farklı durumlar şunlardır:

<div id="condensed">
  ### Özetlenmiş
</div>

Dosya veya klasörler bağlam penceresine sığmayacak kadar büyük olduğunda, Cursor bunları otomatik olarak özetler. Özetleme, modele işlev imzaları, sınıflar ve yöntemler gibi temel yapısal öğeleri gösterir. Bu özet görünümden model, gerekirse belirli dosyaları genişletmeyi seçebilir. Bu yaklaşım, mevcut bağlam penceresinin etkin kullanımını en üst düzeye çıkarır.

<Frame>
  <img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/context-management/condensed.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=0c3a07b6fef6402945138f7ee38b44c1" alt="Bağlam menüsü" data-og-width="1226" width="1226" data-og-height="793" height="793" data-path="images/context/context-management/condensed.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/context-management/condensed.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=4cc08626f9cfce1d186cdd6aa96c7d09 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/context-management/condensed.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=fa49ce9605bdb0186c98712f4c0a32cc 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/context-management/condensed.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=84874b2f40bff0a2cd54796865469914 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/context-management/condensed.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=050290a85c154e92f9298883afcdf892 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/context-management/condensed.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=f953aa28f11926b2d6fdf734cf928402 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/context-management/condensed.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=50aa9973ccf2027814860f3d97a2b031 2500w" />
</Frame>

<div id="significantly-condensed">
  ### Önemli ölçüde kısaltıldı
</div>

Bir dosya adı "Önemli ölçüde kısaltıldı" etiketini taşıyorsa, dosya tam hâliyle, hatta kısaltılmış biçimde bile dahil edilemeyecek kadar büyüktü. Modele yalnızca dosya adı gösterilecek.

<div id="not-included">
  ### Kapsama alınmadı
</div>

Bir dosya veya klasörün yanında bir uyarı simgesi belirdiğinde, öğe, yoğunlaştırılmış biçimde bile bağlam penceresine sığmayacak kadar büyük demektir. Bu, kod tabanının hangi kısımlarının modele erişilebilir olduğunu anlamana yardımcı olur.

<Frame>
  <img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/context-management/not-included.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=06df9854c74c257d1ceb7d18b1864ceb" alt="Context menu" data-og-width="1090" width="1090" data-og-height="346" height="346" data-path="images/context/context-management/not-included.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/context-management/not-included.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=072e75878f27a151f1310007d0e5e534 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/context-management/not-included.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=c6f3f71351ddf8e367096651b455bf9d 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/context-management/not-included.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=c407f7870412007549f8eb2871f9ca12 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/context-management/not-included.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=b0d17023b5734c8d7584c56f5419bd1a 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/context-management/not-included.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=f1bedff398cee6c957fe62877f7d2012 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/context-management/not-included.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=8b00fbaff658c384f69bfddf3f3a4cfe 2500w" />
</Frame>

---

← Previous: [Geçmiş](./gemi.md) | [Index](./index.md) | Next: [Sekmeler](./sekmeler.md) →