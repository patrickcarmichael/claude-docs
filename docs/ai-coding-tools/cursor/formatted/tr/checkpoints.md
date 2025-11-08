---
title: "Checkpoints"
source: "https://docs.cursor.com/tr/agent/chat/checkpoints"
language: "tr"
language_name: "Turkish"
---

# Checkpoints
Source: https://docs.cursor.com/tr/agent/chat/checkpoints

Agent değişikliklerinden sonra önceki durumları kaydet ve geri yükle

Checkpoints, Agent'in kod tabanında yaptığı değişikliklerin otomatik anlık görüntüleridir. Gerekirse Agent’in yaptığı değişiklikleri geri almanı sağlar.

<Frame>
  <video src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/restore-checkpoint.mp4?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=7cededf7892f15a6342a81953ea0aa38" autoPlay loop muted playsInline controls data-path="images/chat/restore-checkpoint.mp4" />
</Frame>

<div id="restoring-checkpoints">
  ## Checkpoint’leri geri yükleme
</div>

Geri yüklemenin iki yolu var:

1. **Girdi kutusundan**: Önceki isteklerde `Restore Checkpoint` düğmesine tıkla
2. **Mesajdan**: Bir mesajın üzerine geldiğinde + düğmesine tıkla

<Warning>
  Checkpoint’ler sürüm kontrolü değildir. Kalıcı geçmiş için Git kullan.
</Warning>

<div id="how-they-work">
  ## Nasıl çalışır
</div>

* Yerelde saklanır, Git’ten ayrı
* Yalnızca Agent değişikliklerini izler (manuel düzenlemeleri değil)
* Otomatik olarak temizlenir

<Note>
  Manuel düzenlemeler izlenmez. Checkpoint’leri sadece Agent değişiklikleri için kullan.
</Note>

<div id="faq">
  ## SSS
</div>

<AccordionGroup>
  <Accordion title="Kontrol noktaları Git'i etkiler mi?">
    Hayır. Git geçmişinden bağımsızdır.
  </Accordion>

  {" "}

  <Accordion title="Ne kadar süre saklanır?">
    Geçerli oturum ve yakın geçmiş için. Otomatik olarak temizlenir.
  </Accordion>

  <Accordion title="Bunları elle oluşturabilir miyim?">
    Hayır. Cursor bunları otomatik olarak oluşturur.
  </Accordion>
</AccordionGroup>

{" "}

---

← Previous: [Uygula](./uygula.md) | [Index](./index.md) | Next: [Komutlar](./komutlar.md) →