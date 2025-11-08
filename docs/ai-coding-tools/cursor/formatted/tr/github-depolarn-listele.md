---
title: "GitHub Depolarını Listele"
source: "https://docs.cursor.com/tr/background-agent/api/list-repositories"
language: "tr"
language_name: "Turkish"
---

# GitHub Depolarını Listele
Source: https://docs.cursor.com/tr/background-agent/api/list-repositories

en/background-agent/api/openapi.yaml get /v0/repositories
Kimliği doğrulanmış kullanıcının erişebildiği GitHub depolarının listesini al.

<Warning>
  **Bu endpoint’in hız limitleri çok katı.**

  İstekleri **kullanıcı başına 1/dakika** ve **kullanıcı başına 30/saat** ile sınırla.

  Birçok depoya erişimi olan kullanıcılar için bu isteğin yanıtı onlarca saniye sürebilir.

  Bu bilginin mevcut olmadığı durumları sorunsuzca ele aldığından emin ol.
</Warning>

---

← Previous: [Modelleri Listele](./modelleri-listele.md) | [Index](./index.md) | Next: [Genel Bakış](./genel-bak.md) →