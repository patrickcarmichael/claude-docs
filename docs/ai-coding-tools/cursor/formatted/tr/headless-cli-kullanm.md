---
title: "Headless CLI Kullanımı"
source: "https://docs.cursor.com/tr/cli/headless"
language: "tr"
language_name: "Turkish"
---

# Headless CLI Kullanımı
Source: https://docs.cursor.com/tr/cli/headless

Otomatik kod analizi, üretimi ve değiştirme için Cursor CLI ile nasıl script yazacağını öğren

Kod analizi, üretimi ve refaktörleme işleri için script’lerde ve otomasyon iş akışlarında Cursor CLI kullan.

<div id="how-it-works">
  ## Nasıl çalışır
</div>

Etkileşimsiz betikleme ve otomasyon için [print mode](/tr/cli/using#non-interactive-mode) (`-p, --print`) kullan.

<div id="file-modification-in-scripts">
  ### Betiklerde dosya değiştirme
</div>

Betiklerde dosyaları değiştirmek için `--print` ile `--force`’u birleştir:

```bash  theme={null}

---

← Previous: [GitHub Actions](./github-actions.md) | [Index](./index.md) | Next: [Kurulum](./kurulum.md) →