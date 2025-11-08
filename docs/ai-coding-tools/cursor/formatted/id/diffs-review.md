---
title: "Diffs & Review"
source: "https://docs.cursor.com/id/agent/review"
language: "id"
language_name: "Indonesian"
---

# Diffs & Review
Source: https://docs.cursor.com/id/agent/review

Tinjau dan kelola perubahan kode yang dihasilkan oleh agen AI

Saat Agent menghasilkan perubahan kode, perubahan tersebut ditampilkan dalam antarmuka review yang menandai penambahan dan penghapusan dengan baris berwarna. Ini memungkinkan kamu meninjau dan menentukan perubahan mana yang diterapkan ke codebase kamu.

Antarmuka review menampilkan perubahan kode dalam format diff yang familiar:

<div id="diffs">
  ## Diffs
</div>

<div className="full-width-table">
  | Type              | Meaning                         | Example                                                                                               |
  | :---------------- | :------------------------------ | :---------------------------------------------------------------------------------------------------- |
  | **Added lines**   | Penambahan kode baru            | <code className="bg-green-100 text-green-800 px-2 py-1 rounded">+ const newVariable = 'hello';</code> |
  | **Deleted lines** | Penghapusan kode                | <code className="bg-red-100 text-red-800 px-2 py-1 rounded">- const oldVariable = 'goodbye';</code>   |
  | **Context lines** | Kode konteks yang tidak berubah | <code className="bg-gray-100 text-gray-600 px-2 py-1 rounded"> function example() {}</code>           |
</div>

<div id="review">
  ## Review
</div>

Setelah proses generasi selesai, bakal muncul prompt buat nge-review semua perubahan sebelum lanjut. Ini ngasih gambaran umum tentang apa aja yang bakal diubah.

<Frame>
  <img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/review/input-review.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=10633167c76c24c1e69748ef93dc3888" alt="Antarmuka review input" data-og-width="2095" width="2095" data-og-height="1178" height="1178" data-path="images/chat/review/input-review.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/review/input-review.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=f462337898ca48f71cd2b570b140d30d 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/review/input-review.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=07c91dfc92110cce444da8bbf3d0b3b5 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/review/input-review.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=492522862dabae6243fa8d33f6fd77f2 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/review/input-review.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=c897e19ce7f508bad4e24fcf8efb2512 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/review/input-review.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=3956c2d2c5c9156181b19e262e301b5b 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/review/input-review.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=907f90b1db432128964a7f4e59523bb6 2500w" />
</Frame>

<div id="file-by-file">
  ### Per berkas
</div>

Bilah review mengambang bakal muncul di bagian bawah layar, bikin lo bisa:

* **Accept** atau **Reject** perubahan untuk berkas saat ini
* Pindah ke **next file** yang masih punya perubahan tertunda
  <Frame>
    <video src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/review/review-bar.mp4?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=5dca0fe7aba3c79e6760cb264821a617" autoPlay loop muted playsInline controls data-path="images/chat/review/review-bar.mp4">
      Browser lo nggak mendukung tag video.
    </video>
  </Frame>

<div id="selective-acceptance">
  ### Penerimaan selektif
</div>

Buat kontrol yang lebih detail:

* Buat nerima sebagian besar perubahan: tolak baris yang nggak diinginkan, lalu klik **Accept all**
* Buat nolak sebagian besar perubahan: terima baris yang diinginkan, lalu klik **Reject all**

<div id="review-changes">
  ## Tinjau perubahan
</div>

Di akhir respons agent, klik tombol **Tinjau perubahan** untuk melihat diff lengkap dari perubahan.

<Frame>
  <video src="https://www.cursor.com/changelog/049/review-ui.mp4" autoPlay loop muted playsInline controls />
</Frame>

---

← Previous: [Perencanaan](./perencanaan.md) | [Index](./index.md) | Next: [Terminal](./terminal.md) →