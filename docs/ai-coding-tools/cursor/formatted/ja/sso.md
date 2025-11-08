---
title: "SSO"
source: "https://docs.cursor.com/ja/account/teams/sso"
language: "ja"
language_name: "Japanese"
---

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

---

← Previous: [はじめ方](./section.md) | [Index](./index.md) | Next: [アップデート受信設定](./section.md) →