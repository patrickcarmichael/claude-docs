---
title: "Diff’ler & İnceleme"
source: "https://docs.cursor.com/tr/agent/review"
language: "tr"
language_name: "Turkish"
---

# Diff’ler & İnceleme
Source: https://docs.cursor.com/tr/agent/review

AI ajanının oluşturduğu kod değişikliklerini incele ve yönet

Agent kod değişiklikleri oluşturduğunda, eklemeleri ve silmeleri renk kodlu satırlarla gösteren bir inceleme arayüzünde sunulur. Bu, kod tabanına hangi değişiklikleri uygulayacağını incelemene ve kontrol etmene olanak tanır.

İnceleme arayüzü, kod değişikliklerini tanıdık bir diff formatında gösterir:

<div id="diffs">
  ## Farklar
</div>

<div className="full-width-table">
  | Tür               | Anlam                          | Örnek                                                                                                 |
  | :---------------- | :----------------------------- | :---------------------------------------------------------------------------------------------------- |
  | **Added lines**   | Yeni eklenen kod satırları     | <code className="bg-green-100 text-green-800 px-2 py-1 rounded">+ const newVariable = 'hello';</code> |
  | **Deleted lines** | Silinen kod satırları          | <code className="bg-red-100 text-red-800 px-2 py-1 rounded">- const oldVariable = 'goodbye';</code>   |
  | **Context lines** | Değişmeyen çevreleyen satırlar | <code className="bg-gray-100 text-gray-600 px-2 py-1 rounded"> function example() {}</code>           |
</div>

<div id="review">
  ## İnceleme
</div>

Oluşturma tamamlandıktan sonra, devam etmeden önce tüm değişiklikleri gözden geçirmen için bir istem göreceksin. Bu, nelerin değiştirileceğine dair genel bir bakış sunar.

<Frame>
  <img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/review/input-review.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=10633167c76c24c1e69748ef93dc3888" alt="Girdi inceleme arayüzü" data-og-width="2095" width="2095" data-og-height="1178" height="1178" data-path="images/chat/review/input-review.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/review/input-review.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=f462337898ca48f71cd2b570b140d30d 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/review/input-review.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=07c91dfc92110cce444da8bbf3d0b3b5 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/review/input-review.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=492522862dabae6243fa8d33f6fd77f2 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/review/input-review.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=c897e19ce7f508bad4e24fcf8efb2512 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/review/input-review.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=3956c2d2c5c9156181b19e262e301b5b 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/review/input-review.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=907f90b1db432128964a7f4e59523bb6 2500w" />
</Frame>

<div id="file-by-file">
  ### Dosya dosya
</div>

Ekranın altında kayan bir inceleme çubuğu belirir ve şunları yapmana olanak tanır:

* Geçerli dosyadaki değişiklikleri **kabul et** veya **reddet**
* Bekleyen değişiklikleri olan **sonraki dosyaya** git
  <Frame>
    <video src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/review/review-bar.mp4?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=5dca0fe7aba3c79e6760cb264821a617" autoPlay loop muted playsInline controls data-path="images/chat/review/review-bar.mp4">
      Tarayıcın video etiketini desteklemiyor.
    </video>
  </Frame>

<div id="selective-acceptance">
  ### Seçimli kabul
</div>

Daha ince ayarlı kontrol için:

* Çoğu değişikliği kabul etmek için: istemediğin satırları reddet, ardından **Tümünü kabul et**’e tıkla
* Çoğu değişikliği reddetmek için: istediğin satırları kabul et, ardından **Tümünü reddet**’e tıkla

<div id="review-changes">
  ## Değişiklikleri gözden geçir
</div>

Agent yanıtının sonunda, yapılan değişikliklerin tüm diff’ini görmek için **Değişiklikleri gözden geçir** düğmesine tıkla.

<Frame>
  <video src="https://www.cursor.com/changelog/049/review-ui.mp4" autoPlay loop muted playsInline controls />
</Frame>

---

← Previous: [Planlama](./planlama.md) | [Index](./index.md) | Next: [Terminal](./terminal.md) →