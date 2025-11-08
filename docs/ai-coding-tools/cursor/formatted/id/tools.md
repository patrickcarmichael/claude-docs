---
title: "Tools"
source: "https://docs.cursor.com/id/agent/tools"
language: "id"
language_name: "Indonesian"
---

# Tools
Source: https://docs.cursor.com/id/agent/tools

Tools yang tersedia untuk agen buat nyari, ngedit, dan ngejalanin kode

Daftar semua tools yang tersedia buat mode di dalam [Agent](/id/agent/overview), yang bisa lo aktifin atau nonaktifin waktu bikin [custom modes](/id/agent/modes#custom) lo sendiri.

<Note>
  Nggak ada batas jumlah panggilan tool yang bisa dilakukan Agent selama suatu tugas. Agent bakal terus pakai tools sesuai kebutuhan sampai permintaan lo kelar.
</Note>

<div id="search">
  ## Pencarian
</div>

Alat untuk menelusuri codebase dan web demi menemukan informasi yang relevan.

<AccordionGroup>
  <Accordion title="Read File" icon="file-lines">
    Membaca hingga 250 baris (750 dalam mode maksimum) dari sebuah file.
  </Accordion>

  <Accordion title="List Directory" icon="folder-open">
    Membaca struktur direktori tanpa membaca isi file.
  </Accordion>

  <Accordion title="Codebase" icon="database">
    Melakukan pencarian semantik dalam [codebase
    yang terindeks](/id/context/codebase-indexing).
  </Accordion>

  <Accordion title="Grep" icon="magnifying-glass">
    Mencari kata kunci atau pola yang persis di dalam file.
  </Accordion>

  <Accordion title="Search Files" icon="file-magnifying-glass">
    Menemukan file berdasarkan nama menggunakan fuzzy matching.
  </Accordion>

  <Accordion title="Web" icon="globe">
    Membuat kueri pencarian dan melakukan penelusuran web.
  </Accordion>

  <Accordion title="Fetch Rules" icon="gavel">
    Mengambil [rules](/id/context/rules) tertentu berdasarkan tipe dan deskripsinya.
  </Accordion>
</AccordionGroup>

<div id="edit">
  ## Edit
</div>

Alat buat ngelakuin edit spesifik ke file dan codebase lo.

<AccordionGroup>
  <Accordion title="Edit & Reapply" icon="pencil">
    Ngasih saran edit ke file dan [nge-apply](/id/agent/apply) secara otomatis.
  </Accordion>

  <Accordion title="Delete File" icon="trash">
    Hapus file secara otomatis (bisa dimatiin di settings).
  </Accordion>
</AccordionGroup>

<div id="run">
  ## Run
</div>

Chat bisa berinteraksi langsung dengan terminal lo.

<AccordionGroup>
  <Accordion title="Terminal" icon="terminal">
    Jalanin perintah terminal dan pantau output-nya.
  </Accordion>
</AccordionGroup>

<Note>Secara default, Cursor bakal pakai profil terminal pertama yang tersedia.</Note>

Buat ngatur profil terminal yang lo pengin:

1. Buka Command Palette (`Cmd/Ctrl+Shift+P`)
2. Cari "Terminal: Select Default Profile"
3. Pilih profil yang lo mau

<div id="mcp">
  ## MCP
</div>

Chat bisa pakai server MCP yang sudah dikonfigurasi buat berinteraksi dengan layanan eksternal, seperti database atau API pihak ketiga.

<AccordionGroup>
  <Accordion title="Toggle MCP Servers" icon="server">
    Nyalakan/nonaktifkan server MCP yang tersedia. Mengikuti konfigurasi auto-run.
  </Accordion>
</AccordionGroup>

Pelajari lebih lanjut tentang [Model Context Protocol](/id/context/model-context-protocol) dan jelajahi server yang tersedia di [direktori MCP](/id/tools).

<div id="advanced-options">
  ## Opsi lanjutan
</div>

<AccordionGroup>
  <Accordion title="Auto-apply Edits" icon="check">
    Terapkan perubahan secara otomatis tanpa konfirmasi manual.
  </Accordion>

  <Accordion title="Auto-run" icon="play">
    Jalankan perintah terminal dan terima perubahan secara otomatis. Berguna untuk menjalankan test suite dan memverifikasi perubahan.

    <Frame>
      <img src="https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=3135722076a5aa636d27dbedec665bae" data-og-width="1624" width="1624" data-og-height="1012" height="1012" data-path="images/agent/auto-run.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=280&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=9f2e2bed8f634201adc51ccb2bd96cd2 280w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=560&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=51704cac2f270a04856fffbeaccf9700 560w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=840&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=01a5034975497a8dff4f41dca0d19f2e 840w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=1100&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=5f19026a0c6e5fb28c935ce795edb706 1100w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=1650&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=a108fc86f8ee7c0db6e5b7ab80ede738 1650w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=2500&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=9ce5f45879c29049640bb5a1494db11e 2500w" />
    </Frame>
  </Accordion>

  <Accordion title="Guardrails" icon="shield">
    Konfigurasikan allow list untuk menentukan tool mana yang boleh berjalan otomatis. Allow list meningkatkan keamanan dengan secara eksplisit mendefinisikan operasi yang diizinkan.
  </Accordion>

  <Accordion title="Auto-fix Errors" icon="wrench">
    Secara otomatis memperbaiki error dan peringatan linter saat ditemui oleh Agent.
  </Accordion>
</AccordionGroup>

---

← Previous: [Terminal](./terminal.md) | [Index](./index.md) | Next: [Agen Latar Belakang](./agen-latar-belakang.md) →