---
title: "Diagram Arsitektur"
source: "https://docs.cursor.com/id/guides/tutorials/architectural-diagrams"
language: "id"
language_name: "Indonesian"
---

# Diagram Arsitektur
Source: https://docs.cursor.com/id/guides/tutorials/architectural-diagrams

Pelajari cara bikin diagram arsitektur pakai Mermaid untuk memvisualisasikan struktur sistem dan alur data

Diagram arsitektur bantu lo ngeh gimana sistem lo bekerja. Lo bisa pakai ini buat ngeksplor logika, ngelacak data, dan ngejelasin struktur. Cursor dukung bikin diagram ini langsung pakai tool kayak Mermaid, jadi lo bisa dari kode ke visual cuma dalam beberapa prompt.

<Frame>
  <img alt="Contoh diagram arsitektur" src="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/tutorials/architectural-diagrams/postgres-flowchart.png?fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=3d8dcd292e919c4640c03456a0959057" data-og-width="2048" width="2048" data-og-height="1326" height="1326" data-path="images/guides/tutorials/architectural-diagrams/postgres-flowchart.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/tutorials/architectural-diagrams/postgres-flowchart.png?w=280&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=b95ed20c23aff9fccf62cd209e817719 280w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/tutorials/architectural-diagrams/postgres-flowchart.png?w=560&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=bdb7d7390be1d8d71a1b560a4fc892ca 560w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/tutorials/architectural-diagrams/postgres-flowchart.png?w=840&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=b171506e9be3be4845966f61515c09de 840w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/tutorials/architectural-diagrams/postgres-flowchart.png?w=1100&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=aeaee70dede56db5b6c6dc92df7ba19e 1100w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/tutorials/architectural-diagrams/postgres-flowchart.png?w=1650&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=89513a2959f659f60f06c68891f89d45 1650w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/tutorials/architectural-diagrams/postgres-flowchart.png?w=2500&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=bdaf6ee66520c0e8b8b53b60f66f0b86 2500w" />
</Frame>

<div id="why-diagrams-matter">
  ## Kenapa diagram penting
</div>

Diagram ngebantu ngejelasin gimana data ngalir dan gimana komponen saling berinteraksi. Diagram berguna ketika lo:

* Pengen ngerti flow control di codebase lo
* Perlu ngelacak data lineage dari input sampai output
* Lagi onboarding orang lain atau lagi mendokumentasikan sistem lo

Diagram juga kece buat debugging dan ngebantu lo nanya pertanyaan yang lebih cerdas. Visual ngebantu lo (dan model) ngeliat gambaran besar.

<div id="two-dimensions-to-consider">
  ## Dua dimensi yang perlu dipertimbangkan
</div>

Ada beberapa sudut pandang yang bisa kamu ambil:

* **Tujuan**: Kamu lagi memetakan logika, alur data, infrastruktur, atau yang lain?
* **Format**: Kamu butuh yang cepat (misalnya diagram Mermaid) atau yang formal (seperti UML)?

<div id="how-to-prompt">
  ## Cara membuat prompt
</div>

Mulai dengan tujuan yang jelas. Berikut beberapa cara umum buat nanya:

* **Alur eksekusi**: "Tunjukin gimana request jalan dari controller ke database."
* **Asal-usul data (data lineage)**: "Lacak variabel ini dari titik masuk sampai ke tujuan akhirnya."
* **Struktur**: "Kasih gue view per komponen dari service ini."

Lo bisa tentuin titik awal dan akhir, atau minta Cursor buat nemuin jalur lengkapnya.

<div id="working-with-mermaid">
  ## Bekerja dengan Mermaid
</div>

Mermaid mudah dipelajari dan bisa dirender langsung di Markdown (dengan ekstensi yang tepat). Cursor bisa menghasilkan diagram seperti:

