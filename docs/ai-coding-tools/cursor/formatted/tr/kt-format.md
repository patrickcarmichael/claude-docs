---
title: "Çıktı formatı"
source: "https://docs.cursor.com/tr/cli/reference/output-format"
language: "tr"
language_name: "Turkish"
---

# Çıktı formatı
Source: https://docs.cursor.com/tr/cli/reference/output-format

Metin, JSON ve stream-JSON formatları için çıktı şeması

Cursor Agent CLI, `--print` ile birlikte kullanıldığında `--output-format` seçeneğiyle birden fazla çıktı formatı sunar. Bu formatlar, programatik kullanım için yapılandırılmış formatları (`json`, `stream-json`) ve insan tarafından okunabilir ilerleme takibi için sadeleştirilmiş bir metin formatını içerir.

<Note>
  Varsayılan `--output-format` `stream-json`'dır. Bu seçenek yalnızca yazdırma (`--print`) yapılırken veya yazdırma modu çıkarımsal olarak belirlendiğinde (TTY olmayan stdout ya da pipe edilen stdin) geçerlidir.
</Note>

<div id="json-format">
  ## JSON format
</div>

`json` çıktı formatı, çalıştırma başarıyla tamamlandığında tek bir JSON nesnesi (ardından bir yeni satır) üretir. Delta’lar ve araç olayları yayınlanmaz; metin nihai sonuca birleştirilir.

Hata durumunda, işlem sıfırdan farklı bir kodla sonlanır ve stderr’e bir hata mesajı yazar. Hata durumlarında iyi biçimlendirilmiş bir JSON nesnesi üretilmez.

<div id="success-response">
  ### Başarılı yanıt
</div>

Başarılı olduğunda, CLI aşağıdaki yapıda bir JSON nesnesi üretir:

```json  theme={null}
{
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "duration_ms": 1234,
  "duration_api_ms": 1234,
  "result": "<asistanın tam metni>",
  "session_id": "<uuid>",
  "request_id": "<isteğe bağlı istek kimliği>"
}
```

<div class="full-width-table">
  | Alan              | Açıklama                                                                    |
  | ----------------- | --------------------------------------------------------------------------- |
  | `type`            | Terminal sonuçları için her zaman `"result"`                                |
  | `subtype`         | Başarılı tamamlamalar için her zaman `"success"`                            |
  | `is_error`        | Başarılı yanıtlar için her zaman `false`                                    |
  | `duration_ms`     | Toplam yürütme süresi (milisaniye)                                          |
  | `duration_api_ms` | API istek süresi (milisaniye) (şu anda `duration_ms` ile aynı)              |
  | `result`          | Asistanın eksiksiz yanıt metni (tüm metin deltalarının birleştirilmiş hâli) |
  | `session_id`      | Benzersiz oturum tanımlayıcısı                                              |
  | `request_id`      | İsteğe bağlı istek tanımlayıcısı (bulunmayabilir)                           |
</div>

<div id="stream-json-format">
  ## Stream JSON formatı
</div>

`stream-json` çıktı formatı, satır sonlarıyla ayrılmış JSON (NDJSON) üretir. Her satır, yürütme sırasında gerçekleşen gerçek zamanlı bir olayı temsil eden tek bir JSON nesnesi içerir.

Akış, başarıyla tamamlandığında sonlandırıcı bir `result` olayıyla biter. Başarısızlık durumunda süreç sıfırdan farklı bir kodla sonlanır ve akış, sonlandırıcı bir olay olmadan erken bitebilir; bir hata mesajı stderr’e yazılır.

<div id="event-types">
  ### Olay türleri
</div>

<div id="system-initialization">
  #### Sistem başlatma
</div>

Her oturumun başında bir kez yayımlanır:

```json  theme={null}
{
  "type": "system",
  "subtype": "init",
  "apiKeySource": "env|flag|login",
  "cwd": "/mutlak/yol",
  "session_id": "<uuid>",
  "model": "<model görüntü adı>",
  "permissionMode": "varsayılan"
}
```

<Note>
  Gelecekte `tools` ve `mcp_servers` gibi alanlar bu olaya eklenebilir.
</Note>

<div id="user-message">
  #### Kullanıcı mesajı
</div>

