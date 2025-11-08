---
title: "Bekerja dengan Konteks"
source: "https://docs.cursor.com/id/guides/working-with-context"
language: "id"
language_name: "Indonesian"
---

# Bekerja dengan Konteks
Source: https://docs.cursor.com/id/guides/working-with-context

Cara bekerja dengan konteks di Cursor

Pertama, apa itu context window? Dan gimana hubungannya dengan ngoding lebih efektif pakai Cursor?

Biar lihat gambaran besarnya dulu: large language model (LLM) adalah model AI yang dilatih buat memprediksi dan menghasilkan teks dengan belajar pola dari dataset yang sangat besar. Ini yang menggerakkan tool seperti Cursor dengan ngerti input kamu dan nyaranin kode atau teks berdasarkan yang pernah dilihat sebelumnya.

Token adalah input dan output dari model-model ini. Token berupa potongan teks, sering kali fragmen kata, yang diproses LLM satu per satu. Model nggak baca satu kalimat penuh sekaligus; mereka memprediksi token berikutnya berdasarkan token-token sebelumnya.

Buat lihat gimana sebuah teks di-tokenize, kamu bisa pakai tokenizer seperti [yang ini](https://tiktokenizer.vercel.app/).

<img src="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/working-with-context/tokenizer.png?fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=29ce8eb4d2c29f254b3757304859d196" alt="Tokenizer" data-og-width="2048" width="2048" data-og-height="1259" height="1259" data-path="images/guides/working-with-context/tokenizer.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/working-with-context/tokenizer.png?w=280&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=4320774dd92cd5ac7c009a20df3c4a63 280w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/working-with-context/tokenizer.png?w=560&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=1a9f636c945c3b6a7d0b7a99408addb6 560w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/working-with-context/tokenizer.png?w=840&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=15c8d4e2cc11dd79179de20312e177cc 840w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/working-with-context/tokenizer.png?w=1100&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=551647ef3c0fa17f5b6bc0c998b9bd2e 1100w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/working-with-context/tokenizer.png?w=1650&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=b1be1180c2a9b94b7230e02d7b9be2ad 1650w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/working-with-context/tokenizer.png?w=2500&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=1af46c0197c8c23e6dbe913c44d90f08 2500w" />

<div id="what-is-context">
  # Apa itu konteks?
</div>

Saat kita menghasilkan saran kode di Cursor, “konteks” mengacu pada informasi yang diberikan ke model (dalam bentuk "input tokens") yang kemudian dipakai model untuk memprediksi informasi berikutnya (dalam bentuk “output tokens”).

Ada dua jenis konteks:

1. **Konteks intent** menjelaskan apa yang user pengin dari model. Misalnya, system prompt biasanya berfungsi sebagai instruksi tingkat tinggi tentang gimana user pengin model berperilaku. Kebanyakan "prompting" yang dilakukan di Cursor adalah konteks intent. “Ubah tombol itu dari biru jadi hijau” adalah contoh intent yang dinyatakan; sifatnya preskriptif.
2. **Konteks state** menggambarkan keadaan dunia saat ini. Ngasih Cursor pesan error, log console, gambar, dan potongan kode adalah contoh konteks yang terkait dengan state. Ini deskriptif, bukan preskriptif.

Dua jenis konteks ini bekerja bareng dengan menggambarkan keadaan saat ini dan keadaan yang diinginkan ke depan, sehingga bantu Cursor ngasih saran coding yang berguna.

```mermaid  theme={null}
flowchart LR
    A["Intent (apa yang kamu mau)"] --> C[Model]
    B["State (apa yang benar)"] --> C
    C -- Memprediksi --> D["Aksi (apa yang dilakukannya)"]
```

<div id="providing-context-in-cursor">
  # Memberikan konteks di Cursor
</div>

Semakin relevan konteks yang kamu kasih ke model, semakin berguna hasilnya. Kalau konteks yang dikasih di Cursor kurang, model bakal coba nyelesain tanpa informasi yang relevan. Biasanya ini bikin:

1. Halusinasi, di mana model coba ngepasin pola (padahal nggak ada polanya) dan hasilnya jadi nggak terduga. Ini bisa sering kejadian di model kayak `claude-3.5-sonnet` kalau nggak dikasih konteks yang cukup.
2. Agent coba ngumpulin konteks sendiri dengan nyari di codebase, baca file, dan manggil tools. Model dengan kemampuan berpikir yang kuat (kayak `claude-3.7-sonnet`) bisa melangkah cukup jauh dengan strategi ini, dan ngasih konteks awal yang tepat bakal nentuin trajektorinya.

Kabar baiknya, Cursor dibangun dengan kesadaran konteks sebagai inti dan didesain supaya butuh intervensi minimal dari pengguna. Cursor otomatis narik bagian-bagian dari codebase kamu yang diperkirakan relevan oleh model, seperti file yang lagi kamu buka, pola yang secara semantik mirip di file lain, dan informasi lain dari sesi kamu.

Tapi karena ada banyak sumber konteks yang bisa ditarik, ngeset konteks secara manual yang kamu tahu relevan buat task itu cara yang efektif buat ngarahin model ke arah yang benar.

<div id="symbol">
  ## Simbol @
</div>

Cara paling gampang buat ngasih konteks eksplisit adalah pakai simbol @. Ini cocok kalau lo udah tahu persis file, folder, website, atau bagian konteks lain yang mau disertakan. Makin spesifik, makin bagus. Berikut rincian cara bikin konteks jadi lebih presisi:

| Symbol    | Example              | Use case                                                                                 | Drawback                                                                          |
| --------- | -------------------- | ---------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| `@code`   | `@LRUCachedFunction` | Lo tahu fungsi, konstanta, atau simbol mana yang relevan buat output yang lagi lo bikin  | Butuh banyak pengetahuan tentang codebase                                         |
| `@file`   | `cache.ts`           | Lo tahu file mana yang harus dibaca atau diedit, tapi belum pasti di bagian mana di file | Bisa nyertain banyak konteks yang nggak relevan buat tugas tergantung ukuran file |
| `@folder` | `utils/`             | Semua atau sebagian besar file di dalam satu folder relevan                              | Bisa nyertain banyak konteks yang nggak relevan buat tugas yang lagi dikerjain    |

<img src="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/working-with-context/context-menu.png?fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=dd9cf0c3dc55465132421c7f4c63321a" alt="Context Menu" data-og-width="1956" width="1956" data-og-height="1266" height="1266" data-path="images/guides/working-with-context/context-menu.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/working-with-context/context-menu.png?w=280&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=bc3b241ff39cf6afd967f86dd8543dc6 280w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/working-with-context/context-menu.png?w=560&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=943522dab894b52ae922d0ba8d370f8e 560w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/working-with-context/context-menu.png?w=840&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=2fc3123a4388b5eab2b288e5c68301da 840w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/working-with-context/context-menu.png?w=1100&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=7ae7698ac325cab31376964994f7cecb 1100w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/working-with-context/context-menu.png?w=1650&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=04f2e442f95b59f2f11191b2f6f9222c 1650w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/working-with-context/context-menu.png?w=2500&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=d24a426d894174534501c6d0ddbbc5ba 2500w" />

<div id="rules">
  ## Aturan
</div>

Anggap aturan sebagai memori jangka panjang yang pengin kamu atau anggota tim lain bisa akses. Menangkap konteks spesifik domain, termasuk alur kerja, pemformatan, dan konvensi lainnya, adalah titik awal yang bagus buat nulis aturan.

Aturan juga bisa dihasilkan dari percakapan yang sudah ada dengan pakai `/Generate Cursor Rules`. Kalau kamu punya percakapan panjang bolak-balik dengan banyak prompt, kemungkinan ada beberapa arahan atau aturan umum yang berguna yang mungkin pengin kamu pakai lagi nanti.

<img src="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/working-with-context/rules.png?fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=7100fd32cff4f24b90910642cd96a31a" alt="Rules" data-og-width="2048" width="2048" data-og-height="1326" height="1326" data-path="images/guides/working-with-context/rules.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/working-with-context/rules.png?w=280&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=181822aa329fa5f575f502f91485411f 280w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/working-with-context/rules.png?w=560&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=e21ae2ff2794ad9a697cd87345670a9d 560w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/working-with-context/rules.png?w=840&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=c5a67c106c0846abb8c970feac85a463 840w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/working-with-context/rules.png?w=1100&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=84b6bcbea6d0950c2edf177a34e5398b 1100w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/working-with-context/rules.png?w=1650&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=682fca965fbaeac3e24b1aeadc22e5d1 1650w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/working-with-context/rules.png?w=2500&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=eb35dfa5784add7c1325429e797ed80f 2500w" />

<div id="mcp">
  ## MCP
</div>

[Model Context Protocol](https://modelcontextprotocol.io/introduction) adalah lapisan ekstensi yang bikin Cursor bisa menjalankan aksi dan ngambil konteks eksternal.

Tergantung setup pengembangan lo, lo mungkin mau pakai tipe server yang berbeda, tapi dua kategori yang menurut kami paling berguna adalah:

* **Dokumentasi internal**: misalnya Notion, Confluence, Google Docs
* **Manajemen proyek**: misalnya Linear, Jira

Kalau lo sudah punya tooling buat ngakses konteks dan ngejalanin aksi lewat API, lo bisa bikin server MCP buat itu. Ini panduan singkat tentang cara bikin [server MCP](https://modelcontextprotocol.io/tutorials/building-mcp-with-llms).

<img src="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/working-with-context/mcp.png?fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=220979c9c6d2d2df274f4e6569f36a65" alt="MCP" data-og-width="2048" width="2048" data-og-height="1326" height="1326" data-path="images/guides/working-with-context/mcp.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/working-with-context/mcp.png?w=280&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=109502940ebd0566ba4aae7973f4ee55 280w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/working-with-context/mcp.png?w=560&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=02b169068621a0260c13aaaebc85988f 560w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/working-with-context/mcp.png?w=840&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=5b78292cbc00f791ec4431130c289e2e 840w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/working-with-context/mcp.png?w=1100&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=2bb9323e56965bdfff44949847dae0ea 1100w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/working-with-context/mcp.png?w=1650&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=f0dc65099b6478a735e451cacdc3f2c3 1650w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/working-with-context/mcp.png?w=2500&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=b7865a098b75bccb25bb93d90e7232ac 2500w" />

<div id="self-gathering-context">
  ## Mengumpulkan konteks secara mandiri
</div>

Salah satu pola ampuh yang banyak dipakai pengguna adalah membiarkan Agent menulis tool berumur pendek yang bisa dijalankan untuk mengumpulkan konteks tambahan. Ini khususnya efektif dalam alur kerja human-in-the-loop, di mana kamu meninjau kode sebelum dieksekusi.

Misalnya, menambahkan pernyataan debugging ke kodenmu, menjalankannya, dan membiarkan model memeriksa output memberi akses ke konteks dinamis yang nggak bisa disimpulkan secara statis.

Di Python, kamu bisa melakukan ini dengan meminta Agent untuk:

1. Menambahkan pernyataan print("debugging: ...") di bagian kode yang relevan
2. Menjalankan kode atau test menggunakan terminal

Agent akan membaca output terminal dan memutuskan langkah berikutnya. Inti idenya adalah memberi Agent akses ke perilaku saat runtime, bukan cuma kode statis.

<img src="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/working-with-context/self-gathering.png?fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=a90ba6d4d4f17148c95f3a4f0d6b382e" alt="Self-Gathering Context" data-og-width="2048" width="2048" data-og-height="1325" height="1325" data-path="images/guides/working-with-context/self-gathering.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/working-with-context/self-gathering.png?w=280&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=234f5240c4f4a74abeccd4d10d79df0b 280w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/working-with-context/self-gathering.png?w=560&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=dfa67903d8d44bbdcaa766533809fd21 560w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/working-with-context/self-gathering.png?w=840&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=ebe9b89eea9e2b942094e57105c79b94 840w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/working-with-context/self-gathering.png?w=1100&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=b4381b453dc4f852885f0229d189f131 1100w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/working-with-context/self-gathering.png?w=1650&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=c5981136bf7465465ac3cc0cc38c897e 1650w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/working-with-context/self-gathering.png?w=2500&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=132bc18e9994be819af3e24a22c7e814 2500w" />

<div id="takeaways">
  # Ringkasan
</div>

* Konteks adalah dasar coding AI yang efektif, terdiri dari intent (apa yang kamu inginkan) dan state (apa yang sudah ada). Memberikan keduanya membantu Cursor membuat prediksi yang akurat.
* Gunakan konteks yang presisi dengan simbol @ (@code, @file, @folder) untuk mengarahkan Cursor secara tepat, alih-alih hanya mengandalkan pengumpulan konteks otomatis.
* Tangkap pengetahuan yang bisa diulang dalam rules agar bisa dipakai seluruh tim, dan perluas kemampuan Cursor dengan Model Context Protocol untuk menghubungkan sistem eksternal.
* Konteks yang kurang memadai bisa memicu halusinasi atau inefisiensi, sementara terlalu banyak konteks yang tidak relevan akan mengaburkan sinyal. Temukan keseimbangan yang pas untuk hasil optimal.

---

← Previous: [Pengembangan Web](./pengembangan-web.md) | [Index](./index.md) | Next: [Edit Inline](./edit-inline.md) →