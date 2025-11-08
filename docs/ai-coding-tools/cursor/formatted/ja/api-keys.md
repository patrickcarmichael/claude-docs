---
title: "API Keys"
source: "https://docs.cursor.com/ja/settings/api-keys"
language: "ja"
language_name: "Japanese"
---

# API Keys
Source: https://docs.cursor.com/ja/settings/api-keys

自分の LLM プロバイダーを使う

自分の API キーを使えば、費用は自己負担で AI メッセージを無制限に送れる。設定すると、Cursor はその API キーで LLM プロバイダーに直接アクセスする。

API キーを使うには、`Cursor Settings` > `Models` に進み、API キーを入力して **Verify** をクリック。検証に成功すると、API キーが有効になる。

<Warning>
  カスタム API キーが使えるのは標準のチャットモデルのみ。専用モデルが必要な機能（Tab Completion など）は、引き続き Cursor の組み込みモデルを使用する。
</Warning>

<div id="supported-providers">
  ## 対応プロバイダー
</div>

* **OpenAI** - 標準の非推論型チャットモデルのみ。モデルピッカーには利用可能な OpenAI モデルが表示される。
* **Anthropic** - Anthropic API で利用可能なすべての Claude モデル。
* **Google** - Google AI API で利用可能な Gemini モデル。
* **Azure OpenAI** - 自分の Azure OpenAI Service インスタンスにデプロイしたモデル。
* **AWS Bedrock** - AWS アクセスキー、シークレットキー、または IAM ロールを使用。Bedrock の設定で有効なモデルで動作する。

Bedrock の IAM ロールを検証すると一意の外部 ID が生成され、追加のセキュリティのために IAM ロールの信頼ポリシーに追加できる。

<div id="faq">
  ## FAQ
</div>

<AccordionGroup>
  <Accordion title="API キーは保存されたり、デバイスの外に送られたりする？">
    API キーは保存されないけど、リクエストごとにサーバーに送られるよ。すべてのリクエストは、最終的なプロンプトを組み立てるためにバックエンド経由で処理される。
  </Accordion>
</AccordionGroup>

---

← Previous: [モデル](./section.md) | [Index](./index.md) | Next: [Tab](./tab.md) →