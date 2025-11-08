---
title: "Checkpoints"
source: "https://docs.cursor.com/id/agent/chat/checkpoints"
language: "id"
language_name: "Indonesian"
---

# Checkpoints
Source: https://docs.cursor.com/id/agent/chat/checkpoints

Simpan dan pulihkan state sebelumnya setelah perubahan Agent

Checkpoints adalah snapshot otomatis dari perubahan Agent ke codebase lo. Fitur ini bikin lo bisa nge-undo modifikasi Agent kalau perlu.

<Frame>
  <video src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/restore-checkpoint.mp4?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=7cededf7892f15a6342a81953ea0aa38" autoPlay loop muted playsInline controls data-path="images/chat/restore-checkpoint.mp4" />
</Frame>

<div id="restoring-checkpoints">
  ## Memulihkan checkpoint
</div>

Ada dua cara untuk memulihkan:

1. **Dari kotak input**: Klik tombol `Restore Checkpoint` pada permintaan sebelumnya
2. **Dari pesan**: Klik tombol + saat mengarahkan kursor ke sebuah pesan

<Warning>
  Checkpoint bukan sistem version control. Pakai Git untuk riwayat permanen.
</Warning>

<div id="how-they-work">
  ## Cara kerjanya
</div>

* Disimpan secara lokal, terpisah dari Git
* Hanya melacak perubahan Agent (bukan edit manual)
* Dibersihkan secara otomatis

<Note>
  Edit manual nggak dilacak. Pakai checkpoint cuma untuk perubahan Agent.
</Note>

<div id="faq">
  ## FAQ
</div>

<AccordionGroup>
  <Accordion title="Apakah checkpoint berpengaruh ke Git?">
    Nggak. Mereka terpisah dari riwayat Git.
  </Accordion>

  {" "}

  <Accordion title="Berapa lama disimpan?">
    Buat sesi saat ini dan riwayat terbaru. Dibersihkan otomatis.
  </Accordion>

  <Accordion title="Bisa bikin manual?">
    Nggak. Mereka dibuat otomatis oleh Cursor.
  </Accordion>
</AccordionGroup>

{" "}

---

← Previous: [Apply](./apply.md) | [Index](./index.md) | Next: [Perintah](./perintah.md) →