---
title: "API Keys"
source: "https://docs.cursor.com/id/settings/api-keys"
language: "id"
language_name: "Indonesian"
---

# API Keys
Source: https://docs.cursor.com/id/settings/api-keys

Pakai penyedia LLM pilihanmu

Pakai API key kamu untuk ngirim pesan AI tanpa batas dengan biaya sendiri. Setelah disetel, Cursor bakal pakai API key kamu buat manggil penyedia LLM secara langsung.

Buat pakai API key, buka `Cursor Settings` > `Models` dan masukin API key kamu. Klik **Verify**. Setelah tervalidasi, API key kamu aktif.

<Warning>
  API key kustom cuma berfungsi dengan model chat standar. Fitur yang butuh model khusus (kayak Tab Completion) bakal tetap pakai model bawaan Cursor.
</Warning>

<div id="supported-providers">
  ## Penyedia yang didukung
</div>

* **OpenAI** - Hanya model chat standar, non-reasoning. Pemilih model akan menampilkan model OpenAI yang tersedia.
* **Anthropic** - Semua model Claude yang tersedia melalui Anthropic API.
* **Google** - Model Gemini yang tersedia melalui Google AI API.
* **Azure OpenAI** - Model yang dideploy di instance Azure OpenAI Service kamu.
* **AWS Bedrock** - Gunakan AWS access key, secret key, atau IAM role. Berfungsi dengan model yang tersedia dalam konfigurasi Bedrock kamu.

Sebuah external ID unik akan dihasilkan setelah IAM role Bedrock kamu tervalidasi, yang bisa kamu tambahkan ke IAM role trust policy untuk keamanan tambahan.

<div id="faq">
  ## FAQ
</div>

<AccordionGroup>
  <Accordion title="Apakah kunci API-ku akan disimpan atau keluar dari perangkatku?">
    Kunci API-ku nggak disimpan, tapi dikirim ke server kami di setiap request. Semua request dialihkan lewat backend kami untuk penyusunan prompt final.
  </Accordion>
</AccordionGroup>

---

← Previous: [Model](./model.md) | [Index](./index.md) | Next: [Tab](./tab.md) →