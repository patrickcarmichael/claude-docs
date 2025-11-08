---
title: "Slack"
source: "https://docs.cursor.com/tr/integrations/slack"
language: "tr"
language_name: "Turkish"
---

# Slack
Source: https://docs.cursor.com/tr/integrations/slack

Slack üzerinden Background Agents ile çalış

export const SlackThread = ({messages = []}) => {
  const MessageWithMentions = ({text}) => {
    const parts = text.split(/(@\w+)/g);
    return <>
        {parts.map((part, index) => {
      if (part.startsWith('@')) {
        return <span key={index} className="text-[#1264A3] bg-[#1264A3]/10 dark:bg-[#1264A3]/25 px-0.5 py-0.5 rounded hover:bg-[#1264A3]/20 cursor-pointer transition-colors">
                {part}
              </span>;
      }
      return <span key={index}>{part}</span>;
    })}
      </>;
  };
  return <div className="border border-neutral-200 dark:border-neutral-700 rounded-lg bg-neutral-50 dark:bg-neutral-900/50 py-4 overflow-hidden">
      {messages.map((msg, index) => <div key={index} className={`group hover:bg-[#f0f0f0] dark:hover:bg-[#333] px-6 py-2 -mx-2 -my-1 transition-colors`}>
          <div className="flex items-start gap-3">
            <div className="w-9 h-9 rounded-md bg-neutral-300 dark:bg-neutral-800 flex items-center justify-center text-white text-sm font-semibold flex-shrink-0">
              {msg.name ? msg.name.charAt(0).toUpperCase() : 'U'}
            </div>

            <div className="flex-1 min-w-0">
              <div className="flex items-baseline gap-2">
                <span className="font-semibold text-neutral-900 dark:text-neutral-100 text-sm">
                  {msg.name || 'User'}
                </span>
                <span className="text-xs text-neutral-500 dark:text-neutral-400">
                  {msg.timestamp || ''}
                </span>
              </div>
              <div className="text-neutral-900 dark:text-neutral-100 text-[15px] leading-relaxed">
                <MessageWithMentions text={msg.message} />
              </div>

              {msg.reactions && msg.reactions.length > 0 && <div className="flex gap-1 mt-1">
                  {msg.reactions.map((reaction, rIndex) => <div key={rIndex} className="inline-flex items-center gap-0.5 px-1.5 py-0.5 bg-white dark:bg-neutral-800 border border-neutral-200 dark:border-neutral-700 rounded text-xs hover:bg-neutral-100 dark:hover:bg-neutral-700 transition-colors cursor-pointer">
                      <span>{reaction.emoji}</span>
                      <span className="text-neutral-600 dark:text-neutral-400">{reaction.count}</span>
                    </div>)}
                </div>}
            </div>
          </div>
        </div>)}
    </div>;
};

export const SlackInlineMessage = ({message}) => {
  const MessageWithMentions = ({text}) => {
    const parts = text.split(/(@\w+)/g);
    return <>
        {parts.map((part, index) => {
      if (part.startsWith('@')) {
        return <span key={index} className="text-[#1264A3] hover:bg-[#1264A3]/10 dark:hover:bg-[#1264A3]/25 px-0.5 rounded">
                {part}
              </span>;
      }
      return <span key={index}>{part}</span>;
    })}
      </>;
  };
  return <span className="inline rounded p-0.5 bg-neutral-50 dark:bg-neutral-800/30">
      <MessageWithMentions text={message} />
    </span>;
};

