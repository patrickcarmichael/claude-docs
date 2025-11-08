---
title: "Headless CLI 사용하기"
source: "https://docs.cursor.com/ko/cli/headless"
language: "ko"
language_name: "Korean"
---

# Headless CLI 사용하기
Source: https://docs.cursor.com/ko/cli/headless

자동 코드 분석, 생성, 수정 작업을 위해 Cursor CLI로 스크립트를 작성하는 방법을 알아봐

스크립트와 자동화 워크플로에서 Cursor CLI를 사용해 코드 분석, 생성, 리팩터링 작업을 수행해봐.

<div id="how-it-works">
  ## 작동 방식
</div>

비대화형 스크립팅과 자동화를 위해 [print 모드](/ko/cli/using#non-interactive-mode) (`-p, --print`)를 사용해.

<div id="file-modification-in-scripts">
  ### 스크립트에서 파일 수정
</div>

스크립트에서 파일을 수정하려면 `--print`와 `--force`를 함께 써:

```bash  theme={null}

---

← Previous: [GitHub Actions](./github-actions.md) | [Index](./index.md) | Next: [설치](./section.md) →