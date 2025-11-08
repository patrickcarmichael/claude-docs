---
title: "Kod İncelemesi"
source: "https://docs.cursor.com/tr/cli/cookbook/code-review"
language: "tr"
language_name: "Turkish"
---

# Kod İncelemesi
Source: https://docs.cursor.com/tr/cli/cookbook/code-review

Cursor CLI kullanarak pull request'leri otomatik inceleyip geri bildirim veren bir GitHub Actions iş akışı oluştur

Bu eğitim, GitHub Actions içinde Cursor CLI ile kod incelemeyi nasıl kuracağını gösterir. İş akışı pull request'leri analiz eder, sorunları tespit eder ve yorum olarak geri bildirim paylaşır.

<Tip>
  Çoğu kullanıcı için bunun yerine [Bugbot](/tr/bugbot) kullanmanı öneririz. Bugbot, herhangi bir kurulum gerektirmeden yönetilen otomatik kod incelemesi sunar. Bu CLI yaklaşımı, yetenekleri keşfetmek ve ileri düzey özelleştirme için faydalıdır.
</Tip>

<div className="space-y-4">
  <Expandable title="tam iş akışı dosyası">
    ```yaml cursor-code-review.yml theme={null}
    name: Kod İncelemesi

    on:
      pull_request:
        types: [opened, synchronize, reopened, ready_for_review]

    permissions:
      pull-requests: write
      contents: read
      issues: write

    jobs:
      code-review:
        runs-on: ubuntu-latest
        # Taslak PR'ler için otomatik kod incelemesini atla
        if: github.event.pull_request.draft == false
        steps:
          - name: Depoyu checkout et
            uses: actions/checkout@v4
            with:
              fetch-depth: 0
              ref: ${{ github.event.pull_request.head.sha }}

          - name: Cursor CLI'yi yükle
            run: |
              curl https://cursor.com/install -fsS | bash
              echo "$HOME/.cursor/bin" >> $GITHUB_PATH

          - name: Git kimliğini yapılandır
            run: |
              git config user.name "Cursor Agent"
              git config user.email "cursoragent@cursor.com"

          - name: Otomatik kod incelemesi yap
            env:
              CURSOR_API_KEY: ${{ secrets.CURSOR_API_KEY }}
              MODEL: gpt-5
              GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
              BLOCKING_REVIEW: ${{ vars.BLOCKING_REVIEW || 'false' }}
            run: |
              cursor-agent --force --model "$MODEL" --output-format=text --print 'Bir GitHub Actions runner’ında otomatik kod incelemesi yapıyorsun. gh CLI mevcut ve GH_TOKEN ile kimliği doğrulanmış. Pull request’lere yorum yapabilirsin.

              Bağlam:
              - Depo: ${{ github.repository }}
              - PR numarası: ${{ github.event.pull_request.number }}
              - PR Head SHA: ${{ github.event.pull_request.head.sha }}
              - PR Base SHA: ${{ github.event.pull_request.base.sha }}
              - Engelleyici inceleme: ${{ env.BLOCKING_REVIEW }}

              Hedefler:
              1) Mevcut inceleme yorumlarını tekrar kontrol et ve ele alındığında “resolved” diyerek yanıtla.
              2) Geçerli PR diff’ini incele ve yalnızca net, yüksek önem dereceli sorunları işaretle.
              3) Yalnızca değişen satırlara çok kısa satır içi yorumlar (1-2 cümle) bırak ve sonunda kısa bir özet ver.

              Prosedür:
              - Mevcut yorumları al: gh pr view --json comments
              - Diff’i al: gh pr diff
              - Satır içi pozisyonları hesaplamak için yamalarla değişen dosyaları al: gh api repos/${{ github.repository }}/pulls/${{ github.event.pull_request.number }}/files --paginate --jq '.[] | {filename,patch}'
              - Her sorun için tam satır içi çapalayıcıları (dosya yolu + diff pozisyonu) hesapla. Yorumlar, diff’te değişen satırın satır içi olarak yerleştirilmeli, üst düzey yorum olmamalı.
              - Bu bot tarafından yazılmış önceki üst düzey “sorun yok” tarzı yorumları tespit et (şu gövdelere benzer: "✅ no issues", "No issues found", "LGTM").
              - MEVCUT çalıştırma sorun buluyor ve önceki “sorun yok” yorumları varsa:
                - Karışıklığı önlemek için bunları kaldırmayı tercih et:
                  - Üst düzey “sorun yok” yorumlarını şu komutla silmeyi dene: gh api -X DELETE repos/${{ github.repository }}/issues/comments/<comment_id>
                  - Silme mümkün değilse, GraphQL ile küçült (minimizeComment) veya “[Yeni bulgular tarafından geçersiz kılındı]” önekiyle düzenle.
                - Ne silme ne küçültme mümkünse, o yoruma şu şekilde yanıt ver: "⚠️ Geçersiz kılındı: yeni commit’lerde sorunlar bulundu"
              - Daha önce bildirilen bir sorun, yakınlardaki değişikliklerle düzelmiş görünüyorsa şöyle yanıtla: ✅ Bu sorun son değişikliklerle çözümlenmiş görünüyor
              - SADECE şunları analiz et:
                - Null/undefined dereference’ları
                - Kaynak sızıntıları (kapatılmamış dosyalar veya bağlantılar)
                - Enjeksiyon (SQL/XSS)
                - Eşzamanlılık/yariș durumları
                - Kritik işlemler için eksik hata işleme
                - Yanlış davranışa yol açan bariz mantık hataları
                - Ölçülebilir etkisi olan belirgin performans karşı örüntüleri
                - Kesin güvenlik açıkları
              - Yinelemelerden kaçın: aynı satırlarda veya yakınında benzer geri bildirim varsa atla.

              Yorum kuralları:
              - Toplam en fazla 10 satır içi yorum; en kritik sorunlara öncelik ver
              - Yorum başına bir sorun; tam değişen satıra yerleştir
              - Tüm sorun yorumları satır içi olmalı (PR diff’inde bir dosyaya ve satıra/pozisyona sabitlenmiş)
              - Doğal ton, spesifik ve eyleme dönük; otomatik veya yüksek güven ibarelerinden bahsetme
              - Emojileri kullan: 🚨 Kritik 🔒 Güvenlik ⚡ Performans ⚠️ Mantık ✅ Çözüldü ✨ İyileştirme

              Gönderim:
              - Raporlanacak HİÇ sorun yoksa ve “sorun yok” belirten mevcut bir üst düzey yorum zaten varsa (örn. "✅ no issues", "No issues found", "LGTM"), yinelenmeyi önlemek için başka bir yorum gönderme. Göndermeyi atla.
              - Raporlanacak HİÇ sorun yoksa ve önceki “sorun yok” yorumu yoksa, sorun olmadığını belirten kısa bir özet yorum gönder.
              - Raporlanacak sorunlar VARSA ve önceki bir “sorun yok” yorumu varsa, yeni incelemeyi göndermeden önce o önceki yorumu sil/küçült/geçersiz kılındı olarak işaretle.
              - Raporlanacak sorunlar VARSA, SADECE satır içi yorumlar ve isteğe bağlı kısa bir özet gövdesi içeren TEK bir inceleme gönder. Yorumların satır içi olduğundan emin olmak için GitHub Reviews API’yi kullan:
                - Build a JSON array of comments like: [{ "path": "<file>", "position": <diff_position>, "body": "..." }]
                - Submit via: gh api repos/${{ github.repository }}/pulls/${{ github.event.pull_request.number }}/reviews -f event=COMMENT -f body="$SUMMARY" -f comments='[$COMMENTS_JSON]'
              - Şunları KULLANMA: gh pr review --approve veya --request-changes

              Engelleme davranışı:
              - BLOCKING_REVIEW true ise ve herhangi bir 🚨 veya 🔒 sorun gönderildiyse: echo "CRITICAL_ISSUES_FOUND=true" >> $GITHUB_ENV
              - Aksi halde: echo "CRITICAL_ISSUES_FOUND=false" >> $GITHUB_ENV
              - Her zaman sonunda CRITICAL_ISSUES_FOUND değerini ayarla
              '

          - name: Engelleyici inceleme sonuçlarını kontrol et
            if: env.BLOCKING_REVIEW == 'true'
            run: |
              echo "Kritik sorunlar kontrol ediliyor..."
              echo "CRITICAL_ISSUES_FOUND: ${CRITICAL_ISSUES_FOUND:-unset}"

              if [ "${CRITICAL_ISSUES_FOUND:-false}" = "true" ]; then
                echo "❌ Kritik sorunlar bulundu ve engelleyici inceleme etkin. İş akışı başarısız oluyor."
                exit 1
              else
                echo "✅ Engelleyici sorun bulunamadı."
              fi
    ```
  </Expandable>

  <Frame>
    <img src="https://mintcdn.com/cursor/KODIqSiRh6LRGwl9/images/cli/cookbook/code-review/comment.png?fit=max&auto=format&n=KODIqSiRh6LRGwl9&q=85&s=31c7e4b54276532df8010645686ebbbc" alt="Bir pull request’te satır içi yorumları gösteren otomatik kod incelemesi" data-og-width="2920" width="2920" data-og-height="1272" height="1272" data-path="images/cli/cookbook/code-review/comment.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/KODIqSiRh6LRGwl9/images/cli/cookbook/code-review/comment.png?w=280&fit=max&auto=format&n=KODIqSiRh6LRGwl9&q=85&s=25e552210fa8425a10ff459bf4cd6006 280w, https://mintcdn.com/cursor/KODIqSiRh6LRGwl9/images/cli/cookbook/code-review/comment.png?w=560&fit=max&auto=format&n=KODIqSiRh6LRGwl9&q=85&s=234bf271bc595e763549c4f04d2e6fbb 560w, https://mintcdn.com/cursor/KODIqSiRh6LRGwl9/images/cli/cookbook/code-review/comment.png?w=840&fit=max&auto=format&n=KODIqSiRh6LRGwl9&q=85&s=b6f6d1444de7fe0197e3d35fa35955e8 840w, https://mintcdn.com/cursor/KODIqSiRh6LRGwl9/images/cli/cookbook/code-review/comment.png?w=1100&fit=max&auto=format&n=KODIqSiRh6LRGwl9&q=85&s=300314314f5071b77f735460be33985f 1100w, https://mintcdn.com/cursor/KODIqSiRh6LRGwl9/images/cli/cookbook/code-review/comment.png?w=1650&fit=max&auto=format&n=KODIqSiRh6LRGwl9&q=85&s=10e4db857ee84c55d17222cef492611d 1650w, https://mintcdn.com/cursor/KODIqSiRh6LRGwl9/images/cli/cookbook/code-review/comment.png?w=2500&fit=max&auto=format&n=KODIqSiRh6LRGwl9&q=85&s=e65add70ffebfeb9ad05c9bb19a5f4e1 2500w" />
  </Frame>
