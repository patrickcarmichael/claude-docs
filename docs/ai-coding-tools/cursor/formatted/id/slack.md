---
title: "Slack"
source: "https://docs.cursor.com/id/integrations/slack"
language: "id"
language_name: "Indonesian"
---

# Slack
Source: https://docs.cursor.com/id/integrations/slack

Gunakan Background Agents langsung dari Slack

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

Dengan integrasi Cursor untuk Slack, lo bisa pakai [Background Agents](/id/background-agent) buat ngerjain tugas langsung dari Slack dengan nge-mention <SlackInlineMessage message="@Cursor" /> plus prompt.

<Frame>
  <video src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-agent.mp4?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=aa7aa2681db1e363047334c6a8e33f72" controls autoplay muted loop data-path="images/background-agent/slack/slack-agent.mp4" />
</Frame>

<div id="get-started">
  ## Mulai
</div>

<div id="installation">
  ### Instalasi
</div>

1. Buka [Cursor integrations](https://www.cursor.com/en/dashboard?tab=integrations)

2. Klik *Connect* di sebelah Slack atau langsung ke [halaman instalasi](https://cursor.com/api/install-slack-app) dari sini

3. Lo bakal diminta buat install aplikasi Cursor untuk Slack di workspace lo.

4. Setelah install di Slack, lo bakal diarahkan balik ke Cursor buat nyelesaiin setup

   1. Hubungin GitHub (kalau belum terhubung) dan pilih repo default
   2. Aktifin pricing berbasis usage
   3. Konfirmasi pengaturan privasi

5. Mulai pakai Background Agents di Slack dengan mention <SlackInlineMessage message="@Cursor" />

<Frame>
  <video src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/cursor-slack-install.mp4?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=bd5b3c65b1a0de08b46c90515b6056a6" controls autoplay muted loop data-path="images/background-agent/slack/cursor-slack-install.mp4" />
</Frame>

<div id="how-to-use">
  ## Cara menggunakan
</div>

Mention <SlackInlineMessage message="@Cursor" /> dan kasih prompt lo. Ini udah ngurusin sebagian besar use case, tapi lo juga bisa pakai perintah di bawah buat ngekustom agen lo.

Contohnya, mention <SlackInlineMessage message="@Cursor fix the login bug" /> langsung di percakapan, atau pakai perintah spesifik kayak <SlackInlineMessage message="@Cursor [repo=torvalds/linux] fix bug" /> buat nargetin repository tertentu.

<div id="commands">
  ### Perintah
</div>

Jalankan <SlackInlineMessage message="@Cursor help" /> buat dapetin daftar perintah terbaru.

<div className="full-width-table">
  | Command                                                     | Description                                                                                |
  | :---------------------------------------------------------- | :----------------------------------------------------------------------------------------- |
  | <SlackInlineMessage message="@Cursor [prompt]" />           | Mulai Background Agent. Di thread yang sudah ada agennya, nambahin instruksi tindak lanjut |
  | <SlackInlineMessage message="@Cursor settings" />           | Konfigurasi default dan repository default channel                                         |
  | <SlackInlineMessage message="@Cursor [options] [prompt]" /> | Pakai opsi lanjutan: `branch`, `model`, `repo`                                             |
  | <SlackInlineMessage message="@Cursor agent [prompt]" />     | Paksa bikin agen baru di sebuah thread                                                     |
  | <SlackInlineMessage message="@Cursor list my agents" />     | Tampilkan agen lo yang lagi jalan                                                          |
</div>

<div id="options">
  #### Opsi
</div>

Kustomisasi perilaku Background Agent dengan opsi berikut:

<div className="full-width-table">
  | Option   | Description                              | Example           |
  | :------- | :--------------------------------------- | :---------------- |
  | `branch` | Tentuin base branch                      | `branch=main`     |
  | `model`  | Pilih model AI                           | `model=o3`        |
  | `repo`   | Nargetin repository tertentu             | `repo=owner/repo` |
  | `autopr` | Aktifin/nonaktifin pembuatan PR otomatis | `autopr=false`    |
</div>

<div id="syntax-formats">
  ##### Format sintaks
</div>

Pakai opsi dengan beberapa cara:

1. **Format bracket**

   <SlackInlineMessage message="@Cursor [branch=dev, model=o3, repo=owner/repo, autopr=false] Fix the login bug" />

2. **Format inline**
   <SlackInlineMessage message="@Cursor branch=dev model=o3 repo=owner/repo autopr=false Fix the login bug" />

<div id="option-precedence">
  ##### Prioritas opsi
</div>

Kalau nggabungin opsi:

* **Nilai eksplisit** ngeganti default
* **Nilai yang muncul belakangan** ngeganti yang lebih awal kalau duplikat
* **Opsi inline** punya prioritas dibanding default di settings modal

Bot nge-parse opsi dari mana pun di pesan, bikin lo bisa nulis perintah secara natural.

<div id="using-thread-context">
  #### Pakai konteks thread
</div>

Background Agents paham dan pakai konteks dari diskusi thread yang udah ada. Berguna pas tim lo ngebahas suatu issue dan lo mau agen nge-implement solusi berdasarkan percakapan itu.

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
  Background Agents bakal baca seluruh thread buat konteks saat dipanggil,
  ngerti dan ngejalanin solusi berdasarkan diskusi tim.
</Note>

<div id="when-to-use-force-commands">
  #### Kapan pakai perintah paksa
</div>

**Kapan gue perlu <SlackInlineMessage message="@Cursor agent" />?**

Di thread yang sudah ada agennya, <SlackInlineMessage message="@Cursor [prompt]" /> nambahin instruksi tindak lanjut (cuma jalan kalau lo pemilik agennya). Pakai <SlackInlineMessage message="@Cursor agent [prompt]" /> buat ngeluncurin agen terpisah.

**Kapan gue perlu `Add follow-up` (dari context menu)?**

Pakai context menu (⋯) di respons agen buat instruksi tindak lanjut. Berguna kalau ada banyak agen di satu thread dan lo perlu nentuin yang mana yang mau di-follow up.

### Status update & handoff

Saat Background Agent jalan, pertama lo bakal dapet opsi buat *Open in Cursor*.

<Frame>
  <img className="p-2" src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-open-in-cursor.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=496d3775ca5cc1e20dd1dc34952f76fd" style={{ backgroundColor: "#1b1d21" }} data-og-width="1236" width="1236" data-og-height="258" height="258" data-path="images/background-agent/slack/slack-open-in-cursor.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-open-in-cursor.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=9136ecf72e3f7e75b2178a2922878fbd 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-open-in-cursor.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=5d6977f43055c3e8cb69071fe7b48367 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-open-in-cursor.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=5264cb584c1160bd8ac3cdeaae320777 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-open-in-cursor.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=a065e6c1a08d4413464e1251eab1b2a6 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-open-in-cursor.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=e067f0dc80ed77bce7843f777f2d7970 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-open-in-cursor.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=fbcb8e474fd1681219964c558ea2952d 2500w" />
</Frame>

Saat Background Agent selesai, kamu bakal dapat notifikasi di Slack dan opsi buat melihat PR yang dibuat di GitHub.

<Frame>
  <img className="p-2" src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-view-pr.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=d0f5f15094f682a5617c936bea88db3d" style={{ backgroundColor: "#1b1d21" }} data-og-width="1272" width="1272" data-og-height="496" height="496" data-path="images/background-agent/slack/slack-view-pr.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-view-pr.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=a51c98f13fef794ba8f54a28ad42e99d 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-view-pr.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=bbde7fe552a04a8ed44b1771bbc3f55c 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-view-pr.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=616811c969184b9061435e9753f63ddb 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-view-pr.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=90fe4582797d75782019c7d0c3232ea8 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-view-pr.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=ffe4d6a78cad700f82e770418c7f6e13 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-view-pr.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=ec4dac244e5982d0150d058ddac0d205 2500w" />
</Frame>

<div id="managing-agents">
  ### Mengelola agent
</div>

Buat lihat semua agent yang sedang berjalan, jalankan <SlackInlineMessage message="@Cursor list my agents" />.

Kelola Background Agents lewat menu konteks dengan klik tiga titik (⋯) di pesan agent mana pun.

<Frame>
  <img className="p-2" src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-context-menu.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=9a92748d0f4d3450d51a2c2cdd989eb1" style={{ backgroundColor: "#1b1d21" }} data-og-width="1982" width="1982" data-og-height="1498" height="1498" data-path="images/background-agent/slack/slack-context-menu.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-context-menu.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=6af034b2f0c1b510510622b111c8d4e7 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-context-menu.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=7d28c9785328aa414eba66704d7f4f08 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-context-menu.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=810f99ed15ec100cdfee183ef9b7f827 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-context-menu.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=f4c00c380996793b50d31ef3ac95219c 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-context-menu.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=94bccdd7d7a9f1301fdb4e832e008efa 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-context-menu.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=90e628735b628ec71d5a78547db2441c 2500w" />
</Frame>

Opsi yang tersedia:

* **Add follow-up**: Tambahkan instruksi ke agent yang sudah ada
* **Delete**: Hentikan dan arsipkan Background Agent
* **View request ID**: Lihat ID permintaan unik untuk troubleshooting (sertakan saat menghubungi support)
* **Give feedback**: Kasih feedback tentang performa agent

<div id="configuration">
  ## Konfigurasi
</div>

Kelola pengaturan default dan opsi privasi dari [Dashboard → Background Agents](https://www.cursor.com/dashboard?tab=background-agents).

<div id="settings">
  ### Pengaturan
</div>

<div id="default-model">
  #### Model Default
</div>

Digunakan ketika tidak ada model yang secara eksplisit ditentukan dengan <SlackInlineMessage message="@Cursor [model=...]" />. Lihat [pengaturan](https://www.cursor.com/dashboard?tab=background-agents) untuk opsi yang tersedia.

<div id="default-repository">
  #### Repositori Default
</div>

Digunakan ketika tidak ada repositori yang ditentukan. Gunakan format berikut:

* `https://github.com/org/repository`
* `org/repository`

<Note>
  Jika kamu mereferensikan repositori yang tidak ada, itu akan terlihat seolah-olah kamu
  tidak punya akses. Hal ini muncul di pesan error ketika Background Agent gagal memulai.
</Note>

<div id="base-branch">
  #### Base Branch
</div>

Branch awal untuk Background Agent. Biarkan kosong untuk menggunakan branch default repositori (biasanya `main`)

<div id="channel-settings">
  ### Pengaturan Channel
</div>

Konfigurasikan pengaturan default di level channel menggunakan <SlackInlineMessage message="@Cursor settings" />. Pengaturan ini per tim dan akan override default personal kamu untuk channel tersebut.

Sangat berguna ketika:

* Channel yang berbeda mengerjakan repositori yang berbeda
* Tim ingin pengaturan konsisten di semua anggota
* Kamu ingin menghindari menetapkan repositori di setiap perintah

Untuk mengonfigurasi pengaturan channel:

1. Jalankan <SlackInlineMessage message="@Cursor settings" /> di channel yang diinginkan
2. Tetapkan repositori default untuk channel tersebut
3. Semua anggota tim yang menggunakan Background Agents di channel itu akan memakai default ini

<Note>
  Pengaturan channel memiliki prioritas di atas default personal, tetapi bisa di-override
  oleh opsi eksplisit seperti{" "}

  <SlackInlineMessage message="@Cursor [repo=...] [prompt]" />
</Note>

<div id="privacy">
  ### Privasi
</div>

Background Agents mendukung Privacy Mode.

Baca lebih lanjut tentang [Privacy Mode](https://www.cursor.com/privacy-overview) atau kelola [pengaturan privasi](https://www.cursor.com/dashboard?tab=background-agents) kamu.

<Warning>
  Privacy Mode (Legacy) tidak didukung. Background Agents memerlukan penyimpanan
  kode sementara saat berjalan.
</Warning>

<div id="display-agent-summary">
  #### Tampilkan Ringkasan Agent
</div>

Tampilkan ringkasan agent dan gambar diff. Mungkin berisi path file atau potongan kode. Bisa dinyalakan/dimatikan.

<div id="display-agent-summary-in-external-channels">
  #### Tampilkan Ringkasan Agent di Channel Eksternal
</div>

Untuk Slack Connect dengan workspace lain atau channel dengan anggota eksternal seperti Guest, pilih untuk menampilkan ringkasan agent di channel eksternal.

<div id="permissions">
  ## Permissions
</div>

Cursor minta izin Slack berikut biar Background Agents bisa jalan di workspace lo:

<div className="full-width-table">
  | Permission          | Description                                                                       |
  | :------------------ | :-------------------------------------------------------------------------------- |
  | `app_mentions:read` | Ngedeteksi @mention buat mulai Background Agents dan ngerespons request           |
  | `channels:history`  | Baca pesan sebelumnya di thread buat konteks saat nambahin instruksi lanjutan     |
  | `channels:join`     | Otomatis join ke public channel saat diundang atau diminta                        |
  | `channels:read`     | Akses metadata channel (ID dan nama) buat ngepost balasan dan update              |
  | `chat:write`        | Kirim update status, notifikasi selesai, dan tautan PR saat agent kelar           |
  | `files:read`        | Download file yang dishare (log, screenshot, contoh kode) buat konteks tambahan   |
  | `files:write`       | Upload ringkasan visual dari perubahan agent buat review cepat                    |
  | `groups:history`    | Baca pesan sebelumnya di private channel buat konteks dalam percakapan multi-turn |
  | `groups:read`       | Akses metadata private channel buat ngepost respons dan jaga alur percakapan      |
  | `im:history`        | Akses riwayat direct message buat konteks percakapan yang berlanjut               |
  | `im:read`           | Baca metadata DM buat ngenalin peserta dan jaga threading yang bener              |
  | `im:write`          | Mulai direct message buat notifikasi privat atau komunikasi individual            |
  | `mpim:history`      | Akses riwayat group DM buat percakapan multi-participant                          |
  | `mpim:read`         | Baca metadata group DM buat nyebut peserta dan pastiin penyampaian yang tepat     |
  | `reactions:read`    | Liat reaksi emoji buat feedback pengguna dan sinyal status                        |
  | `reactions:write`   | Nambahin reaksi emoji buat nandain status — ⏳ lagi jalan, ✅ selesai, ❌ gagal      |
  | `team:read`         | Ngenalin detail workspace buat misahin instalasi dan terapin pengaturan           |
  | `users:read`        | Cocokin user Slack dengan akun Cursor buat permission dan akses yang aman         |
</div>

---

← Previous: [Linear](./linear.md) | [Index](./index.md) | Next: [Model](./model.md) →