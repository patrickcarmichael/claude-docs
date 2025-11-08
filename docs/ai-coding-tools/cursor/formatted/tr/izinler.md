---
title: "İzinler"
source: "https://docs.cursor.com/tr/cli/reference/permissions"
language: "tr"
language_name: "Turkish"
---

# İzinler
Source: https://docs.cursor.com/tr/cli/reference/permissions

Ajanın dosya ve komutlara erişimini kontrol etmek için izin türleri

CLI yapılandırmanda izin belirteçlerini kullanarak ajanın neleri yapmasına izin verildiğini ayarla. İzinler `~/.cursor/cli-config.json` (genel) veya `<project>/.cursor/cli.json` (projeye özel) içinde belirlenir.

<div id="permission-types">
  ## İzin türleri
</div>

<div id="shell-commands">
  ### Shell komutları
</div>

**Biçim:** `Shell(commandBase)`

Shell komutlarına erişimi kontrol eder. `commandBase`, komut satırındaki ilk tokendir.

<div class="full-width-table">
  | Örnek        | Açıklama                                                |
  | ------------ | ------------------------------------------------------- |
  | `Shell(ls)`  | `ls` komutlarının çalıştırılmasına izin ver             |
  | `Shell(git)` | Herhangi bir `git` alt komutuna izin ver                |
  | `Shell(npm)` | npm paket yöneticisi komutlarına izin ver               |
  | `Shell(rm)`  | Yıkıcı dosya silmeyi engelle (genellikle `deny` içinde) |
</div>

<div id="file-reads">
  ### Dosya okuma
</div>

**Biçim:** `Read(pathOrGlob)`

Dosya ve dizinler için okuma erişimini kontrol eder. Glob desenlerini destekler.

<div class="full-width-table">
  | Örnek               | Açıklama                                               |
  | ------------------- | ------------------------------------------------------ |
  | `Read(src/**/*.ts)` | `src` içindeki TypeScript dosyalarını okumaya izin ver |
  | `Read(**/*.md)`     | Her yerdeki markdown dosyalarını okumaya izin ver      |
  | `Read(.env*)`       | Ortam dosyalarını okumaya izin verme                   |
  | `Read(/etc/passwd)` | Sistem dosyalarını okumaya izin verme                  |
</div>

<div id="file-writes">
  ### Dosya yazma
</div>

**Biçim:** `Write(pathOrGlob)`

Dosya ve dizinler için yazma erişimini kontrol eder. Glob desenlerini destekler. Print modunda kullanırken dosya yazmak için `--force` gerekir.

<div class="full-width-table">
  | Örnek                 | Açıklama                                              |
  | --------------------- | ----------------------------------------------------- |
  | `Write(src/**)`       | `src` altındaki herhangi bir dosyaya yazmaya izin ver |
  | `Write(package.json)` | package.json'ı değiştirmeye izin ver                  |
  | `Write(**/*.key)`     | Özel anahtar dosyalarına yazmaya izin verme           |
  | `Write(**/.env*)`     | Ortam dosyalarına yazmaya izin verme                  |
</div>

<div id="configuration">
  ## Yapılandırma
</div>

CLI yapılandırma dosyandaki `permissions` nesnesine izinler ekle:

```json  theme={null}
{
  "permissions": {
    "allow": [
      "Shell(ls)",
      "Shell(git)", 
      "Read(src/**/*.ts)",
      "Write(package.json)"
    ],
    "deny": [
      "Shell(rm)",
      "Read(.env*)",
      "Write(**/*.key)"
    ]
  }
}
```

<div id="pattern-matching">
  ## Desen eşleştirme
</div>

* Glob desenleri `**`, `*` ve `?` joker karakterlerini kullanır
* Göreli yollar geçerli çalışma alanıyla sınırlıdır
* Mutlak yollar projedeki kapsamın dışındaki dosyaları hedefleyebilir
* Reddetme kuralları, izin verme kurallarına göre önceliklidir

---

← Previous: [Parametreler](./parametreler.md) | [Index](./index.md) | Next: [Slash komutları](./slash-komutlar.md) →