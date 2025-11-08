# Panduan Pemecahan Masalah

**Navigation:** [← Previous](./18-slack.md) | [Index](./index.md) | [Next →](./20-bugbot.md)

---

# Panduan Pemecahan Masalah
Source: https://docs.cursor.com/id/troubleshooting/troubleshooting-guide

Langkah untuk memperbaiki masalah dan melaporkan bug

Masalah di Cursor bisa berasal dari ekstensi, data aplikasi, atau gangguan sistem. Coba langkah pemecahan masalah berikut.

<CardGroup cols={1}>
  <Card horizontal title="Melaporkan Masalah" icon="bug" href="#reporting-an-issue">
    Langkah untuk melaporkan masalah ke tim Cursor
  </Card>
</CardGroup>

<div id="troubleshooting">
  ## Pemecahan Masalah
</div>

<Steps>
  <Step title="Periksa konektivitas jaringan">
    Pertama, cek apakah Cursor bisa terhubung ke layanannya.

    **Jalankan diagnostik jaringan:** Buka `Cursor Settings` > `Network` dan klik `Run Diagnostics`. Ini akan menguji koneksi ke server Cursor dan mengidentifikasi masalah jaringan yang memengaruhi fitur AI, pembaruan, atau fungsionalitas online lainnya.

    Kalau diagnostik menunjukkan masalah konektivitas, cek pengaturan firewall, konfigurasi proxy, atau pembatasan jaringan yang memblokir akses Cursor.
  </Step>

  <Step title="Menghapus data ekstensi">
    Untuk masalah ekstensi:

    **Nonaktifkan semua ekstensi sementara:** Jalankan `cursor --disable-extensions` dari command line. Kalau masalahnya hilang, aktifkan lagi ekstensi satu per satu untuk menemukan yang bermasalah.

    **Reset data ekstensi:** Copot dan pasang ulang ekstensi yang bermasalah untuk mereset data yang tersimpan. Cek juga pengaturan ekstensi yang tetap bertahan setelah pemasangan ulang.
  </Step>

  <Step title="Menghapus data aplikasi">
    <Warning>
      Tindakan ini akan menghapus data aplikasi, termasuk ekstensi, tema, snippet, dan data terkait instalasi. Ekspor profil dulu biar data ini tetap tersimpan.
    </Warning>

    Cursor menyimpan data aplikasi di luar aplikasi agar bisa dipulihkan saat pembaruan atau pemasangan ulang.

    Untuk menghapus data aplikasi:

    **Windows:** Jalankan perintah berikut di Command Prompt:

    ```txt  theme={null}
    rd /s /q "%USERPROFILE%\AppData\Local\Programs\Cursor"
    rd /s /q "%USERPROFILE%\AppData\Local\Cursor"
    rd /s /q "%USERPROFILE%\AppData\Roaming\Cursor"
    del /f /q "%USERPROFILE%\.cursor*"
    rd /s /q "%USERPROFILE%\.cursor"
    ```

    **MacOS:** Jalankan `sudo rm -rf ~/Library/Application\ Support/Cursor` dan `rm -f ~/.cursor.json` di Terminal.

    **Linux:** Jalankan `rm -rf ~/.cursor ~/.config/Cursor/` di Terminal.
  </Step>

  <Step title="Menghapus instalasi Cursor">
    Untuk menghapus instalasi Cursor:

    <CardGroup cols={1}>
      <Card horizontal title="Windows" icon="windows">
        Cari "Add or Remove Programs" di Start Menu, temukan "Cursor", klik "Uninstall".
      </Card>

      <Card horizontal title="MacOS" icon="apple">
        Buka folder Applications, klik kanan "Cursor", pilih "Move to Trash".
      </Card>

      <Card horizontal title="Linux" icon="linux">
        **Untuk paket .deb:** `sudo apt remove cursor`

        **Untuk paket .rpm:** `sudo dnf remove cursor` atau `sudo yum remove cursor`

        **Untuk AppImage:** Hapus file Cursor.appimage dari lokasinya.
      </Card>
    </CardGroup>
  </Step>

  <Step title="Menginstal ulang Cursor">
    Instal ulang dari [halaman Downloads](https://www.cursor.com/downloads). Kalau kamu nggak menghapus data aplikasi, Cursor akan dipulihkan ke keadaan sebelumnya. Kalau dihapus, kamu bakal dapat instalasi yang benar-benar baru.
  </Step>
</Steps>

<div id="reporting-an-issue">
  ## Melaporkan Masalah
</div>

Kalau langkah-langkah ini nggak membantu, laporkan ke [forum](https://forum.cursor.com/).

<Card horizontal title="Cursor Forum" icon="message" href="https://forum.cursor.com/">
  Laporkan bug atau masalah di forum Cursor
</Card>

Biar cepat ditangani, sertakan:

<CardGroup cols={2}>
  <Card title="Screenshot of Issue" icon="image">
    Ambil screenshot, sembunyikan info sensitif.
  </Card>

  <Card title="Steps to Reproduce" icon="list-check">
    Dokumentasikan langkah-langkah persis untuk mereproduksi masalah.
  </Card>

  <Card title="System Information" icon="computer">
    Dapatkan info sistem dari:

    <br />

    `Cursor` > `Help` > `About`
  </Card>

  <Card title="Request IDs" icon="shield-halved" href="/id/troubleshooting/request-reporting">
    Klik untuk melihat panduan mengumpulkan Request ID
  </Card>

  <Card title="Console Errors" icon="bug">
    Cek developer console: <br />
    `Developer: Toggle Developer Tools`
  </Card>

  <Card title="Logs" icon="file-lines">
    Akses log: <br />
    `Developer: Open Logs Folder`
  </Card>
</CardGroup>



# Selamat datang
Source: https://docs.cursor.com/id/welcome

Kenalan dengan Cursor dan cara mulai pakai

Cursor adalah editor kode bertenaga AI yang paham codebase lo dan bantu lo ngoding lebih cepat lewat bahasa natural. Cukup jelasin apa yang mau lo bikin atau ubah, dan Cursor bakal ngehasilin kodenya buat lo.

<Frame>
  <img src="https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/welcome.png?fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=bf7bbe430ee044eea33a0ca66edf910d" className="rounded-lg" data-og-width="2000" width="2000" data-og-height="1275" height="1275" data-path="images/welcome.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/welcome.png?w=280&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=fa28a55e9896b15cbec778edf8597b5f 280w, https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/welcome.png?w=560&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=701e61d65b8f296aba427b3fe79d5360 560w, https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/welcome.png?w=840&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=8cf10e0727ab76689bc983e9d69d002f 840w, https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/welcome.png?w=1100&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=cddcb51dd8ccf60c6fc0b4135f3e6933 1100w, https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/welcome.png?w=1650&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=e2e9068dc6b3e9b81c4124e7736ecd8f 1650w, https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/welcome.png?w=2500&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=2bd03fc2dc3a340795c5bfa868b7d30b 2500w" />
</Frame>

<CardGroup cols={3}>
  <Card title="Mulai" icon="rocket" href="/id/get-started/installation">
    <div>
      Download, install, dan mulai ngebangun dengan Cursor dalam hitungan menit
    </div>
  </Card>

  <Card title="Changelog" icon="sparkles" href="https://www.cursor.com/changelog">
    <div>
      Tetap up-to-date dengan fitur dan peningkatan terbaru
    </div>
  </Card>

  <Card title="CLI" icon="terminal" href="/id/cli/overview">
    <div>
      Pakai Cursor di terminal lo
    </div>
  </Card>

  <Card title="Konsep" icon="lightbulb" href="/id/get-started/concepts">
    <div>
      Pahami konsep dan fitur inti yang ngejalanin Cursor
    </div>
  </Card>

  <Card title="Model" icon="brain" href="/id/models">
    <div>
      Jelajahi model AI yang tersedia dan cara milih yang pas
    </div>
  </Card>

  <Card title="Panduan" icon="book" href="/id/guides/working-with-context">
    <div>
      Pelajari best practices dan workflow buat berbagai use case
    </div>
  </Card>

  <Card title="Unduhan" icon="download" href="https://cursor.com/downloads" arrow>
    <div>
      Dapetin Cursor buat komputer lo
    </div>
  </Card>

  <Card title="Forum" icon="message" href="https://forum.cursor.com">
    <div>
      Buat pertanyaan teknis dan berbagi pengalaman, mampir ke forum kita
    </div>
  </Card>

  <Card title="Dukungan" icon="headset" href="mailto:hi@cursor.com">
    <div>
      Buat pertanyaan akun dan billing, email tim support kita
    </div>
  </Card>
</CardGroup>



# Agentのセキュリティ
Source: https://docs.cursor.com/ja/account/agent-security

Cursor Agentを使用する際のセキュリティに関する考慮事項

プロンプトインジェクションやAIのハルシネーションなどにより、AIが予期せぬ、場合によっては悪意ある動作を取ることがある。プロンプトインジェクションの根本的な解決に継続的に取り組みつつ、Cursor製品では、エージェントが実行できる操作に対するガードレール（既定で機密性の高い操作に手動承認を必須とすることを含む）を主な保護手段としている。本ドキュメントの目的は、これらのガードレールの内容と、それによってユーザーが何を期待できるかを説明すること。

以下のコントロールと動作はすべて、デフォルトかつ推奨の設定。

<div id="first-party-tool-calls">
  ## ファーストパーティ製ツールの呼び出し
</div>

Cursor には、エージェントがユーザーのコード作成を支援するためのツールが同梱されている。これには、ファイルの読み取り、編集、ターミナルコマンドの実行、ドキュメントのウェブ検索などが含まれる。

読み取り系ツールは承認不要（例: ファイルの読み取り、コードベース全体の検索）。ユーザーは [.cursorignore](/ja/context/ignore-files) を使って特定ファイルへのエージェントのアクセスを完全にブロックできるが、それ以外では一般に承認なしで読み取りが許可される。機微情報の流出リスクがあるアクションには明示的な承認が必要。

現在のワークスペース内のファイルを変更する場合は、一部の例外を除き明示的な承認は不要。エージェントがファイルに変更を加えると、即座にディスクへ保存される。ファイル内容をいつでも元に戻せるよう、バージョン管理されたワークスペースで Cursor を実行することを推奨する。エディタのワークスペース設定ファイルなど、IDE/CLI の設定を変更するファイルを書き換える前には明示的な承認が必要。ただし、ファイル変更で自動リロードする設定にしているユーザーは、エージェントの変更がレビュー前に自動実行を引き起こす可能性がある点に注意してほしい。

エージェントが提案するすべてのターミナルコマンドは、デフォルトで承認が必要。エージェントが実行する前に毎回コマンドを確認することを推奨する。リスクを受け入れるユーザーは、承認なしで全コマンドを実行する設定にすることも可能。Cursor には [allowlist](/ja/agent/tools) 機能があるが、セキュリティコントロールとは見なしていない。特定のコマンドのみを許可する運用を選ぶユーザーもいるが、これはベストエフォートであり回避される可能性がある。「Run Everything」は、設定した allowlist をすべて迂回するため推奨しない。

<div id="third-party-tool-calls">
  ## サードパーティ製ツールの呼び出し
</div>

Cursor は [MCP](/ja/context/mcp) を介して外部ツールと接続できる。すべてのサードパーティ製 MCP 接続は、ユーザーによる明示的な承認が必要。ユーザーが MCP を承認すると、デフォルトでは、外部 MCP 連携において Agent Mode が提案する各ツール呼び出しは、実行前に個別に明示的な承認が必要になる。

<div id="network-requests">
  ## ネットワークリクエスト
</div>

ネットワークリクエストは、攻撃者によるデータの持ち出しに悪用される可能性がある。現時点では、厳選したホスト（例：GitHub）向けのリクエスト、明示的なリンク取得、そして限られたプロバイダによるウェブ検索のサポートを除き、ファーストパーティ製ツールからのネットワークリクエストはサポートしていない。任意のエージェントによるネットワークリクエストは、デフォルト設定で無効化している。

<div id="workspace-trust">
  ## ワークスペースの信頼
</div>

Cursor IDE は、既定で無効になっている標準の[ワークスペース信頼](https://code.visualstudio.com/docs/editing/workspaces/workspace-trust)機能をサポートしてる。ワークスペース信頼は、新しいワークスペースを開いたときに、通常モードか制限モードかを選ぶプロンプトを表示する。制限モードにすると、AI をはじめ、Cursor を使う主な機能が動かなくなる。信頼できないリポジトリを扱う場合は、基本的なテキストエディタなど、別のツールの利用をおすすめする。

ワークスペース信頼は、次の手順でユーザー設定から有効化できる:

1. ユーザーの settings.json ファイルを開く
2. 次の設定を追加する:
   ```json  theme={null}
   "security.workspace.trust.enabled": true
   ```

この設定は、Mobile Device Management (MDM) ソリューションを通じて組織全体に強制適用することもできる。

<div id="responsible-disclosure">
  ## 責任ある開示
</div>

Cursor の脆弱性を見つけたと思ったら、GitHub の Security ページにあるガイドに従ってそこで報告してね。もし GitHub が使えない場合は、[security@cursor.com](mailto:security@cursor.com) に連絡してもOK。

脆弱性報告は5営業日以内に受領を通知して、できるだけ早く対応するよ。対応結果は GitHub の Security ページでセキュリティアドバイザリとして公開する。重大なインシデントは、GitHub の Security ページでの告知に加えて、すべてのユーザーにメールでも案内する。



# Billing
Source: https://docs.cursor.com/ja/account/billing

Cursor のサブスクリプション、返金、請求書の管理

<div id="how-do-i-access-billing-settings">
  ### 請求設定にはどうやってアクセスするの？
</div>

[Dashboard](https://cursor.com/dashboard) の「Billing」をクリックして請求ポータルへアクセス。ここで請求関連の作業を安全に実行できるよ。

<div id="what-are-cursors-billing-cycles">
  ### Cursor の課金サイクルはどうなってるの？
</div>

課金サイクルは月次または年次で、契約開始日を起点に進むよ。Teams アカウントは席数単位で課金されて、新規メンバーには日割り課金が適用される。

<div id="how-do-seats-work-for-teams-accounts">
  ### Teams アカウントの席数はどう扱われるの？
</div>

Teams アカウントは席数（メンバー1人につき1席）ごとに課金されるよ。サイクル途中にメンバーを追加すると、残り期間分だけ請求。メンバーがクレジットを使ってから削除された場合、その席は請求サイクル終了まで占有されたまま—日割りの返金はないよ。席の管理はダッシュボードからチーム管理者が行える。

<div id="can-i-switch-between-monthly-and-annual-billing">
  ### 月払いと年払いは切り替えられる？
</div>

うん！やり方はこれ：

**Pro プラン**

1. Cursor の [dashboard](https://cursor.com/dashboard) に移動
2. 左サイドバーの「Billing and Invoices」をクリックして請求ページへ
3. 「Manage subscription」をクリック
4. 「Update subscription」をクリック
5. 「Yearly」または「Monthly」を選んで「Continue」をクリック

**Teams プラン**

1. Cursor の [dashboard](https://cursor.com/dashboard) に移動
2. 左サイドバーの「Billing and Invoices」をクリックして請求ページへ
3. 年払いへ切り替えるには「Upgrade Now」ボタンをクリック

<Note>
  月払いから年払いへの切り替えはセルフサービスのみ対応だよ。年払いから月払いへ変更する場合は
  [hi@cursor.com](mailto:hi@cursor.com) に連絡してね。
</Note>

<div id="where-can-i-find-my-invoices">
  ### 請求書はどこで見つかる？
</div>

請求ポータルで請求履歴を確認できるよ。現在および過去の請求書を表示・ダウンロードできる。

<div id="can-i-get-invoices-automatically-emailed-to-me">
  ### 請求書を自動メール送信してもらえる？
</div>

請求書は請求ポータルから手動でダウンロードしてね。自動送信メールは開発中。利用可能になったらオプトインできるようにするよ。

<div id="how-do-i-update-my-billing-information">
  ### 請求情報はどうやって更新するの？
</div>

支払い方法、会社名、住所、税情報は請求ポータルから更新できるよ。決済は Stripe で安全に処理してる。変更は今後の請求書にのみ反映されて、過去の請求書は修正できないよ。

<div id="how-do-i-cancel-my-subscription">
  ### サブスクリプションはどうやって解約するの？
</div>

「Billing and Invoices」ページで「Manage Subscription」を開いて「Cancel subscription」ボタンをクリック。現在の請求期間が終わるまでアクセスは継続するよ。

<div id="im-having-other-billing-issues-how-can-i-get-help">
  ### ほかの請求関連の問題がある。どうやって助けてもらえる？
</div>

ここにない請求の質問は、アカウントに紐づくメールアドレスから [hi@cursor.com](mailto:hi@cursor.com) にメールしてね。アカウント情報と問い合わせ内容を含めて送ってくれると助かるよ。



# 料金
Source: https://docs.cursor.com/ja/account/pricing

Cursor のプランと料金

Cursor は無料で試すことも、個人プランやチームプランを購入することもできるよ。

<div id="individual">
  ## 個人
</div>

すべての個人プランに含まれる内容:

* 無制限のタブ補完
* すべてのモデルで拡張されたエージェント使用上限
* Bugbot へのアクセス
* Background Agents へのアクセス

各プランには、モデル推論の [API 価格](/ja/models#model-pricing) に基づく従量課金の使用が含まれる:

* Pro: API エージェント使用 \$20 分 + 追加のボーナス使用枠
* Pro Plus: API エージェント使用 \$70 分 + 追加のボーナス使用枠
* Ultra: API エージェント使用 \$400 分 + 追加のボーナス使用枠

保証された同梱の使用量に加えて、追加のボーナス容量もできるだけ提供してる。モデルごとに API コストが異なるため、選んだモデルによってトークン出力や含まれる使用量の消費速度が変わる。[ダッシュボード](https://cursor.com/dashboard?tab=usage)で使用量とトークン内訳を確認できる。上限通知はエディタ内で定期的に表示される。

<img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/usage-limits.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=c42b8ad6347f6fe9d075647dfece934c" alt="使用上限" style={{ borderRadius: 16 }} data-og-width="666" width="666" data-og-height="394" height="394" data-path="images/account/usage-limits.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/usage-limits.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=e1ca3b5ab64a6ba6f3ad7d75b1ee72e2 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/usage-limits.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=d39dc254e7d059ac24310f26ea47dd5d 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/usage-limits.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=153472f14b4c10ec9a096b7a9db59888 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/usage-limits.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=0dc8b0cdb5c0677e45c1a082d0002880 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/usage-limits.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=cf4ac9875f5e587d16d4c6f1e7fdc057 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/usage-limits.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=13f21676cda8e4c2973bc3371892f4aa 2500w" />

<div id="how-much-usage-do-i-need">
  ### どれくらいの使用量が必要？
</div>

使用データに基づくと、想定される使用レベルは次のとおり:

* **Daily Tab ユーザー**: 常に \$20 以内
* **Limited Agent ユーザー**: 付帯の \$20 以内に収まることが多い
* **Daily Agent ユーザー**: ふつうは合計 $60–$100/月
* **Power ユーザー（複数エージェント/自動化）**: 多くの場合 合計 \$200+/月

使用データに基づくと、上限は*中央値のユーザー*でおおむね次のとおり:

* Pro: 約 225 件の Sonnet 4 リクエスト、約 550 件の Gemini リクエスト、または約 500 件の GPT 5 リクエスト
* Pro+: 約 675 件の Sonnet 4 リクエスト、約 1,650 件の Gemini リクエスト、または約 1,500 件の GPT 5 リクエスト
* Ultra: 約 4,500 件の Sonnet 4 リクエスト、約 11,000 件の Gemini リクエスト、または約 10,000 件の GPT 5 リクエスト

<div id="what-happens-when-i-reach-my-limit">
  ### 上限に達したらどうなる？
</div>

毎月の含まれる使用量を超えると、エディタ内で通知が出て、次のどれかを選べるよ:

* **オンデマンド使用量を追加**: 同じ API レートで、従量課金のまま Cursor を使い続けられる
* **プランをアップグレード**: 含まれる使用量が多い上位プランに移行する

オンデマンド使用量は、含まれる使用量と同じレートで毎月請求される。リクエストの品質や速度が下がることはないよ。

<div id="teams">
  ## Teams
</div>

チーム向けプランは2種類: Teams (\$40/user/mo) と Enterprise (Custom)。

Teams プランには次の追加機能が含まれる:

* Privacy Mode の適用（強制）
* 利用状況の統計を確認できる管理者ダッシュボード
* チーム請求の一元管理
* SAML/OIDC による SSO

セルフサーブで十分なら Teams がおすすめ。優先サポート、使用量のプール、請求書払い、SCIM、または高度なセキュリティ管理が必要なら [Enterprise](/ja/contact-sales) をおすすめ。

[Teams の料金](/ja/account/teams/pricing)を詳しく見る。

<div id="auto">
  ## Auto
</div>

Auto を有効にすると、Cursor が目のタスクに最適で、需要状況に応じて信頼性が最も高いプレミアムモデルを選んでくれる。この機能は出力の劣化を検知して、自動でモデルを切り替え、問題を解消するよ。

<Frame>
  <img src="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/models/model-picker.png?fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=9f039569ed0dc2ad7e02bb1b2e9cea71" data-og-width="2256" width="2256" data-og-height="1248" height="1248" data-path="images/models/model-picker.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/models/model-picker.png?w=280&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=49c6a091945972253eb6e819593e45f0 280w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/models/model-picker.png?w=560&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=f9bddfb2e130789d8d51a3d1a4eeba94 560w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/models/model-picker.png?w=840&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=db7273f399bb5decfed9d1b06f389df4 840w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/models/model-picker.png?w=1100&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=920fe98d4f99b5d7fddd47a14fb45699 1100w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/models/model-picker.png?w=1650&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=3b049686e5826263800b63299f4c19ca 1650w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/models/model-picker.png?w=2500&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=72ddd56b4d3ea9b2efa4001a155566fd 2500w" />
</Frame>

<Note>Auto の品質と総合的なパフォーマンスには大きく投資してきたよ。9月15日以降の次回の請求更新から、Auto の使用は以下の API レートで計上される。</Note>

* **Input + Cache Write**: 1M tokens あたり \$1.25
* **Output**: 1M tokens あたり \$6.00
* **Cache Read**: 1M tokens あたり \$0.25

エディタとダッシュボードの両方で、Auto を含む使用量が確認できる。モデルを直接選ぶ場合は、そのモデルのリスト API 価格で計上されるよ。

<div id="max-mode">
  ## Max Mode
</div>

一部のモデルは [Max Mode](/ja/models#max-mode) に対応していて、最大 1M トークンまでの長尺な推論と大きなコンテキストウィンドウを扱える。大半のコーディングタスクでは Max Mode は不要だけど、特に大きなファイルやコードベースを扱う複雑なクエリでは役立つ。Max Mode を使うと使用量の消費は増える。[ダッシュボード](https://cursor.com/dashboard?tab=usage) で全リクエストとトークン内訳を確認できる。

<div id="bugbot">
  ## Bugbot
</div>

Bugbot は Cursor のサブスクリプションとは別の製品で、独自の料金プランがある。

* **Pro** (\$40/月): 月あたり最大 200 件の PR に対して無制限のレビュー、Cursor Ask への無制限アクセス、バグ修正のための Cursor との連携、Bugbot Rules へのアクセス
* **Teams** (\$40/ユーザー/月): すべての PR に対する無制限のコードレビュー、Cursor Ask への無制限アクセス、チームでの使用量プール、拡張ルールと設定
* **Enterprise** (カスタム): Teams の内容に加え、高度な分析とレポーティング、優先サポート、アカウント管理

[Bugbot の料金](https://cursor.com/bugbot#pricing)について詳しく見る。

<div id="background-agent">
  ## Background Agent
</div>

Background Agent は、選択した[model](/ja/models)の API 料金で課金される。初回の利用開始時に、Background Agent の支出上限額を設定するよう求められるよ。

<Info>
  Background Agent 向けの Virtual Machine (VM) のコンピュート費用は、今後価格が設定される予定。
</Info>



# Admin API
Source: https://docs.cursor.com/ja/account/teams/admin-api

API 経由でチームのメトリクス、利用データ、支出情報にアクセス

Admin API は、メンバー情報、利用メトリクス、支出の詳細など、チームのデータへプログラムからアクセスできる。カスタムダッシュボードや監視ツールを作成したり、既存のワークフローに統合したりできる。

<Note>
  この API は初回リリース。フィードバックに基づいて機能を拡張中—必要なエンドポイントを教えてね！
</Note>

<div id="authentication">
  ## 認証
</div>

すべての API リクエストには API キーによる認証が必要。API キーの作成と管理ができるのはチーム管理者のみ。

API キーは組織に紐づき、すべての管理者が閲覧でき、作成者本人のアカウント状況の影響は受けない。

<div id="creating-an-api-key">
  ### APIキーの作成
</div>

1. **cursor.com/dashboard** → **Settings** タブ → **Cursor Admin API Keys** に移動
2. **Create New API Key** をクリック
3. キーにわかりやすい名前を付ける（例：「Usage Dashboard Integration」）
4. 生成されたキーはその場でコピーしておく—あとからは確認できない

形式: `key_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`

<div id="using-your-api-key">
  ### APIキーの使用
</div>

基本認証では、ユーザー名にAPIキーを指定する:

**Basic認証を使った curl の例:**

```bash  theme={null}
curl https://api.cursor.com/{route} -u API_KEY:
```

**または Authorization ヘッダーを直接指定する:**

```bash  theme={null}
Authorization: Basic {base64_encode('API_KEY:')}
```

<div id="base-url">
  ## ベースURL
</div>

すべてのAPIエンドポイントは次を使用する：

```
https://api.cursor.com
```

<div id="endpoints">
  ## エンドポイント
</div>

<div id="get-team-members">
  ### チームメンバーの取得
</div>

すべてのチームメンバーとその詳細を取得する。

```
GET /teams/members
```

#### レスポンス

チームメンバーオブジェクトの配列を返す：

```typescript  theme={null}
{
  teamMembers: {
    name: string;
    email: string;
    role: 'オーナー' | 'メンバー' | 'フリー・オーナー';
  }[];
}
```

#### 応答例

```json  theme={null}
{
  "teamMembers": [
    {
      "name": "Alex",
      "email": "developer@company.com",
      "role": "メンバー"
    },
    {
      "name": "Sam",
      "email": "admin@company.com",
      "role": "オーナー"
    }
  ]
}

```

#### 例: リクエスト

```bash  theme={null}
curl -X GET https://api.cursor.com/teams/members \
  -u YOUR_API_KEY:
```

<div id="get-daily-usage-data">
  ### 日次利用データを取得
</div>

指定した日付範囲でチームの詳細な日次利用メトリクスを取得。コード編集、AI支援の利用状況、受け入れ率に関するインサイトを提供するよ。

```
POST /teams/daily-usage-data
```

#### リクエストボディ

<div className="full-width-table">
  | パラメーター      | 型      | 必須  | 説明           |
  | :---------- | :----- | :-- | :----------- |
  | `startDate` | number | Yes | エポックミリ秒の開始日時 |
  | `endDate`   | number | Yes | エポックミリ秒の終了日時 |
</div>

<Note>
  日付範囲は90日を超えない。より長い期間は複数回に分けてリクエストしてね。
</Note>

#### 応答

```typescript  theme={null}
{
  data: {
    date: number;
    isActive: boolean;
    totalLinesAdded: number;
    totalLinesDeleted: number;
    acceptedLinesAdded: number;
    acceptedLinesDeleted: number;
    totalApplies: number;
    totalAccepts: number;
    totalRejects: number;
    totalTabsShown: number;
    totalTabsAccepted: number;
    composerRequests: number;
    chatRequests: number;
    agentRequests: number;
    cmdkUsages: number;
    subscriptionIncludedReqs: number;
    apiKeyReqs: number;
    usageBasedReqs: number;
    bugbotUsages: number;
    mostUsedModel: string;
    applyMostUsedExtension?: string;
    tabMostUsedExtension?: string;
    clientVersion?: string;
    email?: string;
  }[];
  period: {
    startDate: number;
    endDate: number;
  };
}
```

<div id="response-fields">
  #### レスポンスフィールド
</div>

<div className="full-width-table">
  | フィールド                      | 説明                   |
  | :------------------------- | :------------------- |
  | `date`                     | エポックミリ秒の日時           |
  | `isActive`                 | 当日のユーザーアクティブ状態       |
  | `totalLinesAdded`          | 追加されたコード行数           |
  | `totalLinesDeleted`        | 削除されたコード行数           |
  | `acceptedLinesAdded`       | 承認されたAI提案による追加行数     |
  | `acceptedLinesDeleted`     | 承認されたAI提案による削除行数     |
  | `totalApplies`             | Applyの実行回数           |
  | `totalAccepts`             | 承認された提案数             |
  | `totalRejects`             | 却下された提案数             |
  | `totalTabsShown`           | 表示されたタブ補完数           |
  | `totalTabsAccepted`        | 承認されたタブ補完数           |
  | `composerRequests`         | Composerリクエスト数       |
  | `chatRequests`             | Chatリクエスト数           |
  | `agentRequests`            | Agentリクエスト数          |
  | `cmdkUsages`               | コマンドパレット（Cmd+K）の使用回数 |
  | `subscriptionIncludedReqs` | サブスクリプション対象のリクエスト数   |
  | `apiKeyReqs`               | APIキー経由のリクエスト数       |
  | `usageBasedReqs`           | 従量課金リクエスト数           |
  | `bugbotUsages`             | バグ検出機能の使用回数          |
  | `mostUsedModel`            | 最も頻繁に使用されたAIモデル      |
  | `applyMostUsedExtension`   | Applyで最も使用されたファイル拡張子 |
  | `tabMostUsedExtension`     | タブで最も使用されたファイル拡張子    |
  | `clientVersion`            | Cursorのバージョン         |
  | `email`                    | ユーザーのメールアドレス         |
</div>

#### 例のレスポンス

```json  theme={null}
{
  "data": [
    {
      "date": 1710720000000,
      "isActive": true,
      "totalLinesAdded": 1543,
      "totalLinesDeleted": 892,
      "acceptedLinesAdded": 1102,
      "acceptedLinesDeleted": 645,
      "totalApplies": 87,
      "totalAccepts": 73,
      "totalRejects": 14,
      "totalTabsShown": 342,
      "totalTabsAccepted": 289,
      "composerRequests": 45,
      "chatRequests": 128,
      "agentRequests": 12,
      "cmdkUsages": 67,
      "subscriptionIncludedReqs": 180,
      "apiKeyReqs": 0,
      "usageBasedReqs": 5,
      "bugbotUsages": 3,
      "mostUsedModel": "gpt-4",
      "applyMostUsedExtension": ".tsx",
      "tabMostUsedExtension": ".ts",
      "clientVersion": "0.25.1",
      "email": "developer@company.com"
    },
    {
      "date": 1710806400000,
      "isActive": true,
      "totalLinesAdded": 2104,
      "totalLinesDeleted": 1203,
      "acceptedLinesAdded": 1876,
      "acceptedLinesDeleted": 987,
      "totalApplies": 102,
      "totalAccepts": 91,
      "totalRejects": 11,
      "totalTabsShown": 456,
      "totalTabsAccepted": 398,
      "composerRequests": 67,
      "chatRequests": 156,
      "agentRequests": 23,
      "cmdkUsages": 89,
      "subscriptionIncludedReqs": 320,
      "apiKeyReqs": 15,
      "usageBasedReqs": 0,
      "bugbotUsages": 5,
      "mostUsedModel": "claude-3-opus",
      "applyMostUsedExtension": ".py",
      "tabMostUsedExtension": ".py",
      "clientVersion": "0.25.1",
      "email": "developer@company.com"
    }
  ],
  "period": {
    "startDate": 1710720000000,
    "endDate": 1710892800000
  }
}
```

#### リクエストの例

```bash  theme={null}
curl -X POST https://api.cursor.com/teams/daily-usage-data \
  -u YOUR_API_KEY: \
  -H "Content-Type: application/json" \
  -d '{
    "startDate": 1710720000000,
    "endDate": 1710892800000
  }'
```

<div id="get-spending-data">
  ### 支出データを取得
</div>

検索、ソート、ページネーションに対応し、当月（暦月）の支出情報を取得する。

```
POST /teams/spend
```

#### リクエストボディ

<div className="full-width-table">
  | パラメータ           | 型      | 必須  | 説明                                           |
  | :-------------- | :----- | :-- | :------------------------------------------- |
  | `searchTerm`    | string | いいえ | ユーザー名とメールアドレス内を検索                            |
  | `sortBy`        | string | いいえ | 並び替え基準: `amount`, `date`, `user`。既定値: `date` |
  | `sortDirection` | string | いいえ | 並び順: `asc`, `desc`。既定値: `desc`               |
  | `page`          | number | いいえ | ページ番号（1始まり）。既定値: `1`                         |
  | `pageSize`      | number | いいえ | 1ページあたりの件数                                   |
</div>

#### レスポンス

```typescript  theme={null}
{
  teamMemberSpend: {
    spendCents: number;
    fastPremiumRequests: number;
    name: string;
    email: string;
    role: 'owner' | 'member' | 'free-owner';
    hardLimitOverrideDollars: number;
  }[];
  subscriptionCycleStart: number;
  totalMembers: number;
  totalPages: number;
}
```

<div id="response-fields">
  #### レスポンスフィールド
</div>

<div className="full-width-table">
  | フィールド                      | 説明                         |
  | :------------------------- | :------------------------- |
  | `spendCents`               | 合計支出（セント）                  |
  | `fastPremiumRequests`      | Fast プレミアムモデルのリクエスト数       |
  | `name`                     | メンバー名                      |
  | `email`                    | メンバーのメールアドレス               |
  | `role`                     | チーム内ロール                    |
  | `hardLimitOverrideDollars` | カスタム支出上限の上書き（ドル）           |
  | `subscriptionCycleStart`   | サブスクリプションサイクル開始時刻（エポックミリ秒） |
  | `totalMembers`             | チームメンバー総数                  |
  | `totalPages`               | 総ページ数                      |
</div>

#### 応答例

```json  theme={null}
{
  "teamMemberSpend": [
    {
      "spendCents": 2450,
      "fastPremiumRequests": 1250,
      "name": "Alex",
      "email": "developer@company.com",
      "role": "メンバー",
      "hardLimitOverrideDollars": 100
    },
    {
      "spendCents": 1875,
      "fastPremiumRequests": 980,
      "name": "Sam",
      "email": "admin@company.com",
      "role": "オーナー"
      "hardLimitOverrideDollars": 0
    },
  ],
  "subscriptionCycleStart": 1708992000000,
  "totalMembers": 15,
  "totalPages": 1
}
```

<div id="example-requests">
  #### リクエスト例
</div>

**基本的な支出データ：**

```bash  theme={null}
curl -X POST https://api.cursor.com/teams/spend \
  -u YOUR_API_KEY: \
  -H "Content-Type: application/json" \
  -d '{}'
```

**ページネーション付きで特定のユーザーを検索する:**

```bash  theme={null}
curl -X POST https://api.cursor.com/teams/spend \
  -u YOUR_API_KEY: \
  -H "Content-Type: application/json" \
  -d '{
    "searchTerm": "alex@company.com",
    "page": 2,
    "pageSize": 25
  }'
```

<div id="get-usage-events-data">
  ### 使用イベントデータの取得
</div>

チームの使用イベントを、柔軟なフィルタリング、検索、ページネーションで詳細に取得できる。このエンドポイントは、個々の API 呼び出し、モデルの利用状況、トークン消費量、コストに関するきめ細かなインサイトを提供する。

```
POST /teams/filtered-usage-events
```

#### リクエストボディ

<div className="full-width-table">
  | パラメータ       | 型      | 必須  | 説明                    |
  | :---------- | :----- | :-- | :-------------------- |
  | `startDate` | number | いいえ | エポックミリ秒の開始日時          |
  | `endDate`   | number | いいえ | エポックミリ秒の終了日時          |
  | `userId`    | number | いいえ | 特定のユーザーIDでフィルタリング     |
  | `page`      | number | いいえ | ページ番号（1始まり）。既定値: `1`  |
  | `pageSize`  | number | いいえ | 1ページあたりの結果数。既定値: `10` |
  | `email`     | string | いいえ | ユーザーのメールアドレスでフィルタリング  |
</div>

#### 応答

```typescript  theme={null}
{
  totalUsageEventsCount: number;
  pagination: {
    numPages: number;
    currentPage: number;
    pageSize: number;
    hasNextPage: boolean;
    hasPreviousPage: boolean;
  };
  usageEvents: {
    timestamp: string;
    model: string;
    kind: string;
    maxMode: boolean;
    requestsCosts: number;
    isTokenBasedCall: boolean;
    tokenUsage?: {
      inputTokens: number;
      outputTokens: number;
      cacheWriteTokens: number;
      cacheReadTokens: number;
      totalCents: number;
    };
    isFreeBugbot: boolean;
    userEmail: string;
  }[];
  period: {
    startDate: number;
    endDate: number;
  };
}
```

<div id="response-fields-explained">
  #### レスポンスフィールドの説明
</div>

<div className="full-width-table">
  | フィールド                   | 説明                                             |
  | :---------------------- | :--------------------------------------------- |
  | `totalUsageEventsCount` | クエリに一致する利用イベントの総数                              |
  | `pagination`            | 結果を移動するためのページネーション用メタデータ                       |
  | `timestamp`             | イベントのエポックミリ秒でのタイムスタンプ                          |
  | `model`                 | リクエストで使用された AI モデル                             |
  | `kind`                  | 利用区分（例: "Usage-based", "Included in Business"） |
  | `maxMode`               | Max Mode が有効だったかどうか                            |
  | `requestsCosts`         | リクエスト単位のコスト                                    |
  | `isTokenBasedCall`      | イベントが従量課金として計上される場合は true                      |
  | `tokenUsage`            | トークン消費の詳細（isTokenBasedCall が true の場合に提供）      |
  | `isFreeBugbot`          | 無料の Bugbot 利用かどうか                              |
  | `userEmail`             | リクエスト実行ユーザーのメールアドレス                            |
  | `period`                | クエリ対象データの期間（日時範囲）                              |
</div>

#### 応答例

```json  theme={null}
{
  "totalUsageEventsCount": 113,
  "pagination": {
    "numPages": 12,
    "currentPage": 1,
    "pageSize": 10,
    "hasNextPage": true,
    "hasPreviousPage": false
  },
  "usageEvents": [
    {
      "timestamp": "1750979225854",
      "model": "claude-4-opus",
      "kind": "利用量課金",
      "maxMode": true,
      "requestsCosts": 5,
      "isTokenBasedCall": true,
      "tokenUsage": {
        "inputTokens": 126,
        "outputTokens": 450,
        "cacheWriteTokens": 6112,
        "cacheReadTokens": 11964,
        "totalCents": 20.18232
      },
      "isFreeBugbot": false,
      "userEmail": "developer@company.com"
    },
    {
      "timestamp": "1750979173824",
      "model": "claude-4-opus",
      "kind": "Usage-based",
      "maxMode": true,
      "requestsCosts": 10,
      "isTokenBasedCall": true,
      "tokenUsage": {
        "inputTokens": 5805,
        "outputTokens": 311,
        "cacheWriteTokens": 11964,
        "cacheReadTokens": 0,
        "totalCents": 40.16699999999999
      },
      "isFreeBugbot": false,
      "userEmail": "developer@company.com"
    },
    {
      "timestamp": "1750978339901",
      "model": "claude-4-sonnet-thinking",
      "kind": "Business に含まれる"
      "maxMode": true,
      "requestsCosts": 1.4,
      "isTokenBasedCall": false,
      "isFreeBugbot": false,
      "userEmail": "admin@company.com"
    }
  ],
  "period": {
    "startDate": 1748411762359,
    "endDate": 1751003762359
  }
}
```

<div id="example-requests">
  #### リクエスト例
</div>

**デフォルトのページネーションで全ての利用イベントを取得:**

```bash  theme={null}
curl -X POST https://api.cursor.com/teams/filtered-usage-events \
  -u YOUR_API_KEY: \
  -H "Content-Type: application/json" \
  -d '{}'
```

**日付範囲と特定のユーザーで絞り込み:**

```bash  theme={null}
curl -X POST https://api.cursor.com/teams/filtered-usage-events \
  -u YOUR_API_KEY: \
  -H "Content-Type: application/json" \
  -d '{
    "startDate": 1748411762359,
    "endDate": 1751003762359,
    "email": "developer@company.com",
    "page": 1,
    "pageSize": 25
  }'
```

**カスタムページネーションで特定ユーザーの利用イベントを取得:**

```bash  theme={null}
curl -X POST https://api.cursor.com/teams/filtered-usage-events \
  -u YOUR_API_KEY: \
  -H "Content-Type: application/json" \
  -d '{
    "userId": 12345,
    "page": 2,
    "pageSize": 50
  }'
```

<div id="set-user-spend-limit">
  ### ユーザーの支出上限を設定
</div>

チームメンバーごとに支出上限を設定できる。これで、チーム内で各ユーザーがAIの利用にどれだけ使えるかを管理できる。

```
POST /teams/user-spend-limit
```

<Note>
  **レート制限:** チームあたり毎分60リクエスト
</Note>

#### リクエストボディ

<div className="full-width-table">
  | パラメータ               | 型      | 必須 | 説明                  |
  | :------------------ | :----- | :- | :------------------ |
  | `userEmail`         | string | はい | チームメンバーのメールアドレス     |
  | `spendLimitDollars` | number | はい | 支出上限（米ドル、整数のみ。小数不可） |
</div>

<Note>
  * ユーザーはすでにチームのメンバーである必要がある
  * 受け付けるのは整数値のみ（小数は不可）
  * `spendLimitDollars` を 0 に設定すると、上限は \$0 になる
</Note>

<div id="response">
  #### Response
</div>

成功または失敗を示す標準化されたレスポンスを返します。

```typescript  theme={null}
{
  outcome: 'success' | 'error';
  message: string;
}
```

<div id="example-responses">
  #### レスポンス例
</div>

**上限を設定しました:**

```json  theme={null}
{
  "outcome": "success",
  "message": "ユーザー developer@company.com の支出上限を $100 に設定しました"
}
```

**エラー応答:**

```json  theme={null}
{
  "outcome": "error",
  "message": "無効なメールアドレス形式です"
}
```

<div id="example-requests">
  #### リクエスト例
</div>

**支出の上限を設定する:**

```bash  theme={null}
curl -X POST https://api.cursor.com/teams/user-spend-limit \
  -u YOUR_API_KEY: \
  -H "Content-Type: application/json" \
  -d '{
    "userEmail": "developer@company.com",
    "spendLimitDollars": 100
  }'
```

<div id="repo-blocklists-api">
  ### Repo Blocklists API
</div>

リポジトリを追加し、パターンを設定して、チームでのコンテキストとしてファイルやディレクトリがインデックス化・利用されるのを防ぐ。

<div id="get-team-repo-blocklists">
  #### チームのリポジトリ・ブロックリストを取得
</div>

チームで構成されているすべてのリポジトリ・ブロックリストを取得する。

```
GET /settings/repo-blocklists/repos
```

##### レスポンス

リポジトリのブロックリストオブジェクトの配列を返す：

```typescript  theme={null}
{
  repos: {
    id: string;
    url: string;
    patterns: string[];
  }[];
}
```

<div id="example-response">
  ##### レスポンスの例
</div>

```json  theme={null}
{
  "repos": [
    {
      "id": "repo_123",
      "url": "https://github.com/company/sensitive-repo",
      "patterns": ["*.env", "config/*", "secrets/**"]
    },
    {
      "id": "repo_456",
      "url": "https://github.com/company/internal-tools",
      "patterns": ["*"]
    }
  ]
}
```

##### リクエストの例

```bash  theme={null}
curl -X GET https://api.cursor.com/settings/repo-blocklists/repos \
  -u 自分のAPIキー:
```

<div id="upsert-repo-blocklists">
  #### リポジトリブロックリストのアップサート
</div>

指定したリポジトリの既存のブロックリストを置き換える。
*注: このエンドポイントは、指定したリポジトリに対するパターンのみを上書きする。他のリポジトリには影響しない。*

```
POST /settings/repo-blocklists/repos/upsert
```

<div id="request-body">
  ##### リクエストボディ
</div>

| Parameter | Type  | Required | Description              |
| --------- | ----- | -------- | ------------------------ |
| repos     | array | Yes      | リポジトリのブロックリスト対象オブジェクトの配列 |

各リポジトリオブジェクトには以下を含める必要がある:

| Field    | Type      | Required | Description                    |
| -------- | --------- | -------- | ------------------------------ |
| url      | string    | Yes      | ブロックリスト対象のリポジトリのURL            |
| patterns | string\[] | Yes      | ブロックするファイルパターンの配列（glob パターン対応） |

##### レスポンス

更新後のリポジトリ・ブロックリスト一覧を返す：

```typescript  theme={null}
{
  repos: {
    id: string;
    url: string;
    patterns: string[];
  }[];
}
```

<div id="example-request">
  ##### 例: リクエスト
</div>

```bash  theme={null}
curl -X POST https://api.cursor.com/settings/repo-blocklists/repos/upsert \
  -u YOUR_API_KEY: \
  -H "Content-Type: application/json" \
  -d '{
    "repos": [
      {
        "url": "https://github.com/company/sensitive-repo",
        "patterns": ["*.env", "config/*", "secrets/**"]
      },
      {
        "url": "https://github.com/company/internal-tools", 
        "patterns": ["*"]
      }
    ]
  }'
```

<div id="delete-repo-blocklist">
  #### リポジトリブロックリストの削除
</div>

ブロックリストから特定のリポジトリを削除する。

```
DELETE /settings/repo-blocklists/repos/:repoId
```

<div id="parameters">
  ##### パラメータ
</div>

| パラメータ  | 型      | 必須 | 説明                   |
| ------ | ------ | -- | -------------------- |
| repoId | string | はい | 削除対象のリポジトリブロックリストのID |

##### レスポンス

削除に成功すると、204 No Content を返します。

##### リクエストの例

```bash  theme={null}
curl -X DELETE https://api.cursor.com/settings/repo-blocklists/repos/repo_123 \
  -u APIキー:
```

<div id="pattern-examples">
  #### パターン例
</div>

一般的なブロックリストのパターン:

* `*` - リポジトリ全体をブロック
* `*.env` - すべての.envファイルをブロック
* `config/*` - configディレクトリ内のすべてのファイルをブロック
* `**/*.secret` - 任意のサブディレクトリ内のすべての.secretファイルをブロック
* `src/api/keys.ts` - 特定のファイルをブロック



# AI Code Tracking API
Source: https://docs.cursor.com/ja/account/teams/ai-code-tracking-api

チームのリポジトリ向けAI生成コード分析へのアクセス

チームのリポジトリに対するAI生成コードの分析にアクセスできる。コミット単位のAI利用状況や、受け入れられたAI変更の粒度の細かい内訳を含む。

<Note>
  このAPIは初回リリース。フィードバックに基づき機能を拡張中—必要なエンドポイントを教えて！
</Note>

* **提供状況**: エンタープライズチーム限定
* **ステータス**: Alpha（レスポンスの形やフィールドは変更される可能性あり）

<div id="authentication">
  ## 認証
</div>

すべての API リクエストには、API キーによる認証が必要。この API は、他のエンドポイントと同じ Admin API の認証方式を使ってる。

詳しい手順は [Admin API authentication](/ja/account/teams/admin-api#authentication) を参照してね。

<div id="base-url">
  ## ベース URL
</div>

すべての API エンドポイントで使用されるのは次のとおり：

```
https://api.cursor.com
```

<div id="rate-limits">
  ## レート制限
</div>

* エンドポイントごと・チームごとに、1分あたり5リクエスト

<div id="query-parameters">
  ## クエリパラメータ
</div>

以下のエンドポイントはすべて、クエリ文字列で同じクエリパラメータを受け付ける:

<div className="full-width-table">
  | Parameter   | Type   | Required | Description                                                                                                                       |                                                                     |
  | :---------- | :----- | :------- | :-------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------- |
  | `startDate` | string | date     | No                                                                                                                                | ISO日付文字列、リテラルの "now"、または "7d" のような相対日数（「現在 - 7日」の意味）。デフォルト: 現在 - 7日 |
  | `endDate`   | string | date     | No                                                                                                                                | ISO日付文字列、リテラルの "now"、または "0d" のような相対日数。デフォルト: 現在                    |
  | `page`      | number | No       | ページ番号（1始まり）。デフォルト: 1                                                                                                              |                                                                     |
  | `pageSize`  | number | No       | 1ページあたりの件数。デフォルト: 100、最大: 1000                                                                                                    |                                                                     |
  | `user`      | string | No       | 単一ユーザーによる任意のフィルタ。メール（例: [developer@company.com](mailto:developer@company.com)）、エンコード済みID（例: user\_abc123...）、または数値ID（例: 42）を受け付ける |                                                                     |
</div>

<Note>
  レスポンスでは、接頭辞 user\_ が付いたエンコード済み外部IDとして userId を返す。これは API 連携で安定して利用できる。
</Note>

<div id="semantics-and-how-metrics-are-computed">
  ## セマンティクスとメトリクスの算出方法
</div>

* **Sources**: "TAB" は受け入れられたインライン補完、"COMPOSER" は Composer で受け入れられた差分を表す
* **Lines metrics**: tabLinesAdded/Deleted と composerLinesAdded/Deleted は個別にカウントされる。nonAiLinesAdded/Deleted は max(0, totalLines - AI lines) で算出される
* **Privacy mode**: クライアントで有効な場合、fileName など一部のメタデータは省略されることがある
* **Branch info**: 現在のブランチがリポジトリのデフォルトブランチと一致する場合、isPrimaryBranch は true。リポジトリ情報が利用できない場合は undefined になることがある

そのファイルを参照すると、コミットと変更がどのように検出され、報告されるかがわかる。

<div id="endpoints">
  ## エンドポイント
</div>

<div id="get-ai-commit-metrics-json-paginated">
  ### AI コミットメトリクスの取得（JSON、ページネーション対応）
</div>

TAB、COMPOSER、非 AI への行の帰属に基づく、コミット単位の集計メトリクスを取得する。

```
GET /analytics/ai-code/commits
```

#### 応答

```typescript  theme={null}
{
  items: AiCommitMetric[];
  totalCount: number;
  page: number;
  pageSize: number;
}
```

<div id="aicommitmetric-fields">
  #### AiCommitMetric フィールド
</div>

<div className="full-width-table">
  | フィールド                  | 型       | 説明                               |                      |
  | :--------------------- | :------ | :------------------------------- | -------------------- |
  | `commitHash`           | string  | Git のコミットハッシュ                    |                      |
  | `userId`               | string  | エンコード済みのユーザー ID（例: user\_abc123） |                      |
  | `userEmail`            | string  | ユーザーのメールアドレス                     |                      |
  | `repoName`             | string  | null                             | リポジトリ名               |
  | `branchName`           | string  | null                             | ブランチ名                |
  | `isPrimaryBranch`      | boolean | null                             | プライマリブランチかどうか        |
  | `totalLinesAdded`      | number  | コミットで追加された行の合計                   |                      |
  | `totalLinesDeleted`    | number  | コミットで削除された行の合計                   |                      |
  | `tabLinesAdded`        | number  | TAB 補完で追加された行数                   |                      |
  | `tabLinesDeleted`      | number  | TAB 補完で削除された行数                   |                      |
  | `composerLinesAdded`   | number  | Composer で追加された行数                |                      |
  | `composerLinesDeleted` | number  | Composer で削除された行数                |                      |
  | `nonAiLinesAdded`      | number  | null                             | 非 AI による追加行数         |
  | `nonAiLinesDeleted`    | number  | null                             | 非 AI による削除行数         |
  | `message`              | string  | null                             | コミットメッセージ            |
  | `commitTs`             | string  | null                             | コミットのタイムスタンプ（ISO 形式） |
  | `createdAt`            | string  | 取り込みタイムスタンプ（ISO 形式）              |                      |
</div>

<div id="example-response">
  #### レスポンス例
</div>

```json  theme={null}
{
  "items": [
    {
      "commitHash": "a1b2c3d4",
      "userId": "user_3k9x8q...",
      "userEmail": "developer@company.com",
      "repoName": "company/repo",
      "branchName": "main",
      "isPrimaryBranch": true,
      "totalLinesAdded": 120,
      "totalLinesDeleted": 30,
      "tabLinesAdded": 50,
      "tabLinesDeleted": 10,
      "composerLinesAdded": 40,
      "composerLinesDeleted": 5,
      "nonAiLinesAdded": 30,
      "nonAiLinesDeleted": 15,
      "message": "リファクタリング: analytics クライアントの抽出"
      "commitTs": "2025-07-30T14:12:03.000Z",
      "createdAt": "2025-07-30T14:12:30.000Z"
    }
  ],
  "totalCount": 42,
  "page": 1,
  "pageSize": 100
}
```

<div id="example-requests">
  #### リクエスト例
</div>

**基本的なリクエスト:**

```bash  theme={null}
curl -X GET "https://api.cursor.com/analytics/ai-code/commits?startDate=7d&endDate=now&page=1&pageSize=100" \
  -u YOUR_API_KEY:
```

**ユーザー（メールアドレス）で絞り込み：**

```bash  theme={null}
curl -X GET "https://api.cursor.com/analytics/ai-code/commits?startDate=2025-06-01T00:00:00Z&endDate=now&user=developer@company.com" \
  -u YOUR_API_KEY:
```

<div id="download-ai-commit-metrics-csv-streaming">
  ### AI Commit Metrics のダウンロード（CSV・ストリーミング）
</div>

大規模なデータ抽出向けに、コミットメトリクスのデータを CSV 形式でダウンロードできる。

```
GET /analytics/ai-code/commits.csv
```

<div id="response">
  #### レスポンス
</div>

ヘッダー:

* Content-Type: text/csv; charset=utf-8

<div id="csv-columns">
  #### CSV カラム
</div>

<div className="full-width-table">
  | Column                   | Type    | Description          |
  | :----------------------- | :------ | :------------------- |
  | `commit_hash`            | string  | Git のコミットハッシュ        |
  | `user_id`                | string  | エンコード済みユーザー ID       |
  | `user_email`             | string  | ユーザーのメールアドレス         |
  | `repo_name`              | string  | リポジトリ名               |
  | `branch_name`            | string  | ブランチ名                |
  | `is_primary_branch`      | boolean | プライマリブランチかどうか        |
  | `total_lines_added`      | number  | コミットで追加された行数（合計）     |
  | `total_lines_deleted`    | number  | コミットで削除された行数（合計）     |
  | `tab_lines_added`        | number  | TAB 補完で追加された行数       |
  | `tab_lines_deleted`      | number  | TAB 補完で削除された行数       |
  | `composer_lines_added`   | number  | Composer で追加された行数    |
  | `composer_lines_deleted` | number  | Composer で削除された行数    |
  | `non_ai_lines_added`     | number  | 非 AI の追加行数           |
  | `non_ai_lines_deleted`   | number  | 非 AI の削除行数           |
  | `message`                | string  | コミットメッセージ            |
  | `commit_ts`              | string  | コミットのタイムスタンプ（ISO 形式） |
  | `created_at`             | string  | 取り込みタイムスタンプ（ISO 形式）  |
</div>

<div id="sample-csv-output">
  #### サンプル CSV 出力
</div>

```csv  theme={null}
commit_hash,user_id,user_email,repo_name,branch_name,is_primary_branch,total_lines_added,total_lines_deleted,tab_lines_added,tab_lines_deleted,composer_lines_added,composer_lines_deleted,non_ai_lines_added,non_ai_lines_deleted,message,commit_ts,created_at
a1b2c3d4,user_3k9x8q...,developer@company.com,company/repo,main,true,120,30,50,10,40,5,30,15,"リファクタ: analytics クライアントを抽出",2025-07-30T14:12:03.000Z,2025-07-30T14:12:30.000Z
e5f6g7h8,user_3k9x8q...,developer@company.com,company/repo,feature-branch,false,85,15,30,5,25,3,30,7,"エラー処理を追加",2025-07-30T13:45:21.000Z,2025-07-30T13:45:45.000Z
```

<div id="example-request">
  #### リクエストの例
</div>

```bash  theme={null}
curl -L "https://api.cursor.com/analytics/ai-code/commits.csv?startDate=2025-07-01T00:00:00Z&endDate=now&user=user_3k9x8q..." \
  -u YOUR_API_KEY: \
  -o commits.csv
```

<div id="get-ai-code-change-metrics-json-paginated">
  ### AIコード変更メトリクスを取得（JSON、ページネーション対応）
</div>

決定的な changeId ごとにグループ化された、粒度の高い承認済みAI変更を取得する。コミットから独立して承認されたAIイベントを分析するのに便利。

```
GET /analytics/ai-code/changes
```

#### 応答

```typescript  theme={null}
{
  items: AiCodeChangeMetric[];
  totalCount: number;
  page: number;
  pageSize: number;
}
```

<div id="aicodechangemetric-fields">
  #### AiCodeChangeMetric のフィールド
</div>

<div className="full-width-table">
  | フィールド               | 型                    | 説明                                          |           |
  | :------------------ | :------------------- | :------------------------------------------ | --------- |
  | `changeId`          | string               | 変更の決定的ID                                    |           |
  | `userId`            | string               | エンコード済みユーザーID（例: user\_abc123）              |           |
  | `userEmail`         | string               | ユーザーのメールアドレス                                |           |
  | `source`            | "TAB" または "COMPOSER" | AI変更の発生元                                    |           |
  | `model`             | string               | null                                        | 使用したAIモデル |
  | `totalLinesAdded`   | number               | 追加行数の合計                                     |           |
  | `totalLinesDeleted` | number               | 削除行数の合計                                     |           |
  | `createdAt`         | string               | 取り込みタイムスタンプ（ISO形式）                          |           |
  | `metadata`          | Array                | ファイルのメタデータ（プライバシーモードでは fileName が省略される場合あり） |           |
</div>

<div id="example-response">
  #### レスポンス例
</div>

```json  theme={null}
{
  "items": [
    {
      "changeId": "749356201",
      "userId": "user_3k9x8q...",
      "userEmail": "developer@company.com",
      "source": "COMPOSER",
      "model": null,
      "totalLinesAdded": 18,
      "totalLinesDeleted": 4,
      "createdAt": "2025-07-30T15:10:12.000Z",
      "metadata": [
        { "fileName": "src/analytics/report.ts", "fileExtension": "ts", "linesAdded": 12, "linesDeleted": 3 },
        { "fileName": "src/analytics/ui.tsx", "fileExtension": "tsx", "linesAdded": 6, "linesDeleted": 1 }
      ]
    }
  ],
  "totalCount": 128,
  "page": 1,
  "pageSize": 200
}
```

<div id="example-requests">
  #### リクエスト例
</div>

**基本的なリクエスト：**

```bash  theme={null}
curl -X GET "https://api.cursor.com/analytics/ai-code/changes?startDate=14d&endDate=now&page=1&pageSize=200" \
  -u YOUR_API_KEY:
```

**ユーザー（エンコード済みID）で絞り込み：**

```bash  theme={null}
curl -X GET "https://api.cursor.com/analytics/ai-code/changes?user=user_3k9x8q..." \
  -u YOUR_API_KEY:
```

**ユーザー（メールアドレス）で絞り込み：**

```bash  theme={null}
curl -X GET "https://api.cursor.com/analytics/ai-code/changes?user=developer@company.com" \
  -u YOUR_API_KEY:
```

<div id="download-ai-code-change-metrics-csv-streaming">
  ### AIコード変更メトリクスをダウンロード（CSV・ストリーミング）
</div>

大規模なデータ抽出のために、変更メトリクスのデータをCSV形式でダウンロードできる。

```
GET /analytics/ai-code/changes.csv
```

<div id="response">
  #### レスポンス
</div>

ヘッダー:

* Content-Type: text/csv; charset=utf-8

<div id="csv-columns">
  #### CSV カラム
</div>

<div className="full-width-table">
  | 列                     | 型      | 説明                          |
  | :-------------------- | :----- | :-------------------------- |
  | `change_id`           | string | 変更を一意に識別する決定的 ID            |
  | `user_id`             | string | エンコードされたユーザー ID             |
  | `user_email`          | string | ユーザーのメールアドレス                |
  | `source`              | string | AI 変更の発生元（TAB または COMPOSER） |
  | `model`               | string | 使用した AI モデル                 |
  | `total_lines_added`   | number | 追加行数の合計                     |
  | `total_lines_deleted` | number | 削除行数の合計                     |
  | `created_at`          | string | 取り込みタイムスタンプ（ISO 形式）         |
  | `metadata_json`       | string | メタデータエントリ配列の JSON 文字列       |
</div>

<div id="notes">
  #### 注意事項
</div>

* metadata\_json はメタデータエントリ配列の JSON 文字列（プライバシーモードでは fileName を省略する場合がある）
* CSV を読み込む場合は、必ず引用符付きフィールドをパースすること

<div id="sample-csv-output">
  #### サンプル CSV 出力
</div>

```csv  theme={null}
change_id,user_id,user_email,source,model,total_lines_added,total_lines_deleted,created_at,metadata_json
749356201,user_3k9x8q...,developer@company.com,COMPOSER,gpt-4o,18,4,2025-07-30T15:10:12.000Z,"[{""fileName"":""src/analytics/report.ts"",""fileExtension"":""ts"",""linesAdded"":12,""linesDeleted"":3},{""fileName"":""src/analytics/ui.tsx"",""fileExtension"":""tsx"",""linesAdded"":6,""linesDeleted"":1}]"
749356202,user_3k9x8q...,developer@company.com,TAB,,8,2,2025-07-30T15:08:45.000Z,"[{""fileName"":""src/utils/helpers.ts"",""fileExtension"":""ts"",""linesAdded"":8,""linesDeleted"":2}]"
```

<div id="example-request">
  #### リクエストの例
</div>

```bash  theme={null}
curl -L "https://api.cursor.com/analytics/ai-code/changes.csv?startDate=30d&endDate=now" \
  -u YOUR_API_KEY: \
  -o changes.csv
```

<div id="tips">
  ## ヒント
</div>

* すべてのエンドポイントで特定のユーザーだけを素早く絞り込むには、`user` パラメータを使う
* 大規模なデータ抽出には CSV エンドポイントを推奨—サーバー側で 10,000 件ごとのページとしてストリーミングされる
* デフォルトブランチをクライアント側で解決できない場合、`isPrimaryBranch` は undefined になることがある
* `commitTs` はコミットのタイムスタンプ、`createdAt` はサーバーでの取り込み時刻
* クライアントでプライバシーモードが有効な場合、一部のフィールドが欠落することがある

<div id="changelog">
  ## 変更履歴
</div>

* **アルファ版リリース**: commits と changes 用の初期エンドポイントを追加。フィードバックに応じてレスポンス形式は変更される可能性があります



# Analytics
Source: https://docs.cursor.com/ja/account/teams/analytics

チームの利用状況とアクティビティ指標を追跡

チーム管理者は[ダッシュボード](/ja/account/teams/dashboard)から各種メトリクスを確認できる。

<Frame>
  <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/analytics.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=a8a4a0ca334e5f5acac55307b2ebeadf" data-og-width="3456" width="3456" data-og-height="1944" height="1944" data-path="images/account/team/analytics.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/analytics.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=73c11df8fcb2862e5c1fd551e6399159 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/analytics.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=c3eaa0d4faa7d6fdf5e3c79dfd11fb5a 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/analytics.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=e9ee5fc554ae46e9d0e2cf53c19e652d 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/analytics.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=5f0afded72e0b02142c5a85e448f2d4e 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/analytics.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=3a6dec2a182ac88d7de75f7a42b1f5ff 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/analytics.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=7a8ac7dafe559da435f3f4974b04df52 2500w" />
</Frame>

<div id="total-usage">
  ### Total Usage
</div>

チーム全体の集計指標を表示。合計タブ数やプレミアムリクエスト数を含む。作成から30日未満のチームでは、作成以降の利用状況を反映し、メンバーの参加前のアクティビティも含む。

<div id="per-active-user">
  ### Per Active User
</div>

アクティブユーザー1人あたりの平均指標を表示：受け入れられたタブ数、コード行数、プレミアムリクエスト数。

<div id="user-activity">
  ### User Activity
</div>

週次・月次のアクティブユーザー数を追跡。

<div id="analytics-report-headers">
  ## 分析レポートのヘッダー
</div>

ダッシュボードから分析データをエクスポートすると、レポートにはユーザー行動と機能利用に関する詳細なメトリクスが含まれる。各ヘッダーの意味は次のとおり。

<div id="user-information">
  ### ユーザー情報
</div>

<ResponseField name="Date" type="ISO 8601 timestamp">
  分析データが記録された日時（例: 2024-01-15T04:30:00.000Z）
</ResponseField>

<ResponseField name="User ID" type="string">
  システム内の各ユーザーに割り当てられた一意の識別子
</ResponseField>

<ResponseField name="Email" type="string">
  アカウントに紐づくユーザーのメールアドレス
</ResponseField>

<ResponseField name="Is Active" type="boolean">
  当日にユーザーがアクティブだったかを示す
</ResponseField>

<div id="ai-generated-code-metrics">
  ### AI生成コードのメトリクス
</div>

<ResponseField name="Chat Suggested Lines Added" type="number">
  AIチャット機能が追加を提案した行の合計
</ResponseField>

<ResponseField name="Chat Suggested Lines Deleted" type="number">
  AIチャット機能が削除を提案した行の合計
</ResponseField>

<ResponseField name="Chat Accepted Lines Added" type="number">
  ユーザーが受け入れてコードに追加したAI提案の行数
</ResponseField>

<ResponseField name="Chat Accepted Lines Deleted" type="number">
  ユーザーが受け入れたAI提案の削除行数
</ResponseField>

<div id="feature-usage-metrics">
  ### 機能利用メトリクス
</div>

<ResponseField name="Chat Total Applies" type="number">
  チャットからAI生成の変更を適用した回数
</ResponseField>

<ResponseField name="Chat Total Accepts" type="number">
  AI提案を受け入れた回数
</ResponseField>

<ResponseField name="Chat Total Rejects" type="number">
  AI提案を拒否した回数
</ResponseField>

<ResponseField name="Chat Tabs Shown" type="number">
  ユーザーにAI提案タブが表示された回数
</ResponseField>

<ResponseField name="Tabs Accepted" type="number">
  ユーザーが受け入れたAI提案タブの数
</ResponseField>

<div id="request-type-metrics">
  ### リクエスト種別メトリクス
</div>

<ResponseField name="Edit Requests" type="number">
  composer/edit機能を通じて行われたリクエスト（Cmd+Kのインライン編集）
</ResponseField>

<ResponseField name="Ask Requests" type="number">
  ユーザーがAIに質問したチャットリクエスト
</ResponseField>

<ResponseField name="Agent Requests" type="number">
  AIエージェント（特化型AIアシスタント）へのリクエスト
</ResponseField>

<ResponseField name="Cmd+K Usages" type="number">
  Cmd+K（またはCtrl+K）のコマンドパレットが使用された回数
</ResponseField>

<div id="subscription-and-api-metrics">
  ### サブスクリプションとAPIのメトリクス
</div>

<ResponseField name="Subscription Included Reqs" type="number">
  ユーザーのサブスクリプションプランでカバーされるAIリクエスト
</ResponseField>

<ResponseField name="API Key Reqs" type="number">
  プログラムからのアクセスでAPIキーを使用して行われたリクエスト
</ResponseField>

<ResponseField name="Usage-Based Reqs" type="number">
  従量課金の対象となるリクエスト
</ResponseField>

<div id="additional-features">
  ### 追加機能
</div>

<ResponseField name="Bugbot Usages" type="number">
  バグ検出/修正AI機能が使用された回数
</ResponseField>

<div id="configuration-information">
  ### 構成情報
</div>

<ResponseField name="Most Used Model" type="string">
  ユーザーが最も頻繁に使用したAIモデル（例: GPT-4、Claude）
</ResponseField>

<ResponseField name="Most Used Apply Extension" type="string">
  AI提案を適用する際に最もよく使用されたファイル拡張子（例: .ts、.py、.java）
</ResponseField>

<ResponseField name="Most Used Tab Extension" type="string">
  タブ補完機能で最もよく使用されたファイル拡張子
</ResponseField>

<ResponseField name="Client Version" type="string">
  使用中のCursorエディタのバージョン
</ResponseField>

<div id="calculated-metrics">
  ### 算出メトリクス
</div>

レポートには、AIのコード貢献度を把握するための加工データも含まれる。

* Total Lines Added/Deleted: すべてのコード変更の生の件数
* Accepted Lines Added/Deleted: AI提案に由来し、受け入れられた行数
* Composer Requests: インラインcomposer機能を通じて行われたリクエスト
* Chat Requests: チャットインターフェースを通じて行われたリクエスト

<Note>
  数値は未設定の場合はすべて0、booleanはfalse、文字列は空文字にデフォルト設定される。メトリクスはユーザーごとの日次で集計される。
</Note>



# Analytics V2
Source: https://docs.cursor.com/ja/account/teams/analyticsV2

高度なチームの利用状況とアクティビティ指標のトラッキング

分析基盤の V2 リリースを進めてるよ。これには、各種メトリクスのトラッキング方法のリファクタリングが含まれる。

**2025年9月1日**時点で、**Cursor version 1.5**を使ってるユーザーは、分析が V2 基盤を利用するようになる。以前のバージョンでは、次のような指標が過少計測されていた:

* 受け入れられたコード行数（合計）
* 提案されたコード行数（合計）
* 受け入れられたタブ数（合計）

引き続きアナリティクスに投資し、この領域で新機能をリリースしていくので、楽しみにしててね。



# Dashboard
Source: https://docs.cursor.com/ja/account/teams/dashboard

ダッシュボードから請求、利用状況、チーム設定を管理

ダッシュボードから請求情報の確認、従量課金の設定、チームの管理ができる。

<div id="overview">
  ## 概要
</div>

チームのアクティビティ、利用統計、最近の変更をすばやく把握できる。概要ページでは、ワークスペースの状況をひと目で確認できるよ。

<Frame>
  <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/dashboard.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=48ee98a4d9b168b93c26a03c1af74ddd" data-og-width="3456" width="3456" data-og-height="1944" height="1944" data-path="images/account/team/dashboard.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/dashboard.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=2ac6f157659354866eaa03b38cd1eb90 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/dashboard.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=8e9e84e894a3faf2846e3aae5deb9a2b 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/dashboard.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=e1034c739d961ccc69c17ba947edda90 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/dashboard.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=dbeed5506f7ae3fc4fabc7d248d69e64 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/dashboard.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=afac07ce763fccf7eded7248fb990745 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/dashboard.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=c4ed8c8161c3f2a964371a237134b1ae 2500w" />
</Frame>

<div id="settings">
  ## 設定
</div>

<Frame>
  <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/settings.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=5edb18df1ddc2d20e69abdd83140a509" data-og-width="1390" width="1390" data-og-height="913" height="913" data-path="images/account/team/settings.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/settings.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=4d4c8f244231868bf4111f05b1f46c93 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/settings.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=582ddf5415a973010e3bcbeeb13d4f64 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/settings.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=74a5d5f4644b701adc25b6d847f5752e 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/settings.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=9250830c64e8c3490c3ca6f7b6f65eec 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/settings.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=7ce96a620ac6d447e79abd901b5c6cdc 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/settings.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=6d24738577e0ffd837d87f8926339215 2500w" />
</Frame>

チーム全体の基本設定とセキュリティ設定を管理できる。設定ページには次の項目が含まれる:

<div id="teams-enterprise-settings">
  ## Teams と Enterprise の設定
</div>

<AccordionGroup>
  <Accordion title="プライバシー設定">
    チームのデータ共有ポリシーを管理。AI プロバイダー（OpenAI、Anthropic、Google Vertex AI、xAI Grok）とのゼロデータ保持ポリシーを設定し、チーム全体のプライバシー運用を統制できる。
  </Accordion>

  {" "}

  <Accordion title="従量課金の設定">
    従量課金を有効化し、支出上限を設定。チームの月次上限や、必要に応じてユーザー単位の上限も設定できる。これらの設定を管理者のみが変更できるよう制御可能。
  </Accordion>

  {" "}

  <Accordion title="Bedrock IAM ロール">
    セキュアなクラウド連携のために AWS Bedrock の IAM ロールを設定。
  </Accordion>

  {" "}

  <Accordion title="シングルサインオン（SSO）">
    エンタープライズチーム向けに SSO 認証を設定して、ユーザーアクセスを効率化し、セキュリティを強化。
  </Accordion>

  {" "}

  <Accordion title="Cursor 管理者 API キー">
    Cursor の管理機能にプログラムからアクセスするための API キーを作成・管理。
  </Accordion>

  {" "}

  <Accordion title="アクティブセッション">
    チーム全体のアクティブなユーザーセッションを監視・管理。
  </Accordion>

  <Accordion title="招待コード管理">
    新しいチームメンバーを追加するための招待コードを作成・管理。
  </Accordion>

  <Accordion title="API エンドポイント">
    Cursor の REST API エンドポイントにプログラムからアクセス。すべての API エンドポイントは Team と Enterprise の両プランで利用可能。ただし [AI Code Tracking API](/ja/docs/account/teams/ai-code-tracking-api) は Enterprise メンバーシップが必要。
  </Accordion>
</AccordionGroup>

<div id="enterprise-only-settings">
  ## エンタープライズ限定の設定
</div>

<AccordionGroup>
  {" "}

  <Accordion title="モデルアクセス制御">
    チームメンバーが使える AI モデルを制御できる。特定のモデルやモデル階層に制限を設けて、コストを管理し、組織全体で適切に使われるようにする。
  </Accordion>

  {" "}

  <Accordion title="自動実行の設定 (0.49+)">
    Cursor バージョン 0.49 以降の自動コマンド実行を設定する。自動実行を許可するコマンドを制御し、コード実行のセキュリティポリシーを定義する。
  </Accordion>

  <Accordion title="リポジトリブロックリスト">
    セキュリティやコンプライアンスの観点から、特定のリポジトリへのアクセスを禁止する。
  </Accordion>

  {" "}

  <Accordion title="MCP 設定 (0.51+)">
    Cursor バージョン 0.51 以降の Model Context Protocol を設定する。開発環境のコンテキストにモデルがどうアクセスし、どう処理するかを管理する。
  </Accordion>

  {" "}

  <Accordion title="Cursor Ignore 設定 (0.50+)">
    Cursor バージョン 0.50 以降で、ファイルやディレクトリの除外パターンを設定する。AI の解析や提案から除外する対象を制御する。
  </Accordion>

  <Accordion title=".cursor ディレクトリ保護 (0.51+)">
    バージョン 0.51 以降で .cursor ディレクトリへの不正アクセスを防ぐ。機密設定やキャッシュファイルの安全性を確保する。
  </Accordion>

  <Accordion title="AI Code Tracking API">
    チームのリポジトリに対する AI 生成コードの詳細な分析にアクセスできる。コミット単位の AI 利用メトリクスや、承認された AI 変更の粒度の高いデータを REST API エンドポイント経由で取得できる。利用には Enterprise プランが必要。詳しくは[こちら](/ja/account/teams/ai-code-tracking-api)。
  </Accordion>
</AccordionGroup>

<Note>
  **SCIM**（System for Cross-domain Identity Management）のプロビジョニングも Enterprise プランで利用可能。セットアップ手順は[SCIM のドキュメント](/ja/account/teams/scim)を参照してね。
</Note>

<div id="members">
  ## メンバー
</div>

チームメンバーを管理し、新規ユーザーを招待してアクセス権限を制御しよう。ロールベースの権限を設定して、メンバーのアクティビティをモニタリングできる。

<Frame>
  <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/members.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=4ac43692626733caf2da4b53e4cd9055" data-og-width="1390" width="1390" data-og-height="591" height="591" data-path="images/account/team/members.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/members.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=a2a24d3282df1e875d73fd2bf29b9c04 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/members.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=1abe9715816149f577a5d9c9e2f3545d 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/members.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=ccc84260c5139119e5b16ad6c214af72 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/members.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=5fe34e422fa9540004c25a61570029c3 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/members.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=dee7c3ade8ef46b5ead5dbe2bfd2a6be 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/members.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=9a42bce921a799886b8e3e0a389b8589 2500w" />
</Frame>

<div id="integrations">
  ## 連携
</div>

<Frame>
  <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/integrations.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=187b9e77d6b99c77caec81e1b3063417" data-og-width="1390" width="1390" data-og-height="592" height="592" data-path="images/account/team/integrations.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/integrations.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=470d5697ff2bfb9db2ae745b2c33cce6 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/integrations.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=e1e7d589f1f208ecdba9840629897968 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/integrations.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=2285e05c99c3a6ace609b51770475a3e 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/integrations.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=7c44649c5e8cd0f2a3791a3085252eca 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/integrations.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=0cf7111171c8019f7a59adc79cb9639d 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/integrations.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=8423a209b4e1c753045dca1514cbfbad 2500w" />
</Frame>

{" "}

Cursor をお気に入りのツールやサービスと連携しよう。バージョン管理システム、プロジェクト管理ツール、その他の開発者向けサービスとの連携を構成できる。

<div id="background-agents">
  ## バックグラウンドエージェント
</div>

<Frame>
  <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/integrations.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=187b9e77d6b99c77caec81e1b3063417" data-og-width="1390" width="1390" data-og-height="592" height="592" data-path="images/account/team/integrations.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/integrations.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=470d5697ff2bfb9db2ae745b2c33cce6 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/integrations.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=e1e7d589f1f208ecdba9840629897968 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/integrations.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=2285e05c99c3a6ace609b51770475a3e 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/integrations.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=7c44649c5e8cd0f2a3791a3085252eca 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/integrations.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=0cf7111171c8019f7a59adc79cb9639d 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/integrations.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=8423a209b4e1c753045dca1514cbfbad 2500w" />
</Frame>

{" "}

ワークスペースで動作しているバックグラウンドエージェントを監視・管理できる。エージェントのステータス、ログ、リソース使用量を確認できる。

<div id="bugbot">
  ## Bugbot
</div>

自動バグ検出と修正機能にアクセス。Bugbot はコードベースのよくある問題を自動で特定し、解決まで手早く進めてくれる。

<Frame>
  <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/bugbot.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=20d841dfc7837445103a933dab18b470" alt="Bugbot code review" data-og-width="1390" width="1390" data-og-height="913" height="913" data-path="images/account/team/bugbot.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/bugbot.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=975f5e3f9f9a0334c8a5bcc12faf72be 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/bugbot.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=17099f8bbe0701750d0ba212879d8a93 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/bugbot.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=041c82a4c3bada0524527609dfc134a4 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/bugbot.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=90ac57ea38768ace4b9404476fafdf32 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/bugbot.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=5785673a93f899ccca7b70e7a3752ef7 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/bugbot.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=a1a1dc51872967e392e10d6b85c31a04 2500w" />
</Frame>

<div id="active-directory-management">
  ## Active Directory 管理
</div>

エンタープライズチーム向けに、Active Directory 連携でユーザー認証とアクセスを管理。SSO とユーザープロビジョニングを設定しよう。

<div id="usage">
  ## 使用状況
</div>

AIリクエスト、モデル利用、リソース消費などの詳細な利用メトリクスを追跡。チームメンバーやプロジェクトをまたいで利用状況をモニタリング。

<Frame>
  <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/usage.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=8744e41430d162199d85ca8e966c91cd" data-og-width="1390" width="1390" data-og-height="913" height="913" data-path="images/account/team/usage.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/usage.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=bc43eaaeca3c2a531a56243037a7a53f 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/usage.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=34700d63fabf072e9906aab74f79f7d9 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/usage.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=7f2bcdb271d6b30e333374c798638989 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/usage.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=424bd0eeda69200668f8f0b86dc360bf 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/usage.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=f0e716c72f01a3297a53a5b63d191ef4 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/usage.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=ffa574322508a07cc5ab867b331b6d35 2500w" />
</Frame>

<div id="billing-invoices">
  ## 請求と請求書
</div>

サブスクの管理、支払い方法の更新、請求履歴の確認ができる。請求書のダウンロードや従量課金の設定管理もできる。

<Frame>
  <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/billing.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=d76d20a7fafc6ed2135f2f9c78ec6c2d" data-og-width="1390" width="1390" data-og-height="913" height="913" data-path="images/account/team/billing.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/billing.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=45501f34dd144ecd74e982fe5f8f8364 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/billing.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=19860b61e083a8550cb3caa16bdb1ba0 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/billing.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=7005bae381a362b39980a49113ca367c 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/billing.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=e47c9ee55e3699ba46429b0ac0563b5b 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/billing.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=039106fd5ff42f2e343b2b853614e7e7 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/billing.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=e598f83559985558f5825a3da25bb554 2500w" />
</Frame>



# エンタープライズ設定
Source: https://docs.cursor.com/ja/account/teams/enterprise-settings

組織のCursor設定を一元管理

<div id="enterprise-settings">
  # Enterprise settings
</div>

デバイス管理ソリューションを通じて Cursor の特定機能を一元管理し、組織の要件に適合させられる。Cursor ポリシーを指定すると、その値がユーザー端末の対応する Cursor 設定を上書きする。

設定エディターで「Extensions: Allowed」設定が組織により管理されていることが示されている。

Cursor では現在、以下の管理者制御機能を管理するポリシーを提供している:

| Policy            | Description                                              | Cursor setting           | Available since |
| ----------------- | -------------------------------------------------------- | ------------------------ | --------------- |
| AllowedExtensions | インストールを許可する拡張機能を制御する。                                    | extensions.allowed       | 1.2             |
| AllowedTeamId     | ログインを許可するチーム ID を制御する。許可されていないチーム ID のユーザーは強制的にログアウトされる。 | cursorAuth.allowedTeamId | 1.3             |

<div id="configure-allowed-extensions">
  ## 許可する拡張機能を設定する
</div>

`extensions.allowed` の Cursor 設定では、インストールを許可する拡張機能を制御できる。この設定は JSON オブジェクトを取り、キーにパブリッシャー名、値にそのパブリッシャーの拡張機能を許可するかどうかを示す boolean を指定する。

たとえば、`extensions.allowed` を `{"anysphere": true, "github": true}` にすると Anysphere と GitHub のパブリッシャーからの拡張機能が許可され、`{"anysphere": false}` にすると Anysphere の拡張機能はブロックされる。

組織で許可する拡張機能を一元管理したい場合は、デバイス管理ソリューションで `AllowedExtensions` ポリシーを構成しよう。このポリシーはユーザーのデバイス上の `extensions.allowed` 設定を上書きする。ポリシーの値は、許可するパブリッシャーを定義する JSON 文字列だ。

Cursor の拡張機能についてもっと知りたいなら、extensions のドキュメントを見てね。

<div id="configure-allowed-team-ids">
  ## 許可されるチーム ID を設定する
</div>

`cursorAuth.allowedTeamId` は、Cursor にログインを許可するチーム ID を制御する設定だ。この設定には、アクセスを許可するチーム ID をカンマ区切りで指定する。

たとえば、`cursorAuth.allowedTeamId` を `"1,3,7"` に設定すると、それらのチーム ID に属するユーザーがログインできる。

許可リストにないチーム ID でログインを試みた場合:

* 即座に強制ログアウトされる
* エラーメッセージが表示される
* 有効なチーム ID が使われるまで、アプリはそれ以上の認証試行をブロックする

組織で許可されるチーム ID を一元管理するには、デバイス管理ソリューションで `AllowedTeamId` ポリシーを構成する。このポリシーは、ユーザーのデバイス上の `cursorAuth.allowedTeamId` 設定を上書きする。ポリシーの値は、許可されたチーム ID をカンマ区切りで並べた文字列だ。

<div id="group-policy-on-windows">
  ## Windows のグループ ポリシー
</div>

Cursor は Windows のレジストリ ベースのグループ ポリシーに対応してる。ポリシー定義をインストールすると、管理者はローカル グループ ポリシー エディターでポリシー値を管理できる。

ポリシーを追加する手順:

1. `AppData\Local\Programs\cursor\policies` からポリシーの ADMX と ADML ファイルをコピー。
2. ADMX ファイルを `C:\Windows\PolicyDefinitions` ディレクトリに、ADML ファイルを `C:\Windows\PolicyDefinitions\<your-locale>\` ディレクトリに貼り付け。
3. ローカル グループ ポリシー エディターを再起動。
4. ローカル グループ ポリシー エディターで適切なポリシー値を設定（例: `AllowedExtensions` ポリシーなら `{"anysphere": true, "github": true}`）。

ポリシーはコンピューター レベルとユーザー レベルの両方で設定できる。両方設定されている場合は、コンピューター レベルが優先される。ポリシー値が設定されていると、その値が Cursor のいずれのレベル（デフォルト、ユーザー、ワークスペース など）で構成された設定値よりも優先される。

<div id="configuration-profiles-on-macos">
  ## macOS の構成プロファイル
</div>

構成プロファイルは macOS デバイスの設定を管理する。プロファイルは、利用可能なポリシーに対応するキーと値のペアを含む XML ファイル。これらのプロファイルは Mobile Device Management (MDM) ソリューションで配布するか、手動でインストールできる。

<Accordion title="Example .mobileconfig file">
  macOS 向けの `.mobileconfig` ファイルの例は次のとおり:

  ```
  <?xml version="1.0" encoding="UTF-8"?>
  <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
  <plist version="1.0">
  	<dict>
  		<key>PayloadContent</key>
  		<array>
  			<dict>
  				<key>PayloadDisplayName</key>
  				<string>Cursor</string>
  				<key>PayloadIdentifier</key>
  				<string>com.todesktop.230313mzl4w4u92.J6B5723A-6539-4F31-8A4E-3CC96E51F48C</string>
  				<key>PayloadType</key>
  				<string>com.todesktop.230313mzl4w4u92</string>
  				<key>PayloadUUID</key>
  				<string>J6B5723A-6539-4F31-8A4E-3CC96E51F48C</string>
  				<key>PayloadVersion</key>
  				<integer>1</integer>
  				<key>AllowedExtensions</key>
  				<string>{"anysphere":true}</string>
  				<key>AllowedTeamId</key>
  				<string>1,2</string>
  			</dict>
  		</array>
  		<key>PayloadDescription</key>
  		<string>This profile manages Cursor.</string>
  		<key>PayloadDisplayName</key>
  		<string>Cursor</string>
  		<key>PayloadIdentifier</key>
  		<string>com.todesktop.230313mzl4w4u92</string>
  		<key>PayloadOrganization</key>
  		<string>Anysphere</string>
  		<key>PayloadType</key>
  		<string>Configuration</string>
  		<key>PayloadUUID</key>
  		<string>F2C1A7B3-9D4E-4B2C-8E1F-7A6C5D4B3E2F</string>
  		<key>PayloadVersion</key>
  		<integer>1</integer>
  		<key>TargetDeviceType</key>
  		<integer>5</integer>
  	</dict>
  </plist>
  ```
</Accordion>

<div id="string-policies">
  ### 文字列ポリシー
</div>

以下の例は `AllowedExtensions` ポリシーの設定方法を示す。サンプルファイルではポリシー値は空で始まり（許可される拡張機能はない）、必要に応じて設定する。

```
<key>AllowedExtensions</key>
<string></string>
```

`<string>` タグの間に、ポリシーを定義する適切な JSON 文字列を追加して。

```
<key>AllowedExtensions</key>
<string>{"anysphere": true, "github": true}</string>
```

`AllowedTeamId` ポリシーには、チーム ID のカンマ区切りリストを追加してね：

```
<key>AllowedTeamId</key>
<string>1,3,7</string>
```

**重要:** 提供された `.mobileconfig` ファイルは、その Cursor バージョンで利用可能なポリシーを**すべて**初期化する。不要なポリシーは削除してね。

サンプルの `.mobileconfig` でポリシーを編集または削除しない場合、そのポリシーは既定の（制限的な）値で適用される。

構成プロファイルは、Finder で `.mobileconfig` をダブルクリックしてインストールし、システム設定の **一般** > **デバイス管理** で有効化すれば手動インストールできる。システム設定からプロファイルを削除すると、Cursor に適用されているポリシーも削除される。

構成プロファイルの詳細は、Apple のドキュメントを参照してね。

<div id="additional-policies">
  ## 追加ポリシー
</div>

目的は、現在の Cursor の設定をポリシーとして打ち出し、既存の設定に忠実に沿うことで、名称と挙動の一貫性を保つこと。さらにポリシーを増やしてほしい場合は、Cursor の GitHub リポジトリで issue を立ててね。チームが、その挙動に対応する既存設定があるか、望まれる挙動を制御するための新しい設定を作るべきかを判断するよ。

<div id="frequently-asked-questions">
  ## よくある質問
</div>

<div id="does-cursor-support-configuration-profiles-on-linux">
  ### CursorはLinuxで設定プロファイルをサポートしてる？
</div>

Linuxのサポートは現在のロードマップにはないよ。Linuxで設定プロファイルが欲しい場合は、CursorのGitHubリポジトリでIssueを立てて、ユースケースの詳細を共有してね。



# メンバーと役割
Source: https://docs.cursor.com/ja/account/teams/members

チームメンバーと役割の管理

Cursor のチームには 3 つの役割がある：

<div id="roles">
  ## 役割
</div>

**Member** はデフォルトのロールで、Cursor の Pro 機能にアクセスできる。

* Cursor の Pro 機能にフルアクセス
* 請求設定や管理者ダッシュボードへのアクセスは不可
* 自分の利用状況と残りの従量課金予算を確認できる

**Admin** はチーム管理とセキュリティ設定を担当する。

* Pro 機能にフルアクセス
* メンバーの追加/削除、ロールの変更、SSO のセットアップ
* 従量課金の設定と支出上限の構成
* チーム分析へのアクセス

**Unpaid Admin** は有料シートを消費せずにチームを管理できる。Cursor へのアクセスが不要な IT や経理担当に最適。

* 請求対象外、Pro 機能なし
* Admin と同等の管理機能

<Info>Unpaid Admin を利用するには、チーム内に少なくとも 1 人の有料ユーザーが必要。</Info>

<div id="role-comparison">
  ## 役割の比較
</div>

<div className="full-width-table">
  | 権限            | メンバー | 管理者 | 無料管理者 |
  | ------------- | :--: | :-: | :---: |
  | Cursor の機能を利用 |   ✓  |  ✓  |       |
  | メンバーを招待       |   ✓  |  ✓  |   ✓   |
  | メンバーを削除       |      |  ✓  |   ✓   |
  | ユーザーの役割を変更    |      |  ✓  |   ✓   |
  | 管理者ダッシュボード    |      |  ✓  |   ✓   |
  | SSO/セキュリティを設定 |      |  ✓  |   ✓   |
  | 請求を管理         |      |  ✓  |   ✓   |
  | アナリティクスを表示    |      |  ✓  |   ✓   |
  | アクセスを管理       |      |  ✓  |   ✓   |
  | 利用制限を設定       |      |  ✓  |   ✓   |
  | 有料シートが必要      |   ✓  |  ✓  |       |
</div>

<div id="managing-members">
  ## メンバーの管理
</div>

すべてのチームメンバーが他の人を招待できる。現時点では招待に制限はない。

<div id="add-member">
  ### メンバーを追加
</div>

メンバーの追加方法は3つ:

1. **メール招待**

   * `Invite Members` をクリック
   * メールアドレスを入力
   * ユーザーに招待メールが届く

2. **招待リンク**

   * `Invite Members` をクリック
   * `Invite Link` をコピー
   * チームメンバーに共有

3. **SSO**
   * [admin dashboard](/ja/account/teams/sso) で SSO を設定
   * ユーザーは SSO のメールでログインすると自動参加

<Warning>
  招待リンクは有効期限が長く、リンクを知っていれば誰でも参加できる。
  リンクを無効化するか、[SSO](/ja/account/teams/sso) を使おう
</Warning>

<div id="remove-member">
  ### メンバーを削除
</div>

管理者はコンテキストメニュー → "Remove" からいつでもメンバーを削除できる。メンバーがクレジットを使用している場合、その席は請求サイクルの終了まで占有されたまま。

<div id="change-role">
  ### 役割を変更
</div>

管理者はコンテキストメニューを開き、"Change role" オプションで他のメンバーの役割を変更できる。<br />

常にチーム内に少なくとも1人の管理者と1人の有料メンバーが必要。

## セキュリティ & SSO

SAML 2.0 シングルサインオン（SSO）は Team プランで利用できるよ。主な機能は次のとおり:

* SSO 接続の構成（[詳しくはこちら](/ja/account/teams/sso)）
* ドメインの検証設定
* ユーザーの自動プロビジョニング
* SSO の強制オプション
* ID プロバイダー連携（Okta など）

<Note>
  <p className="!mb-0">SSO を有効にするには、ドメインの検証が必要だよ。</p>
</Note>

<Frame>
  <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=76608c26daf1f9ab2bbc2c4ccb156c0e" style={{ padding: `32px 64px`, backgroundColor: "#0c0c0c" }} data-og-width="802" width="802" data-og-height="440" height="440" data-path="images/account/sso-settings.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=334dc1fc107338d19ec7b0052e7ea0e4 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=543b3d868c19960a5fb4c526d9895bd3 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=a06655178ba10f6a72919e9f7d598191 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=e280fc911306fe8d3b8e90b7221b0c11 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=ffd8f2c0168e2ac4f95431062b226021 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=1c17e4eac666b663d676ce874f1c4ba5 2500w" />
</Frame>

<div id="usage-controls">
  ## 利用コントロール
</div>

利用設定で次の操作ができる:

* 従量課金を有効にする
* プレミアムモデルで有効にする
* 管理者のみ変更可能にする
* 月間支出上限を設定する
* チーム全体の利用状況をモニタリングする

<Frame>
  <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/usage-based-pricing.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=e8149f830c27308af1bcc329c25e38b5" style={{ backgroundColor: "#0c0c0c" }} data-og-width="1668" width="1668" data-og-height="1160" height="1160" data-path="images/account/usage-based-pricing.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/usage-based-pricing.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=bc308a967251694ad7b03189c1083c61 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/usage-based-pricing.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=ddc293e19fa993e65be8c09ced649b4f 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/usage-based-pricing.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=3a4df7d48d75c6166ab215550a641ca6 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/usage-based-pricing.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=f9051947c802ae54fd964196c50a3701 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/usage-based-pricing.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=ed775e3e98611ead1b938aedaf917f11 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/usage-based-pricing.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=b26f86bce94dc981d3cf71853a965374 2500w" />
</Frame>

<div id="billing">
  ## 請求
</div>

チームメンバーを追加する場合:

* 各メンバーまたは管理者は課金対象のシートを追加する（[pricing](https://cursor.com/pricing) を参照）
* 新規メンバーには、請求期間の残り日数に応じて按分課金される
* 未払いの管理者シートはカウントされない

月途中の追加は、使用日数分のみ課金。クレジットを使用したメンバーを削除しても、そのシートは請求サイクル終了まで占有されたままになり、日割りでの返金は行われない。

役割の変更（例: Admin → Unpaid Admin）は、変更日から請求が調整される。請求は月払いまたは年払いを選択できる。

月払い/年払いの更新は、メンバー変更に関係なく、初回サインアップ日を基準に行われる。

<div id="switch-to-yearly-billing">
  ### 年払いに切り替える
</div>

月払いから年払いに切り替えると **20%** 節約:

1. [Dashboard](https://cursor.com/dashboard) に移動
2. アカウントセクションで「Advanced」をクリックし、「Upgrade to yearly billing」を選択

<Note>
  月払いから年払いへの切り替えはダッシュボードからのみ可能。年払いから月払いに切り替える場合は、[hi@cursor.com](mailto:hi@cursor.com) まで連絡してね。
</Note>



# SCIM
Source: https://docs.cursor.com/ja/account/teams/scim

ユーザーとグループの自動管理に向けて SCIM プロビジョニングを設定

<div id="overview">
  ## 概要
</div>

SCIM 2.0 プロビジョニングは、アイデンティティプロバイダー経由でチームメンバーとディレクトリグループを自動的に管理するよ。SSO を有効にした Enterprise プランで利用できる。

<product_visual type="screenshot">
  SCIM 設定ダッシュボードの Active Directory Management 構成
</product_visual>

<div id="prerequisites">
  ## 前提条件
</div>

* Cursor Enterprise プラン
* 先に SSO を設定しておくこと — **SCIM を使うにはアクティブな SSO 接続が必要**
* アイデンティティプロバイダー（Okta、Azure AD など）への管理者アクセス
* Cursor 組織への管理者アクセス

<div id="how-it-works">
  ## 仕組み
</div>

<div id="user-provisioning">
  ### ユーザーのプロビジョニング
</div>

ID プロバイダーで SCIM アプリに割り当てると、ユーザーは自動的に Cursor に追加される。割り当てを外すと削除される。変更はリアルタイムで同期される。

<div id="directory-groups">
  ### ディレクトリグループ
</div>

ディレクトリグループとそのメンバーは ID プロバイダーから同期される。グループやユーザーの管理は ID プロバイダーで行う必要があり、Cursor では参照のみで表示される。

<div id="spend-management">
  ### 予算管理
</div>

ディレクトリグループごとにユーザー単位の利用上限を設定できる。ディレクトリグループの上限はチームレベルの上限より優先される。複数のグループに所属しているユーザーには、適用可能な上限のうち最も高いものが適用される。

<div id="setup">
  ## セットアップ
</div>

<Steps>
  <Step title="SSO が設定済みか確認">
    SCIM を使うには、先に SSO のセットアップが必要。まだ設定してないなら、
    先に [SSO セットアップガイド](/ja/account/teams/sso) を見てから進めてね。
  </Step>

  <Step title="Active Directory Management にアクセス">
    管理者アカウントで
    [cursor.com/dashboard?tab=active-directory](https://www.cursor.com/dashboard?tab=active-directory)
    にアクセスするか、ダッシュボードの設定から
    「Active Directory Management」タブを選択。
  </Step>

  <Step title="SCIM セットアップを開始">
    SSO の検証が完了すると、手順付きの SCIM セットアップへのリンクが表示される。
    それをクリックして設定ウィザードを開始しよう。
  </Step>

  <Step title="ID プロバイダーで SCIM を構成">
    ID プロバイダー側で: - SCIM アプリを作成または構成 - Cursor が提供する SCIM エンドポイントとトークンを使用 - ユーザーおよびグループのプッシュ型プロビジョニングを有効化 - 接続テストを実行
  </Step>

  <Step title="支出上限を設定（任意）">
    Cursor の Active Directory Management ページに戻って: - 同期済みのディレクトリグループを確認 - 必要に応じて特定グループ向けにユーザー単位の支出上限を設定 - 複数グループに所属するユーザーに適用される上限を確認
  </Step>
</Steps>

<div id="identity-provider-setup">
  ### ID プロバイダーのセットアップ
</div>

プロバイダーごとのセットアップ手順:

<Card title="Identity Provider ガイド" icon="book" href="https://workos.com/docs/integrations">
  Okta、Azure AD、Google Workspace などのセットアップ手順。
</Card>

<div id="managing-users-and-groups">
  ## ユーザーとグループの管理
</div>

<Warning>
  ユーザーとグループの管理は、すべてアイデンティティプロバイダー側で行ってね。
  アイデンティティプロバイダーでの変更は自動的に Cursor と同期されるけど、
  Cursor 上でユーザーやグループを直接変更することはできないよ。
</Warning>

<div id="user-management">
  ### ユーザー管理
</div>

* アイデンティティプロバイダーで SCIM アプリに割り当ててユーザーを追加
* SCIM アプリの割り当てを解除してユーザーを削除
* ユーザープロフィールの変更（名前、メールアドレス）はアイデンティティプロバイダーから自動同期

<div id="group-management">
  ### グループ管理
</div>

* ディレクトリグループはアイデンティティプロバイダーから自動同期される
* グループメンバーシップの変更はリアルタイムに反映される
* グループを使ってユーザーを整理し、異なる利用上限を設定できる

<div id="spend-limits">
  ### 利用上限
</div>

* ディレクトリグループごとにユーザー単位の上限を個別に設定
* ユーザーは所属するグループのうち最も高い利用上限を継承
* グループの上限は、チーム全体のデフォルトのユーザー単位上限を上書きする

<div id="faq">
  ## FAQ
</div>

<div id="why-isnt-scim-management-showing-up-in-my-dashboard">
  ### ダッシュボードに SCIM 管理が表示されないのはなぜ？
</div>

SCIM を設定する前に、SSO が正しく構成されていて正常に動作してるか確認して。SCIM は有効な SSO 接続が必要だよ。

<div id="why-arent-users-syncing">
  ### ユーザーが同期されないのはなぜ？
</div>

アイデンティティプロバイダーで、ユーザーが SCIM アプリに割り当てられてるか確認して。Cursor に表示されるには、ユーザーは明示的に割り当てが必要だよ。

<div id="why-arent-groups-appearing">
  ### グループが表示されないのはなぜ？
</div>

アイデンティティプロバイダーの SCIM 設定で、プッシュ型のグループプロビジョニングが有効になってるか確認して。グループ同期はユーザー同期とは別に設定が必要だよ。

<div id="why-arent-spend-limits-applying">
  ### 利用上限が適用されないのはなぜ？
</div>

アイデンティティプロバイダーで、ユーザーが想定どおりのグループに正しく割り当てられてるか確認して。どの利用上限が適用されるかはグループメンバーシップで決まるよ。

<div id="can-i-manage-scim-users-and-groups-directly-in-cursor">
  ### SCIM のユーザーとグループを Cursor 上で直接管理できる？
</div>

できないよ。ユーザーとグループの管理はすべてアイデンティティプロバイダー側で行う必要がある。Cursor ではこの情報は読み取り専用で表示されるよ。

<div id="how-quickly-do-changes-sync">
  ### 変更はどれくらいの速さで同期される？
</div>

アイデンティティプロバイダーでの変更はリアルタイムで Cursor に同期される。大規模な一括処理では短い遅延が発生する場合があるよ。



# はじめ方
Source: https://docs.cursor.com/ja/account/teams/setup

Cursor のチームを作成してセットアップする

<div id="cursor-for-teams">
  ## Cursor for Teams
</div>

Cursorは個人でもチームでも使える。Teamsプランでは、SSO、チーム管理、アクセス制御、利用状況の分析といった組織向けのツールを提供する。

<div id="creating-a-team">
  ## チームの作成
</div>

次の手順でチームを作成しよう:

<Steps>
  <Step title="Teams プランを設定">
    チームを作成するには、次の手順に従ってね:

    1. **新規ユーザー向け**: [cursor.com/team/new-team](https://cursor.com/team/new-team) にアクセスして、新しいアカウントとチームを作成
    2. **既存ユーザー向け**: 自分の[ダッシュボード](/ja/account/dashboard)に移動して「Upgrade to Teams」をクリック
  </Step>

  <Step title="チームの詳細を入力">
    チーム名と請求サイクルを選択

    <Frame>
      <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/new-team.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=3b9df20d032b544dcbc0343d9ddf056f" data-og-width="3456" width="3456" data-og-height="2158" height="2158" data-path="images/account/team/new-team.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/new-team.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=b81f3241069a8a0fb9278b6a2e246057 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/new-team.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=c26976bf06297d36ec9224ec1496a630 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/new-team.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=fed5c7c95914ff47cfceae81f1441208 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/new-team.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=0dc5986368419ef54f45803547741cfe 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/new-team.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=4eb38a9618399ddadbf7596b185d2732 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/new-team.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=1c7d720a1e20d2aa23463a1b9001d545 2500w" />
    </Frame>
  </Step>

  <Step title="メンバーを招待">
    チームメンバーを招待。ユーザー数は日割りで精算されるから、メンバーである期間分だけ支払えばOK。

    <Frame>
      <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/invite-members.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=bbd84dd96a7003415c2d2f038b1aaa77" style={{ paddingLeft: 16, paddingRight: 16, backgroundColor: '#0c0c0c' }} data-og-width="880" width="880" data-og-height="422" height="422" data-path="images/account/invite-members.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/invite-members.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=988e36ee874f704dfaae1b0a69ed2f84 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/invite-members.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=c0f85aacd3be59e11b1bfd05f9e5d6cd 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/invite-members.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=411456e375f8c406ad2972965e0b549e 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/invite-members.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=57ae04799be300a7e61464490344146f 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/invite-members.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=2faa0cf8ed56865c19916e33fde97900 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/invite-members.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=0bdb5040f44338e748246b4f1ddf2ddf 2500w" />
    </Frame>
  </Step>

  <Step title="SSO を有効化 (任意)">
    セキュリティ強化と自動オンボーディングのために[SSO](/ja/account/teams/sso)を有効化。

    <Frame>
      <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=76608c26daf1f9ab2bbc2c4ccb156c0e" data-og-width="802" width="802" data-og-height="440" height="440" data-path="images/account/sso-settings.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=334dc1fc107338d19ec7b0052e7ea0e4 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=543b3d868c19960a5fb4c526d9895bd3 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=a06655178ba10f6a72919e9f7d598191 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=e280fc911306fe8d3b8e90b7221b0c11 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=ffd8f2c0168e2ac4f95431062b226021 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=1c17e4eac666b663d676ce874f1c4ba5 2500w" />
    </Frame>
  </Step>
</Steps>

<div id="faq">
  ## FAQ
</div>

<AccordionGroup>
  <Accordion title="チームで Zscaler / プロキシ / VPN を使ってるけど、Cursor は動く？">
    Cursor はデフォルトで HTTP/2 を使う。プロキシや VPN によってはブロックされることがある。

    設定で HTTP/1.1 フォールバックを有効にして、HTTP/1.1 を使ってね。
  </Accordion>

  <Accordion title="会社向けにライセンスを購入するには？">
    Cursor はシート数ではなくアクティブユーザー単位で課金する。ユーザーの追加・削除はいつでもOK。新規メンバーは残り期間に応じて日割りで請求される。削除したユーザーがクレジットを使用している場合、そのシートは請求サイクルの終了まで占有されたままになる。

    更新日は変わらない。
  </Accordion>

  <Accordion title="自分が Cursor を使っていない状態でチームをセットアップするには？">
    ライセンスなしで管理できるよう、自分のロールを[Unpaid Admin](/ja/account/teams/members)に設定してね。

    <Warning>
      チームには最低でも 1 名の有料メンバーが必要。先にセットアップしてメンバーを招待し、請求前に自分のロールを変更できる。
    </Warning>
  </Accordion>

  <Accordion title="会社の MDM に Cursor を追加するには？">
    すべてのプラットフォーム向けのダウンロードリンクは [cursor.com/downloads](https://cursor.com/downloads) にある。

    MDM の手順:

    * [Omnissa Workspace ONE](https://docs.omnissa.com/bundle/MobileApplicationManagementVSaaS/page/DeployInternalApplications.html)（旧 VMware）
    * [Microsoft Intune（Windows）](https://learn.microsoft.com/en-us/mem/intune-service/apps/apps-win32-app-management)
    * [Microsoft Intune（Mac）](https://learn.microsoft.com/en-us/mem/intune-service/apps/lob-apps-macos-dmg)
    * [Kandji MDM](https://support.kandji.io/kb/custom-apps-overview)
  </Accordion>
</AccordionGroup>



# SSO
Source: https://docs.cursor.com/ja/account/teams/sso

チームのシングルサインオンを設定する

<div id="overview">
  ## 概要
</div>

SAML 2.0 SSO は Business プランで追加費用なしで使える。既存のアイデンティティプロバイダー（IdP）を使って、別途 Cursor アカウントを作らなくてもチームメンバーを認証できる。

<Frame>
  <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=76608c26daf1f9ab2bbc2c4ccb156c0e" style={{ padding: 32, backgroundColor: "#0c0c0c" }} data-og-width="802" width="802" data-og-height="440" height="440" data-path="images/account/sso-settings.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=334dc1fc107338d19ec7b0052e7ea0e4 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=543b3d868c19960a5fb4c526d9895bd3 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=a06655178ba10f6a72919e9f7d598191 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=e280fc911306fe8d3b8e90b7221b0c11 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=ffd8f2c0168e2ac4f95431062b226021 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=1c17e4eac666b663d676ce874f1c4ba5 2500w" />
</Frame>

<div id="prerequisites">
  ## 前提条件
</div>

* Cursor Team プラン
* アイデンティティプロバイダー（例：Okta）への管理者権限
* Cursor 組織への管理者権限

<div id="configuration-steps">
  ## 設定手順
</div>

<Steps>
  <Step title="Cursor アカウントにサインイン">
    管理者アカウントで [cursor.com/dashboard?tab=settings](https://www.cursor.com/dashboard?tab=settings) にアクセス。
  </Step>

  <Step title="SSO 設定を開く">
    「Single Sign-On (SSO)」セクションを見つけて展開。
  </Step>

  <Step title="セットアップを開始">
    「SSO Provider Connection settings」ボタンをクリックして SSO のセットアップを開始し、ウィザードに沿って進める。
  </Step>

  <Step title="アイデンティティプロバイダを設定">
    使っているアイデンティティプロバイダ（例: Okta）で:

    * 新しい SAML アプリケーションを作成
    * Cursor の情報を使って SAML 設定を構成
    * Just-in-Time (JIT) プロビジョニングを設定
  </Step>

  <Step title="ドメインの確認">
    Cursor で「Domain verification settings」ボタンをクリックして、ユーザーのドメインを確認。
  </Step>
</Steps>

<div id="identity-provider-setup-guides">
  ### アイデンティティプロバイダのセットアップガイド
</div>

プロバイダごとのセットアップ手順:

<Card title="Identity Provider Guides" icon="book" href="https://workos.com/docs/integrations">
  Okta、Azure AD、Google Workspace などのセットアップ手順。
</Card>

<div id="additional-settings">
  ## 追加設定
</div>

* 管理者ダッシュボードで SSO の適用を管理
* 新規ユーザーは SSO 経由のサインインで自動的に登録
* ユーザー管理はアイデンティティプロバイダー側で実施

<div id="troubleshooting">
  ## トラブルシューティング
</div>

問題が発生した場合は次を確認:

* Cursor でドメインが検証済みか
* SAML 属性が正しくマッピングされているか
* 管理ダッシュボードで SSO が有効になっているか
* アイデンティティプロバイダーと Cursor 間で名・姓が一致しているか
* 上記のプロバイダー別ガイドを参照
* 解決しない場合は [hi@cursor.com](mailto:hi@cursor.com) まで連絡



# アップデート受信設定
Source: https://docs.cursor.com/ja/account/update-access

アップデートの受け取り頻度を選ぶ

export const Kbd = ({children, tooltip, os}) => {
  const keysInput = typeof children === 'string' && children.trim() !== '' ? children : null;
  if (!keysInput) {
    return null;
  }
  const isModifier = key => {
    const modifiers = ['⌘', '⇧', '⌥', '⌃', '⏎', '⌫', '⌦', '⎋', '⇥', '⌁', '←', '→', '↑', '↓', 'Ctrl', 'Shift', 'Alt', 'Cmd', 'Opt', 'Return', 'Backspace', 'Delete', 'Escape', 'Tab', 'Space', 'Enter', 'Esc', 'ArrowLeft', 'ArrowRight', 'ArrowUp', 'ArrowDown', 'Left', 'Right', 'Up', 'Down'];
    return modifiers.includes(key.trim());
  };
  const capitalizeFirstLetter = string => {
    return string.charAt(0).toUpperCase() + string.slice(1);
  };
  const isMac = os ? os.toLowerCase() === 'mac' || os.toLowerCase() === 'macos' : typeof navigator !== 'undefined' && (navigator.platform.toUpperCase().indexOf('MAC') >= 0 || navigator.userAgent.toUpperCase().indexOf('MAC') >= 0);
  const convertToSymbols = shortcut => {
    if (isMac) {
      return shortcut.replace(/⌘|Cmd|CMD/gi, '⌘').replace(/⌥|Opt|OPT/gi, '⌥').replace(/⌃|Ctrl/gi, '⌃').replace(/⇧|Shift/gi, '⇧').replace(/⏎|Return/gi, '⏎').replace(/⌫|Backspace/gi, '⌫').replace(/⌦|Delete/gi, '⌦').replace(/␛|Escape/gi, '␛').replace(/⇥|Tab/gi, '⇥').replace(/⌁|Space/gi, '⌁').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, '←').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, '→').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, '↑').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, '↓');
    } else {
      const converted = shortcut.replace(/⌘|Cmd|CMD/gi, 'Ctrl').replace(/⌥|Opt|OPT/gi, 'Alt').replace(/⌃|Ctrl/gi, 'Ctrl').replace(/⇧|Shift/gi, 'Shift').replace(/⏎|Return/gi, 'Enter').replace(/⌫|Backspace/gi, 'Backspace').replace(/⌦|Delete/gi, 'Delete').replace(/⎋|Escape/gi, 'Esc').replace(/⇥|Tab/gi, 'Tab').replace(/⌁|Space/gi, 'Space').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, 'Arrow-Left').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, 'Arrow-Right').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, 'Arrow-Up').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, 'Arrow-Down');
      const keyList = converted.split(/[\+\s]+/).filter(key => key.trim());
      return keyList.join('+');
    }
  };
  const convertToReadableText = shortcut => {
    const converted = shortcut.replace(/⌘|Cmd|CMD/gi, 'Cmd').replace(/⌥|Opt|OPT/gi, 'Opt').replace(/⌃|Ctrl/gi, 'Ctrl').replace(/⇧|Shift/gi, 'Shift').replace(/⏎|Return/gi, 'Return').replace(/⌫|Backspace/gi, 'Backspace').replace(/⌦|Delete/gi, 'Delete').replace(/⎋|Escape/gi, 'Escape').replace(/⇥|Tab/gi, 'Tab').replace(/⌁|Space/gi, 'Space').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, 'Arrow-Left').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, 'Arrow-Right').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, 'Arrow-Up').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, 'Arrow-Down');
    const keyList = converted.split(/[\+\s]+/).filter(key => key.trim());
    return keyList.map(key => {
      const trimmedKey = key.trim();
      return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
    }).join('+');
  };
  const displayShortcut = convertToSymbols(keysInput);
  const tooltipText = isMac ? tooltip ? `${convertToReadableText(keysInput)}: ${tooltip}` : convertToReadableText(keysInput) : tooltip || null;
  const processedKeys = isMac ? displayShortcut.split(/[\+\s]+/).filter(key => key.trim()).map(key => {
    const trimmedKey = key.trim();
    return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
  }).join('') : displayShortcut.split('+').map(key => {
    const trimmedKey = key.trim();
    return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
  }).join('+');
  return tooltipText ? <Tooltip tip={tooltipText}>
      <kbd>
        {processedKeys}
      </kbd>
    </Tooltip> : <kbd>
      {processedKeys}
    </kbd>;
};

Cursor にはアップデートチャネルが 2 つある。

<Tabs>
  <Tab title="Default">
    テスト済みリリースのデフォルトのアップデートチャネル。

    * 安定版リリース
    * プレリリース検証に基づくバグ修正
    * すべてのユーザーでのデフォルト
    * チームユーザーはこのオプションのみ

    <Note>
      Team と Business アカウントは Default モードを使用する。
    </Note>
  </Tab>

  <Tab title="Early Access">
    新機能を含むプレリリース版。

    <Warning>
      Early Access のビルドには、バグや安定性の問題が含まれる場合がある。
    </Warning>

    * 開発中の機能にアクセスできる
    * バグを含む可能性がある
    * チームアカウントでは利用不可
  </Tab>
</Tabs>

<div id="change-update-channel">
  ## アップデートチャネルを変更する
</div>

1. **設定を開く**: <Kbd>Cmd+Shift+J</Kbd> を押す
2. **Beta に移動**: サイドバーで Beta を選択
3. **チャネルを選択**: Default か Early Access を選ぶ

<Frame>
  <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/early-access.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=36c55c2deb93bc734b6ee0099a0d184c" data-og-width="1798" width="1798" data-og-height="442" height="442" data-path="images/account/early-access.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/early-access.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=624bfea7b3643f55afaa85b38b1c56e1 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/early-access.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=f32c8e59596f024223735b4f929949e0 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/early-access.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=bd8c4bf3265ab802b6188aa81a620244 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/early-access.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=e8600f42cc363c61377f158972187e01 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/early-access.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=32c83b2109587d299959c2d46ce67353 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/early-access.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=b2c4032824d39c62a7cbada5578b1a98 2500w" />
</Frame>

Early Access の問題は [Forum](https://forum.cursor.com) で報告してね。



# Apply
Source: https://docs.cursor.com/ja/agent/apply

Apply を使って、チャットのコード提案を適用・承認・却下する方法を学ぶ

<div id="how-apply-works">
  ## Apply の仕組み
</div>

Apply は、chat が生成したコードを受け取り、ファイルに統合するための Cursor 専用モデル。チャットの会話からコードブロックを抽出し、コードベースに変更を適用する。

Apply 自体はコードを生成しない。コードは chat モデルが生成し、Apply は既存ファイルへの統合を担当する。複数ファイルや大規模なコードベースにまたがる変更も処理できる。

<div id="apply-code-blocks">
  ## コードブロックの適用
</div>

コードブロックの提案を適用するには、コードブロック右上の再生ボタンを押して。

<Frame>
  <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/apply.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=634492fa2f63b4f6eada08b2a1ded47e" data-og-width="1032" width="1032" data-og-height="410" height="410" data-path="images/chat/apply.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/apply.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=7dbc88cfe20429c73e627a289b17c964 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/apply.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=721e2d51bdb16dbb817e19d96d93c9d9 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/apply.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=8faea188ca903e58d347ddfec2c9bf6e 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/apply.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=f3bc38701cab63602b54374dfaa9e024 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/apply.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=fddad51f5b12c32493e2370ed326712d 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/apply.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=1584d431007b33a595905e23b5e1b453 2500w" />
</Frame>



# Checkpoints
Source: https://docs.cursor.com/ja/agent/chat/checkpoints

Agent の変更後に以前の状態を保存・復元

Checkpoints は、Agent がコードベースに加えた変更を自動でスナップショット化する機能。必要に応じて Agent の変更を取り消せる。

<Frame>
  <video src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/restore-checkpoint.mp4?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=7cededf7892f15a6342a81953ea0aa38" autoPlay loop muted playsInline controls data-path="images/chat/restore-checkpoint.mp4" />
</Frame>

<div id="restoring-checkpoints">
  ## チェックポイントの復元
</div>

復元方法は2つ:

1. **入力ボックスから**: 過去のリクエストで `Restore Checkpoint` ボタンをクリック
2. **メッセージから**: メッセージにホバーすると表示される「+」ボタンをクリック

<Warning>
  チェックポイントはバージョン管理ではないよ。恒久的な履歴には Git を使ってね。
</Warning>

<div id="how-they-work">
  ## 動作概要
</div>

* Git とは別にローカルに保存
* Agent による変更のみを追跡（手動編集は対象外）
* 自動でクリーンアップ

<Note>
  手動編集は追跡されないよ。チェックポイントは Agent の変更にだけ使ってね。
</Note>

<div id="faq">
  ## よくある質問
</div>

<AccordionGroup>
  <Accordion title="チェックポイントはGitに影響する？">
    しないよ。Gitの履歴とは別物だよ。
  </Accordion>

  {" "}

  <Accordion title="どれくらいの期間保持される？">
    現在のセッションと直近の履歴まで。自動でクリーンアップされるよ。
  </Accordion>

  <Accordion title="手動で作成できる？">
    できないよ。Cursorが自動で作成するよ。
  </Accordion>
</AccordionGroup>

{" "}



# コマンド
Source: https://docs.cursor.com/ja/agent/chat/commands

再利用可能なワークフロー用のコマンドを定義する

カスタムコマンドを使うと、チャット入力欄で「/」を付けるだけで呼び出せる再利用可能なワークフローを作成できる。コマンドはチーム全体のプロセスを標準化し、よくある作業をより効率的にしてくれる。

<Frame>
    <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/commands/input.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=0d25ac517b091210da1c6eff4c8e3098" alt="Commands input example" data-og-width="1689" width="1689" data-og-height="1079" height="1079" data-path="images/chat/commands/input.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/commands/input.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=680f0cbf1491ef1303171dbd18115288 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/commands/input.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=d6a5397e565ab2c90435e6fdd2b7b27a 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/commands/input.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=ae074e2f2b26741544fd8c8ecfa529e3 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/commands/input.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=564aad432affcc04e51b624725f386ad 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/commands/input.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=5c1bd5d49babc2f08eb0efcd24ba7783 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/commands/input.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=3244c3be31c9bc704468a706c6e6b38e 2500w" />
</Frame>

<Info>
  コマンドは現在ベータ版。今後の改良に伴い、機能や構文が変更される場合がある。
</Info>

<div id="how-commands-work">
  ## コマンドの仕組み
</div>

コマンドはプレーンな Markdown ファイルとして定義されていて、次の2か所に保存できる:

1. **プロジェクトコマンド**: プロジェクトの `.cursor/commands` ディレクトリに保存
2. **グローバルコマンド**: ホームディレクトリの `~/.cursor/commands` ディレクトリに保存

チャットの入力欄で `/` を打つと、Cursor が両方のディレクトリから使えるコマンドを自動検出して表示し、ワークフロー全体で即座に使えるようになる。

<div id="creating-commands">
  ## コマンドの作成
</div>

1. プロジェクトのルートに `.cursor/commands` ディレクトリを作成
2. 説明的な名前の `.md` ファイルを追加（例: `review-code.md`, `write-tests.md`）
3. コマンドの目的と挙動を説明するプレーンな Markdown を書く
4. チャットで `/` を入力すると、コマンドが自動的に表示される

コマンドディレクトリの構成は次のようになる例:

```
.cursor/
└── commands/
    ├── address-github-pr-comments.md
    ├── code-review-checklist.md
    ├── create-pr.md
    ├── light-review-existing-diffs.md
    ├── onboard-new-developer.md
    ├── run-all-tests-and-fix.md
    ├── security-audit.md
    └── setup-new-feature.md
```

<div id="examples">
  ## 例
</div>

プロジェクトで次のコマンドを試して、どう動くか感覚をつかもう。

<AccordionGroup>
  <Accordion title="コードレビュー・チェックリスト">
    ```markdown  theme={null}
    # コードレビュー・チェックリスト

    ## 概要
    品質・セキュリティ・保守性を確保するための徹底的なコードレビュー用チェックリスト。

    ## レビューカテゴリ

    ### 機能
    - [ ] コードが意図どおりに動作している
    - [ ] 例外的なケースまで考慮されている
    - [ ] エラーハンドリングが適切
    - [ ] 明らかなバグやロジックエラーがない

    ### コード品質
    - [ ] 読みやすく、構造が明確
    - [ ] 関数が小さく、責務が明確
    - [ ] 変数名がわかりやすい
    - [ ] 重複コードがない
    - [ ] プロジェクトの規約に従っている

    ### セキュリティ
    - [ ] 明らかなセキュリティ上の脆弱性がない
    - [ ] 入力バリデーションが実装されている
    - [ ] 機微なデータが適切に扱われている
    - [ ] シークレットがハードコードされていない
    ```
  </Accordion>

  <Accordion title="セキュリティ監査">
    ```markdown  theme={null}
    # セキュリティ監査

    ## 概要
    コードベースの脆弱性を特定して修正するための包括的なセキュリティレビュー

    ## 手順
    1. **依存関係の監査**
       - 既知の脆弱性を確認
       - 旧バージョンのパッケージを更新
       - サードパーティ依存関係をレビュー

    2. **コードセキュリティレビュー**
       - 代表的な脆弱性を確認
       - 認証／認可をレビュー
       - データ取り扱いの方針・実装を監査

    3. **インフラセキュリティ**
       - 環境変数の管理をレビュー
       - アクセス制御を確認
       - ネットワークセキュリティを監査

    ## セキュリティチェックリスト
    - [ ] 依存関係が最新かつ安全
    - [ ] ハードコードされたシークレットがない
    - [ ] 入力検証が実装済み
    - [ ] 認証が安全
    - [ ] 認可が適切に構成済み
    ```
  </Accordion>

  <Accordion title="新機能のセットアップ">
    ```markdown  theme={null}
    # 新機能のセットアップ

    ## 概要
    初期の企画から実装体制の構築まで、新機能を体系的にセットアップする。

    ## 手順
    1. **要件定義**
       - 機能のスコープと目標を明確にする
       - ユーザーストーリーと受け入れ条件を洗い出す
       - 技術的アプローチを策定する

    2. **フィーチャーブランチを作成**
       - main/develop からブランチを切る
       - ローカル開発環境をセットアップする
       - 新規依存関係を設定する

    3. **アーキテクチャ設計**
       - データモデルと API を設計する
       - UI コンポーネントとフローを設計する
       - テスト戦略を検討する

    ## 機能セットアップ・チェックリスト
    - [ ] 要件が文書化されている
    - [ ] ユーザーストーリーが作成されている
    - [ ] 技術的アプローチが策定されている
    - [ ] フィーチャーブランチが作成されている
    - [ ] 開発環境が整備されている
    ```
  </Accordion>

  <Accordion title="プルリクエストを作成">
    ```markdown  theme={null}
    # PR を作成

    ## 概要
    適切な説明・ラベル・レビュアーを含む、よく整理されたプルリクエストを作成する。

    ## 手順
    1. **ブランチを準備**
       - すべての変更がコミットされていることを確認
       - ブランチをリモートにプッシュ
       - ブランチが main と最新同期されていることを確認

    2. **PR の説明を書く**
       - 変更点を明確に要約
       - 背景や目的を含める
       - 破壊的変更があれば列挙
       - UI の変更があればスクリーンショットを追加

    3. **PR を設定**
       - 内容が伝わるタイトルで PR を作成
       - 適切なラベルを追加
       - レビュアーをアサイン
       - 関連する issue をリンク

    ## PR テンプレート
    - [ ] 機能 A
    - [ ] バグ修正 B
    - [ ] ユニットテスト合格
    - [ ] 手動テスト完了
    ```
  </Accordion>

  <Accordion title="テストを実行して失敗を修正する">
    ```markdown  theme={null}
    # すべてのテストを実行して失敗を修正する

    ## 概要
    フルテストスイートを実行し、失敗を体系的に修正して、コード品質と機能を確保する。

    ## 手順
    1. **テストスイートを実行**
       - プロジェクト内のすべてのテストを実行
       - 出力を収集して失敗を特定
       - ユニットテストと統合テストの両方を確認

    2. **失敗を分析**
       - 種別で分類: フレーク、破損、新規の失敗
       - 影響度に基づいて修正の優先度を決定
       - 失敗が直近の変更に起因していないか確認

    3. **体系的に問題を修正**
       - 最もクリティカルな失敗から着手
       - 1件ずつ修正
       - 各修正後にテストを再実行
    ```
  </Accordion>

  <Accordion title="新しい開発者をオンボードする">
    ```markdown  theme={null}
    # 新任開発者のオンボーディング

    ## 概要
    新任開発者がすぐに開発を開始できるようにする包括的なオンボーディング手順。

    ## 手順
    1. **環境セットアップ**
       - 必要なツールをインストール
       - 開発環境をセットアップ
       - IDE と拡張機能を設定
       - Git と SSH 鍵をセットアップ

    2. **プロジェクトの理解**
       - プロジェクト構成を確認
       - アーキテクチャを把握
       - 主要ドキュメントを読む
       - ローカルデータベースをセットアップ

    ## オンボーディングチェックリスト
    - [ ] 開発環境の準備完了
    - [ ] すべてのテストが合格
    - [ ] アプリケーションをローカルで実行できる
    - [ ] データベースのセットアップと動作確認済み
    - [ ] 最初の PR を提出
    ```
  </Accordion>
</AccordionGroup>



# コンパクト
Source: https://docs.cursor.com/ja/agent/chat/compact

コンパクトモードのインターフェースでチャットスペースを節約

コンパクトモードは、視覚的ノイズを抑えて会話に使える領域を最大化し、すっきりとしたチャットインターフェースを提供するよ。

<div id="overview">
  ## 概要
</div>

有効にすると、コンパクトモードはチャットインターフェースを次のように最適化する:

* **アイコンを非表示**にして、よりクリーンでミニマルな見た目に
* **diff を自動で折りたたみ**、視覚的ノイズを低減
* **入力欄を自動で折りたたみ**、会話スペースを最大化

この設定は、画面の小さい環境で作業するときや、集中できるノイズレスなチャット体験を好むときに特に便利。

<div id="before-and-after">
  ## Before and After
</div>

<div id="default-mode">
  ### デフォルトモード
</div>

<Frame>
  <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/compact/off.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=e0f8b97ecd5201be396fcd09cec54de6" alt="すべてのアイコンが表示され、要素が展開されたデフォルトモードのチャットインターフェース" data-og-width="2048" width="2048" data-og-height="2350" height="2350" data-path="images/chat/compact/off.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/compact/off.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=9395c8d1f324033631508dc9cdfd6f3e 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/compact/off.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=5d8025ef65ad2fc9fe8c30e5c4fcda32 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/compact/off.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=28050b27b683af948bc1ed939f31786c 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/compact/off.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=dc443705188da9d3368acefd917cc890 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/compact/off.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=be6603e2cedb7e88e7c20d797b18599c 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/compact/off.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=3afe563c9cd4576623adce5dcaaccddf 2500w" />
</Frame>

<div id="compact-mode">
  ### コンパクトモード
</div>

<Frame>
  <img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/compact/on.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=e9f068889026827422b2a9d943b55ded" alt="アイコンが非表示になり、要素が折りたたまれたコンパクトモードのチャットインターフェース" data-og-width="2048" width="2048" data-og-height="2350" height="2350" data-path="images/chat/compact/on.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/compact/on.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=44e86a79eb893b4de6c57c65487bbe9a 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/compact/on.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=539b71c72ed2fb3508e3aec0624429c1 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/compact/on.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=2c0da715a5daf93e94dbf2a5eefbb7eb 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/compact/on.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=b5bddca39109779c9d91bb6bc8bb42e9 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/compact/on.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=8bb334bb055e49d4d51cd137d2396db0 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/compact/on.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=70730d151a24440eeb6dc31e18189c7d 2500w" />
</Frame>

<div id="enabling-compact-mode">
  ## コンパクトモードを有効にする
</div>

コンパクトモードを有効にするには:

1. Cursor の設定を開く
2. **Chat** を開く
3. **Compact Mode** をオンにする

インターフェースがすぐにコンパクトな表示に切り替わって、会話に集中できるスペースが広がるよ。



# Duplicate
Source: https://docs.cursor.com/ja/agent/chat/duplicate

会話の任意のポイントからブランチを作成

現在の会話を失わずに、チャットを複製/フォークして別解を探ろう。

<Frame>
  <video src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/duplicate-chat.mp4?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=29fdb23214ba3e2c5b94ccefc01f7615" autoPlay loop muted playsInline controls data-path="images/chat/duplicate-chat.mp4" />
</Frame>

<div id="how-to-duplicate">
  ## 複製する方法
</div>

1. 分岐させたい場所を見つける
2. メッセージの三点メニューをクリック
3. 「Duplicate Chat」を選択

<div id="what-happens">
  ## 何が起きるか
</div>

* その時点までのコンテキストは保持される
* 元の会話には変更が加えられない
* 両方のチャットはそれぞれ別個の履歴を持つ



# エクスポート
Source: https://docs.cursor.com/ja/agent/chat/export

チャットをMarkdown形式でエクスポート

AgentのチャットをMarkdownファイルとしてエクスポートして、共有やドキュメントに使える。

<Frame>
  <video src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/export-chat.mp4?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=c6aa9d23a6a80ffae5864cd494907961" autoPlay loop muted playsInline controls data-path="images/chat/export-chat.mp4" />
</Frame>

<div id="whats-exported">
  ## エクスポート内容
</div>

* すべてのメッセージと応答
* 構文ハイライト付きコードブロック
* ファイル参照とコンテキスト
* 会話の時系列フロー

<div id="how-to-export">
  ## エクスポート方法
</div>

1. エクスポートしたいチャットを開く
2. コンテキストメニュー → 「Export Chat」をクリック
3. ファイルをローカルに保存

<Warning>
  エクスポートに機密データが含まれていないか確認してね：APIキー、内部URL、専有コード、
  個人情報
</Warning>



# 履歴
Source: https://docs.cursor.com/ja/agent/chat/history

チャット履歴の表示と管理

export const Kbd = ({children, tooltip, os}) => {
  const keysInput = typeof children === 'string' && children.trim() !== '' ? children : null;
  if (!keysInput) {
    return null;
  }
  const isModifier = key => {
    const modifiers = ['⌘', '⇧', '⌥', '⌃', '⏎', '⌫', '⌦', '⎋', '⇥', '⌁', '←', '→', '↑', '↓', 'Ctrl', 'Shift', 'Alt', 'Cmd', 'Opt', 'Return', 'Backspace', 'Delete', 'Escape', 'Tab', 'Space', 'Enter', 'Esc', 'ArrowLeft', 'ArrowRight', 'ArrowUp', 'ArrowDown', 'Left', 'Right', 'Up', 'Down'];
    return modifiers.includes(key.trim());
  };
  const capitalizeFirstLetter = string => {
    return string.charAt(0).toUpperCase() + string.slice(1);
  };
  const isMac = os ? os.toLowerCase() === 'mac' || os.toLowerCase() === 'macos' : typeof navigator !== 'undefined' && (navigator.platform.toUpperCase().indexOf('MAC') >= 0 || navigator.userAgent.toUpperCase().indexOf('MAC') >= 0);
  const convertToSymbols = shortcut => {
    if (isMac) {
      return shortcut.replace(/⌘|Cmd|CMD/gi, '⌘').replace(/⌥|Opt|OPT/gi, '⌥').replace(/⌃|Ctrl/gi, '⌃').replace(/⇧|Shift/gi, '⇧').replace(/⏎|Return/gi, '⏎').replace(/⌫|Backspace/gi, '⌫').replace(/⌦|Delete/gi, '⌦').replace(/␛|Escape/gi, '␛').replace(/⇥|Tab/gi, '⇥').replace(/⌁|Space/gi, '⌁').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, '←').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, '→').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, '↑').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, '↓');
    } else {
      const converted = shortcut.replace(/⌘|Cmd|CMD/gi, 'Ctrl').replace(/⌥|Opt|OPT/gi, 'Alt').replace(/⌃|Ctrl/gi, 'Ctrl').replace(/⇧|Shift/gi, 'Shift').replace(/⏎|Return/gi, 'Enter').replace(/⌫|Backspace/gi, 'Backspace').replace(/⌦|Delete/gi, 'Delete').replace(/⎋|Escape/gi, 'Esc').replace(/⇥|Tab/gi, 'Tab').replace(/⌁|Space/gi, 'Space').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, 'Arrow-Left').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, 'Arrow-Right').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, 'Arrow-Up').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, 'Arrow-Down');
      const keyList = converted.split(/[\+\s]+/).filter(key => key.trim());
      return keyList.join('+');
    }
  };
  const convertToReadableText = shortcut => {
    const converted = shortcut.replace(/⌘|Cmd|CMD/gi, 'Cmd').replace(/⌥|Opt|OPT/gi, 'Opt').replace(/⌃|Ctrl/gi, 'Ctrl').replace(/⇧|Shift/gi, 'Shift').replace(/⏎|Return/gi, 'Return').replace(/⌫|Backspace/gi, 'Backspace').replace(/⌦|Delete/gi, 'Delete').replace(/⎋|Escape/gi, 'Escape').replace(/⇥|Tab/gi, 'Tab').replace(/⌁|Space/gi, 'Space').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, 'Arrow-Left').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, 'Arrow-Right').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, 'Arrow-Up').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, 'Arrow-Down');
    const keyList = converted.split(/[\+\s]+/).filter(key => key.trim());
    return keyList.map(key => {
      const trimmedKey = key.trim();
      return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
    }).join('+');
  };
  const displayShortcut = convertToSymbols(keysInput);
  const tooltipText = isMac ? tooltip ? `${convertToReadableText(keysInput)}: ${tooltip}` : convertToReadableText(keysInput) : tooltip || null;
  const processedKeys = isMac ? displayShortcut.split(/[\+\s]+/).filter(key => key.trim()).map(key => {
    const trimmedKey = key.trim();
    return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
  }).join('') : displayShortcut.split('+').map(key => {
    const trimmedKey = key.trim();
    return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
  }).join('+');
  return tooltipText ? <Tooltip tip={tooltipText}>
      <kbd>
        {processedKeys}
      </kbd>
    </Tooltip> : <kbd>
      {processedKeys}
    </kbd>;
};

履歴パネルから過去のAgentとの会話にアクセスできる。

<Frame>
  <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/chat-history.jpeg?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=d9ec96fad0c8c2fb132bbf5ce8ea35f7" alt="Chat History" data-og-width="2048" width="2048" data-og-height="1317" height="1317" data-path="images/chat/chat-history.jpeg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/chat-history.jpeg?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=a3ad71e9891c3c9642f4288953a78e97 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/chat-history.jpeg?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=76139a177ebfeb0c55add7fb955f9000 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/chat-history.jpeg?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=1af22180859c017542777ab36b434b7a 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/chat-history.jpeg?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=751e7fa0888e5790f841432ef7521337 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/chat-history.jpeg?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=86b447c18601a9d44af8866d0042719e 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/chat-history.jpeg?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=88c84a8fb1b764ad3070e3211f539408 2500w" />
</Frame>

<div id="opening-history">
  ## 履歴を開く
</div>

* Agent サイドペインの履歴アイコンをクリック
* <Kbd tooltip="チャット履歴を開く">Opt + Cmd + '</Kbd> を押す

<div id="managing-chats">
  ## チャットの管理
</div>

* **タイトルを編集**: クリックして名前を変更
* **削除**: 不要なチャットを削除
* **開く**: クリックして会話全体を確認

チャット履歴は、ローカルの SQLite データベースに保存されるよ。

<Note>
  チャットを残したい場合は、[エクスポート](/ja/agent/chats/export)して Markdown にしてね。
</Note>

<div id="background-agents">
  ## Background Agents
</div>

バックグラウンドエージェントのチャットは通常の履歴には含まれず、リモートデータベースに保存される。表示するには <Kbd tooltip="Open background agent control panel">Cmd E</Kbd> を使おう。

<div id="referencing-past-chats">
  ## 過去のチャットを参照する
</div>

現在のチャットに以前のやり取りの文脈を取り込むには、[@Past Chats](/ja/context/@-symbols/@-past-chats) を使ってね。



# 要約
Source: https://docs.cursor.com/ja/agent/chat/summarization

チャットでの長文会話におけるコンテキスト管理

<div id="message-summarization">
  ## メッセージの要約
</div>

会話が長くなると、Cursor が自動的に要約してコンテキストを管理し、チャットを効率的に保つ。コンテキストメニューの使い方や、ファイルがモデルのコンテキストウィンドウに収まるようにどのように要約・圧縮されるかを学ぼう。

<div id="using-the-summarize-command">
  ### /summarize コマンドを使う
</div>

チャットで `/summarize` コマンドを使うと、手動で要約を実行できる。会話が長くなってきたときにコンテキストを整理して、重要な情報を逃さずに効率よく作業を続けられるようにする。

<Info>
  Cursor でのコンテキストの仕組みをもっと知りたいなら、[Working with
  Context](/ja/guides/working-with-context) ガイドをチェックしてね。
</Info>

<div id="how-summarization-works">
  ### 要約の仕組み
</div>

会話が長くなると、モデルのコンテキストウィンドウの上限を超える:

<Frame>
  <div className="font-mono text-xs w-full bg-neutral-100 p-4 rounded-lg">
    <div className="relative">
      <div className="bg-white px-3 py-2 mb-2 rounded border border-dashed border-neutral-400 w-full">
        <div className="text-xs text-neutral-700 font-medium">User</div>
      </div>

      <div className="bg-white px-3 py-2 mb-2 rounded border border-dashed border-neutral-400 w-full">
        <div className="text-xs text-neutral-700 font-medium">Cursor</div>
      </div>

      <div className="bg-white px-3 py-2 mb-2 rounded border border-dashed border-neutral-400 w-full">
        <div className="text-xs text-neutral-700 font-medium">User</div>
      </div>

      <div className="relative my-4">
        <div className="absolute top-0 left-1/2 transform -translate-x-1/2 -translate-y-1/2 text-center text-xs text-black bg-neutral-100 px-2">コンテキストウィンドウの上限</div>

        <div className="w-full h-px bg-black" />
      </div>

      <div className="bg-white px-3 py-2 mb-2 rounded border border-neutral-400 w-full">
        <div className="text-xs text-neutral-700 font-medium">Cursor</div>
      </div>

      <div className="bg-white px-3 py-2 mb-2 rounded border border-neutral-400 w-full">
        <div className="text-xs text-neutral-700 font-medium">User</div>
      </div>

      <div className="bg-white px-3 py-2 mb-2 rounded border border-neutral-400 w-full">
        <div className="text-xs text-neutral-700 font-medium">Cursor</div>
      </div>
    </div>
  </div>
</Frame>

これに対処するため、Cursor は古いメッセージを要約して、新しいやり取りのための余地を確保する。

<Frame>
  <div className="font-mono text-xs w-full bg-neutral-100 p-4 rounded-lg">
    <div className="relative">
      <div className="relative my-4">
        <div className="absolute top-0 left-1/2 transform -translate-x-1/2 -translate-y-1/2 text-center text-xs text-black bg-neutral-100 px-2">
          コンテキストウィンドウの上限
        </div>

        <div className="w-full h-px bg-black" />
      </div>

      <div className="bg-neutral-100 px-3 py-2 mb-2 rounded border border-dashed border-neutral-400 w-full">
        <div className="text-xs text-neutral-700 font-medium">
          要約メッセージ
        </div>
      </div>

      <div className="bg-white px-3 py-2 mb-2 rounded border border-neutral-400 w-full">
        <div className="text-xs text-neutral-700 font-medium">Cursor</div>
      </div>

      <div className="bg-white px-3 py-2 mb-2 rounded border border-neutral-400 w-full">
        <div className="text-xs text-neutral-700 font-medium">User</div>
      </div>

      <div className="bg-white px-3 py-2 mb-2 rounded border border-neutral-400 w-full">
        <div className="text-xs text-neutral-700 font-medium">Cursor</div>
      </div>
    </div>
  </div>
</Frame>

<div id="file-folder-condensation">
  ## ファイルとフォルダの凝縮
</div>

長い会話はチャット要約で対応する一方、Cursor は大きなファイルやフォルダの管理に別のアプローチ――**スマート凝縮**――を使ってる。会話にファイルを含めると、Cursor はファイルのサイズと利用可能なコンテキスト領域に応じて、最適な表示方法を判断してくれる。

ファイル／フォルダが取りうる状態は次のとおり:

<div id="condensed">
  ### 省略表示
</div>

ファイルやフォルダがコンテキストウィンドウに収まりきらないほど大きい場合、Cursor は自動的にそれらを省略表示にする。省略表示では、モデルに関数シグネチャ、クラス、メソッドといった主要な構造要素を提示する。この省略ビューから、必要に応じてモデルが特定のファイルを展開できる。このアプローチにより、利用可能なコンテキストウィンドウを最大限に活用できる。

<Frame>
  <img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/context-management/condensed.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=0c3a07b6fef6402945138f7ee38b44c1" alt="Context menu" data-og-width="1226" width="1226" data-og-height="793" height="793" data-path="images/context/context-management/condensed.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/context-management/condensed.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=4cc08626f9cfce1d186cdd6aa96c7d09 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/context-management/condensed.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=fa49ce9605bdb0186c98712f4c0a32cc 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/context-management/condensed.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=84874b2f40bff0a2cd54796865469914 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/context-management/condensed.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=050290a85c154e92f9298883afcdf892 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/context-management/condensed.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=f953aa28f11926b2d6fdf734cf928402 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/context-management/condensed.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=50aa9973ccf2027814860f3d97a2b031 2500w" />
</Frame>

<div id="significantly-condensed">
  ### 大幅に圧縮
</div>

ファイル名に「大幅に圧縮」のラベルが付いている場合、そのファイルは圧縮後でも全文を含めるには大きすぎるため、モデルにはファイル名のみが表示される。

<div id="not-included">
  ### 含まれていないもの
</div>

ファイルやフォルダの横に警告アイコンが表示されている場合、その項目は圧縮してもコンテキストウィンドウに収めるには大きすぎる。これによって、コードベースのどの部分にモデルがアクセスできるかを把握できる。

<Frame>
  <img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/context-management/not-included.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=06df9854c74c257d1ceb7d18b1864ceb" alt="Context menu" data-og-width="1090" width="1090" data-og-height="346" height="346" data-path="images/context/context-management/not-included.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/context-management/not-included.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=072e75878f27a151f1310007d0e5e534 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/context-management/not-included.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=c6f3f71351ddf8e367096651b455bf9d 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/context-management/not-included.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=c407f7870412007549f8eb2871f9ca12 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/context-management/not-included.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=b0d17023b5734c8d7584c56f5419bd1a 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/context-management/not-included.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=f1bedff398cee6c957fe62877f7d2012 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/context-management/not-included.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=8b00fbaff658c384f69bfddf3f3a4cfe 2500w" />
</Frame>



# タブ
Source: https://docs.cursor.com/ja/agent/chat/tabs

複数の Agent との会話を同時に進行

export const Kbd = ({children, tooltip, os}) => {
  const keysInput = typeof children === 'string' && children.trim() !== '' ? children : null;
  if (!keysInput) {
    return null;
  }
  const isModifier = key => {
    const modifiers = ['⌘', '⇧', '⌥', '⌃', '⏎', '⌫', '⌦', '⎋', '⇥', '⌁', '←', '→', '↑', '↓', 'Ctrl', 'Shift', 'Alt', 'Cmd', 'Opt', 'Return', 'Backspace', 'Delete', 'Escape', 'Tab', 'Space', 'Enter', 'Esc', 'ArrowLeft', 'ArrowRight', 'ArrowUp', 'ArrowDown', 'Left', 'Right', 'Up', 'Down'];
    return modifiers.includes(key.trim());
  };
  const capitalizeFirstLetter = string => {
    return string.charAt(0).toUpperCase() + string.slice(1);
  };
  const isMac = os ? os.toLowerCase() === 'mac' || os.toLowerCase() === 'macos' : typeof navigator !== 'undefined' && (navigator.platform.toUpperCase().indexOf('MAC') >= 0 || navigator.userAgent.toUpperCase().indexOf('MAC') >= 0);
  const convertToSymbols = shortcut => {
    if (isMac) {
      return shortcut.replace(/⌘|Cmd|CMD/gi, '⌘').replace(/⌥|Opt|OPT/gi, '⌥').replace(/⌃|Ctrl/gi, '⌃').replace(/⇧|Shift/gi, '⇧').replace(/⏎|Return/gi, '⏎').replace(/⌫|Backspace/gi, '⌫').replace(/⌦|Delete/gi, '⌦').replace(/␛|Escape/gi, '␛').replace(/⇥|Tab/gi, '⇥').replace(/⌁|Space/gi, '⌁').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, '←').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, '→').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, '↑').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, '↓');
    } else {
      const converted = shortcut.replace(/⌘|Cmd|CMD/gi, 'Ctrl').replace(/⌥|Opt|OPT/gi, 'Alt').replace(/⌃|Ctrl/gi, 'Ctrl').replace(/⇧|Shift/gi, 'Shift').replace(/⏎|Return/gi, 'Enter').replace(/⌫|Backspace/gi, 'Backspace').replace(/⌦|Delete/gi, 'Delete').replace(/⎋|Escape/gi, 'Esc').replace(/⇥|Tab/gi, 'Tab').replace(/⌁|Space/gi, 'Space').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, 'Arrow-Left').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, 'Arrow-Right').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, 'Arrow-Up').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, 'Arrow-Down');
      const keyList = converted.split(/[\+\s]+/).filter(key => key.trim());
      return keyList.join('+');
    }
  };
  const convertToReadableText = shortcut => {
    const converted = shortcut.replace(/⌘|Cmd|CMD/gi, 'Cmd').replace(/⌥|Opt|OPT/gi, 'Opt').replace(/⌃|Ctrl/gi, 'Ctrl').replace(/⇧|Shift/gi, 'Shift').replace(/⏎|Return/gi, 'Return').replace(/⌫|Backspace/gi, 'Backspace').replace(/⌦|Delete/gi, 'Delete').replace(/⎋|Escape/gi, 'Escape').replace(/⇥|Tab/gi, 'Tab').replace(/⌁|Space/gi, 'Space').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, 'Arrow-Left').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, 'Arrow-Right').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, 'Arrow-Up').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, 'Arrow-Down');
    const keyList = converted.split(/[\+\s]+/).filter(key => key.trim());
    return keyList.map(key => {
      const trimmedKey = key.trim();
      return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
    }).join('+');
  };
  const displayShortcut = convertToSymbols(keysInput);
  const tooltipText = isMac ? tooltip ? `${convertToReadableText(keysInput)}: ${tooltip}` : convertToReadableText(keysInput) : tooltip || null;
  const processedKeys = isMac ? displayShortcut.split(/[\+\s]+/).filter(key => key.trim()).map(key => {
    const trimmedKey = key.trim();
    return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
  }).join('') : displayShortcut.split('+').map(key => {
    const trimmedKey = key.trim();
    return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
  }).join('+');
  return tooltipText ? <Tooltip tip={tooltipText}>
      <kbd>
        {processedKeys}
      </kbd>
    </Tooltip> : <kbd>
      {processedKeys}
    </kbd>;
};

<Frame>
  <video src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/chat-tabs.mp4?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=57fd5305279dc0a3139055b353ce4b7a" autoPlay loop muted playsInline controls data-path="images/chat/chat-tabs.mp4" />
</Frame>

<div id="overview">
  ## 概要
</div>

<Kbd>Cmd+T</Kbd> で新しいタブを作成できる。各タブは会話履歴、コンテキスト、モデルの選択をそれぞれ独立して保持する。

<Tip>
  並行して作業したいなら、[Background Agents](/ja/background-agents) を試してみて
</Tip>

<div id="managing-tabs">
  ## タブの管理
</div>

* <Kbd>Cmd+T</Kbd>で新しいタブを作成。各タブは新しい会話から始まり、独自のコンテキストを保持する。

* タブのヘッダーをクリックするか、<Kbd>Ctrl+Tab</Kbd>で巡回して切り替えできる。

* タブのタイトルは最初のメッセージ後に自動生成されるけど、タブのヘッダーを右クリックして名前を変更できる。

<Tip>
  タブごとにタスクを1つにして、最初に明確な説明を書いて、終わったタブは閉じて
  ワークスペースを整理しておこう。
</Tip>

<div id="conflicts">
  ### 競合
</div>

Cursor は同じファイルを複数のタブで編集できないようにしてる。競合が発生した場合は解決を促される。

<div id="reference-other-chats">
  ## 他のチャットを参照する
</div>

[@Past Chats](/ja/context/@-symbols/@-past-chats) を使って、他のタブや過去のセッションの文脈を取り込もう。



# モード
Source: https://docs.cursor.com/ja/agent/modes

タスクに最適なモードを選択 — 自律的なコーディングからピンポイントな編集まで

export const Kbd = ({children, tooltip, os}) => {
  const keysInput = typeof children === 'string' && children.trim() !== '' ? children : null;
  if (!keysInput) {
    return null;
  }
  const isModifier = key => {
    const modifiers = ['⌘', '⇧', '⌥', '⌃', '⏎', '⌫', '⌦', '⎋', '⇥', '⌁', '←', '→', '↑', '↓', 'Ctrl', 'Shift', 'Alt', 'Cmd', 'Opt', 'Return', 'Backspace', 'Delete', 'Escape', 'Tab', 'Space', 'Enter', 'Esc', 'ArrowLeft', 'ArrowRight', 'ArrowUp', 'ArrowDown', 'Left', 'Right', 'Up', 'Down'];
    return modifiers.includes(key.trim());
  };
  const capitalizeFirstLetter = string => {
    return string.charAt(0).toUpperCase() + string.slice(1);
  };
  const isMac = os ? os.toLowerCase() === 'mac' || os.toLowerCase() === 'macos' : typeof navigator !== 'undefined' && (navigator.platform.toUpperCase().indexOf('MAC') >= 0 || navigator.userAgent.toUpperCase().indexOf('MAC') >= 0);
  const convertToSymbols = shortcut => {
    if (isMac) {
      return shortcut.replace(/⌘|Cmd|CMD/gi, '⌘').replace(/⌥|Opt|OPT/gi, '⌥').replace(/⌃|Ctrl/gi, '⌃').replace(/⇧|Shift/gi, '⇧').replace(/⏎|Return/gi, '⏎').replace(/⌫|Backspace/gi, '⌫').replace(/⌦|Delete/gi, '⌦').replace(/␛|Escape/gi, '␛').replace(/⇥|Tab/gi, '⇥').replace(/⌁|Space/gi, '⌁').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, '←').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, '→').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, '↑').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, '↓');
    } else {
      const converted = shortcut.replace(/⌘|Cmd|CMD/gi, 'Ctrl').replace(/⌥|Opt|OPT/gi, 'Alt').replace(/⌃|Ctrl/gi, 'Ctrl').replace(/⇧|Shift/gi, 'Shift').replace(/⏎|Return/gi, 'Enter').replace(/⌫|Backspace/gi, 'Backspace').replace(/⌦|Delete/gi, 'Delete').replace(/⎋|Escape/gi, 'Esc').replace(/⇥|Tab/gi, 'Tab').replace(/⌁|Space/gi, 'Space').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, 'Arrow-Left').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, 'Arrow-Right').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, 'Arrow-Up').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, 'Arrow-Down');
      const keyList = converted.split(/[\+\s]+/).filter(key => key.trim());
      return keyList.join('+');
    }
  };
  const convertToReadableText = shortcut => {
    const converted = shortcut.replace(/⌘|Cmd|CMD/gi, 'Cmd').replace(/⌥|Opt|OPT/gi, 'Opt').replace(/⌃|Ctrl/gi, 'Ctrl').replace(/⇧|Shift/gi, 'Shift').replace(/⏎|Return/gi, 'Return').replace(/⌫|Backspace/gi, 'Backspace').replace(/⌦|Delete/gi, 'Delete').replace(/⎋|Escape/gi, 'Escape').replace(/⇥|Tab/gi, 'Tab').replace(/⌁|Space/gi, 'Space').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, 'Arrow-Left').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, 'Arrow-Right').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, 'Arrow-Up').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, 'Arrow-Down');
    const keyList = converted.split(/[\+\s]+/).filter(key => key.trim());
    return keyList.map(key => {
      const trimmedKey = key.trim();
      return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
    }).join('+');
  };
  const displayShortcut = convertToSymbols(keysInput);
  const tooltipText = isMac ? tooltip ? `${convertToReadableText(keysInput)}: ${tooltip}` : convertToReadableText(keysInput) : tooltip || null;
  const processedKeys = isMac ? displayShortcut.split(/[\+\s]+/).filter(key => key.trim()).map(key => {
    const trimmedKey = key.trim();
    return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
  }).join('') : displayShortcut.split('+').map(key => {
    const trimmedKey = key.trim();
    return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
  }).join('+');
  return tooltipText ? <Tooltip tip={tooltipText}>
      <kbd>
        {processedKeys}
      </kbd>
    </Tooltip> : <kbd>
      {processedKeys}
    </kbd>;
};

Agent には特定のタスク向けに最適化された複数のモードがある。ワークフローに合わせて、それぞれ異なる機能とツールが使える。

<div className="full-width-table">
  | Mode                  | For              | Capabilities     | Tools      |
  | :-------------------- | :--------------- | :--------------- | :--------- |
  | **[Agent](#agent)**   | 複雑な機能開発、リファクタリング | 自律的な探索、複数ファイル編集  | すべてのツールが有効 |
  | **[Ask](#ask)**       | 学習、計画、質問         | 読み取り専用の探索、自動変更なし | 検索系ツールのみ   |
  | **[Custom](#custom)** | 特化ワークフロー         | ユーザー定義の機能        | 設定可能       |
</div>

<div id="agent">
  ## Agent
</div>

複雑なコーディングタスク向けのデフォルトモード。Agent はコードベースを自律的に探索し、複数のファイルを編集し、コマンドを実行してエラーを修正し、リクエストを完了する。

<Frame>
  <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/agent.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=9cd06dd9f59e019b3d76aa0fd9f934ba" data-og-width="3600" width="3600" data-og-height="2025" height="2025" data-path="images/chat/agent.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/agent.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=d979435c61e2112ebcb784f16a49327f 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/agent.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=1a88e2085ffe80f02daea9a523887282 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/agent.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=de98a8bf766c3f35a6187e87190e30f9 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/agent.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=8648638c4240b718e0512a6ec2274171 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/agent.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=45b9898d65f5b425d276eaa44d4e1940 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/agent.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=30fef2b190d453ee0166e554a4005bd1 2500w" />
</Frame>

<div id="ask">
  ## Ask
</div>

学習や探索のための読み取り専用モード。Ask はコードベースを検索し、変更を一切加えずに回答を返す—コードを変更する前に理解を深めるのに最適。

<Frame>
  <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/ask.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=15e531cb84f0a18228723870fd84fa4f" data-og-width="3600" width="3600" data-og-height="2025" height="2025" data-path="images/chat/ask.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/ask.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=592ac5a681910a075ae88dec89bee25d 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/ask.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=74b98cce3b5bb83c79d0566cd3c65c34 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/ask.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=c4d80f50e20e7ca28db5a3ee71718979 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/ask.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=a4a6e017fd64149cf68d997114bbf6b6 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/ask.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=7354479ecd644b86ddbcb9fe1131f100 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/ask.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=274125e614eadd17522e0dacfcc6a38e 2500w" />
</Frame>

<div id="custom">
  ## カスタム
</div>

特定のツールの組み合わせと指示で、独自のモードを作成しよう。ワークフローに合わせて機能を自由に組み合わせて使える。

<Note>
  カスタムモードはベータ版。`Cursor Settings` → `Chat` → `Custom
      Modes` で有効化
</Note>

<div id="examples">
  ### 例
</div>

<AccordionGroup>
  <Accordion title="学習">
    **ツール:** All Search\
    **指示:** 概念を丁寧かつ徹底的に説明し、不明点を明確にするための質問を行う
  </Accordion>

  {" "}

  <Accordion title="リファクタ">
    **ツール:** Edit & Reapply **指示:** 新機能を追加せずにコード構造を改善する
  </Accordion>

  {" "}

  <Accordion title="計画">
    **ツール:** Codebase, Read file, Terminal **指示:** `plan.md` に詳細な実装計画を作成する
  </Accordion>

  <Accordion title="デバッグ">
    **ツール:** All Search, Terminal, Edit & Reapply\
    **指示:** 修正提案に入る前に問題を徹底的に調査する
  </Accordion>
</AccordionGroup>

<div id="switching-modes">
  ## モードの切り替え
</div>

* Agent のモードピッカーのドロップダウンを使う
* <Kbd>Cmd+.</Kbd> で素早く切り替える
* [設定](#settings) でキーボードショートカットを設定する

<div id="settings">
  ## 設定
</div>

すべてのモードには共通の設定項目がある:

<div className="full-width-table">
  | 設定           | 説明                  |
  | :----------- | :------------------ |
  | モデル          | 使用するAIモデルを選択        |
  | キーボードショートカット | モード切り替え用のショートカットを設定 |
</div>

モード固有の設定:

<div className="full-width-table">
  | モード        | 設定            | 説明                                     |
  | :--------- | :------------ | :------------------------------------- |
  | **Agent**  | 自動実行とエラーの自動修正 | コマンドを自動実行し、エラーを自動修正                    |
  | **Ask**    | コードベース検索      | 関連ファイルを自動で特定                           |
  | **Custom** | ツール選択 & 指示    | [tools](/ja/agent/tools) とカスタムプロンプトを設定 |
</div>



# 概要
Source: https://docs.cursor.com/ja/agent/overview

自律型のコーディング作業、ターミナルコマンド、コード編集を支援するアシスタント

export const Kbd = ({children, tooltip, os}) => {
  const keysInput = typeof children === 'string' && children.trim() !== '' ? children : null;
  if (!keysInput) {
    return null;
  }
  const isModifier = key => {
    const modifiers = ['⌘', '⇧', '⌥', '⌃', '⏎', '⌫', '⌦', '⎋', '⇥', '⌁', '←', '→', '↑', '↓', 'Ctrl', 'Shift', 'Alt', 'Cmd', 'Opt', 'Return', 'Backspace', 'Delete', 'Escape', 'Tab', 'Space', 'Enter', 'Esc', 'ArrowLeft', 'ArrowRight', 'ArrowUp', 'ArrowDown', 'Left', 'Right', 'Up', 'Down'];
    return modifiers.includes(key.trim());
  };
  const capitalizeFirstLetter = string => {
    return string.charAt(0).toUpperCase() + string.slice(1);
  };
  const isMac = os ? os.toLowerCase() === 'mac' || os.toLowerCase() === 'macos' : typeof navigator !== 'undefined' && (navigator.platform.toUpperCase().indexOf('MAC') >= 0 || navigator.userAgent.toUpperCase().indexOf('MAC') >= 0);
  const convertToSymbols = shortcut => {
    if (isMac) {
      return shortcut.replace(/⌘|Cmd|CMD/gi, '⌘').replace(/⌥|Opt|OPT/gi, '⌥').replace(/⌃|Ctrl/gi, '⌃').replace(/⇧|Shift/gi, '⇧').replace(/⏎|Return/gi, '⏎').replace(/⌫|Backspace/gi, '⌫').replace(/⌦|Delete/gi, '⌦').replace(/␛|Escape/gi, '␛').replace(/⇥|Tab/gi, '⇥').replace(/⌁|Space/gi, '⌁').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, '←').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, '→').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, '↑').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, '↓');
    } else {
      const converted = shortcut.replace(/⌘|Cmd|CMD/gi, 'Ctrl').replace(/⌥|Opt|OPT/gi, 'Alt').replace(/⌃|Ctrl/gi, 'Ctrl').replace(/⇧|Shift/gi, 'Shift').replace(/⏎|Return/gi, 'Enter').replace(/⌫|Backspace/gi, 'Backspace').replace(/⌦|Delete/gi, 'Delete').replace(/⎋|Escape/gi, 'Esc').replace(/⇥|Tab/gi, 'Tab').replace(/⌁|Space/gi, 'Space').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, 'Arrow-Left').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, 'Arrow-Right').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, 'Arrow-Up').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, 'Arrow-Down');
      const keyList = converted.split(/[\+\s]+/).filter(key => key.trim());
      return keyList.join('+');
    }
  };
  const convertToReadableText = shortcut => {
    const converted = shortcut.replace(/⌘|Cmd|CMD/gi, 'Cmd').replace(/⌥|Opt|OPT/gi, 'Opt').replace(/⌃|Ctrl/gi, 'Ctrl').replace(/⇧|Shift/gi, 'Shift').replace(/⏎|Return/gi, 'Return').replace(/⌫|Backspace/gi, 'Backspace').replace(/⌦|Delete/gi, 'Delete').replace(/⎋|Escape/gi, 'Escape').replace(/⇥|Tab/gi, 'Tab').replace(/⌁|Space/gi, 'Space').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, 'Arrow-Left').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, 'Arrow-Right').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, 'Arrow-Up').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, 'Arrow-Down');
    const keyList = converted.split(/[\+\s]+/).filter(key => key.trim());
    return keyList.map(key => {
      const trimmedKey = key.trim();
      return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
    }).join('+');
  };
  const displayShortcut = convertToSymbols(keysInput);
  const tooltipText = isMac ? tooltip ? `${convertToReadableText(keysInput)}: ${tooltip}` : convertToReadableText(keysInput) : tooltip || null;
  const processedKeys = isMac ? displayShortcut.split(/[\+\s]+/).filter(key => key.trim()).map(key => {
    const trimmedKey = key.trim();
    return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
  }).join('') : displayShortcut.split('+').map(key => {
    const trimmedKey = key.trim();
    return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
  }).join('+');
  return tooltipText ? <Tooltip tip={tooltipText}>
      <kbd>
        {processedKeys}
      </kbd>
    </Tooltip> : <kbd>
      {processedKeys}
    </kbd>;
};

Agent は Cursor のアシスタントで、複雑なコーディング作業を自律的にこなし、ターミナルコマンドを実行し、コードを編集できる。サイドペインで <Kbd>Cmd+I</Kbd> を押してアクセス。

<Frame caption="サイドペインの Agent">
  <video src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/overview.mp4?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=b17d6a1225b4992ea19978b6a6c259e1" autoPlay loop muted playsInline data-path="images/chat/overview.mp4" />
</Frame>

<div className="mt-24 flex flex-col gap-12">
  <Columns className="gap-4">
    <div>
      <h2 className="text-lg font-medium mb-2">
        <a href="/ja/agent/modes" className="hover:text-primary transition-colors">
          モード
        </a>
      </h2>

      <p className="text-sm">
        Agent、Ask から選ぶか、カスタムモードを作成しよう。各モードは
        ワークフローに合わせて異なる機能とツールを備えてる。
      </p>
    </div>

    <Frame>
      <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/agent.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=9cd06dd9f59e019b3d76aa0fd9f934ba" alt="Agent モード" data-og-width="3600" width="3600" data-og-height="2025" height="2025" data-path="images/chat/agent.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/agent.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=d979435c61e2112ebcb784f16a49327f 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/agent.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=1a88e2085ffe80f02daea9a523887282 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/agent.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=de98a8bf766c3f35a6187e87190e30f9 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/agent.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=8648638c4240b718e0512a6ec2274171 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/agent.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=45b9898d65f5b425d276eaa44d4e1940 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/agent.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=30fef2b190d453ee0166e554a4005bd1 2500w" />
    </Frame>
  </Columns>

  <Columns className="gap-4">
    <div>
      <h3 className="text-lg font-medium mb-2">
        <a href="/ja/agent/tools" className="hover:text-primary transition-colors">
          ツール
        </a>
      </h3>

      <p className="text-sm">
        Agent はツールを使って検索・編集・コマンド実行を行う。セマンティックなコードベース検索からターミナルでの実行まで、これらのツールが自律的なタスク完了を支える。
      </p>
    </div>

    <div>
      <Frame>
        <img src="https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=3135722076a5aa636d27dbedec665bae" alt="Agent tools" data-og-width="1624" width="1624" data-og-height="1012" height="1012" data-path="images/agent/auto-run.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=280&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=9f2e2bed8f634201adc51ccb2bd96cd2 280w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=560&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=51704cac2f270a04856fffbeaccf9700 560w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=840&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=01a5034975497a8dff4f41dca0d19f2e 840w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=1100&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=5f19026a0c6e5fb28c935ce795edb706 1100w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=1650&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=a108fc86f8ee7c0db6e5b7ab80ede738 1650w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=2500&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=9ce5f45879c29049640bb5a1494db11e 2500w" />
      </Frame>
    </div>
  </Columns>

  <Columns className="gap-4">
    <div>
      <h3 className="text-lg font-medium mb-2">
        <a href="/ja/agent/apply" className="hover:text-primary transition-colors">
          変更を適用
        </a>
      </h3>

      <p className="text-sm">
        AI が提案したコードブロックをコードベースに統合しよう。Apply は、精度を保ちつつ大規模な変更を効率的に反映できる。
      </p>
    </div>

    <div>
      <Frame>
        <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/apply.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=634492fa2f63b4f6eada08b2a1ded47e" alt="変更を適用" data-og-width="1032" width="1032" data-og-height="410" height="410" data-path="images/chat/apply.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/apply.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=7dbc88cfe20429c73e627a289b17c964 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/apply.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=721e2d51bdb16dbb817e19d96d93c9d9 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/apply.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=8faea188ca903e58d347ddfec2c9bf6e 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/apply.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=f3bc38701cab63602b54374dfaa9e024 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/apply.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=fddad51f5b12c32493e2370ed326712d 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/apply.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=1584d431007b33a595905e23b5e1b453 2500w" />
      </Frame>
    </div>
  </Columns>

  <Columns className="gap-4">
    <div>
      <h3 className="text-lg font-medium mb-2">
        <a href="/ja/agent/review" className="hover:text-primary transition-colors">
          差分をレビュー
        </a>
      </h3>

      <p className="text-sm">
        取り込む前に変更を確認しよう。レビュー画面では、追加と削除が色分けされた行で表示され、変更を細かくコントロールできる。
      </p>
    </div>

    <div>
      <Frame>
        <video src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/review/review-bar.mp4?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=5dca0fe7aba3c79e6760cb264821a617" autoPlay loop muted playsInline controls data-path="images/chat/review/review-bar.mp4" />
      </Frame>
    </div>
  </Columns>

  <Columns className="gap-4">
    <div>
      <h3 className="text-lg font-medium mb-2">
        <a href="/ja/agent/chats/tabs" className="hover:text-primary transition-colors">
          チャットタブ
        </a>
      </h3>

      <p className="text-sm">
        <Kbd>Cmd+T</Kbd> で複数の会話を同時に進行できる。各タブは独立したコンテキスト、履歴、モデル選択を保持する。
      </p>
    </div>

    <div>
      <Frame>
        <video src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/chat-tabs.mp4?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=57fd5305279dc0a3139055b353ce4b7a" autoPlay loop muted playsInline controls data-path="images/chat/chat-tabs.mp4" />
      </Frame>
    </div>
  </Columns>

  <Columns className="gap-4">
    <div>
      <h3 className="text-lg font-medium mb-2">
        <a href="/ja/agent/chats/checkpoints" className="hover:text-primary transition-colors">
          チェックポイント
        </a>
      </h3>

      <p className="text-sm">
        自動スナップショットでAgentの変更履歴を記録。想定どおりに動かないときや別の手法を試したいときは、以前の状態にロールバックできる。
      </p>
    </div>

    <div>
      <Frame>
        <video src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/restore-checkpoint.mp4?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=7cededf7892f15a6342a81953ea0aa38" autoPlay loop muted playsInline controls data-path="images/chat/restore-checkpoint.mp4" />
      </Frame>
    </div>
  </Columns>

  <Columns className="gap-4">
    <div>
      <h3 className="text-lg font-medium mb-2">
        <a href="/ja/agent/terminal" className="hover:text-primary transition-colors">
          ターミナル連携
        </a>
      </h3>

      <p className="text-sm">
        Agent はターミナルコマンドを実行し、出力を監視し、複数の手順からなる
        プロセスを処理する。信頼できるワークフローには自動実行を設定できるし、
        安全性のために確認を必須にすることもできる。
      </p>
    </div>

    <div>
      <Frame>
        <img src="https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=3135722076a5aa636d27dbedec665bae" alt="Terminal integration" data-og-width="1624" width="1624" data-og-height="1012" height="1012" data-path="images/agent/auto-run.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=280&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=9f2e2bed8f634201adc51ccb2bd96cd2 280w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=560&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=51704cac2f270a04856fffbeaccf9700 560w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=840&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=01a5034975497a8dff4f41dca0d19f2e 840w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=1100&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=5f19026a0c6e5fb28c935ce795edb706 1100w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=1650&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=a108fc86f8ee7c0db6e5b7ab80ede738 1650w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=2500&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=9ce5f45879c29049640bb5a1494db11e 2500w" />
      </Frame>
    </div>
  </Columns>

  <Columns className="gap-4">
    <div>
      <h3 className="text-lg font-medium mb-2">
        <a href="/ja/agent/chats/history" className="hover:text-primary transition-colors">
          チャット履歴
        </a>
      </h3>

      <p className="text-sm">
        <Kbd>Opt Cmd '</Kbd> で過去の会話にアクセス。以前のやり取りを振り返って、コーディングセッションを追跡し、過去のチャットの文脈を参照できる。
      </p>
    </div>

    <div>
      <Frame>
        <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/chat-history.jpeg?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=d9ec96fad0c8c2fb132bbf5ce8ea35f7" alt="Chat history" data-og-width="2048" width="2048" data-og-height="1317" height="1317" data-path="images/chat/chat-history.jpeg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/chat-history.jpeg?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=a3ad71e9891c3c9642f4288953a78e97 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/chat-history.jpeg?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=76139a177ebfeb0c55add7fb955f9000 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/chat-history.jpeg?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=1af22180859c017542777ab36b434b7a 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/chat-history.jpeg?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=751e7fa0888e5790f841432ef7521337 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/chat-history.jpeg?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=86b447c18601a9d44af8866d0042719e 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/chat-history.jpeg?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=88c84a8fb1b764ad3070e3211f539408 2500w" />
      </Frame>
    </div>
  </Columns>

  <Columns className="gap-4">
    <div>
      <h3 className="text-lg font-medium mb-2">
        <a href="/ja/agent/chats/export" className="hover:text-primary transition-colors">
          チャットをエクスポート
        </a>
      </h3>

      <p className="text-sm">
        会話をMarkdown形式でエクスポート。チームメンバーと解決策を共有したり、意思決定を記録したり、コーディングセッションからナレッジベースを作成できる。
      </p>
    </div>

    <div>
      <Frame>
        <video src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/export-chat.mp4?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=c6aa9d23a6a80ffae5864cd494907961" autoPlay loop muted playsInline controls data-path="images/chat/export-chat.mp4" />
      </Frame>
    </div>
  </Columns>

  <Columns className="gap-4">
    <div>
      <h3 className="text-lg font-medium mb-2">
        <a href="/ja/context/rules" className="hover:text-primary transition-colors">
          ルール
        </a>
      </h3>

      <p className="text-sm">
        Agent の動作に関するカスタム指示を定義する。ルールはコーディング標準の維持、パターンの徹底、そして Agent によるプロジェクト支援のパーソナライズに役立つ。
      </p>
    </div>

    <div>
      <Frame>
        <img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rules-applied.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=e637bab83cfd5dcc8a3b15ed6fd9fc15" alt="Agent rules" data-og-width="1198" width="1198" data-og-height="674" height="674" data-path="images/context/rules/rules-applied.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rules-applied.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=78e3c392987c6f95a02fc106753c5f98 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rules-applied.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=9d3a8b76ba99ada5ca302cba9fb63810 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rules-applied.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=f5ab7fb374a1a4c5fe2f50e2e50d233a 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rules-applied.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=5d25394a29c1da4172a3e673ee384c07 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rules-applied.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=0fc125bd3c2a93551674252c0523d3ec 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rules-applied.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=c576ea053ee18c30d2781c6bdd394a70 2500w" />
      </Frame>
    </div>
  </Columns>
</div>



# 企画
Source: https://docs.cursor.com/ja/agent/planning

Agent が ToDo とキューイングを用いて複雑なタスクを計画・管理する方法

export const Kbd = ({children, tooltip, os}) => {
  const keysInput = typeof children === 'string' && children.trim() !== '' ? children : null;
  if (!keysInput) {
    return null;
  }
  const isModifier = key => {
    const modifiers = ['⌘', '⇧', '⌥', '⌃', '⏎', '⌫', '⌦', '⎋', '⇥', '⌁', '←', '→', '↑', '↓', 'Ctrl', 'Shift', 'Alt', 'Cmd', 'Opt', 'Return', 'Backspace', 'Delete', 'Escape', 'Tab', 'Space', 'Enter', 'Esc', 'ArrowLeft', 'ArrowRight', 'ArrowUp', 'ArrowDown', 'Left', 'Right', 'Up', 'Down'];
    return modifiers.includes(key.trim());
  };
  const capitalizeFirstLetter = string => {
    return string.charAt(0).toUpperCase() + string.slice(1);
  };
  const isMac = os ? os.toLowerCase() === 'mac' || os.toLowerCase() === 'macos' : typeof navigator !== 'undefined' && (navigator.platform.toUpperCase().indexOf('MAC') >= 0 || navigator.userAgent.toUpperCase().indexOf('MAC') >= 0);
  const convertToSymbols = shortcut => {
    if (isMac) {
      return shortcut.replace(/⌘|Cmd|CMD/gi, '⌘').replace(/⌥|Opt|OPT/gi, '⌥').replace(/⌃|Ctrl/gi, '⌃').replace(/⇧|Shift/gi, '⇧').replace(/⏎|Return/gi, '⏎').replace(/⌫|Backspace/gi, '⌫').replace(/⌦|Delete/gi, '⌦').replace(/␛|Escape/gi, '␛').replace(/⇥|Tab/gi, '⇥').replace(/⌁|Space/gi, '⌁').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, '←').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, '→').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, '↑').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, '↓');
    } else {
      const converted = shortcut.replace(/⌘|Cmd|CMD/gi, 'Ctrl').replace(/⌥|Opt|OPT/gi, 'Alt').replace(/⌃|Ctrl/gi, 'Ctrl').replace(/⇧|Shift/gi, 'Shift').replace(/⏎|Return/gi, 'Enter').replace(/⌫|Backspace/gi, 'Backspace').replace(/⌦|Delete/gi, 'Delete').replace(/⎋|Escape/gi, 'Esc').replace(/⇥|Tab/gi, 'Tab').replace(/⌁|Space/gi, 'Space').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, 'Arrow-Left').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, 'Arrow-Right').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, 'Arrow-Up').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, 'Arrow-Down');
      const keyList = converted.split(/[\+\s]+/).filter(key => key.trim());
      return keyList.join('+');
    }
  };
  const convertToReadableText = shortcut => {
    const converted = shortcut.replace(/⌘|Cmd|CMD/gi, 'Cmd').replace(/⌥|Opt|OPT/gi, 'Opt').replace(/⌃|Ctrl/gi, 'Ctrl').replace(/⇧|Shift/gi, 'Shift').replace(/⏎|Return/gi, 'Return').replace(/⌫|Backspace/gi, 'Backspace').replace(/⌦|Delete/gi, 'Delete').replace(/⎋|Escape/gi, 'Escape').replace(/⇥|Tab/gi, 'Tab').replace(/⌁|Space/gi, 'Space').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, 'Arrow-Left').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, 'Arrow-Right').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, 'Arrow-Up').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, 'Arrow-Down');
    const keyList = converted.split(/[\+\s]+/).filter(key => key.trim());
    return keyList.map(key => {
      const trimmedKey = key.trim();
      return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
    }).join('+');
  };
  const displayShortcut = convertToSymbols(keysInput);
  const tooltipText = isMac ? tooltip ? `${convertToReadableText(keysInput)}: ${tooltip}` : convertToReadableText(keysInput) : tooltip || null;
  const processedKeys = isMac ? displayShortcut.split(/[\+\s]+/).filter(key => key.trim()).map(key => {
    const trimmedKey = key.trim();
    return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
  }).join('') : displayShortcut.split('+').map(key => {
    const trimmedKey = key.trim();
    return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
  }).join('+');
  return tooltipText ? <Tooltip tip={tooltipText}>
      <kbd>
        {processedKeys}
      </kbd>
    </Tooltip> : <kbd>
      {processedKeys}
    </kbd>;
};

Agent は、構造化されたTo-Doリストとメッセージキューで先を見据えた計画と複雑なタスク管理ができるから、長期的なタスクも把握しやすく、追跡もしやすくなる。

<div id="agent-to-dos">
  ## Agent のTo-do
</div>

Agent は、依存関係を考慮して長めのタスクを扱いやすいステップに分解し、進捗に合わせて更新される構造化プランを作るよ。

<video autoPlay loop muted playsInline controls>
  <source src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/agent/planning/agent-todo.mp4?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=b0285913832a3ef123fe149516ee37ea" type="video/mp4" data-path="images/agent/planning/agent-todo.mp4" />
</video>

<div id="how-it-works">
  ### 仕組み
</div>

* Agent が複雑なタスクに対して自動で To-do リストを作成
* 各アイテムに他のタスクへの依存関係を設定できる
* 進捗に合わせてリストがリアルタイムに更新
* 完了したタスクは自動でチェックされる

<div id="visibility">
  ### 表示
</div>

* To-do はチャットインターフェースに表示される
* [Slack 連携](/ja/slack) を設定していれば、Slack でも表示される
* いつでもタスクの詳細なブレークダウンを確認できる

<Tip>
  より良い計画のために、最終目標をはっきり書いてみて。スコープが明確なほど、
  Agent はもっと正確なタスク分解を作ってくれるよ。
</Tip>

<Note>現時点では、auto mode での計画と To-do はサポートされていないよ。</Note>

<div id="queued-messages">
  ## キューされたメッセージ
</div>

Agent が現在のタスクに取り組んでいる間、フォローアップメッセージをキューに入れよう。指示は順番に待機し、準備ができ次第自動で実行される。

<video autoPlay loop muted playsInline controls>
  <source src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/agent/planning/agent-queue.mp4?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=4cdd6a7d1e12c67e520bc3ba67a42e0d" type="video/mp4" data-path="images/agent/planning/agent-queue.mp4" />
</video>

<div id="using-the-queue">
  ### キューの使い方
</div>

1. Agent の作業中に次の指示を入力する
2. <Kbd>Ctrl+Enter</Kbd> を押してキューに追加する
3. メッセージはアクティブなタスクの下に順番で表示される
4. 矢印をクリックしてキュー内のメッセージを並べ替える
5. Agent は完了後に順番に処理する

<div id="override-the-queue">
  ### キューのオーバーライド
</div>

通常の送信ではなくメッセージをキューに入れるには、<Kbd>Ctrl+Enter</Kbd> を使おう。キューに入れずに即時送信するには、<Kbd>Cmd+Enter</Kbd> を使う。これはキューをバイパスしてその場で実行するため、メッセージを「強制プッシュ」する動作になる。

<div id="default-messaging">
  ## デフォルトのメッセージ送信
</div>

メッセージはデフォルトでできるだけ速く送られ、たいていは Agent がツール呼び出しを終えた直後に表示される。これがいちばんレスポンスの良い体験になる。

<div id="how-default-messaging-works">
  ### デフォルトのメッセージ送信の仕組み
</div>

* メッセージはチャットの直近のユーザーメッセージに追記される
* メッセージは通常、ツール結果にひも付いて、準備でき次第すぐ送信される
* これにより、Agent の作業を中断せずに、より自然な会話の流れになる
* デフォルトでは、Agent の作業中に Enter を押すとこれが起きる



# Diffs & Review
Source: https://docs.cursor.com/ja/agent/review

AIエージェントが提案したコード変更をレビューして管理する

Agent がコード変更を生成すると、追加と削除を色分けした行で表示するレビュー用インターフェースに並ぶ。これで、どの変更をコードベースに適用するかを確認してコントロールできる。

レビュー用インターフェースは、見慣れた diff 形式でコード変更を表示する:

<div id="diffs">
  ## Diffs
</div>

<div className="full-width-table">
  | Type              | Meaning    | Example                                                                                               |
  | :---------------- | :--------- | :---------------------------------------------------------------------------------------------------- |
  | **Added lines**   | 新規コードの追加   | <code className="bg-green-100 text-green-800 px-2 py-1 rounded">+ const newVariable = 'hello';</code> |
  | **Deleted lines** | コードの削除     | <code className="bg-red-100 text-red-800 px-2 py-1 rounded">- const oldVariable = 'goodbye';</code>   |
  | **Context lines** | 変更のない周辺コード | <code className="bg-gray-100 text-gray-600 px-2 py-1 rounded"> function example() {}</code>           |
</div>

<div id="review">
  ## レビュー
</div>

生成が完了すると、先に進む前にすべての変更を確認するよう促すプロンプトが表示される。これで、どこが変更されるかを俯瞰できる。

<Frame>
  <img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/review/input-review.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=10633167c76c24c1e69748ef93dc3888" alt="入力レビューインターフェース" data-og-width="2095" width="2095" data-og-height="1178" height="1178" data-path="images/chat/review/input-review.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/review/input-review.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=f462337898ca48f71cd2b570b140d30d 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/review/input-review.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=07c91dfc92110cce444da8bbf3d0b3b5 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/review/input-review.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=492522862dabae6243fa8d33f6fd77f2 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/review/input-review.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=c897e19ce7f508bad4e24fcf8efb2512 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/review/input-review.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=3956c2d2c5c9156181b19e262e301b5b 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/review/input-review.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=907f90b1db432128964a7f4e59523bb6 2500w" />
</Frame>

<div id="file-by-file">
  ### ファイルごと
</div>

画面下部にフローティングのレビュー バーが表示され、次の操作ができる:

* 現在のファイルの変更を**承認**または**却下**する
* 保留中の変更がある**次のファイル**へ移動する
  <Frame>
    <video src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/review/review-bar.mp4?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=5dca0fe7aba3c79e6760cb264821a617" autoPlay loop muted playsInline controls data-path="images/chat/review/review-bar.mp4">
      お使いのブラウザは video タグをサポートしていません。
    </video>
  </Frame>

<div id="selective-acceptance">
  ### 選択的な承認
</div>

細かく制御するには:

* 変更の大半を承認したい場合: 不要な行を却下してから **Accept all** をクリック
* 変更の大半を却下したい場合: 必要な行を承認してから **Reject all** をクリック

<div id="review-changes">
  ## 変更内容を確認
</div>

エージェントの応答の最後で **Review changes** ボタンをクリックすると、変更の差分全体を確認できる。

<Frame>
  <video src="https://www.cursor.com/changelog/049/review-ui.mp4" autoPlay loop muted playsInline controls />
</Frame>



# Terminal
Source: https://docs.cursor.com/ja/agent/terminal

エージェントの操作の一環としてターミナルコマンドを自動実行

Agent は履歴を保持したまま、Cursor のネイティブターミナルでコマンドを実行する。skip をクリックすると <kbd>Ctrl+C</kbd> を送信して、コマンドを中断できる。

<div id="troubleshooting">
  ## トラブルシューティング
</div>

<Info>
  一部のシェルテーマ（例: Powerlevel9k/Powerlevel10k）が、インラインのターミナル出力に干渉することがある。コマンド出力が途中で切れていたり、表示が崩れて見える場合は、テーマを無効化するか、Agent 実行時はよりシンプルなプロンプトに切り替えてね。
</Info>

<div id="disable-heavy-prompts-for-agent-sessions">
  ### Agent セッションでは重いプロンプトを無効化する
</div>

シェルの設定で `CURSOR_AGENT` 環境変数を使って、Agent が実行中かどうかを検出し、リッチなプロンプトやテーマの初期化をスキップしよう。

```zsh  theme={null}

# ~/.zshrc — Cursor Agent 実行時は Powerlevel10k を無効化
if [[ -n "$CURSOR_AGENT" ]]; then
  # 互換性向上のためにテーマ初期化をスキップ
else
  [[ -r ~/.p10k.zsh ]] && source ~/.p10k.zsh
fi
```

```bash  theme={null}

# ~/.bashrc — Agent セッションでは簡易プロンプトにフォールバック
if [[ -n "$CURSOR_AGENT" ]]; then
  PS1='\u@\h \W \$ '
fi
```



# ツール
Source: https://docs.cursor.com/ja/agent/tools

コードの検索・編集・実行に利用できるエージェント用ツール

[Agent](/ja/agent/overview) の各モードで使えるツールの一覧。自分の[カスタムモード](/ja/agent/modes#custom)を作るときに有効・無効を切り替えられる。

<Note>
  1つのタスク中に Agent が行うツール呼び出し回数に上限はない。リクエストを完了するまで、Agent は必要に応じてツールを使い続ける。
</Note>

<div id="search">
  ## 検索
</div>

コードベースやウェブを検索して関連情報を見つけるためのツール。

<AccordionGroup>
  <Accordion title="Read File" icon="file-lines">
    ファイルを最大250行（最大モードでは750行）まで読み込む。
  </Accordion>

  <Accordion title="List Directory" icon="folder-open">
    ファイル内容を読まずにディレクトリ構造を取得する。
  </Accordion>

  <Accordion title="Codebase" icon="database">
    インデックス化された
    [コードベース](/ja/context/codebase-indexing)内でセマンティック検索を実行する。
  </Accordion>

  <Accordion title="Grep" icon="magnifying-glass">
    正確なキーワードやパターンをファイル内から検索する。
  </Accordion>

  <Accordion title="Search Files" icon="file-magnifying-glass">
    あいまい一致でファイル名からファイルを見つける。
  </Accordion>

  <Accordion title="Web" icon="globe">
    検索クエリを生成してウェブ検索を実行する。
  </Accordion>

  <Accordion title="Fetch Rules" icon="gavel">
    種類と説明に基づいて特定の
    [ルール](/ja/context/rules)を取得する。
  </Accordion>
</AccordionGroup>

<div id="edit">
  ## 編集
</div>

ファイルやコードベースに対してピンポイントに編集するためのツール。

<AccordionGroup>
  <Accordion title="Edit & Reapply" icon="pencil">
    ファイルへの変更案を出して、そのまま自動で[適用](/ja/agent/apply)する。
  </Accordion>

  <Accordion title="Delete File" icon="trash">
    ファイルを自動で削除（設定でオフにできる）。
  </Accordion>
</AccordionGroup>

<div id="run">
  ## 実行
</div>

Chat はターミナルとやり取りできるよ。

<AccordionGroup>
  <Accordion title="Terminal" icon="terminal">
    ターミナルコマンドを実行して、出力をモニタリングできる。
  </Accordion>
</AccordionGroup>

<Note>デフォルトでは、Cursor は利用可能な最初のターミナルプロファイルを使うよ。</Note>

好みのターミナルプロファイルを設定するには:

1. Command Palette を開く（`Cmd/Ctrl+Shift+P`）
2. 「Terminal: Select Default Profile」を検索
3. 使いたいプロファイルを選ぶ

<div id="mcp">
  ## MCP
</div>

Chat は、設定済みの MCP サーバーを使って、データベースやサードパーティ製 API などの外部サービスとやり取りできる。

<AccordionGroup>
  <Accordion title="MCP サーバーの切り替え" icon="server">
    利用可能な MCP サーバーを切り替える。自動実行の設定に従う。
  </Accordion>
</AccordionGroup>

[Model Context Protocol](/ja/context/model-context-protocol) について詳しく知って、[MCP ディレクトリ](/ja/tools) で利用可能なサーバーをチェックしてみよう。

<div id="advanced-options">
  ## 詳細オプション
</div>

<AccordionGroup>
  <Accordion title="Auto-apply Edits" icon="check">
    手動での確認なしに編集を自動適用するよ。
  </Accordion>

  <Accordion title="Auto-run" icon="play">
    ターミナルコマンドを自動実行し、編集を自動承認する。テストスイートの実行や変更の検証に便利だよ。

    <Frame>
      <img src="https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=3135722076a5aa636d27dbedec665bae" data-og-width="1624" width="1624" data-og-height="1012" height="1012" data-path="images/agent/auto-run.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=280&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=9f2e2bed8f634201adc51ccb2bd96cd2 280w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=560&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=51704cac2f270a04856fffbeaccf9700 560w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=840&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=01a5034975497a8dff4f41dca0d19f2e 840w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=1100&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=5f19026a0c6e5fb28c935ce795edb706 1100w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=1650&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=a108fc86f8ee7c0db6e5b7ab80ede738 1650w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=2500&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=9ce5f45879c29049640bb5a1494db11e 2500w" />
    </Frame>
  </Accordion>

  <Accordion title="Guardrails" icon="shield">
    自動実行を許可するツールを指定する許可リストを設定する。許可リストは、許可された操作を明示的に定義することでセキュリティを強化できる。
  </Accordion>

  <Accordion title="Auto-fix Errors" icon="wrench">
    Agent が検出したリンターのエラーや警告を自動で修正する。
  </Accordion>
</AccordionGroup>



# バックグラウンドエージェント
Source: https://docs.cursor.com/ja/background-agent

Cursor の非同期リモートエージェント

export const Kbd = ({children, tooltip, os}) => {
  const keysInput = typeof children === 'string' && children.trim() !== '' ? children : null;
  if (!keysInput) {
    return null;
  }
  const isModifier = key => {
    const modifiers = ['⌘', '⇧', '⌥', '⌃', '⏎', '⌫', '⌦', '⎋', '⇥', '⌁', '←', '→', '↑', '↓', 'Ctrl', 'Shift', 'Alt', 'Cmd', 'Opt', 'Return', 'Backspace', 'Delete', 'Escape', 'Tab', 'Space', 'Enter', 'Esc', 'ArrowLeft', 'ArrowRight', 'ArrowUp', 'ArrowDown', 'Left', 'Right', 'Up', 'Down'];
    return modifiers.includes(key.trim());
  };
  const capitalizeFirstLetter = string => {
    return string.charAt(0).toUpperCase() + string.slice(1);
  };
  const isMac = os ? os.toLowerCase() === 'mac' || os.toLowerCase() === 'macos' : typeof navigator !== 'undefined' && (navigator.platform.toUpperCase().indexOf('MAC') >= 0 || navigator.userAgent.toUpperCase().indexOf('MAC') >= 0);
  const convertToSymbols = shortcut => {
    if (isMac) {
      return shortcut.replace(/⌘|Cmd|CMD/gi, '⌘').replace(/⌥|Opt|OPT/gi, '⌥').replace(/⌃|Ctrl/gi, '⌃').replace(/⇧|Shift/gi, '⇧').replace(/⏎|Return/gi, '⏎').replace(/⌫|Backspace/gi, '⌫').replace(/⌦|Delete/gi, '⌦').replace(/␛|Escape/gi, '␛').replace(/⇥|Tab/gi, '⇥').replace(/⌁|Space/gi, '⌁').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, '←').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, '→').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, '↑').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, '↓');
    } else {
      const converted = shortcut.replace(/⌘|Cmd|CMD/gi, 'Ctrl').replace(/⌥|Opt|OPT/gi, 'Alt').replace(/⌃|Ctrl/gi, 'Ctrl').replace(/⇧|Shift/gi, 'Shift').replace(/⏎|Return/gi, 'Enter').replace(/⌫|Backspace/gi, 'Backspace').replace(/⌦|Delete/gi, 'Delete').replace(/⎋|Escape/gi, 'Esc').replace(/⇥|Tab/gi, 'Tab').replace(/⌁|Space/gi, 'Space').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, 'Arrow-Left').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, 'Arrow-Right').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, 'Arrow-Up').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, 'Arrow-Down');
      const keyList = converted.split(/[\+\s]+/).filter(key => key.trim());
      return keyList.join('+');
    }
  };
  const convertToReadableText = shortcut => {
    const converted = shortcut.replace(/⌘|Cmd|CMD/gi, 'Cmd').replace(/⌥|Opt|OPT/gi, 'Opt').replace(/⌃|Ctrl/gi, 'Ctrl').replace(/⇧|Shift/gi, 'Shift').replace(/⏎|Return/gi, 'Return').replace(/⌫|Backspace/gi, 'Backspace').replace(/⌦|Delete/gi, 'Delete').replace(/⎋|Escape/gi, 'Escape').replace(/⇥|Tab/gi, 'Tab').replace(/⌁|Space/gi, 'Space').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, 'Arrow-Left').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, 'Arrow-Right').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, 'Arrow-Up').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, 'Arrow-Down');
    const keyList = converted.split(/[\+\s]+/).filter(key => key.trim());
    return keyList.map(key => {
      const trimmedKey = key.trim();
      return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
    }).join('+');
  };
  const displayShortcut = convertToSymbols(keysInput);
  const tooltipText = isMac ? tooltip ? `${convertToReadableText(keysInput)}: ${tooltip}` : convertToReadableText(keysInput) : tooltip || null;
  const processedKeys = isMac ? displayShortcut.split(/[\+\s]+/).filter(key => key.trim()).map(key => {
    const trimmedKey = key.trim();
    return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
  }).join('') : displayShortcut.split('+').map(key => {
    const trimmedKey = key.trim();
    return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
  }).join('+');
  return tooltipText ? <Tooltip tip={tooltipText}>
      <kbd>
        {processedKeys}
      </kbd>
    </Tooltip> : <kbd>
      {processedKeys}
    </kbd>;
};

バックグラウンドエージェントで、リモート環境上でコードを編集・実行する非同期エージェントを起動できる。ステータスを確認したり、追跡メッセージを送ったり、いつでも自分で引き継げる。

<div id="how-to-use">
  ## 使い方
</div>

バックグラウンドエージェントには次の2通りでアクセスできる:

1. **Background Agent Sidebar**: Cursor のネイティブサイドバーにある background agent タブで、アカウントに紐づくすべてのバックグラウンドエージェントを一覧表示し、既存のエージェントを検索したり、新しいエージェントを起動できる。
2. **Background Agent Mode**: UI でバックグラウンドエージェントモードを有効化するには、<Kbd tooltip="Trigger background agent mode">Cmd E</Kbd> を押す。

プロンプトを送信したら、リストからエージェントを選んでステータスを確認し、マシンに入る。

<Note>
  <p className="!mb-0">
    バックグラウンドエージェントには、数日程度のデータ保持が必要。
  </p>
</Note>

<div id="setup">
  ## セットアップ
</div>

バックグラウンドエージェントは、デフォルトで分離された Ubuntu ベースのマシン上で動作する。エージェントはインターネットにアクセスでき、パッケージをインストールできる。

<div id="github-connection">
  #### GitHub 連携
</div>

バックグラウンドエージェントは GitHub からリポジトリをクローンし、別ブランチで作業して、スムーズに引き継げるようリポジトリにプッシュする。

リポジトリ（および依存リポジトリやサブモジュール）に読み取り/書き込み権限を付与してね。今後は他のプロバイダー（GitLab、Bitbucket など）にも対応予定。

<div id="ip-allow-list-configuration">
  ##### IP許可リストの設定
</div>

組織でGitHubのIP許可リスト機能を使っている場合は、バックグラウンドエージェントへのアクセスを設定する必要があるよ。連絡先情報やIPアドレスを含む完全なセットアップ手順は、[GitHub連携のドキュメント](/ja/integrations/github#ip-allow-list-configuration)を確認してね。

<div id="base-environment-setup">
  #### ベース環境のセットアップ
</div>

高度なケースでは、自分で環境をセットアップしよう。リモートマシンに接続された IDE インスタンスを用意して、マシンをセットアップし、ツールやパッケージをインストールしてからスナップショットを取得。実行時設定を構成する:

* Install コマンドはエージェントが起動する前に実行され、ランタイム依存関係をインストールする。これは `npm install` や `bazel build` を走らせることを意味する場合がある。
* Terminals は、エージェントが動作している間にバックグラウンドプロセスを実行する—たとえば、Web サーバーの起動や protobuf ファイルのコンパイルなど。

さらに高度なケースでは、マシンセットアップに Dockerfile を使おう。Dockerfile ならシステムレベルの依存関係をセットアップできる: 特定のコンパイラやデバッガのバージョンを入れる、ベース OS イメージを切り替える、など。プロジェクト全体を `COPY` しないで—ワークスペース管理と正しいコミットのチェックアウトはこっちでやる。依存関係のインストールは引き続き install スクリプトで扱って。

開発環境に必要なシークレットを入力してね—それらはデータベース内で KMS を使って暗号化保存され、バックグラウンドのエージェント環境に渡される。

マシンセットアップは `.cursor/environment.json` にあり、リポジトリにコミット（推奨）することも、プライベートに保存することもできる。セットアップフローが `environment.json` の作成をガイドする。

<div id="maintenance-commands">
  #### メンテナンスコマンド
</div>

新しいマシンをセットアップするときは、まずベース環境を用意してから、`environment.json` の `install` コマンドを実行する。これはブランチを切り替えるときに開発者が実行する想定のコマンドで、新しい依存関係をインストールするためのもの。

多くの場合、`install` コマンドは `npm install` か `bazel build`。

マシンの起動を高速化するために、`install` コマンド実行後のディスク状態をキャッシュする。複数回実行しても問題ないように設計しておこう。永続化されるのは `install` コマンドによるディスク状態だけで、ここで起動したプロセスはエージェント起動時には残らない。

<div id="startup-commands">
  #### スタートアップコマンド
</div>

`install` を実行するとマシンが立ち上がり、続けて `start` コマンド、そのあとに必要な `terminals` を起動する。これで、エージェントの実行時に常駐していてほしいプロセスが立ち上がる。

`start` コマンドは省略できることが多い。開発環境が Docker に依存してるなら使って—`start` コマンドに `sudo service docker start` を入れておこう。

`terminals` はアプリのコード用。これらのターミナルは、きみとエージェントが使える `tmux` セッション内で実行される。例えば、多くのウェブサイトのリポジトリでは `npm run watch` をターミナルとして設定してる。

<div id="the-environmentjson-spec">
  #### `environment.json` の仕様
</div>

`environment.json` ファイルは次のようになるよ:

```json  theme={null}
{
  "snapshot": "POPULATED_FROM_SETTINGS",
  "install": "npm install",
  "terminals": [
    {
      "name": "Next.js を起動"
      "command": "npm run dev"
    }
  ]
}
```

形式仕様は[こちらで定義されている](https://www.cursor.com/schemas/environment.schema.json)。

<div id="models">
  ## モデル
</div>

バックグラウンドエージェントで使えるのは、[Max Mode](/ja/context/max-mode) 対応のモデルだけ。

<div id="pricing">
  ## 料金
</div>

[Background Agent の料金](/ja/account/pricing#background-agent)について詳しく見る。

<div id="security">
  ## セキュリティ
</div>

Background Agents は Privacy Mode で利用できる。コードを学習に使うことは絶対にないし、エージェントの実行に必要な範囲でしかコードは保持しない。[Privacy Mode の詳細](https://www.cursor.com/privacy-overview)

知っておいてほしいこと:

1. 編集したいリポジトリには、GitHub アプリに読み書き権限を付与してね。これを使ってリポジトリをクローンして変更するよ。
2. コードは AWS 上の分離された VM 内で実行され、エージェントが動作している間は VM のディスクに保存される。
3. エージェントはインターネットにアクセスできる。
4. エージェントはすべてのターミナルコマンドを自動実行し、テストを反復できる。これは、すべてのコマンドにユーザー承認が必要な foreground agent とは異なる。自動実行にはデータ流出リスクがある—攻撃者が prompt injection 攻撃でエージェントを欺き、悪意あるサイトにコードをアップロードさせる可能性がある。[background agents に対する prompt injection のリスクに関する OpenAI の説明](https://platform.openai.com/docs/codex/agent-network#risks-of-agent-internet-access)を参照。
5. Privacy Mode を無効にしている場合、プロダクト改善のためにプロンプトと開発環境情報を収集する。
6. background agent の起動時に Privacy Mode を無効にして、その実行中に有効に切り替えても、エージェントは完了するまで Privacy Mode 無効のまま動作し続ける。

<div id="dashboard-settings">
  ## ダッシュボード設定
</div>

Workspace の管理者は、ダッシュボードの Background Agents タブから追加の設定を行えるよ。

<div id="defaults-settings">
  ### デフォルト設定
</div>

* **Default model** – 実行時にモデルが指定されていない場合に使われるモデル。Max Mode をサポートしている任意のモデルを選んでね。
* **Default repository** – 空の場合、エージェントがリポジトリの選択をユーザーに促す。ここでリポジトリを指定しておくと、そのステップをスキップできるよ。
* **Base branch** – プルリクエスト作成時にエージェントがフォーク元として使うブランチ。空のままにすると、そのリポジトリのデフォルトブランチが使われるよ。

<div id="security-settings">
  ### セキュリティ設定
</div>

すべてのセキュリティオプションは管理者権限が必要。

* **ユーザー制限** – *なし*（全メンバーがバックグラウンドエージェントを起動可能）か *許可リスト* を選択。*許可リスト* の場合、エージェントを作成できるメンバーを正確に指定できる。
* **チームのフォローアップ** – 有効にすると、ワークスペース内の誰でも他のメンバーが開始したエージェントにフォローアップメッセージを追加できる。無効にすると、フォローアップはエージェントの所有者と管理者に限定される。
* **エージェント概要の表示** – Cursor がエージェントのファイル差分イメージやコードスニペットを表示するかどうかを制御。サイドバーでファイルパスやコードを表示したくない場合は無効化する。
* **外部チャンネルでエージェント概要を表示** – 上記のトグルを、接続済みの Slack などの外部チャンネルにも適用。

変更は即時に保存され、新しいエージェントにすぐ反映される。



# フォローアップを追加
Source: https://docs.cursor.com/ja/background-agent/api/add-followup

en/background-agent/api/openapi.yaml post /v0/agents/{id}/followup
実行中のバックグラウンドエージェントに追加の指示を送信する。




# Agent Conversation
Source: https://docs.cursor.com/ja/background-agent/api/agent-conversation

en/background-agent/api/openapi.yaml get /v0/agents/{id}/conversation
バックグラウンドエージェントの会話履歴を取得する

バックグラウンドエージェントが削除されている場合は、会話履歴にはアクセスできないよ。



# エージェントの状態
Source: https://docs.cursor.com/ja/background-agent/api/agent-status

en/background-agent/api/openapi.yaml get /v0/agents/{id}
特定のバックグラウンドエージェントの現在の状態と結果を取得する。




# API キー情報
Source: https://docs.cursor.com/ja/background-agent/api/api-key-info

en/background-agent/api/openapi.yaml get /v0/me
認証に使用している API キーのメタデータを取得する。




# エージェントを削除
Source: https://docs.cursor.com/ja/background-agent/api/delete-agent

en/background-agent/api/openapi.yaml delete /v0/agents/{id}
バックグラウンドエージェントとその関連リソースを完全に削除します。




# エージェントを起動
Source: https://docs.cursor.com/ja/background-agent/api/launch-an-agent

en/background-agent/api/openapi.yaml post /v0/agents
リポジトリで作業する新しいバックグラウンドエージェントを起動する。




# エージェントの一覧
Source: https://docs.cursor.com/ja/background-agent/api/list-agents

en/background-agent/api/openapi.yaml get /v0/agents
認証済みユーザーのバックグラウンドエージェントをページネーションで取得する。




# モデル一覧
Source: https://docs.cursor.com/ja/background-agent/api/list-models

en/background-agent/api/openapi.yaml get /v0/models
バックグラウンドエージェント向けの推奨モデル一覧を取得する

作成時にバックグラウンドエージェントのモデルを指定したい場合は、このエンドポイントで推奨モデルの一覧を確認できる。

その場合は「Auto」オプションを用意しておくのもおすすめ。作成エンドポイントにモデル名を渡さず、最適なモデルはこっちで選ぶよ。



# GitHub リポジトリの一覧
Source: https://docs.cursor.com/ja/background-agent/api/list-repositories

en/background-agent/api/openapi.yaml get /v0/repositories
認証済みユーザーがアクセス可能な GitHub リポジトリの一覧を取得する。

<Warning>
  **このエンドポイントには非常に厳しいレート制限がある。**

  リクエストは **1/ユーザー/分**、**30/ユーザー/時** に制限してね。

  多数のリポジトリにアクセスできるユーザーは、レスポンスに数十秒かかることがある。

  この情報が取得できない場合でも、処理が破綻しないようにしておこう。
</Warning>



# 概要
Source: https://docs.cursor.com/ja/background-agent/api/overview

リポジトリで動作するバックグラウンドエージェントをプログラムから作成・管理する

<div id="background-agents-api">
  # Background Agents API
</div>

<Badge variant="beta">ベータ</Badge>

Background Agents API は、リポジトリ上で自律的に動作する AI 搭載のコーディングエージェントをプログラムから作成・管理できる API だよ。
この API を使えば、ユーザーのフィードバックへの自動対応、バグ修正、ドキュメント更新などを自動化できるよ。

<Info>
  Background Agents API は現在ベータ版。ぜひフィードバックを聞かせてね！
</Info>

<div id="key-features">
  ## 主な機能
</div>

* **自律コード生成** - プロンプトを理解してコードベースを変更できるエージェントを作成
* **リポジトリ連携** - GitHub リポジトリと直接やり取り
* フォローアッププロンプト - 実行中のエージェントに追加の指示を付与
* **使用量ベースの料金** - 使ったトークン分だけ支払う
* **スケーラブル** - API キーごとに最大 256 件のアクティブエージェントをサポート

<div id="quick-start">
  ## クイックスタート
</div>

<div id="1-get-your-api-key">
  ### 1. API キーを取得
</div>

[Cursor ダッシュボード → Integrations](https://cursor.com/dashboard?tab=integrations) に**アクセス**して、API キーを作成しよう。

<div id="2-start-using-the-api">
  ### 2. API を使い始める
</div>

すべての API エンドポイントは次の URL を基準に相対指定されている：

```
https://api.cursor.com
```

エンドポイントの詳細な一覧は、[APIリファレンス](/ja/background-agent/api/launch-an-agent)を参照してね。

<div id="authentication">
  ## 認証
</div>

すべての API リクエストは Bearer トークンによる認証が必須です。

```
Authorization: Bearer YOUR_API_KEY
```

API キーは [Cursor Dashboard](https://cursor.com/dashboard?tab=integrations) で作成できるよ。キーはアカウント単位のスコープで、エージェントの作成と管理が許可される（プランの上限やリポジトリのアクセス権に従う）。

<div id="pricing">
  ## 料金
</div>

このAPIは現在ベータ版で、料金はBackground Agentsと同じだよ。サービスの拡大に伴い、料金が変更される場合がある。詳しくは[Background Agentの料金](/ja/account/pricing#background-agent)を見てね。

<div id="next-steps">
  ## 次のステップ
</div>

* 環境、権限、ワークフローを理解するために、まずは[Background Agents の概要](/ja/background-agent)を読もう。
* [Web とモバイル](/ja/background-agent/web-and-mobile)から Background Agents を試してみよう。
* [Discord の #background-agent](https://discord.gg/jfgpZtYpmb)でディスカッションに参加するか、[background-agent-feedback@cursor.com](mailto:background-agent-feedback@cursor.com) へメールしよう。



# Webhooks
Source: https://docs.cursor.com/ja/background-agent/api/webhooks

バックグラウンドエージェントのステータス変更をリアルタイムで受け取る

<div id="webhooks">
  # Webhooks
</div>

webhook の URL を指定してエージェントを作成すると、Cursor はステータス変更を通知するために HTTP POST リクエストを送信する。現在サポートされているのは `statusChange` イベントのみで、エージェントが `ERROR` または `FINISHED` の状態になったときに送信される。

<div id="webhook-verification">
  ## Webhook の検証
</div>

Webhook リクエストが確実に Cursor からのものか確認するため、各リクエストに含まれる署名を検証してね:

<div id="headers">
  ### ヘッダー
</div>

各 Webhook リクエストには次のヘッダーが含まれるよ:

* **`X-Webhook-Signature`** – 形式 `sha256=<hex_digest>` の HMAC-SHA256 署名を含む
* **`X-Webhook-ID`** – この配信の一意の識別子（ログに便利）
* **`X-Webhook-Event`** – イベントタイプ（現在は `statusChange` のみ）
* **`User-Agent`** – 常に `Cursor-Agent-Webhook/1.0` が設定されている

<div id="signature-verification">
  ### 署名の検証
</div>

Webhook の署名を検証するには、期待される署名を算出して、受信した署名と照合してね:

```javascript  theme={null}
const crypto = require('crypto');

function verifyWebhook(secret, rawBody, signature) {
  const expectedSignature = 'sha256=' +
    crypto.createHmac('sha256', secret)
          .update(rawBody)
          .digest('hex');
  
  return signature === expectedSignature;
}
```

```python  theme={null}
import hmac
import hashlib

def verify_webhook(secret, raw_body, signature):
    expected_signature = 'sha256=' + hmac.new(
        secret.encode(),
        raw_body,
        hashlib.sha256
    ).hexdigest()
    
    return signature == expected_signature
```

シグネチャを計算するときは、必ずパース前の生のリクエストボディを使用して。

<div id="payload-format">
  ## ペイロード形式
</div>

Webhook のペイロードは、次の構造の JSON として送信される:

```json  theme={null}
{
  "event": "statusChange",
  "timestamp": "2024-01-15T10:30:00Z",
  "id": "bc_abc123",
  "status": "FINISHED",
  "source": {
    "repository": "https://github.com/your-org/your-repo",
    "ref": "main"
  },
  "target": {
    "url": "https://cursor.com/agents?id=bc_abc123",
    "branchName": "cursor/add-readme-1234",
    "prUrl": "https://github.com/your-org/your-repo/pull/1234"
  },
  "summary": "インストール手順を追加した README.md を追加"
}
```

一部のフィールドは任意で、利用可能な場合にのみ含まれる点に注意してね。

<div id="best-practices">
  ## ベストプラクティス
</div>

* **署名の検証** – リクエストが Cursor からのものか確かめるため、必ず webhook の署名を検証しよう
* **リトライへの対応** – エンドポイントがエラーステータスコードを返した場合、webhook は再送されることがある
* **すばやく返す** – 可能な限り早く 2xx のステータスコードを返そう
* **HTTPS を使う** – 本番環境の webhook エンドポイントには必ず HTTPS の URL を使おう
* **生ペイロードを保存** – デバッグや将来の検証のために、生の webhook ペイロードを保存しておこう



# Web とモバイル
Source: https://docs.cursor.com/ja/background-agent/web-and-mobile

どのデバイスからでもコーディングエージェントを実行し、デスクトップへシームレスに引き継げる

<div id="overview">
  ## 概要
</div>

Cursor の Agent on web は、強力なコーディングアシスタントをあらゆるデバイスで使えるようにする。散歩中にスマホを使ってても、Web ブラウザで作業してても、バックグラウンドで動くパワフルなコーディングエージェントをすぐに起動できる。
処理が終わったら、Cursor で作業を引き継いで変更をレビューしてマージしたり、チームにリンクを共有してコラボしたりできる。

[cursor.com/agents](https://cursor.com/agents) から始めよう。

<Frame><img src="https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/webagent/cursor-web-1.png?fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=79c7d14df82cfcae369bccb8a1431cf3" alt="Cursor web agent interface" data-og-width="4095" width="4095" data-og-height="2048" height="2048" data-path="images/webagent/cursor-web-1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/webagent/cursor-web-1.png?w=280&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=099c28633151e6c20eebc7fe03b3d420 280w, https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/webagent/cursor-web-1.png?w=560&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=452e0216c7e270d760072032f1e2b36d 560w, https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/webagent/cursor-web-1.png?w=840&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=baaa4a73d4822b5daa293814dc201d37 840w, https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/webagent/cursor-web-1.png?w=1100&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=8c5255fbf16aa60924e78a8285afb95d 1100w, https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/webagent/cursor-web-1.png?w=1650&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=7cc5a04ff6b24ad4ce0cfb4a35a9919c 1650w, https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/webagent/cursor-web-1.png?w=2500&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=f5f1b15fa508e20f89a4089f81417774 2500w" /></Frame>

<div id="getting-started">
  ## はじめ方
</div>

<div id="quick-setup">
  ### クイックセットアップ
</div>

1. **Webアプリにアクセス**: どのデバイスでも [cursor.com/agents](https://cursor.com/agents) にアクセス
2. **サインイン**: Cursorアカウントでログイン
3. **GitHubを連携**: リポジトリにアクセスできるようにGitHubアカウントを連携
4. **最初のエージェントを起動**: タスクを入力してエージェントの動作を確認

<div id="mobile-installation">
  ### モバイルへのインストール
</div>

モバイルでベストな体験にするには、CursorをPWA（Progressive Web App）としてインストールしよう:

* **iOS**: Safariで [cursor.com/agents](https://cursor.com/agents) を開き、共有ボタンをタップして「ホーム画面に追加」
* **Android**: ChromeでURLを開き、メニューをタップして「ホーム画面に追加」または「アプリをインストール」

<Tip>
  PWAとしてインストールすると、次のようなネイティブに近い体験が得られる: - 全画面インターフェース - 高速起動 - ホーム画面のアプリアイコン
</Tip>

<div id="working-across-devices">
  ## 複数デバイスでの作業
</div>

Web とモバイルのエージェントはデスクトップのワークフローと連携するように設計されてるよ。"Open in Cursor" をクリックして、IDE でエージェントの作業を続けよう。

<Frame><img src="https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/webagent/cursor-web-2.png?fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=352140fd4bf3f3d98a1e1b9f4a995cad" alt="レビューとハンドオフ" data-og-width="4095" width="4095" data-og-height="2048" height="2048" data-path="images/webagent/cursor-web-2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/webagent/cursor-web-2.png?w=280&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=eedd50318503fd3d3961b6da27a386d9 280w, https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/webagent/cursor-web-2.png?w=560&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=fd8c730cf62a0af6f873945a6a23b90b 560w, https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/webagent/cursor-web-2.png?w=840&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=ac537cc639471556f1afa0e09425ef30 840w, https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/webagent/cursor-web-2.png?w=1100&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=d512cddda6890c0749a7ad6396682def 1100w, https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/webagent/cursor-web-2.png?w=1650&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=e208297f414976bcfeea6850b39e8abb 1650w, https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/webagent/cursor-web-2.png?w=2500&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=54683ff7f25750fdc788e87c30bb6d6d 2500w" /></Frame>

<div id="team-collaboration">
  ### チームでのコラボレーション
</div>

* **共有アクセス**: リンクをチームメンバーと共有して、エージェントの実行に一緒に取り組もう。
* **レビュー手順**: コラボレーターは差分をレビューして、フィードバックを出せるよ。
* **Pull request の管理**: Web インターフェースから直接、Pull request の作成・レビュー・マージができる。

<div id="slack-integration">
  ### Slack 連携
</div>

Slack で `@Cursor` にメンションして、エージェントを直接起動できるよ。Web やモバイルからエージェントを開始するときに、完了時の Slack 通知を受け取るか選べる。

<Card title="Slack で Cursor を使う" icon="slack" href="/ja/slack">
  Slack 連携の設定と使い方、エージェントの起動や通知の受け取りについて
  さらに詳しく見てみよう。
</Card>

<div id="pricing">
  ## 料金
</div>

Web とモバイルのエージェントは、Background Agents と同じ料金モデルだよ。

[Background Agent の料金](/ja/account/pricing#background-agent)の詳細はこちら。

<div id="troubleshooting">
  ## トラブルシューティング
</div>

<AccordionGroup>
  <Accordion title="Agent runs are not starting">
    * ログイン済みで、GitHub アカウントを連携しているか確認してね。 - 対象リポジトリへの必要な権限があるかチェックしてね。 - Pro Trial か有料プランで、従量課金（usage-based pricing）が有効になっている必要があるよ。従量課金を有効化するには、
      [Dashboard](https://www.cursor.com/dashboard?tab=settings) の Settings タブに移動してね。
  </Accordion>

  <Accordion title="Can't see agent runs on mobile">
    ページをリフレッシュするか、ブラウザのキャッシュをクリアしてみて。同じアカウントで複数デバイスにログインしているかも確認してね。
  </Accordion>

  <Accordion title="Slack integration not working">
    ワークスペース管理者が Cursor の Slack アプリをインストールしていて、必要な権限が付与されているか確認してね。
  </Accordion>
</AccordionGroup>




---

**Navigation:** [← Previous](./18-slack.md) | [Index](./index.md) | [Next →](./20-bugbot.md)