</div>

<div id="configure-authentication">
  ## Kimlik doğrulamayı yapılandır
</div>

GitHub Actions’ta Cursor CLI’yi kimlik doğrulamak için [API anahtarını ve depo gizlerini ayarla](/tr/cli/github-actions#authentication).

<div id="set-up-agent-permissions">
  ## Aracı izinlerini ayarla
</div>

Aracın hangi işlemleri yapabileceğini kontrol etmek için bir yapılandırma dosyası oluştur. Bu, koda push atmak veya pull request açmak gibi istenmeyen işlemleri önler.

Depo kök dizininde `.cursor/cli.json` dosyasını oluştur:

```json  theme={null}
{
  "permissions": {
    "deny": [
      "Shell(git push)",
      "Shell(gh pr create)",
      "Write(**)"
    ]
  }
}
```

Bu yapılandırma, agent’in dosyaları okumasına ve yorum eklemek için GitHub CLI’yi kullanmasına izin verir, ama depoda değişiklik yapmasını engeller. Daha fazla yapılandırma seçeneği için [izinler referansı](/tr/cli/reference/permissions) sayfasına bak.

<div id="build-the-github-actions-workflow">
  ## GitHub Actions iş akışını oluştur
</div>

Şimdi iş akışını adım adım kuralım.

<div id="set-up-the-workflow-trigger">
  ### İş akışı tetikleyicisini ayarla
</div>

`.github/workflows/cursor-code-review.yml` dosyasını oluştur ve pull request’lerde çalışacak şekilde yapılandır:

```yaml  theme={null}
name: Cursor Kod İncelemesi

on:
  pull_request:
    types: [opened, synchronize, reopened, ready_for_review]

jobs:
  code-review:
    runs-on: ubuntu-latest
    permissions:
      contents: read
      pull-requests: write
    
    steps:
```

<div id="checkout-the-repository">
  ### Depoyu checkout et
</div>

Pull request koduna erişmek için checkout adımını ekle:

```yaml  theme={null}
- name: Depoyu çek
  uses: actions/checkout@v4
  with:
    fetch-depth: 0
    ref: ${{ github.event.pull_request.head.sha }}
```

### Cursor CLI'yi yükle

CLI kurulum adımını ekle:

```yaml  theme={null}
- name: Cursor CLI'yi yükle
  run: |
    curl https://cursor.com/install -fsS | bash
    echo "$HOME/.cursor/bin" >> $GITHUB_PATH
```

<div id="configure-the-review-agent">
  ### İnceleme aracını yapılandır
</div>

Tam inceleme adımına geçmeden önce, inceleme istemimizin yapısını anlayalım. Bu bölüm, agent’ın nasıl davranmasını istediğimizi özetliyor:

**Amaç**:
Agent’ın mevcut PR diff’ini gözden geçirip yalnızca net ve yüksek önem dereceli sorunları işaretlemesini, ardından sadece değişen satırlara çok kısa satır içi yorumlar (1-2 cümle) bırakmasını ve sonda kısa bir özet vermesini istiyoruz. Bu, sinyal-gürültü oranını dengede tutar.

**Biçim**:
Yorumların kısa ve direkt olmasını istiyoruz. Yorumları taramayı kolaylaştırmak için emoji kullanıyoruz ve sonda tüm incelemenin yüksek seviyeli bir özetini istiyoruz.

**Gönderim**:
İnceleme bittiğinde, agent incelemede bulunanlara dayalı kısa bir yorum eklemeli. Agent, satır içi yorumları ve özlü bir özeti içeren tek bir inceleme göndermeli.

**Köşe durumları**:
Şunları ele almamız gerekiyor:

* Mevcut yorumların çözümlenmesi: Ele alındıklarında agent bunları tamamlandı olarak işaretlemeli
* Mükerrelerden kaçınma: Aynı veya yakın satırlarda benzer geri bildirim zaten varsa agent yorum yapmayı atlamalı

**Nihai istem**:
Tam istem, odaklı ve uygulanabilir geri bildirim üretmek için bu davranışsal gereksinimlerin tümünü birleştirir

Şimdi inceleme agent’ı adımını uygulayalım:

```yaml  theme={null}
- name: Kod incelemesi yap
  env:
    CURSOR_API_KEY: ${{ secrets.CURSOR_API_KEY }}
    GH_TOKEN: ${{ github.token }}
  run: |
    cursor-agent --force --model "$MODEL" --output-format=text --print "GitHub Actions runner’ında otomatik kod incelemesi yapıyorsun. gh CLI mevcut ve GH_TOKEN ile kimliği doğrulanmış. Pull request’lere yorum yapabilirsin.
    
    Bağlam:
    - Depo: ${{ github.repository }}
    - PR Numarası: ${{ github.event.pull_request.number }}
    - PR Head SHA: ${{ github.event.pull_request.head.sha }}
    - PR Base SHA: ${{ github.event.pull_request.base.sha }}
    
    Hedefler:
    1) Mevcut inceleme yorumlarını yeniden kontrol et ve ele alındıysa resolved diye yanıtla
    2) Mevcut PR diff’ini incele ve yalnızca net, yüksek önem dereceli sorunları işaretle
    3) Yalnızca değişen satırlara çok kısa satır içi yorumlar (1-2 cümle) bırak ve sonunda kısa bir özet ekle
    
    Prosedür:
    - Mevcut yorumları getir: gh pr view --json comments
    - Diff’i al: gh pr diff
    - Daha önce bildirilen bir sorun yakın değişikliklerle düzelmiş görünüyorsa şu şekilde yanıtla: ✅ Bu sorun son değişikliklerle çözülmüş görünüyor
    - Yinelenenleri önle: aynı veya benzer geri bildirim aynı satırlarda veya yakınında zaten varsa atla
    
    Yorum kuralları:
    - Toplam en fazla 10 satır içi yorum; en kritik sorunlara öncelik ver
    - Yorum başına tek sorun; tam olarak değişen satıra yerleştir
    - Doğal, spesifik ve uygulanabilir bir ton kullan; otomasyon veya yüksek güven ifadesinden bahsetme
    - Emojileri kullan: 🚨 Kritik 🔒 Güvenlik ⚡ Performans ⚠️ Mantık ✅ Çözüldü ✨ İyileştirme
    
    Gönderim:
    - Satır içi yorumlar artı özlü bir özet içeren tek bir inceleme gönder
    - Yalnızca şunu kullan: gh pr review --comment
    - Şunları kullanma: gh pr review --approve veya --request-changes"
```

```text  theme={null}
.
├── .cursor/
│   └── cli.json
├── .github/
│   └── workflows/
│       └── cursor-code-review.yml
```

<div id="test-your-reviewer">
  ## İnceleyicini test et
</div>

İş akışının çalıştığını ve agent’ın emojiyle geri bildirim veren inceleme yorumları paylaştığını doğrulamak için bir test pull request’i oluştur.

<Frame>
  <img src="https://mintcdn.com/cursor/KODIqSiRh6LRGwl9/images/cli/cookbook/code-review/github-actions.png?fit=max&auto=format&n=KODIqSiRh6LRGwl9&q=85&s=aa989eb5b7520e6718a48afd8daa70d9" alt="Belirli satırlarda emojiler ve satır içi geri bildirim içeren otomatik inceleme yorumlarını gösteren pull request" data-og-width="1250" width="1250" data-og-height="704" height="704" data-path="images/cli/cookbook/code-review/github-actions.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/KODIqSiRh6LRGwl9/images/cli/cookbook/code-review/github-actions.png?w=280&fit=max&auto=format&n=KODIqSiRh6LRGwl9&q=85&s=9f2e324beb1cccb8052dcd0682323e47 280w, https://mintcdn.com/cursor/KODIqSiRh6LRGwl9/images/cli/cookbook/code-review/github-actions.png?w=560&fit=max&auto=format&n=KODIqSiRh6LRGwl9&q=85&s=f08497ddb17921f4bb4638ef4eec3379 560w, https://mintcdn.com/cursor/KODIqSiRh6LRGwl9/images/cli/cookbook/code-review/github-actions.png?w=840&fit=max&auto=format&n=KODIqSiRh6LRGwl9&q=85&s=3c869c0ed8eb8b5743dd3821e57cd406 840w, https://mintcdn.com/cursor/KODIqSiRh6LRGwl9/images/cli/cookbook/code-review/github-actions.png?w=1100&fit=max&auto=format&n=KODIqSiRh6LRGwl9&q=85&s=19e98ed953f4cc17b2c578ce543cf88d 1100w, https://mintcdn.com/cursor/KODIqSiRh6LRGwl9/images/cli/cookbook/code-review/github-actions.png?w=1650&fit=max&auto=format&n=KODIqSiRh6LRGwl9&q=85&s=4d9f47472af81254bd09b5f6234fc97f 1650w, https://mintcdn.com/cursor/KODIqSiRh6LRGwl9/images/cli/cookbook/code-review/github-actions.png?w=2500&fit=max&auto=format&n=KODIqSiRh6LRGwl9&q=85&s=f3af19e3edd7f8bbbb77ba6566d8e183 2500w" />
</Frame>

<div id="next-steps">
  ## Sonraki adımlar
</div>

Artık çalışan bir otomatik kod inceleme sistemin var. Şunları da eklemeyi düşün:

* [CI hatalarını düzeltmek](/tr/cli/cookbook/fix-ci) için ek iş akışları kur
* Farklı dallar için farklı inceleme seviyeleri yapılandır
* Ekibinin mevcut kod inceleme süreciyle entegre et
* Farklı dosya türleri veya dizinler için agent'ın davranışını özelleştir

<Expandable title="Gelişmiş: Engelleyici incelemeler">
  Kritik sorunlar bulunduğunda iş akışını başarısız olacak şekilde yapılandırabilir, böylece ele alınıncaya kadar pull request'in birleştirilmesini engelleyebilirsin.

  **İsteme engelleyici davranış ekle**

  Önce, `BLOCKING_REVIEW` ortam değişkenini eklemek için inceleme agent'ı adımını güncelle ve bu engelleyici davranışı isteme ekle:

  ```
  Engelleyici davranış:
  - Eğer BLOCKING_REVIEW true ise ve herhangi bir 🚨 veya 🔒 sorun paylaşıldıysa: echo "CRITICAL_ISSUES_FOUND=true" >> $GITHUB_ENV
  - Aksi halde: echo "CRITICAL_ISSUES_FOUND=false" >> $GITHUB_ENV
  - Her zaman sonunda CRITICAL_ISSUES_FOUND değişkenini ayarla
  ```

  **Engelleyici kontrol adımını ekle**

  Ardından bu yeni adımı kod inceleme adımının sonrasına ekle:

  ```yaml  theme={null}
        - name: Check blocking review results
          if: env.BLOCKING_REVIEW == 'true'
          run: |
            echo "Checking for critical issues..."
            echo "CRITICAL_ISSUES_FOUND: ${CRITICAL_ISSUES_FOUND:-unset}"

            if [ "${CRITICAL_ISSUES_FOUND:-false}" = "true" ]; then
              echo "❌ Critical issues found and blocking review is enabled. Failing the workflow."
              exit 1
            else
              echo "✅ No blocking issues found."
            fi
  ```
</Expandable>

---

← Previous: [Bugbot](./bugbot.md) | [Index](./index.md) | Next: [CI Hatalarını Düzelt](./ci-hatalarn-dzelt.md) →