* `flowchart` untuk logika dan alur
* `sequenceDiagram` untuk interaksi
* `classDiagram` untuk struktur objek
* `graph TD` untuk peta berarah sederhana

```mermaid  theme={null}
sequenceDiagram
    participant User
    participant Server
    participant Database

    User->>Server: Kirim Formulir
    Server->>Database: Simpan Entri
    Database-->>Server: Berhasil
    Server-->>User: Konfirmasi

```

Kamu bisa pasang [ekstensi Mermaid](https://marketplace.cursorapi.com/items?itemName=bierner.markdown-mermaid) buat nge-preview diagram.

1. Buka tab Extensions
2. Cari Mermaid
3. Pasang

<Frame>
  <img alt="Menginstal ekstensi Mermaid" src="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/tutorials/architectural-diagrams/installing-mermaid.png?fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=8d5ee8d972dcc3d3789696a6d383efe6" data-og-width="1365" width="1365" data-og-height="884" height="884" data-path="images/guides/tutorials/architectural-diagrams/installing-mermaid.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/tutorials/architectural-diagrams/installing-mermaid.png?w=280&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=bcb03e9519816da6bf4a8220fea8a319 280w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/tutorials/architectural-diagrams/installing-mermaid.png?w=560&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=52805242ed097f948b7da2b078c9ee02 560w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/tutorials/architectural-diagrams/installing-mermaid.png?w=840&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=5e2405e72459b4c099be1b3439b2bbd9 840w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/tutorials/architectural-diagrams/installing-mermaid.png?w=1100&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=296d1022a39afa4b2016425347901452 1100w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/tutorials/architectural-diagrams/installing-mermaid.png?w=1650&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=88bdac627e50291bb0550eb9313f8d1f 1650w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/tutorials/architectural-diagrams/installing-mermaid.png?w=2500&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=a9d3d7539bf41b023f1d53d68abc2dea 2500w" />
</Frame>

<div id="diagram-strategy">
  ## Strategi diagram
</div>

Mulai kecil dulu. Jangan coba memetakan semuanya sekaligus.

* Pilih satu fungsi, rute, atau proses
* Minta Cursor membuat diagram bagian itu dengan Mermaid
* Setelah kamu punya beberapa, minta untuk menggabungkannya

Ini selaras dengan **model C4** – kamu mulai dari level rendah (kode atau komponen) lalu naik ke ringkasan level yang lebih tinggi.

<div id="recommended-flow">
  ### Alur yang direkomendasikan
</div>

1. Mulai dengan diagram detail level rendah
2. Ringkas jadi tampilan level menengah
3. Ulangi sampai mencapai tingkat abstraksi yang kamu inginkan
4. Minta Cursor menggabungkannya jadi satu diagram atau peta sistem

```mermaid  theme={null}
graph TD
    subgraph Level 1: Komponen tingkat rendah
        A1[AuthService] --> A2[TokenValidator]
        A1 --> A3[UserDB]
        B1[PaymentService] --> B2[BillingEngine]
        B1 --> B3[InvoiceDB]
    end

    subgraph Level 2: Sistem tingkat menengah
        A[Sistem Pengguna] --> A1
        B[Sistem Penagihan] --> B1
    end

    subgraph Level 3: Aplikasi tingkat tinggi
        App[Aplikasi Utama] --> A
        App --> B
    end

```

<div id="takeaways">
  ## Ringkasan
</div>

* Gunakan diagram untuk memahami alur, logika, dan data
* Mulai dengan prompt kecil dan kembangkan diagram dari sana
* Mermaid adalah format yang paling mudah digunakan di Cursor
* Mulai dari level rendah lalu naikkan abstraksinya, seperti di model C4
* Cursor bisa bantu kamu membuat, menyempurnakan, dan menggabungkan diagram dengan mudah

---

← Previous: [VS Code](./vs-code.md) | [Index](./index.md) | Next: [Membangun Server MCP](./membangun-server-mcp.md) →