Kullanıcının girdi istemini içerir:

```json  theme={null}
{
  "type": "user",
  "message": {
    "role": "user",
    "content": [{ "type": "text", "text": "<prompt>" }]
  },
  "session_id": "<uuid>"
}
```

<div id="assistant-text-delta">
  #### Asistan metin deltası
</div>

Asistan yanıtını üretirken birden çok kez yayımlanır. Bu olaylar artımlı metin parçaları içerir:

```json  theme={null}
{
  "type": "assistant",
  "message": {
    "role": "assistant",
    "content": [{ "type": "text", "text": "<delta parçacığı>" }]
  },
  "session_id": "<uuid>"
}
```

<Note>
  Tam asistan yanıtını yeniden oluşturmak için tüm `message.content[].text` değerlerini sırayla birleştir.
</Note>

<div id="tool-call-events">
  #### Araç çağrısı olayları
</div>

Araç çağrıları başlangıç ve tamamlanma olaylarıyla izlenir:

**Araç çağrısı başlatıldı:**

```json  theme={null}
{
  "type": "tool_call",
  "subtype": "started",
  "call_id": "<string id>",
  "tool_call": {
    "readToolCall": {
      "args": { "path": "file.txt" }
    }
  },
  "session_id": "<uuid>"
}
```

**Araç çağrısı tamamlandı:**

```json  theme={null}
{
  "type": "tool_call",
  "subtype": "completed",
  "call_id": "<string id>",
  "tool_call": {
    "readToolCall": {
      "args": { "path": "file.txt" },
      "result": {
        "success": {
          "content": "dosya içeriği...",
          "isEmpty": false,
          "exceededLimit": false,
          "totalLines": 54,
          "totalChars": 1254
        }
      }
    }
  },
  "session_id": "<uuid>"
}
```

<div id="tool-call-types">
  #### Araç çağrısı türleri
</div>

**Dosya okuma aracı:**

* **Başlatıldı**: `tool_call.readToolCall.args` `{ "path": "file.txt" }` içerir
* **Tamamlandı**: `tool_call.readToolCall.result.success` dosya üstverisini ve içeriğini içerir

**Dosya yazma aracı:**

* **Başlatıldı**: `tool_call.writeToolCall.args` `{ "path": "file.txt", "fileText": "content...", "toolCallId": "id" }` içerir
* **Tamamlandı**: `tool_call.writeToolCall.result.success` `{ "path": "/absolute/path", "linesCreated": 19, "fileSize": 942 }` içerir

**Diğer araçlar:**

* `tool_call.function` yapısını `{ "name": "tool_name", "arguments": "..." }` ile kullanabilir

<div id="terminal-result">
  #### Terminal sonucu
</div>

Başarıyla tamamlandığında yayımlanan son olay:

```json  theme={null}
{
  "type": "result",
  "subtype": "success",
  "duration_ms": 1234,
  "duration_api_ms": 1234,
  "is_error": false,
  "result": "<tam asistan metni>",
  "session_id": "<uuid>",
  "request_id": "<opsiyonel istek kimliği>"
}
```

<div id="example-sequence">
  ### Örnek dizisi
</div>

İşte tipik olay akışını gösteren örnek bir NDJSON dizisi:

