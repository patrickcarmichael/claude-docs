---
title: "Headless CLI の使用"
source: "https://docs.cursor.com/ja/cli/headless"
language: "ja"
language_name: "Japanese"
---

# Headless CLI の使用
Source: https://docs.cursor.com/ja/cli/headless

Cursor CLI を使って、自動コード解析・生成・変更のためのスクリプトを書く方法を学ぶ

コード解析・生成・リファクタリングのタスク向けに、スクリプトや自動化ワークフローで Cursor CLI を使おう。

<div id="how-it-works">
  ## 仕組み
</div>

非対話型のスクリプトや自動化には [print mode](/ja/cli/using#non-interactive-mode) (`-p, --print`) を使おう。

<div id="file-modification-in-scripts">
  ### スクリプトでのファイル変更
</div>

スクリプト内でファイルを変更するなら、`--print` と `--force` を組み合わせよう:

```bash  theme={null}

---

← Previous: [GitHub Actions](./github-actions.md) | [Index](./index.md) | Next: [インストール](./section.md) →