export const SlackUserMessage = ({message, reactions = [], replies = null}) => {
  const MessageWithMentions = ({text}) => {
    const parts = text.split(/(@\w+)/g);
    return <>
        {parts.map((part, index) => {
      if (part.startsWith('@')) {
        return <span key={index} className="text-[#1264A3] bg-[#1264A3]/10 dark:bg-[#1264A3]/25 px-0.5 py-0.5 rounded hover:bg-[#1264A3]/20 cursor-pointer transition-colors">
                {part}
              </span>;
      }
      return <span key={index}>{part}</span>;
    })}
      </>;
  };
  return <div className="border border-neutral-200 dark:border-neutral-700 rounded-lg hover:bg-neutral-50 dark:hover:bg-neutral-800/50 transition-colors px-5 py-3 group">
      <div className="text-neutral-900 dark:text-neutral-100 text-[15px] leading-relaxed">
        <MessageWithMentions text={message} />
      </div>

      {reactions.length > 0 && <div className="flex gap-1 mt-1">
          {reactions.map((reaction, index) => <div key={index} className="inline-flex items-center gap-0.5 px-1.5 py-0.5 bg-neutral-100 dark:bg-neutral-800 rounded text-xs hover:bg-neutral-200 dark:hover:bg-neutral-700 transition-colors cursor-pointer">
              <span>{reaction.emoji}</span>
              <span className="text-neutral-600 dark:text-neutral-400">{reaction.count}</span>
            </div>)}
        </div>}

      {replies && <div className="flex items-center gap-1.5 mt-2 text-[#1264A3] hover:underline cursor-pointer">
          <svg className="w-4 h-4" fill="currentColor" viewBox="0 0 20 20">
            <path d="M7.707 10.293a1 1 0 10-1.414 1.414l3 3a1 1 0 001.414 0l3-3a1 1 0 00-1.414-1.414L11 11.586V6h5a2 2 0 012 2v7a2 2 0 01-2 2H4a2 2 0 01-2-2V8a2 2 0 012-2h5v5.586l-1.293-1.293z" />
          </svg>
          <span className="text-sm font-medium">{replies.count} {replies.count === 1 ? 'reply' : 'replies'}</span>
          {replies.lastReplyTime && <span className="text-xs text-neutral-500 dark:text-neutral-400">{replies.lastReplyTime}</span>}
        </div>}
    </div>;
};

Cursor'ın Slack entegrasyonuyla, [Background Agents](/tr/background-agent) sayesinde Slack’ten doğrudan görevlerinde çalışmak için bir istemle <SlackInlineMessage message="@Cursor" /> etiketleyebilirsin.

<Frame>
  <video src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-agent.mp4?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=aa7aa2681db1e363047334c6a8e33f72" controls autoplay muted loop data-path="images/background-agent/slack/slack-agent.mp4" />
</Frame>

<div id="get-started">
  ## Başlarken
</div>

<div id="installation">
  ### Kurulum
</div>

