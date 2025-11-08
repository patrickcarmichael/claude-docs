---
title: "Analytics"
source: "https://docs.cursor.com/tr/account/teams/analytics"
language: "tr"
language_name: "Turkish"
---

# Analytics
Source: https://docs.cursor.com/tr/account/teams/analytics

Takım kullanımını ve etkinlik metriklerini takip et

Takım adminleri metrikleri [dashboard](/tr/account/teams/dashboard) üzerinden takip edebilir.

<Frame>
  <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/analytics.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=a8a4a0ca334e5f5acac55307b2ebeadf" data-og-width="3456" width="3456" data-og-height="1944" height="1944" data-path="images/account/team/analytics.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/analytics.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=73c11df8fcb2862e5c1fd551e6399159 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/analytics.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=c3eaa0d4faa7d6fdf5e3c79dfd11fb5a 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/analytics.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=e9ee5fc554ae46e9d0e2cf53c19e652d 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/analytics.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=5f0afded72e0b02142c5a85e448f2d4e 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/analytics.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=3a6dec2a182ac88d7de75f7a42b1f5ff 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/analytics.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=7a8ac7dafe559da435f3f4974b04df52 2500w" />
</Frame>

<div id="total-usage">
  ### Total Usage
</div>

Takım genelinde toplam sekmeler ve premium istekler dahil olmak üzere toplu metrikleri görüntüle. 30 günden küçük takımlar için metrikler, oluşturulduğu tarihten itibaren kullanımı yansıtır ve takım üyelerinin katılmadan önceki etkinliklerini de içerir.

<div id="per-active-user">
  ### Per Active User
</div>

Aktif kullanıcı başına ortalama metrikleri gör: kabul edilen sekmeler, kod satırları ve premium istekler.

<div id="user-activity">
  ### User Activity
</div>

Haftalık ve aylık aktif kullanıcıları takip et.

<div id="analytics-report-headers">
  ## Analitik Rapor Başlıkları
</div>

Kontrol panelinden analitik verileri dışa aktardığında, rapor kullanıcı davranışı ve özellik kullanımı hakkında ayrıntılı metrikler içerir. İşte her başlığın anlamı:

<div id="user-information">
  ### Kullanıcı Bilgileri
</div>

<ResponseField name="Date" type="ISO 8601 timestamp">
  Analitik verilerinin kaydedildiği tarih (örn. 2024-01-15T04:30:00.000Z)
</ResponseField>

<ResponseField name="User ID" type="string">
  Sistemindeki her kullanıcı için benzersiz tanımlayıcı
</ResponseField>

<ResponseField name="Email" type="string">
  Kullanıcının hesabıyla ilişkili e‑posta adresi
</ResponseField>

<ResponseField name="Is Active" type="boolean">
  Kullanıcının bu tarihte aktif olup olmadığını belirtir
</ResponseField>

<div id="ai-generated-code-metrics">
  ### AI Tarafından Üretilen Kod Metrikleri
</div>

<ResponseField name="Chat Suggested Lines Added" type="number">
  AI sohbet özelliği tarafından önerilen toplam eklenen kod satırı
</ResponseField>

<ResponseField name="Chat Suggested Lines Deleted" type="number">
  AI sohbet tarafından silinmesi önerilen toplam kod satırı
</ResponseField>

<ResponseField name="Chat Accepted Lines Added" type="number">
  Kullanıcının kabul edip koduna eklediği AI önerili satırlar
</ResponseField>

<ResponseField name="Chat Accepted Lines Deleted" type="number">
  Kullanıcının kabul ettiği AI önerili silmeler
</ResponseField>

<div id="feature-usage-metrics">
  ### Özellik Kullanım Metrikleri
</div>

<ResponseField name="Chat Total Applies" type="number">
  Bir kullanıcının sohbette AI tarafından üretilen değişiklikleri uygulama sayısı
</ResponseField>

<ResponseField name="Chat Total Accepts" type="number">
  Bir kullanıcının AI önerilerini kabul etme sayısı
</ResponseField>

<ResponseField name="Chat Total Rejects" type="number">
  Bir kullanıcının AI önerilerini reddetme sayısı
</ResponseField>

<ResponseField name="Chat Tabs Shown" type="number">
  AI öneri sekmelerinin kullanıcıya gösterilme sayısı
</ResponseField>

<ResponseField name="Tabs Accepted" type="number">
  Kullanıcı tarafından kabul edilen AI öneri sekmeleri
</ResponseField>

<div id="request-type-metrics">
  ### İstek Türü Metrikleri
</div>

<ResponseField name="Edit Requests" type="number">
  composer/edit özelliğiyle yapılan istekler (Cmd+K satır içi düzenlemeler)
</ResponseField>

<ResponseField name="Ask Requests" type="number">
  Kullanıcıların AI’ye soru sorduğu sohbet istekleri
</ResponseField>

<ResponseField name="Agent Requests" type="number">
  AI ajanlarına yapılan istekler (uzmanlaşmış AI asistanları)
</ResponseField>

<ResponseField name="Cmd+K Usages" type="number">
  Cmd+K (veya Ctrl+K) komut paletinin kullanılma sayısı
</ResponseField>

<div id="subscription-and-api-metrics">
  ### Abonelik ve API Metrikleri
</div>

<ResponseField name="Subscription Included Reqs" type="number">
  Kullanıcının abonelik planı kapsamında karşılanan AI istekleri
</ResponseField>

<ResponseField name="API Key Reqs" type="number">
  Programatik erişim için API anahtarları kullanılarak yapılan istekler
</ResponseField>

<ResponseField name="Usage-Based Reqs" type="number">
  Kullanıma dayalı faturalamaya dahil olan istekler
</ResponseField>

<div id="additional-features">
  ### Ek Özellikler
</div>

<ResponseField name="Bugbot Usages" type="number">
  Hata tespit/düzeltme AI özelliğinin kullanılma sayısı
</ResponseField>

<div id="configuration-information">
  ### Yapılandırma Bilgileri
</div>

<ResponseField name="Most Used Model" type="string">
  Kullanıcının en sık kullandığı AI modeli (örn. GPT-4, Claude)
</ResponseField>

<ResponseField name="Most Used Apply Extension" type="string">
  AI önerilerini uygularken en sık kullanılan dosya uzantısı (örn. .ts,
  .py, .java)
</ResponseField>

<ResponseField name="Most Used Tab Extension" type="string">
  Sekme tamamlama özellikleriyle en sık kullanılan dosya uzantısı
</ResponseField>

<ResponseField name="Client Version" type="string">
  Kullanılan Cursor editörünün sürümü
</ResponseField>

<div id="calculated-metrics">
  ### Hesaplanmış Metrikler
</div>

Rapor ayrıca AI kod katkısını anlamaya yardımcı olan işlenmiş veriler de içerir:

* Total Lines Added/Deleted: Tüm kod değişikliklerinin ham sayımı
* Accepted Lines Added/Deleted: AI önerilerinden kaynaklanıp kabul edilen satırlar
* Composer Requests: Satır içi composer özelliğiyle yapılan istekler
* Chat Requests: Sohbet arayüzü üzerinden yapılan istekler

<Note>
  Tüm sayısal değerler yoksa varsayılan olarak 0, boolean değerler false ve string değerler boş string olarak kabul edilir. Metrikler kullanıcı başına günlük düzeyde toplanır.
</Note>

---

← Previous: [AI Kod Takip API'si](./ai-kod-takip-apisi.md) | [Index](./index.md) | Next: [Analytics V2](./analytics-v2.md) →