---
title: "Linear"
source: "https://docs.cursor.com/tr/integrations/linear"
language: "tr"
language_name: "Turkish"
---

# Linear
Source: https://docs.cursor.com/tr/integrations/linear

Linear üzerinden Arka Plan Ajanlarıyla çalış

[Arka Plan Ajanları](/tr/background-agent)'nı Linear'dan doğrudan kullan; işleri Cursor'a devret ya da yorumlarda `@Cursor`'ı mentionla.

<Frame>
  <video src="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-agent.mp4?fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=ac4bacf6bf42c541f45325ba72f8c25f" controls autoPlay muted loop playsInline data-path="images/integrations/linear/linear-agent.mp4" />
</Frame>

<div id="get-started">
  ## Başlarken
</div>

<div id="installation">
  ### Kurulum
</div>

<Note>
  Linear entegrasyonunu bağlamak için Cursor yöneticisi olman gerekiyor. Diğer ekip ayarları yönetici olmayan üyeler için de kullanılabilir.
</Note>

1. [Cursor integrations](https://www.cursor.com/en/dashboard?tab=integrations) sayfasına git
2. Linear’ın yanındaki *Connect* düğmesine tıkla
3. Linear çalışma alanını bağla ve ekibi seç
4. *Authorize* düğmesine tıkla
5. Cursor’da kalan Background Agent kurulumunu tamamla:
   * GitHub’ı bağla ve varsayılan depoyu seç
   * Kullanım tabanlı fiyatlandırmayı etkinleştir
   * Gizlilik ayarlarını onayla

<div id="account-linking">
  ### Hesap bağlantısı
</div>

İlk kullanımda Cursor ile Linear arasında hesap bağlantısı gerekir. PR oluşturmak için GitHub bağlantısı zorunludur.

<div id="how-to-use">
  ## Nasıl kullanılır
</div>

İşleri Cursor’a devret ya da yorumlarda `@Cursor`’dan bahset. Cursor, işleri analiz eder ve geliştirme dışı işleri otomatik olarak filtreler.

<div id="delegating-issues">
  ### İşleri devretme
</div>

1. Linear’da ilgili işi aç
2. Atanan kişi (assignee) alanına tıkla
3. "Cursor"ı seç

<Frame>
  <img src="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-delegate.png?fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=c9a6536a083cfe4a7798c626360e53cc" alt="Linear’da bir işi Cursor’a devretme" data-og-width="1637" width="1637" data-og-height="1046" height="1046" data-path="images/integrations/linear/linear-delegate.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-delegate.png?w=280&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=b30e2ccb68c4a15b921cf86721878676 280w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-delegate.png?w=560&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=1ac5dfd75e06451de0e688ff87e1ce4c 560w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-delegate.png?w=840&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=7393e80c07e1fe5c33690a970029fe31 840w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-delegate.png?w=1100&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=2a07cc74a1d65581a341cf2225b51a37 1100w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-delegate.png?w=1650&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=5684841fe823ef85472f74748730278c 1650w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-delegate.png?w=2500&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=9f7818cae47a652e14557eb20f20b04e 2500w" />
</Frame>

<div id="mentioning-cursor">
  ### Cursor’dan bahsetme
</div>

Yeni bir agent atamak ya da ek talimat vermek için bir yorumda `@Cursor`’dan bahset, örneğin: `@Cursor yukarıda açıklanan kimlik doğrulama hatasını düzelt`.

<div id="workflow">
  ## İş Akışı
</div>

Background Agents, Linear’da gerçek zamanlı durum gösterir ve tamamlandığında PR’leri otomatik olarak açar. İlerlemeyi [Cursor panosunda](https://www.cursor.com/dashboard?tab=background-agents) takip et.

<Frame>
  <img src="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-activity.png?fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=eecf562be6db4d44c397f4786b8ef273" alt="Linear’da Background Agent durum güncellemeleri" data-og-width="3456" width="3456" data-og-height="2158" height="2158" data-path="images/integrations/linear/linear-activity.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-activity.png?w=280&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=238da245aee71392f22644cb85f7cee4 280w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-activity.png?w=560&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=e21f515fbd2e5917fcf63b8801f66307 560w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-activity.png?w=840&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=9f88441301e6d614ba47756cb886e023 840w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-activity.png?w=1100&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=4927a8d00768a3dbbc0bd5be1faad80e 1100w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-activity.png?w=1650&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=1707f8223126480c46639428ad5fc85a 1650w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-activity.png?w=2500&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=74ca2ad37e8158bbb86188821bf96299 2500w" />
</Frame>

<div id="follow-up-instructions">
  ### Takip talimatları
</div>

Agent oturumunda yanıt verebilirsin; bu yanıt agent’a takip olarak iletilir. Çalışan bir Background Agent’a ek yönlendirme vermek için Linear yorumunda `@Cursor`’ı mention’la.

<div id="configuration">
  ## Yapılandırma
</div>

[Dashboard → Background Agents](https://www.cursor.com/dashboard?tab=background-agents) üzerinden Background Agent ayarlarını yapılandır.

<div className="full-width-table">
  | Ayar                 | Konum            | Açıklama                                                               |
  | :------------------- | :--------------- | :--------------------------------------------------------------------- |
  | **Varsayılan Depo**  | Cursor Dashboard | Herhangi bir proje deposu tanımlanmadığında kullanılacak birincil depo |
  | **Varsayılan Model** | Cursor Dashboard | Background Agents için kullanılacak AI modeli                          |
  | **Temel Dal**        | Cursor Dashboard | PR’lerin oluşturulacağı dal (genellikle `main` veya `develop`)         |
</div>

<div id="configuration-options">
  ### Yapılandırma seçenekleri
</div>

Background Agent davranışını birkaç yöntemle ayarlayabilirsin:

**Issue açıklaması veya yorumlar**: `[key=value]` sözdizimini kullan, örneğin:

* `@cursor please fix [repo=anysphere/everysphere]`
* `@cursor implement feature [model=claude-3.5-sonnet] [branch=feature-branch]`

**Issue etiketleri**: Üst etiketin yapılandırma anahtarı, alt etiketin değer olduğu ebeveyn-çocuk etiket yapısını kullan.

**Proje etiketleri**: Issue etiketleriyle aynı ebeveyn-çocuk yapı, proje düzeyinde uygulanır.

Desteklenen yapılandırma anahtarları:

* `repo`: Hedef depoyu belirt (ör. `owner/repository`)
* `branch`: PR oluşturmak için temel dalı belirt
* `model`: Kullanılacak AI modelini belirt

<div id="repository-selection">
  ### Depo seçimi
</div>

Cursor, çalışılacak depoyu şu öncelik sırasıyla belirler:

1. **Issue açıklaması/yorumları**: Issue metninde veya yorumlarda `[repo=owner/repository]` sözdizimi
2. **Issue etiketleri**: İlgili Linear issue’una ekli depo etiketleri
3. **Proje etiketleri**: Linear projesine ekli depo etiketleri
4. **Varsayılan depo**: Cursor dashboard ayarlarında belirtilen depo

<div id="setting-up-repository-labels">
  #### Depo etiketlerini ayarlama
</div>

Linear’da depo etiketleri oluşturmak için:

1. Linear çalışma alanında **Settings**’e git
2. **Labels**’a tıkla
3. **New group**’a tıkla
4. Gruba “repo” adını ver (büyük/küçük harfe duyarsız — tam olarak “repo” olmalı, “Repository” veya diğer varyasyonlar değil)
5. Bu grubun içinde her depo için `owner/repo` formatını kullanarak etiketler oluştur

Bu etiketler, Background Agent’ın hangi depoda çalışması gerektiğini belirtmek için issue’lara veya projelere atanabilir.

<Frame>
  <img src="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-project-labels.png?fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=6e2b90ce09957a72fdef3c1ed4ef93aa" alt="Linear’da depo etiketlerini yapılandırma" data-og-width="3456" width="3456" data-og-height="2158" height="2158" data-path="images/integrations/linear/linear-project-labels.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-project-labels.png?w=280&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=1933d2112631527116bd1d817f1a6153 280w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-project-labels.png?w=560&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=93f344ff848172ce6bd97ef652ab03de 560w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-project-labels.png?w=840&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=ea9f19d7248f39086a20606c6ec14ac6 840w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-project-labels.png?w=1100&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=55bfa5cf5b87def6cbe51c3345579eee 1100w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-project-labels.png?w=1650&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=d99c0f06c5fbf33794408350b143f655 1650w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-project-labels.png?w=2500&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=b1f731d1978dc5e60c545b745bb9d8ad 2500w" />
</Frame>

{/* ### Getting help

  Check [agent activity](https://www.cursor.com/dashboard?tab=background-agents) and include request IDs when contacting support.

  ## Feedback

  Share feedback through Linear comments or your Cursor dashboard support channels. */}

---

← Previous: [GitHub](./github.md) | [Index](./index.md) | Next: [Slack](./slack.md) →