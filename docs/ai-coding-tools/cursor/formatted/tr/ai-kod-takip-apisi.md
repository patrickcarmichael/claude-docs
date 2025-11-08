---
title: "AI Kod Takip API'si"
source: "https://docs.cursor.com/tr/account/teams/ai-code-tracking-api"
language: "tr"
language_name: "Turkish"
---

# AI Kod Takip API'si
Source: https://docs.cursor.com/tr/account/teams/ai-code-tracking-api

Ekibinin depoları için yapay zekâ tarafından üretilen kod analizlerine eriş

Ekibinin depoları için yapay zekâ tarafından üretilen kod analizlerine eriş. Buna commit başına yapay zekâ kullanımı ve ayrıntılı düzeyde kabul edilen yapay zekâ değişiklikleri de dâhil.

<Note>
  API ilk sürümünde. Geri bildirimlere göre yetenekleri genişletiyoruz — hangi endpoint'lere ihtiyaç duyduğunu bize söyle!
</Note>

* **Kullanılabilirlik**: Yalnızca kurumsal ekipler için
* **Durum**: Alfa (yanıt yapı ve alanları değişebilir)

<div id="authentication">
  ## Kimlik Doğrulama
</div>

Tüm API istekleri, bir API anahtarıyla kimlik doğrulaması gerektirir. Bu API, diğer uç noktalarla aynı Admin API kimlik doğrulamasını kullanır.

