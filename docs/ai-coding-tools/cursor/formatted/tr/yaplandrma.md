---
title: "Yapılandırma"
source: "https://docs.cursor.com/tr/cli/reference/configuration"
language: "tr"
language_name: "Turkish"
---

# Yapılandırma
Source: https://docs.cursor.com/tr/cli/reference/configuration

cli-config.json için Agent CLI yapılandırma başvuru rehberi

Agent CLI'yi `cli-config.json` dosyasıyla yapılandır.

<div id="file-location">
  ## Dosya konumu
</div>

<div class="full-width-table">
  | Tür   | Platform    | Yol                                        |
  | :---- | :---------- | :----------------------------------------- |
  | Genel | macOS/Linux | `~/.cursor/cli-config.json`                |
  | Genel | Windows     | `$env:USERPROFILE\.cursor\cli-config.json` |
  | Proje | Tümü        | `<project>/.cursor/cli.json`               |
</div>

<Note>Yalnızca izinler proje düzeyinde yapılandırılabilir. Diğer tüm CLI ayarları global olarak ayarlanmalı.</Note>

Ortam değişkenleriyle geçersiz kılma:

* **`CURSOR_CONFIG_DIR`**: özel dizin yolu
* **`XDG_CONFIG_HOME`** (Linux/BSD): `$XDG_CONFIG_HOME/cursor/cli-config.json` kullanır

<div id="schema">
  ## Şema
</div>

<div id="required-fields">
  ### Zorunlu alanlar
</div>

<div class="full-width-table">
  | Alan                | Tür       | Açıklama                                                                  |
  | :------------------ | :-------- | :------------------------------------------------------------------------ |
  | `version`           | number    | Yapılandırma şema sürümü (mevcut: `1`)                                    |
  | `editor.vimMode`    | boolean   | Vim kısayollarını etkinleştir (varsayılan: `false`)                       |
  | `permissions.allow` | string\[] | İzin verilen işlemler (bkz. [Permissions](/tr/cli/reference/permissions)) |
  | `permissions.deny`  | string\[] | Yasaklanan işlemler (bkz. [Permissions](/tr/cli/reference/permissions))   |
</div>

<div id="optional-fields">
  ### İsteğe bağlı alanlar
</div>

<div class="full-width-table">
  | Alan                     | Tür     | Açıklama                                              |
  | :----------------------- | :------ | :---------------------------------------------------- |
  | `model`                  | object  | Seçilen model yapılandırması                          |
  | `hasChangedDefaultModel` | boolean | CLI tarafından yönetilen model geçersiz kılma bayrağı |
</div>

<div id="examples">
  ## Örnekler
</div>

<div id="minimal-config">
  ### En basit yapılandırma
</div>

```json  theme={null}
{
  "version": 1,
  "editor": { "vimMode": false },
  "permissions": { "allow": ["Shell(ls)"], "deny": [] }
}
```

<div id="enable-vim-mode">
  ### Vim modunu aç
</div>

```json  theme={null}
{
  "version": 1,
  "editor": { "vimMode": true },
  "permissions": { "allow": ["Shell(ls)"], "deny": [] }
}
```

<div id="configure-permissions">
  ### İzinleri yapılandırma
</div>

```json  theme={null}
{
  "version": 1,
  "editor": { "vimMode": false },
  "permissions": {
    "allow": ["Shell(ls)", "Shell(echo)"],
    "deny": ["Shell(rm)"]
  }
}
```

Kullanılabilir izin türleri ve örnekler için [Permissions](/tr/cli/reference/permissions) sayfasına bak.

<div id="troubleshooting">
  ## Sorun Giderme
</div>

**Yapılandırma hataları**: Dosyayı bir kenara alıp yeniden başlat:

```bash  theme={null}
mv ~/.cursor/cli-config.json ~/.cursor/cli-config.json.bad
```

**Değişiklikler kalıcı değil**: JSON’un geçerli olduğundan ve yazma iznin bulunduğundan emin ol. Bazı alanlar CLI tarafından yönetilir ve üzerine yazılabilir.

<div id="notes">
  ## Notlar
</div>

* Yalın JSON formatı (yorum yok)
* CLI, eksik alanları kendi kendine onarır
* Bozulmuş dosyalar `.bad` olarak yedeklenir ve yeniden oluşturulur
* İzin girişleri birebir dizelerdir (ayrıntılar için [Permissions](/tr/cli/reference/permissions) sayfasına bak)

---

← Previous: [Kimlik Doğrulama](./kimlik-dorulama.md) | [Index](./index.md) | Next: [Çıktı formatı](./kt-format.md) →