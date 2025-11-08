---
title: "SCIM"
source: "https://docs.cursor.com/ja/account/teams/scim"
language: "ja"
language_name: "Japanese"
---

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

---

← Previous: [メンバーと役割](./section.md) | [Index](./index.md) | Next: [はじめ方](./section.md) →