Ayrıntılı kimlik doğrulama yönergeleri için bkz. [Admin API kimlik doğrulama](/tr/account/teams/admin-api#authentication).

<div id="base-url">
  ## Temel URL
</div>

Tüm API uç noktaları şu adresi kullanır:

```
https://api.cursor.com
```

<div id="rate-limits">
  ## Oran Sınırları
</div>

* Her ekip için, her uç nokta için dakikada 5 istek

<div id="query-parameters">
  ## Sorgu Parametreleri
</div>

Aşağıdaki tüm uç noktalar, aynı sorgu parametrelerini sorgu dizesiyle kabul eder:

<div className="full-width-table">
  | Parametre   | Tür    | Gerekli | Açıklama                                                                                                                                                                                             |                                                                                                         |
  | :---------- | :----- | :------ | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
  | `startDate` | string | date    | Hayır                                                                                                                                                                                                | ISO tarih dizesi, birebir "now" veya "7d" gibi göreli günler (şu an - 7 gün). Varsayılan: şu an - 7 gün |
  | `endDate`   | string | date    | Hayır                                                                                                                                                                                                | ISO tarih dizesi, birebir "now" veya "0d" gibi göreli günler. Varsayılan: şu an                         |
  | `page`      | number | Hayır   | Sayfa numarası (1 tabanlı). Varsayılan: 1                                                                                                                                                            |                                                                                                         |
  | `pageSize`  | number | Hayır   | Sayfa başına sonuç sayısı. Varsayılan: 100, Maks: 1000                                                                                                                                               |                                                                                                         |
  | `user`      | string | Hayır   | Tek bir kullanıcıya göre isteğe bağlı filtre. E-posta (örn. [developer@company.com](mailto:developer@company.com)), kodlanmış kimlik (örn. user\_abc123...) veya sayısal kimlik (örn. 42) kabul eder |                                                                                                         |
</div>

<Note>
  Yanıtlarda userId, user\_ önekiyle kodlanmış harici bir kimlik olarak döner. Bu, API kullanımı için kararlıdır.
</Note>

<div id="semantics-and-how-metrics-are-computed">
  ## Anlambilim ve Metriklerin Nasıl Hesaplandığı
</div>

* **Kaynaklar**: "TAB", kabul edilen satır içi tamamlamaları temsil eder; "COMPOSER", Composer’dan kabul edilen diff’leri temsil eder
* **Satır metrikleri**: tabLinesAdded/Deleted ve composerLinesAdded/Deleted ayrı ayrı sayılır; nonAiLinesAdded/Deleted, max(0, totalLines - AI lines) olarak türetilir
* **Gizlilik modu**: İstemcide etkinleştirilirse, bazı meta veriler (örn. fileName) atlanabilir
* **Dal bilgisi**: isPrimaryBranch, geçerli dal repo’nun varsayılan dalına eşitse true olur; repo bilgisi yoksa undefined olabilir

Commit’lerin ve değişikliklerin nasıl algılanıp raporlandığını anlamak için o dosyayı inceleyebilirsin.

<div id="endpoints">
  ## Uç Noktalar
</div>

<div id="get-ai-commit-metrics-json-paginated">
  ### AI Commit Metriklerini Getir (JSON, sayfalı)
</div>

Commit başına, satırları TAB, COMPOSER ve AI dışı kaynaklara atfeden toplu metrikleri al.

```
GET /analytics/ai-code/commits
```

<div id="response">
  #### Yanıt
</div>

```typescript  theme={null}
{
  items: AiCommitMetric[];
  totalCount: number;
  page: number;
  pageSize: number;
}
```

<div id="aicommitmetric-fields">
  #### AiCommitMetric Alanları
</div>

<div className="full-width-table">
  | Alan                   | Tür     | Açıklama                                        |                                              |
  | :--------------------- | :------ | :---------------------------------------------- | -------------------------------------------- |
  | `commitHash`           | string  | Git commit karma değeri                         |                                              |
  | `userId`               | string  | Kodlanmış kullanıcı kimliği (örn. user\_abc123) |                                              |
  | `userEmail`            | string  | Kullanıcının e‑posta adresi                     |                                              |
  | `repoName`             | string  | null                                            | Depo adı                                     |
  | `branchName`           | string  | null                                            | Dal adı                                      |
  | `isPrimaryBranch`      | boolean | null                                            | Birincil dal olup olmadığı                   |
  | `totalLinesAdded`      | number  | Commit’te eklenen toplam satır                  |                                              |
  | `totalLinesDeleted`    | number  | Commit’te silinen toplam satır                  |                                              |
  | `tabLinesAdded`        | number  | TAB tamamlamalarıyla eklenen satırlar           |                                              |
  | `tabLinesDeleted`      | number  | TAB tamamlamalarıyla silinen satırlar           |                                              |
  | `composerLinesAdded`   | number  | Composer ile eklenen satırlar                   |                                              |
  | `composerLinesDeleted` | number  | Composer ile silinen satırlar                   |                                              |
  | `nonAiLinesAdded`      | number  | null                                            | Yapay zekâ kaynaklı olmayan eklenen satırlar |
  | `nonAiLinesDeleted`    | number  | null                                            | Yapay zekâ kaynaklı olmayan silinen satırlar |
  | `message`              | string  | null                                            | Commit mesajı                                |
  | `commitTs`             | string  | null                                            | Commit zaman damgası (ISO biçimi)            |
  | `createdAt`            | string  | Alım zaman damgası (ISO biçimi)                 |                                              |
</div>

<div id="example-response">
  #### Örnek Yanıt
</div>

```json  theme={null}
{
  "items": [
    {
      "commitHash": "a1b2c3d4",
      "userId": "user_3k9x8q...",
      "userEmail": "developer@company.com",
      "repoName": "company/repo",
      "branchName": "main",
      "isPrimaryBranch": true,
      "totalLinesAdded": 120,
      "totalLinesDeleted": 30,
      "tabLinesAdded": 50,
      "tabLinesDeleted": 10,
      "composerLinesAdded": 40,
      "composerLinesDeleted": 5,
      "nonAiLinesAdded": 30,
      "nonAiLinesDeleted": 15,
      "message": "Refactor: analytics istemcisini ayır"
      "commitTs": "2025-07-30T14:12:03.000Z",
      "createdAt": "2025-07-30T14:12:30.000Z"
    }
  ],
  "totalCount": 42,
  "page": 1,
  "pageSize": 100
}
```

<div id="example-requests">
  #### Örnek İstekler
</div>

**Basit istek:**

```bash  theme={null}
curl -X GET "https://api.cursor.com/analytics/ai-code/commits?startDate=7d&endDate=now&page=1&pageSize=100" \
  -u API_ANAHTARIN:
```

**Kullanıcıya göre filtrele (e‑posta):**

```bash  theme={null}
curl -X GET "https://api.cursor.com/analytics/ai-code/commits?startDate=2025-06-01T00:00:00Z&endDate=now&user=developer@company.com" \
  -u API_ANAHTARIN:
```

<div id="download-ai-commit-metrics-csv-streaming">
  ### AI Commit Metrics’i indir (CSV, akış)
</div>

Büyük hacimli veri çıkarımları için commit metriklerini CSV formatında indir.

```
GET /analytics/ai-code/commits.csv
```

<div id="response">
  #### Yanıt
</div>

Üstbilgiler:

* Content-Type: text/csv; charset=utf-8

<div id="csv-columns">
  #### CSV Sütunları
</div>

<div className="full-width-table">
  | Sütun                    | Tür     | Açıklama                           |
  | :----------------------- | :------ | :--------------------------------- |
  | `commit_hash`            | string  | Git commit özeti (hash)            |
  | `user_id`                | string  | Kodlanmış kullanıcı kimliği        |
  | `user_email`             | string  | Kullanıcının e‑posta adresi        |
  | `repo_name`              | string  | Depo adı                           |
  | `branch_name`            | string  | Dal adı                            |
  | `is_primary_branch`      | boolean | Birincil dal olup olmadığı         |
  | `total_lines_added`      | number  | Commit’te eklenen toplam satır     |
  | `total_lines_deleted`    | number  | Commit’te silinen toplam satır     |
  | `tab_lines_added`        | number  | TAB tamamlamalarıyla eklenen satır |
  | `tab_lines_deleted`      | number  | TAB tamamlamalarıyla silinen satır |
  | `composer_lines_added`   | number  | Composer ile eklenen satır         |
  | `composer_lines_deleted` | number  | Composer ile silinen satır         |
  | `non_ai_lines_added`     | number  | Yapay zekâ dışı eklenen satır      |
  | `non_ai_lines_deleted`   | number  | Yapay zekâ dışı silinen satır      |
  | `message`                | string  | Commit mesajı                      |
  | `commit_ts`              | string  | Commit zaman damgası (ISO biçimi)  |
  | `created_at`             | string  | Alım zaman damgası (ISO biçimi)    |
</div>

<div id="sample-csv-output">
  #### Örnek CSV Çıktısı
</div>

```csv  theme={null}
commit_hash,user_id,user_email,repo_name,branch_name,is_primary_branch,total_lines_added,total_lines_deleted,tab_lines_added,tab_lines_deleted,composer_lines_added,composer_lines_deleted,non_ai_lines_added,non_ai_lines_deleted,message,commit_ts,created_at
a1b2c3d4,user_3k9x8q...,developer@company.com,company/repo,main,true,120,30,50,10,40,5,30,15,"Refactor: analytics istemcisini ayır",2025-07-30T14:12:03.000Z,2025-07-30T14:12:30.000Z
e5f6g7h8,user_3k9x8q...,developer@company.com,company/repo,feature-branch,false,85,15,30,5,25,3,30,7,"Hata işleme ekle",2025-07-30T13:45:21.000Z,2025-07-30T13:45:45.000Z
```

<div id="example-request">
  #### Örnek İstek
</div>

```bash  theme={null}
curl -L "https://api.cursor.com/analytics/ai-code/commits.csv?startDate=2025-07-01T00:00:00Z&endDate=now&user=user_3k9x8q..." \
  -u YOUR_API_KEY: \
  -o commits.csv
```

<div id="get-ai-code-change-metrics-json-paginated">
  ### AI Kod Değişikliği Metriğini Al (JSON, sayfalı)
</div>

Deterministik changeId ile gruplanmış, ayrıntılı olarak kabul edilmiş AI değişikliklerini al. Commit’lerden bağımsız kabul edilmiş AI olaylarını analiz etmek için işe yarar.

```
GET /analytics/ai-code/changes
```

<div id="response">
  #### Yanıt
</div>

```typescript  theme={null}
{
  items: AiCodeChangeMetric[];
  totalCount: number;
  page: number;
  pageSize: number;
}
```

<div id="aicodechangemetric-fields">
  #### AiCodeChangeMetric Alanları
</div>

<div className="full-width-table">
  | Alan                | Tür    | Açıklama                                                   |                           |
  | :------------------ | :----- | :--------------------------------------------------------- | ------------------------- |
  | `changeId`          | string | Değişikliğe ait deterministik kimlik                       |                           |
  | `userId`            | string | Kodlanmış kullanıcı kimliği (ör. user\_abc123)             |                           |
  | `userEmail`         | string | Kullanıcının e-posta adresi                                |                           |
  | `source`            | "TAB"  | "COMPOSER"                                                 | AI değişikliğinin kaynağı |
  | `model`             | string | null                                                       | Kullanılan AI modeli      |
  | `totalLinesAdded`   | number | Eklenen toplam satır                                       |                           |
  | `totalLinesDeleted` | number | Silinen toplam satır                                       |                           |
  | `createdAt`         | string | İçeri aktarma zaman damgası (ISO biçimi)                   |                           |
  | `metadata`          | Array  | Dosya üst verileri (gizlilik modunda fileName atlanabilir) |                           |
</div>

<div id="example-response">
  #### Örnek Yanıt
</div>

```json  theme={null}
{
  "items": [
    {
      "changeId": "749356201",
      "userId": "user_3k9x8q...",
      "userEmail": "developer@company.com",
      "source": "COMPOSER",
      "model": null,
      "totalLinesAdded": 18,
      "totalLinesDeleted": 4,
      "createdAt": "2025-07-30T15:10:12.000Z",
        { "fileName": "src/analytics/report.ts", "fileExtension": "ts", "linesAdded": 12, "linesDeleted": 3 },
        { "fileName": "src/analytics/ui.tsx", "fileExtension": "tsx", "linesAdded": 6, "linesDeleted": 1 }
        { "fileName": "src/analytics/ui.tsx", "fileExtension": "tsx", "linesAdded": 6, "linesDeleted": 1 }
      ]
    }
  ],
  "totalCount": 128,
  "page": 1,
  "pageSize": 200
}
```

<div id="example-requests">
  #### Örnek İstekler
</div>

**Basit istek:**

```bash  theme={null}
curl -X GET "https://api.cursor.com/analytics/ai-code/changes?startDate=14d&endDate=now&page=1&pageSize=200" \
  -u API_ANAHTARIN:
```

**Kullanıcıya göre filtrele (kodlanmış kimlik):**

```bash  theme={null}
curl -X GET "https://api.cursor.com/analytics/ai-code/changes?user=user_3k9x8q..." \
  -u API_ANAHTARIN:
```

**Kullanıcıya göre filtrele (e-posta):**

```bash  theme={null}
curl -X GET "https://api.cursor.com/analytics/ai-code/changes?user=developer@company.com" \
  -u YOUR_API_KEY:
```

<div id="download-ai-code-change-metrics-csv-streaming">
  ### AI Kod Değişikliği Metriklerini İndir (CSV, akış)
</div>

Büyük veri çıkarımları için değişiklik metriklerini CSV formatında indir.

```
GET /analytics/ai-code/changes.csv
```

<div id="response">
  #### Yanıt
</div>

Başlıklar:

* Content-Type: text/csv; charset=utf-8

<div id="csv-columns">
  #### CSV Sütunları
</div>

<div className="full-width-table">
  | Sütun                 | Tür    | Açıklama                                               |
  | :-------------------- | :----- | :----------------------------------------------------- |
  | `change_id`           | string | Değişiklik için deterministik kimlik                   |
  | `user_id`             | string | Kodlanmış kullanıcı kimliği                            |
  | `user_email`          | string | Kullanıcının e-posta adresi                            |
  | `source`              | string | AI değişikliğinin kaynağı (TAB veya COMPOSER)          |
  | `model`               | string | Kullanılan AI modeli                                   |
  | `total_lines_added`   | number | Eklenen toplam satır sayısı                            |
  | `total_lines_deleted` | number | Silinen toplam satır sayısı                            |
  | `created_at`          | string | Alım zaman damgası (ISO biçimi)                        |
  | `metadata_json`       | string | JSON olarak dizgeleştirilmiş metadata girdileri dizisi |
</div>

<div id="notes">
  #### Notlar
</div>

* metadata\_json, JSON olarak dizgeleştirilmiş metadata girdileri dizisidir (gizlilik modunda fileName atlanabilir)
* CSV’yi işlerken tırnak içindeki alanları ayrıştırdığından emin ol

<div id="sample-csv-output">
  #### Örnek CSV Çıktısı
</div>

```csv  theme={null}
change_id,user_id,user_email,kaynak,model,toplam_eklenen_satır,toplam_silinen_satır,oluşturulma_tarihi,metadata_json
749356201,user_3k9x8q...,developer@company.com,COMPOSER,gpt-4o,18,4,2025-07-30T15:10:12.000Z,"[{""fileName"":""src/analytics/report.ts"",""fileExtension"":""ts"",""linesAdded"":12,""linesDeleted"":3},{""fileName"":""src/analytics/ui.tsx"",""fileExtension"":""tsx"",""linesAdded"":6,""linesDeleted"":1}]"
749356202,user_3k9x8q...,developer@company.com,TAB,,8,2,2025-07-30T15:08:45.000Z,"[{""fileName"":""src/utils/helpers.ts"",""fileExtension"":""ts"",""linesAdded"":8,""linesDeleted"":2}]"
```

<div id="example-request">
  #### Örnek İstek
</div>

```bash  theme={null}
curl -L "https://api.cursor.com/analytics/ai-code/changes.csv?startDate=30d&endDate=now" \
  -u YOUR_API_KEY: \
  -o changes.csv
```

<div id="tips">
  ## İpuçları
</div>

* Tüm endpoint’ler genelinde tek bir kullanıcıyı hızlıca filtrelemek için `user` parametresini kullan
* Büyük veri çıkarımları için CSV endpoint’lerini tercih et — sunucu tarafında 10.000 kayıttan oluşan sayfalar halinde akış (stream) olarak iletilir
* Varsayılan branch çözülemediyse `isPrimaryBranch` tanımsız olabilir
* `commitTs` commit zaman damgasıdır; `createdAt` sunucularımızda işlenme (ingestion) zamanıdır
* İstemcide gizlilik modu etkinse bazı alanlar bulunmayabilir

<div id="changelog">
  ## Değişiklik Günlüğü
</div>

* **Alfa sürümü**: Commit ve değişiklikler için başlangıç uç noktaları. Geri bildirimlere göre yanıt biçimleri değişebilir

---

← Previous: [Admin API](./admin-api.md) | [Index](./index.md) | Next: [Analytics](./analytics.md) →