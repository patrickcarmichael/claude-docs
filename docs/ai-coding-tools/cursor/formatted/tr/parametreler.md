---
title: "Parametreler"
source: "https://docs.cursor.com/tr/cli/reference/parameters"
language: "tr"
language_name: "Turkish"
---

# Parametreler
Source: https://docs.cursor.com/tr/cli/reference/parameters

Cursor Agent CLI için eksiksiz komut başvuru kılavuzu

<div id="global-options">
  ## Global options
</div>

Global options herhangi bir komutla kullanılabilir:

<div class="full-width-table">
  | Option                     | Description                                                                                                   |
  | -------------------------- | ------------------------------------------------------------------------------------------------------------- |
  | `-v, --version`            | Sürüm numarasını göster                                                                                       |
  | `-a, --api-key <key>`      | Kimlik doğrulama için API anahtarı (`CURSOR_API_KEY` ortam değişkeni de kullanılabilir)                       |
  | `-p, --print`              | Yanıtları konsola yazdır (betikler veya etkileşimsiz kullanım için). write ve bash dahil tüm araçlara erişir. |
  | `--output-format <format>` | Çıktı biçimi (yalnızca `--print` ile çalışır): `text`, `json` veya `stream-json` (varsayılan: `stream-json`)  |
  | `-b, --background`         | Arka plan modunda başlat (başlangıçta composer seçicisini aç)                                                 |
  | `--fullscreen`             | Tam ekran modunu etkinleştir                                                                                  |
  | `--resume [chatId]`        | Bir sohbet oturumunu devam ettir                                                                              |
  | `-m, --model <model>`      | Kullanılacak model                                                                                            |
  | `-f, --force`              | Açıkça reddedilmedikçe komutlara zorla izin ver                                                               |
  | `-h, --help`               | Komut için yardımı görüntüle                                                                                  |
</div>

<div id="commands">
  ## Komutlar
</div>

<div class="full-width-table">
  | Komut             | Açıklama                                              | Kullanım                                          |
  | ----------------- | ----------------------------------------------------- | ------------------------------------------------- |
  | `login`           | Cursor'a kimlik doğrulamayla giriş yap                | `cursor-agent login`                              |
  | `logout`          | Oturumu kapat ve kayıtlı kimlik doğrulamasını temizle | `cursor-agent logout`                             |
  | `status`          | Kimlik doğrulama durumunu kontrol et                  | `cursor-agent status`                             |
  | `mcp`             | MCP sunucularını yönet                                | `cursor-agent mcp`                                |
  | `update\|upgrade` | Cursor Agent'ı en son sürüme güncelle                 | `cursor-agent update` veya `cursor-agent upgrade` |
  | `ls`              | Bir sohbet oturumunu listele                          | `cursor-agent ls`                                 |
  | `resume`          | Son sohbet oturumunu sürdür                           | `cursor-agent resume`                             |
  | `help [command]`  | Komut için yardımı göster                             | `cursor-agent help [command]`                     |
</div>

<Note>
  Herhangi bir komut belirtilmezse, Cursor Agent varsayılan olarak etkileşimli sohbet modunda başlar.
</Note>

<div id="mcp">
  ## MCP
</div>

Cursor Agent için yapılandırılmış MCP sunucularını yönet.

<div class="full-width-table">
  | Alt komut                 | Açıklama                                                                          | Kullanım                                   |
  | ------------------------- | --------------------------------------------------------------------------------- | ------------------------------------------ |
  | `login <identifier>`      | `.cursor/mcp.json` içinde yapılandırılmış bir MCP sunucusunda kimlik doğrula      | `cursor-agent mcp login <identifier>`      |
  | `list`                    | Yapılandırılmış MCP sunucularını ve durumlarını listele                           | `cursor-agent mcp list`                    |
  | `list-tools <identifier>` | Belirli bir MCP için kullanılabilir araçları ve bunların argüman adlarını listele | `cursor-agent mcp list-tools <identifier>` |
</div>

Tüm MCP komutları, komuta özel yardım için `-h, --help` seçeneklerini destekler.

<div id="arguments">
  ## Argümanlar
</div>

Sohbet modunda başlarken (varsayılan), başlangıç istemi verebilirsin:

**Argümanlar:**

* `prompt` — Aracın için başlangıç istemi

<div id="getting-help">
  ## Yardım alma
</div>

Tüm komutlar, komuta özgü yardımı göstermek için genel `-h, --help` seçeneğini destekler.

---

← Previous: [Çıktı formatı](./kt-format.md) | [Index](./index.md) | Next: [İzinler](./izinler.md) →