```json  theme={null}
{"type":"system","subtype":"init","apiKeySource":"login","cwd":"/Users/user/project","session_id":"c6b62c6f-7ead-4fd6-9922-e952131177ff","model":"Claude 4 Sonnet","permissionMode":"default"}
{"type":"user","message":{"role":"user","content":[{"type":"text","text":"README.md dosyasını oku ve bir özet çıkar"}]},"session_id":"c6b62c6f-7ead-4fd6-9922-e952131177ff"}
{"type":"assistant","message":{"role":"assistant","content":[{"type":"text","text":"Ben "}]},"session_id":"c6b62c6f-7ead-4fd6-9922-e952131177ff"}
{"type":"assistant","message":{"role":"assistant","content":[{"type":"text","text":"README.md dosyasını okuyacağım"}]},"session_id":"c6b62c6f-7ead-4fd6-9922-e952131177ff"}
{"type":"tool_call","subtype":"started","call_id":"toolu_vrtx_01NnjaR886UcE8whekg2MGJd","tool_call":{"readToolCall":{"args":{"path":"README.md"}}},"session_id":"c6b62c6f-7ead-4fd6-9922-e952131177ff"}
{"type":"tool_call","subtype":"completed","call_id":"toolu_vrtx_01NnjaR886UcE8whekg2MGJd","tool_call":{"readToolCall":{"args":{"path":"README.md"},"result":{"success":{"content":"# Proje\n\nBu bir örnek proje...","isEmpty":false,"exceededLimit":false,"totalLines":54,"totalChars":1254}}}},"session_id":"c6b62c6f-7ead-4fd6-9922-e952131177ff"}
{"type":"assistant","message":{"role":"assistant","content":[{"type":"text","text":" ve bir özet çıkaracağım"}]},"session_id":"c6b62c6f-7ead-4fd6-9922-e952131177ff"}
{"type":"tool_call","subtype":"started","call_id":"toolu_vrtx_01Q3VHVnWFSKygaRPT7WDxrv","tool_call":{"writeToolCall":{"args":{"path":"summary.txt","fileText":"# README Özeti\n\nBu proje şu öğeleri içeriyor...","toolCallId":"toolu_vrtx_01Q3VHVnWFSKygaRPT7WDxrv"}}},"session_id":"c6b62c6f-7ead-4fd6-9922-e952131177ff"}
{"type":"tool_call","subtype":"completed","call_id":"toolu_vrtx_01Q3VHVnWFSKygaRPT7WDxrv","tool_call":{"writeToolCall":{"args":{"path":"summary.txt","fileText":"# README Özeti\n\nBu proje şu öğeleri içeriyor...","toolCallId":"toolu_vrtx_01Q3VHVnWFSKygaRPT7WDxrv"},"result":{"success":{"path":"/Users/user/project/summary.txt","linesCreated":19,"fileSize":942}}}},"session_id":"c6b62c6f-7ead-4fd6-9922-e952131177ff"}
{"type":"result","subtype":"success","duration_ms":5234,"duration_api_ms":5234,"is_error":false,"result":"README.md dosyasını okuyup bir özet çıkaracağım","session_id":"c6b62c6f-7ead-4fd6-9922-e952131177ff","request_id":"10e11780-df2f-45dc-a1ff-4540af32e9c0"}
```

<div id="text-format">
  ## Metin formatı
</div>

`text` çıktı formatı, ajanın eylemlerinin basitleştirilmiş, insan tarafından okunabilir bir akışını sunar. Ayrıntılı JSON olayları yerine, ajanın gerçek zamanlı olarak ne yaptığını özlü metin açıklamalarıyla verir.

Bu format, yapılandırılmış verileri ayrıştırma yükü olmadan ajanın ilerlemesini izlemek için kullanışlıdır; bu da onu günlükleme, hata ayıklama veya basit ilerleme takibi için ideal kılar.

<div id="example-output">
  ### Örnek çıktı
</div>

```
Dosya okundu
Dosya düzenlendi
Terminal komutu çalıştırıldı
Yeni dosya oluşturuldu
```

Aracının her adımı, gerçekleştirildikçe yeni bir satırda görünür ve görevin ilerleyişine dair anında geri bildirim sağlar.

<div id="implementation-notes">
  ## Uygulama notları
</div>

* Her olay, `\n` ile sonlandırılan tek bir satır olarak yayımlanır
* `thinking` olayları yazdırma modunda bastırılır ve hiçbir çıktı biçiminde görünmez
* Alan eklemeleri zaman içinde geriye dönük uyumlu şekilde yapılabilir (tüketiciler bilinmeyen alanları yok saymalı)
* Akış biçimi gerçek zamanlı güncellemeler sağlar, JSON biçimi ise sonuçları yazdırmadan önce tamamlanmayı bekler
* Tam yanıtı yeniden oluşturmak için tüm `assistant` mesaj deltalarını birleştir
* Araç çağrısı kimlikleri, başlangıç/tamamlama olaylarını ilişkilendirmek için kullanılabilir
* Oturum kimlikleri tek bir ajan yürütümü boyunca tutarlı kalır

---

← Previous: [Yapılandırma](./yaplandrma.md) | [Index](./index.md) | Next: [Parametreler](./parametreler.md) →