1. [Cursor integrations](https://www.cursor.com/en/dashboard?tab=integrations) sayfasına git

2. Slack’in yanındaki *Connect* düğmesine tıkla ya da buradan [installation page](https://cursor.com/api/install-slack-app) sayfasına geç

3. Çalışma alanında Slack için Cursor uygulamasını yüklemen istenecek.

4. Slack’te yükledikten sonra kurulumu tamamlamak için Cursor’a geri yönlendirileceksin

   1. GitHub’ı bağla (henüz bağlı değilse) ve varsayılan bir repository seç
   2. Kullanıma dayalı fiyatlandırmayı etkinleştir
   3. Gizlilik ayarlarını onayla

5. <SlackInlineMessage message="@Cursor" /> şeklinde bahsederek Slack’te Background Agents kullanmaya başla

<Frame>
  <video src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/cursor-slack-install.mp4?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=bd5b3c65b1a0de08b46c90515b6056a6" controls autoplay muted loop data-path="images/background-agent/slack/cursor-slack-install.mp4" />
</Frame>

<div id="how-to-use">
  ## Nasıl kullanılır
</div>

<SlackInlineMessage message="@Cursor" /> diye bahset ve prompt’unu yaz. Bu çoğu kullanım durumunu karşılar, ama ajanını özelleştirmek için aşağıdaki komutları da kullanabilirsin.

Örneğin, sohbetin içinde doğrudan <SlackInlineMessage message="@Cursor fix the login bug" /> diyebilir ya da belirli bir depoyu hedeflemek için <SlackInlineMessage message="@Cursor [repo=torvalds/linux] fix bug" /> gibi spesifik komutlar kullanabilirsin.

<div id="commands">
  ### Komutlar
</div>

Güncel komut listesi için <SlackInlineMessage message="@Cursor help" /> çalıştır.

<div className="full-width-table">
  | Komut                                                       | Açıklama                                                                                              |
  | :---------------------------------------------------------- | :---------------------------------------------------------------------------------------------------- |
  | <SlackInlineMessage message="@Cursor [prompt]" />           | Bir Background Agent başlatır. İlgili ajanların bulunduğu konuşma dizilerinde takip talimatları ekler |
  | <SlackInlineMessage message="@Cursor settings" />           | Varsayılanları ve kanalın varsayılan deposunu yapılandırır                                            |
  | <SlackInlineMessage message="@Cursor [options] [prompt]" /> | Gelişmiş seçenekleri kullan: `branch`, `model`, `repo`                                                |
  | <SlackInlineMessage message="@Cursor agent [prompt]" />     | Bir dizide yeni bir ajan oluşturmayı zorlar                                                           |
  | <SlackInlineMessage message="@Cursor list my agents" />     | Çalışan ajanlarını gösterir                                                                           |
</div>

<div id="options">
  #### Seçenekler
</div>

Background Agent davranışını şu seçeneklerle özelleştir:

<div className="full-width-table">
  | Seçenek  | Açıklama                         | Örnek             |
  | :------- | :------------------------------- | :---------------- |
  | `branch` | Temel branch’i belirt            | `branch=main`     |
  | `model`  | AI modelini seç                  | `model=o3`        |
  | `repo`   | Belirli bir depoyu hedefle       | `repo=owner/repo` |
  | `autopr` | Otomatik PR oluşturmayı aç/kapat | `autopr=false`    |
</div>

<div id="syntax-formats">
  ##### Söz dizimi biçimleri
</div>

Seçenekleri birkaç şekilde kullan:

1. **Köşeli parantez biçimi**

   <SlackInlineMessage message="@Cursor [branch=dev, model=o3, repo=owner/repo, autopr=false] Fix the login bug" />

2. **Satır içi biçim**
   <SlackInlineMessage message="@Cursor branch=dev model=o3 repo=owner/repo autopr=false Fix the login bug" />

<div id="option-precedence">
  ##### Seçenek önceliği
</div>

Seçenekleri birleştirirken:

* **Açıkça belirtilen değerler** varsayılanları geçersiz kılar
* **Sonraki değerler**, yinelenmişse önceki değerleri geçersiz kılar
* **Satır içi seçenekler**, ayarlar modalindeki varsayılanlara üstün gelir

Bot, doğal komut yazımına izin vererek mesajın herhangi bir yerinden seçenekleri ayrıştırır.

<div id="using-thread-context">
  #### Konu (thread) bağlamını kullanma
</div>

Background Agent’lar mevcut konu tartışmalarının bağlamını anlar ve kullanır. Ekibin bir sorunu tartıştığı ve ajanın çözümü o konuşmaya dayanarak uygulamasını istediğin durumlarda işine yarar.

<SlackThread
  messages={[
{
  message:
    "Hey team, we're getting reports that users can't log in after the latest deploy",
  timestamp: "2:30 PM",
  name: "Sarah",
},
{
  message:
    "I checked the logs - looks like the auth token validation is failing on line 247 of auth.js",
  timestamp: "2:32 PM",
  name: "Mike",
},
{
  message:
    "Oh, I think it's because we changed the token format but didn't update the validation regex",
  timestamp: "2:33 PM",
  name: "Alex",
},
{
  message:
    "Yeah, the regex still expects the old format. We need to update it to handle both old and new formats for backwards compatibility",
  timestamp: "2:35 PM",
  name: "Sarah",
},
{
  message: "@Cursor fix this",
  timestamp: "2:36 PM",
  name: "You",
  reactions: [{ emoji: "⏳", count: 1 }],
},
]}
/>

<Note>
  Background Agent’lar çağrıldığında bağlam için tüm konuyu okur,
  ekibin tartışmasına dayanarak çözümleri anlar ve uygular.
</Note>

<div id="when-to-use-force-commands">
  #### Zorlama komutları ne zaman kullanılır
</div>

**Ne zaman <SlackInlineMessage message="@Cursor agent" /> gerekir?**

Var olan ajanların bulunduğu konularda <SlackInlineMessage message="@Cursor [prompt]" /> takip talimatları ekler (sadece ajanın sahibiyse çalışır). Ayrı bir ajan başlatmak için <SlackInlineMessage message="@Cursor agent [prompt]" /> kullan.

**Ne zaman `Add follow-up` (bağlam menüsünden) gerekir?**

Takip talimatları için bir ajanın yanıtındaki bağlam menüsünü (⋯) kullan. Bir konuda birden fazla ajan olduğunda ve hangisine takip yapılacağını belirtmen gerektiğinde kullanışlıdır.

<div id="status-updates-handoff">
  ### Durum güncellemeleri ve devretme
</div>

Background Agent çalıştığında, önce *Cursor’da Aç* seçeneği gelir.

<Frame>
  <img className="p-2" src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-open-in-cursor.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=496d3775ca5cc1e20dd1dc34952f76fd" style={{ backgroundColor: "#1b1d21" }} data-og-width="1236" width="1236" data-og-height="258" height="258" data-path="images/background-agent/slack/slack-open-in-cursor.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-open-in-cursor.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=9136ecf72e3f7e75b2178a2922878fbd 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-open-in-cursor.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=5d6977f43055c3e8cb69071fe7b48367 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-open-in-cursor.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=5264cb584c1160bd8ac3cdeaae320777 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-open-in-cursor.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=a065e6c1a08d4413464e1251eab1b2a6 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-open-in-cursor.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=e067f0dc80ed77bce7843f777f2d7970 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-open-in-cursor.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=fbcb8e474fd1681219964c558ea2952d 2500w" />
</Frame>

Background Agent tamamlandığında, Slack’te bir bildirim alırsın ve GitHub’da oluşturulan PR’ı görüntüleyebilirsin.

<Frame>
  <img className="p-2" src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-view-pr.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=d0f5f15094f682a5617c936bea88db3d" style={{ backgroundColor: "#1b1d21" }} data-og-width="1272" width="1272" data-og-height="496" height="496" data-path="images/background-agent/slack/slack-view-pr.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-view-pr.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=a51c98f13fef794ba8f54a28ad42e99d 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-view-pr.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=bbde7fe552a04a8ed44b1771bbc3f55c 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-view-pr.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=616811c969184b9061435e9753f63ddb 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-view-pr.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=90fe4582797d75782019c7d0c3232ea8 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-view-pr.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=ffe4d6a78cad700f82e770418c7f6e13 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-view-pr.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=ec4dac244e5982d0150d058ddac0d205 2500w" />
</Frame>

<div id="managing-agents">
  ### Agent’leri yönetme
</div>

Çalışan tüm agent’leri görmek için <SlackInlineMessage message="@Cursor list my agents" /> komutunu çalıştır.

Herhangi bir agent mesajındaki üç noktaya (⋯) tıklayarak bağlam menüsünden Background Agent’leri yönet.

<Frame>
  <img className="p-2" src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-context-menu.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=9a92748d0f4d3450d51a2c2cdd989eb1" style={{ backgroundColor: "#1b1d21" }} data-og-width="1982" width="1982" data-og-height="1498" height="1498" data-path="images/background-agent/slack/slack-context-menu.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-context-menu.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=6af034b2f0c1b510510622b111c8d4e7 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-context-menu.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=7d28c9785328aa414eba66704d7f4f08 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-context-menu.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=810f99ed15ec100cdfee183ef9b7f827 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-context-menu.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=f4c00c380996793b50d31ef3ac95219c 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-context-menu.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=94bccdd7d7a9f1301fdb4e832e008efa 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-context-menu.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=90e628735b628ec71d5a78547db2441c 2500w" />
</Frame>

Kullanılabilir seçenekler:

* **Add follow-up**: Var olan bir agent’e talimat ekle
* **Delete**: Background Agent’i durdur ve arşivle
* **View request ID**: Sorun gidermeye yönelik benzersiz istek kimliğini görüntüle (destekle iletişime geçerken ekle)
* **Give feedback**: Agent performansı hakkında geri bildirim ver

<div id="configuration">
  ## Yapılandırma
</div>

Varsayılan ayarları ve gizlilik seçeneklerini [Dashboard → Background Agents](https://www.cursor.com/dashboard?tab=background-agents) üzerinden yönet.

<div id="settings">
  ### Ayarlar
</div>

<div id="default-model">
  #### Varsayılan Model
</div>

<SlackInlineMessage message="@Cursor [model=...]" /> ile açıkça bir model belirtilmediğinde kullanılır. Mevcut seçenekler için [settings](https://www.cursor.com/dashboard?tab=background-agents) sayfasına bak.

<div id="default-repository">
  #### Varsayılan Depo
</div>

Herhangi bir depo belirtilmediğinde kullanılır. Şu biçimleri kullan:

* `https://github.com/org/repository`
* `org/repository`

<Note>
  Var olmayan bir depoya referans verirsen, sanki erişimin yokmuş gibi
  görünür. Bu, Background Agent başlatılamadığında hata mesajında gösterilir.
</Note>

<div id="base-branch">
  #### Temel Dal
</div>

Background Agent için başlangıç dalı. Depodaki varsayılan dalı (genellikle `main`) kullanmak için boş bırak.

<div id="channel-settings">
  ### Kanal Ayarları
</div>

<SlackInlineMessage message="@Cursor settings" /> kullanarak kanal düzeyinde varsayılan ayarları yapılandır. Bu ayarlar ekip bazındadır ve o kanal için kişisel varsayılanlarını geçersiz kılar.

Şu durumlarda özellikle kullanışlıdır:

* Farklı kanallar farklı depolar üzerinde çalışıyorsa
* Ekipler tüm üyelerde tutarlı ayarlar istiyorsa
* Her komutta depoyu belirtmekten kaçınmak istiyorsan

Kanal ayarlarını yapılandırmak için:

1. İstediğin kanalda <SlackInlineMessage message="@Cursor settings" /> çalıştır
2. O kanal için varsayılan depoyu ayarla
3. O kanalda Background Agents kullanan tüm ekip üyeleri bu varsayılanları kullanır

<Note>
  Kanal ayarları kişisel varsayılanlardan daha önceliklidir ancak{" "}
  <SlackInlineMessage message="@Cursor [repo=...] [prompt]" /> gibi açık seçeneklerle
  geçersiz kılınabilir
</Note>

<div id="privacy">
  ### Gizlilik
</div>

Background Agents, Privacy Mode'u destekler.

[Privacy Mode](https://www.cursor.com/privacy-overview) hakkında daha fazla bilgi al veya [privacy settings](https://www.cursor.com/dashboard?tab=background-agents) ayarlarını yönet.

<Warning>
  Eski Privacy Mode (Legacy) desteklenmez. Background Agents çalışırken geçici
  kod depolamasına ihtiyaç duyar.
</Warning>

<div id="display-agent-summary">
  #### Agent Özetini Göster
</div>

Agent özetlerini ve diff görsellerini gösterir. Dosya yolları veya kod parçacıkları içerebilir. Açık/Kapalı yapılabilir.

<div id="display-agent-summary-in-external-channels">
  #### Dış Kanallarda Agent Özetini Göster
</div>

Diğer çalışma alanlarıyla Slack Connect üzerinden veya Misafir gibi dış üyelerin bulunduğu kanallar için, agent özetlerinin dış kanallarda gösterilip gösterilmeyeceğini seç.

<div id="permissions">
  ## İzinler
</div>

Background Agents'ın çalışma alanında çalışabilmesi için Cursor şu Slack izinlerini ister:

<div className="full-width-table">
  | Permission          | Açıklama                                                                                         |
  | :------------------ | :----------------------------------------------------------------------------------------------- |
  | `app_mentions:read` | Background Agents'ı başlatmak ve isteklere yanıt vermek için @bahsetmeleri algılar               |
  | `channels:history`  | Ek takip talimatları eklerken bağlam sağlamak için dizilerdeki önceki mesajları okur             |
  | `channels:join`     | Davet edildiğinde veya istendiğinde herkese açık kanallara otomatik olarak katılır               |
  | `channels:read`     | Yanıt ve güncelleme göndermek için kanal meta verilerine (kimlikler ve adlar) erişir             |
  | `chat:write`        | Ajanlar tamamladığında durum güncellemeleri, tamamlanma bildirimleri ve PR bağlantıları gönderir |
  | `files:read`        | Ek bağlam için paylaşılan dosyaları (loglar, ekran görüntüleri, kod örnekleri) indirir           |
  | `files:write`       | Hızlı inceleme için ajan değişikliklerinin görsel özetlerini yükler                              |
  | `groups:history`    | Çok turlu konuşmalarda bağlam sağlamak için özel kanallardaki önceki mesajları okur              |
  | `groups:read`       | Yanıt göndermek ve konuşma akışını sürdürmek için özel kanal meta verilerine erişir              |
  | `im:history`        | Devam eden konuşmalarda bağlam sağlamak için direkt mesaj geçmişine erişir                       |
  | `im:read`           | Katılımcıları belirlemek ve doğru iş parçacığı düzenini korumak için DM meta verilerini okur     |
  | `im:write`          | Özel bildirimler veya bire bir iletişim için direkt mesaj başlatır                               |
  | `mpim:history`      | Çok katılımcılı konuşmalar için grup DM geçmişine erişir                                         |
  | `mpim:read`         | Katılımcılara hitap etmek ve doğru iletimi sağlamak için grup DM meta verilerini okur            |
  | `reactions:read`    | Kullanıcı geri bildirimi ve durum sinyalleri için emoji tepkilerini gözlemler                    |
  | `reactions:write`   | Durumu belirtmek için emoji tepkileri ekler — ⏳ çalışıyor, ✅ tamamlandı, ❌ başarısız             |
  | `team:read`         | Kurulumları ayırmak ve ayarları uygulamak için çalışma alanı ayrıntılarını belirler              |
  | `users:read`        | İzinler ve güvenli erişim için Slack kullanıcılarını Cursor hesaplarıyla eşleştirir              |
</div>

---

← Previous: [Linear](./linear.md) | [Index](./index.md) | Next: [Modeller](./modeller.md) →