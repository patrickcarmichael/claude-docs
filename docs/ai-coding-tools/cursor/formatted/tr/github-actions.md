---
title: "GitHub Actions"
source: "https://docs.cursor.com/tr/cli/github-actions"
language: "tr"
language_name: "Turkish"
---

# GitHub Actions
Source: https://docs.cursor.com/tr/cli/github-actions

GitHub Actions ve diğer sürekli entegrasyon sistemlerinde Cursor CLI'yi nasıl kullanacağını öğren

GitHub Actions ve diğer CI/CD sistemlerinde Cursor CLI'yi kullanarak geliştirme görevlerini otomatikleştir.

<div id="github-actions-integration">
  ## GitHub Actions ile entegrasyon
</div>

Temel kurulum:

```yaml  theme={null}
- name: Cursor CLI'yi Yükle
  run: |
    curl https://cursor.com/install -fsS | bash
    echo "$HOME/.cursor/bin" >> $GITHUB_PATH

- name: Cursor Agent'ı Çalıştır
  env:
    CURSOR_API_KEY: ${{ secrets.CURSOR_API_KEY }}
  run: |
    cursor-agent -p "İstemini buraya yaz" --model gpt-5
```

<div id="cookbook-examples">
  ## Cookbook örnekleri
</div>

Pratik iş akışları için cookbook örneklerimize göz at: [dokümantasyonu güncelleme](/tr/cli/cookbook/update-docs) ve [CI sorunlarını düzeltme](/tr/cli/cookbook/fix-ci).

<div id="other-ci-systems">
  ## Diğer CI sistemleri
</div>

Cursor CLI'yi herhangi bir CI/CD sisteminde şöyle kullan:

* **Kabuk betiği çalıştırma** (bash, zsh, vb.)
* API anahtarını yapılandırmak için **ortam değişkenleri**
* Cursor'un API'sine erişmek için **internet bağlantısı**

<div id="autonomy-levels">
  ## Otonomi seviyeleri
</div>

Agent'inin otonomi seviyesini seç:

<div id="full-autonomy-approach">
  ### Tam otonomi yaklaşımı
</div>

Agente git işlemleri, API çağrıları ve harici etkileşimler üzerinde tam kontrol ver. Kurulumu daha basit, daha fazla güven gerektirir.

**Örnek:** [Update Documentation](/tr/cli/cookbook/update-docs) rehberimizde, ilk iş akışı agente şunları yapma olanağı verir:

* PR değişikliklerini analiz et
* Git branch’leri oluştur ve yönet
* Değişiklikleri commit’le ve push et
* Pull request’lere yorum yap
* Tüm hata senaryolarını yönet

```yaml  theme={null}
- name: Belgeleri güncelle (tam özerklik)
  run: |
    cursor-agent -p "Git, GitHub CLI ve PR işlemlerine tam erişimin var. 
    Commit’ler, push’lar ve PR yorumları dahil tüm belge güncelleme iş akışını yönet."
```

<div id="restricted-autonomy-approach">
  ### Kısıtlı özerklik yaklaşımı
</div>

<Note>
  Üretim CI iş akışları için bu yaklaşımı **izin tabanlı kısıtlamalarla** kullanmanı öneriyoruz. Böylece en iyi dengeyi yakalarsın: ajan karmaşık analizleri ve dosya değişikliklerini akıllıca yönetebilirken kritik işlemler deterministik ve denetlenebilir kalır.
</Note>

Ajanın yapabileceklerini sınırla; kritik adımları ayrı iş akışı adımlarında yürüt. Daha iyi kontrol ve öngörülebilirlik.

**Örnek:** Aynı cookbook’taki ikinci iş akışı, ajanı yalnızca dosya değişiklikleriyle sınırlar:

```yaml  theme={null}
- name: Doküman güncellemeleri oluştur (kısıtlı)
  run: |
    cursor-agent -p "ÖNEMLİ: Branch oluşturma, commit, push yapma veya PR yorumu yazma. 
    Sadece çalışma dizinindeki dosyaları değiştir. Yayınlama daha sonraki bir iş akışı adımında yapılır."

- name: Docs dalını yayınla (deterministik)
  run: |
    # Deterministik git işlemleri CI tarafından yönetilir
    git checkout -B "docs/${{ github.head_ref }}"
    git add -A
    git commit -m "docs: PR için güncelleme"
    git push origin "docs/${{ github.head_ref }}"

- name: PR yorumunu paylaş (deterministik)  
  run: |
    # Deterministik PR yorumları CI tarafından yönetilir
    gh pr comment ${{ github.event.pull_request.number }} --body "Docs güncellendi"
```

<div id="permission-based-restrictions">
  ### İzne dayalı kısıtlamalar
</div>

Kısıtlamaları CLI düzeyinde zorunlu kılmak için [izin yapılandırmalarını](/tr/cli/reference/permissions) kullan:

```json  theme={null}
{
  "permissions": {
    "allow": [
      "Read(**/*.md)",
      "Write(docs/**/*)",
      "Shell(grep)",
      "Shell(find)"
    ],
    "deny": [
      "Shell(git)",
      "Shell(gh)", 
      "Write(.env*)",
      "Write(package.json)"
    ]
  }
}
```

<div id="authentication">
  ## Kimlik doğrulama
</div>

<div id="generate-your-api-key">
  ### API anahtarını oluştur
</div>

Önce Cursor panenden [bir API anahtarı oluştur](/tr/cli/reference/authentication#api-key-authentication).

<div id="configure-repository-secrets">
  ### Depo sırlarını yapılandır
</div>

Cursor API anahtarını deponda güvenli şekilde sakla:

1. GitHub depona git
2. **Settings** → **Secrets and variables** → **Actions**’a tıkla
3. **New repository secret**’a tıkla
4. Adını `CURSOR_API_KEY` koy
5. Değer olarak API anahtarını yapıştır
6. **Add secret**’a tıkla

<div id="use-in-workflows">
  ### İş akışlarında kullan
</div>

`CURSOR_API_KEY` ortam değişkenini ayarla:

```yaml  theme={null}
env:
  CURSOR_API_KEY: ${{ secrets.CURSOR_API_KEY }}
```

---

← Previous: [Dokümanları Güncelle](./dokmanlar-gncelle.md) | [Index](./index.md) | Next: [Headless CLI Kullanımı](./headless-cli-kullanm.md) →