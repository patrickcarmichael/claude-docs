---
title: "Code Review"
source: "https://docs.cursor.com/ko/cli/cookbook/code-review"
language: "ko"
language_name: "Korean"
---

# Code Review
Source: https://docs.cursor.com/ko/cli/cookbook/code-review

Cursor CLI로 pull request를 자동 리뷰하고 피드백을 남기는 GitHub Actions 워크플로 구축

이 튜토리얼에선 GitHub Actions에서 Cursor CLI로 코드 리뷰를 설정하는 방법을 보여줄게. 워크플로는 pull request를 분석하고, 문제를 찾아내며, 댓글로 피드백을 남겨.

<Tip>
  대부분의 사용자에겐 [Bugbot](/ko/bugbot)을 쓰는 걸 추천해. Bugbot은 별도 설정 없이 관리형 자동 코드 리뷰를 제공해. 이 CLI 방식은 기능을 탐색하거나 고급 커스터마이징이 필요할 때 유용해.
</Tip>

<div className="space-y-4">
  <Expandable title="전체 워크플로 파일">
    ```yaml cursor-code-review.yml theme={null}
    name: 코드 리뷰

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
        # 드래프트 PR은 자동 코드 리뷰 건너뛰기
        if: github.event.pull_request.draft == false
        steps:
          - name: 리포지토리 체크아웃
            uses: actions/checkout@v4
            with:
              fetch-depth: 0
              ref: ${{ github.event.pull_request.head.sha }}

          - name: Cursor CLI 설치
            run: |
              curl https://cursor.com/install -fsS | bash
              echo "$HOME/.cursor/bin" >> $GITHUB_PATH

          - name: git 사용자 정보 설정
            run: |
              git config user.name "Cursor 에이전트"
              git config user.email "cursoragent@cursor.com"

          - name: 자동 코드 리뷰 실행
            env:
              CURSOR_API_KEY: ${{ secrets.CURSOR_API_KEY }}
              MODEL: gpt-5
              GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
              BLOCKING_REVIEW: ${{ vars.BLOCKING_REVIEW || 'false' }}
            run: |
              cursor-agent --force --model "$MODEL" --output-format=text --print 'GitHub Actions 러너에서 자동 코드 리뷰를 수행 중이야. gh CLI는 GH_TOKEN으로 인증되어 있고 사용 가능해. 풀 리퀘스트에 코멘트를 남길 수 있어.

              컨텍스트:
              - 리포지토리: ${{ github.repository }}
              - PR 번호: ${{ github.event.pull_request.number }}
              - PR 헤드 SHA: ${{ github.event.pull_request.head.sha }}
              - PR 베이스 SHA: ${{ github.event.pull_request.base.sha }}
              - 차단 리뷰: ${{ env.BLOCKING_REVIEW }}

              목표:
              1) 기존 리뷰 코멘트를 다시 확인하고 해결됐으면 resolved로 답장해.
              2) 현재 PR diff를 리뷰하고 명확하고 심각도가 높은 이슈만 표시해.
              3) 변경된 라인에만 아주 짧은 인라인 코멘트(1~2문장)와 끝에 간단한 요약을 남겨.

              절차:
              - 기존 코멘트 가져오기: gh pr view --json comments
              - diff 가져오기: gh pr diff
              - 인라인 위치 계산을 위한 패치 포함 변경 파일 가져오기: gh api repos/${{ github.repository }}/pulls/${{ github.event.pull_request.number }}/files --paginate --jq '.[] | {filename,patch}'
              - 각 이슈에 대한 정확한 인라인 앵커 계산(파일 경로 + diff 위치). 코멘트는 반드시 diff의 변경된 라인에 인라인으로 달고, 최상위 코멘트로 달면 안 돼.
              - 이 봇이 작성한 이전의 최상위 "문제 없음" 스타일 코멘트를 감지해(본문이 "✅ no issues", "No issues found", "LGTM"과 유사한 경우 매칭).
              - 이번 실행에서 이슈가 발견되고 과거 "문제 없음" 코멘트가 있으면:
                - 혼란을 피하기 위해 제거하는 걸 우선해:
                  - 최상위 해당 코멘트 삭제 시도: gh api -X DELETE repos/${{ github.repository }}/issues/comments/<comment_id>
                  - 삭제가 불가하면 GraphQL(minimizeComment)로 최소화하거나 "[Superseded by new findings]" 접두사를 붙여 편집해.
                - 삭제/최소화 모두 불가하면 이렇게 답장해: "⚠️ 대체됨: 최신 커밋에서 이슈가 발견됐어"
              - 이전에 보고된 이슈가 인접한 변경으로 해결된 것 같으면, 이렇게 답장해: ✅ 최근 변경으로 이 이슈가 해결된 것으로 보여
              - 다음만 분석:
                - null/undefined 역참조
                - 리소스 누수(닫히지 않은 파일 또는 연결)
                - 인젝션(SQL/XSS)
                - 동시성/경쟁 상태
                - 중요 작업의 오류 처리 누락
                - 잘못된 동작을 유발하는 명백한 로직 오류
                - 측정 가능한 영향이 있는 명확한 성능 안티패턴
                - 명백한 보안 취약점
              - 중복 방지: 동일하거나 인접한 라인에 유사한 피드백이 이미 있으면 건너뛰어.

              코멘트 규칙:
              - 인라인 코멘트 최대 10개; 가장 중요한 이슈에 우선순위를 둬
              - 코멘트당 하나의 이슈; 정확히 변경된 라인에 배치해
              - 모든 이슈 코멘트는 반드시 인라인(PR diff의 파일과 위치에 고정)
              - 자연스러운 톤으로 구체적이고 실행 가능하게; 자동화나 확신도 언급 금지
              - 이모지 사용: 🚨 중대 🔒 보안 ⚡ 성능 ⚠️ 로직 ✅ 해결 ✨ 개선

              제출:
              - 보고할 이슈가 없고 기존의 "문제 없음" 최상위 코멘트가 이미 있으면(예: "✅ no issues", "No issues found", "LGTM") 새 코멘트를 제출하지 마. 중복을 피하기 위해 건너뛰어.
              - 보고할 이슈가 없고 이전 "문제 없음" 코멘트도 없으면, 간단한 요약 코멘트 하나로 문제 없음을 알려.
              - 보고할 이슈가 있고 이전 "문제 없음" 코멘트가 있으면, 새 리뷰 제출 전에 그 코멘트를 삭제/최소화/대체됨으로 표시해.
              - 보고할 이슈가 있으면, 인라인 코멘트만 포함한 리뷰 하나와 선택적 간결 요약 본문을 제출해. 인라인을 보장하려면 GitHub Reviews API를 사용해:
                - 다음 형식의 코멘트 JSON 배열을 구성: [{ "path": "<file>", "position": <diff_position>, "body": "..." }]
                - 다음으로 제출: gh api repos/${{ github.repository }}/pulls/${{ github.event.pull_request.number }}/reviews -f event=COMMENT -f body="$SUMMARY" -f comments='[$COMMENTS_JSON]'
              - 사용 금지: gh pr review --approve 또는 --request-changes

              차단 동작:
              - BLOCKING_REVIEW가 true이고 🚨 또는 🔒 이슈가 하나라도 올라왔으면: echo "CRITICAL_ISSUES_FOUND=true" >> $GITHUB_ENV
              - 그 외에는: echo "CRITICAL_ISSUES_FOUND=false" >> $GITHUB_ENV
              - 마지막에 항상 CRITICAL_ISSUES_FOUND를 설정해
              '

          - name: 차단 리뷰 결과 확인
            if: env.BLOCKING_REVIEW == 'true'
            run: |
              echo "중대한 이슈가 있는지 확인 중..."
              echo "CRITICAL_ISSUES_FOUND: ${CRITICAL_ISSUES_FOUND:-unset}"

              if [ "${CRITICAL_ISSUES_FOUND:-false}" = "true" ]; then
                echo "❌ 중대한 이슈가 발견됐고 차단 리뷰가 활성화되어 있어. 워크플로를 실패 처리할게."
                exit 1
              else
                echo "✅ 차단되는 이슈는 발견되지 않았어."
              fi
    ```
  </Expandable>

  <Frame>
    <img src="https://mintcdn.com/cursor/KODIqSiRh6LRGwl9/images/cli/cookbook/code-review/comment.png?fit=max&auto=format&n=KODIqSiRh6LRGwl9&q=85&s=31c7e4b54276532df8010645686ebbbc" alt="풀 리퀘스트에서 인라인 코멘트를 표시하는 자동 코드 리뷰" data-og-width="2920" width="2920" data-og-height="1272" height="1272" data-path="images/cli/cookbook/code-review/comment.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/KODIqSiRh6LRGwl9/images/cli/cookbook/code-review/comment.png?w=280&fit=max&auto=format&n=KODIqSiRh6LRGwl9&q=85&s=25e552210fa8425a10ff459bf4cd6006 280w, https://mintcdn.com/cursor/KODIqSiRh6LRGwl9/images/cli/cookbook/code-review/comment.png?w=560&fit=max&auto=format&n=KODIqSiRh6LRGwl9&q=85&s=234bf271bc595e763549c4f04d2e6fbb 560w, https://mintcdn.com/cursor/KODIqSiRh6LRGwl9/images/cli/cookbook/code-review/comment.png?w=840&fit=max&auto=format&n=KODIqSiRh6LRGwl9&q=85&s=b6f6d1444de7fe0197e3d35fa35955e8 840w, https://mintcdn.com/cursor/KODIqSiRh6LRGwl9/images/cli/cookbook/code-review/comment.png?w=1100&fit=max&auto=format&n=KODIqSiRh6LRGwl9&q=85&s=300314314f5071b77f735460be33985f 1100w, https://mintcdn.com/cursor/KODIqSiRh6LRGwl9/images/cli/cookbook/code-review/comment.png?w=1650&fit=max&auto=format&n=KODIqSiRh6LRGwl9&q=85&s=10e4db857ee84c55d17222cef492611d 1650w, https://mintcdn.com/cursor/KODIqSiRh6LRGwl9/images/cli/cookbook/code-review/comment.png?w=2500&fit=max&auto=format&n=KODIqSiRh6LRGwl9&q=85&s=e65add70ffebfeb9ad05c9bb19a5f4e1 2500w" />
  </Frame>
</div>

<div id="configure-authentication">
  ## 인증 구성
</div>

GitHub Actions에서 Cursor CLI를 인증하려면 [API 키랑 리포지토리 시크릿을 설정](/ko/cli/github-actions#authentication)해.

<div id="set-up-agent-permissions">
  ## 에이전트 권한 설정
</div>

에이전트가 수행할 수 있는 작업을 제어할 설정 파일을 만들어. 이렇게 하면 코드 푸시나 풀 리퀘스트 생성 같은 의도치 않은 작업을 막을 수 있어.

리포지토리 루트에 `.cursor/cli.json`을 만들어:

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

이 구성은 에이전트가 파일을 읽고 댓글을 달 때 GitHub CLI를 쓰게 해주지만, 저장소에는 변경을 못 하게 막아. 더 많은 구성 옵션은 [permissions reference](/ko/cli/reference/permissions)를 확인해.

<div id="build-the-github-actions-workflow">
  ## GitHub Actions 워크플로 빌드하기
</div>

이제 워크플로를 단계별로 만들어 보자.

<div id="set-up-the-workflow-trigger">
  ### 워크플로 트리거 설정
</div>

`.github/workflows/cursor-code-review.yml`를 만들고, pull request에서 실행되도록 설정해:

```yaml  theme={null}
name: Cursor 코드 리뷰

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
  ### 리포지토리 체크아웃
</div>

Pull request 코드를 가져오려면 checkout 단계를 추가해:

```yaml  theme={null}
- name: 저장소 체크아웃
  uses: actions/checkout@v4
  with:
    fetch-depth: 0
    ref: ${{ github.event.pull_request.head.sha }}
```

<div id="install-cursor-cli">
  ### Cursor CLI 설치
</div>

CLI 설치 단계를 추가해:

```yaml  theme={null}
- name: Cursor CLI 설치
  run: |
    curl https://cursor.com/install -fsS | bash
    echo "$HOME/.cursor/bin" >> $GITHUB_PATH
```

<div id="configure-the-review-agent">
  ### 리뷰 에이전트 구성하기
</div>

전체 리뷰 단계를 구현하기 전에, 리뷰 프롬프트의 구성을 먼저 이해해 보자. 이 섹션은 에이전트가 어떻게 동작해야 하는지 설명해:

**목표**:
에이전트가 현재 PR diff를 검토해 명확하고 심각도가 높은 이슈만 표시하고, 변경된 라인에만 매우 짧은 인라인 코멘트(1\~2문장)를 남긴 뒤 마지막에 간단한 요약을 추가하길 원해. 이렇게 하면 신호 대 잡음 비율이 적절하게 유지돼.

**형식**:
코멘트는 짧고 핵심만 담아야 해. 스캔을 빠르게 하려고 이모지를 사용하고, 마지막에 전체 리뷰에 대한 상위 수준 요약을 붙여.

**제출**:
리뷰가 끝나면, 리뷰에서 발견된 내용을 바탕으로 에이전트가 짧은 코멘트를 포함해야 해. 에이전트는 인라인 코멘트와 간결한 요약을 담은 하나의 리뷰로 제출해야 해.

**엣지 케이스**:
다음을 처리해야 해:

* 기존 코멘트가 해결됨: 해결된 경우 에이전트가 완료로 표시해야 해
* 중복 방지: 동일하거나 인접한 라인에 유사한 피드백이 이미 있으면 코멘트 작성을 건너뛰어야 해

**최종 프롬프트**:
완성된 프롬프트는 이러한 동작 요구사항을 모두 결합해 집중적이고 실행 가능한 피드백을 만들어

이제 리뷰 에이전트 단계를 구현해 보자:

```yaml  theme={null}
- name: 코드 리뷰 수행
  env:
    CURSOR_API_KEY: ${{ secrets.CURSOR_API_KEY }}
    GH_TOKEN: ${{ github.token }}
  run: |
    cursor-agent --force --model "$MODEL" --output-format=text --print "너는 GitHub Actions 러너에서 자동 코드 리뷰를 수행하고 있어. gh CLI는 GH_TOKEN으로 인증되어 있어. 풀 리퀘스트에 댓글을 남길 수 있어.
    
    Context:
    - Repo: ${{ github.repository }}
    - PR Number: ${{ github.event.pull_request.number }}
    - PR Head SHA: ${{ github.event.pull_request.head.sha }}
    - PR Base SHA: ${{ github.event.pull_request.base.sha }}
    
    Objectives:
    1) 기존 리뷰 댓글을 재확인하고 해결되었으면 resolved로 답장하기
    2) 현재 PR diff를 검토하고 명확하며 심각도가 높은 이슈만 표시하기
    3) 변경된 줄에만 매우 짧은 인라인 댓글(1~2문장)을 남기고 끝에 간단한 요약 추가하기
    
    Procedure:
    - 기존 댓글 가져오기: gh pr view --json comments
    - diff 가져오기: gh pr diff
    - 이전에 보고된 이슈가 인접한 변경으로 해결된 것으로 보이면 이렇게 답장: ✅ 최근 변경으로 이 이슈가 해결된 것으로 보입니다
    - 중복 방지: 동일하거나 유사한 피드백이 같은 줄 또는 인근 줄에 이미 있으면 건너뛰기
    
    Commenting rules:
    - 인라인 댓글은 최대 10개; 가장 치명적인 이슈에 우선순위 두기
    - 댓글당 하나의 이슈; 정확히 변경된 줄에 달기
    - 자연스럽고 구체적이며 실행 가능하게; 자동화 여부나 높은 확신 같은 표현은 언급하지 않기
    - 이모지 사용: 🚨 Critical 🔒 Security ⚡ Performance ⚠️ Logic ✅ Resolved ✨ Improvement
    
    Submission:
    - 인라인 댓글과 간결한 요약을 포함한 단일 리뷰 제출
    - 다음만 사용: gh pr review --comment
    - 다음은 사용하지 않기: gh pr review --approve 또는 --request-changes"
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
  ## 리뷰어 테스트하기
</div>

워크플로가 제대로 동작하는지, 에이전트가 이모지 피드백과 함께 리뷰 댓글을 남기는지 확인하려고 테스트용 pull request를 만들어봐.

<Frame>
  <img src="https://mintcdn.com/cursor/KODIqSiRh6LRGwl9/images/cli/cookbook/code-review/github-actions.png?fit=max&auto=format&n=KODIqSiRh6LRGwl9&q=85&s=aa989eb5b7520e6718a48afd8daa70d9" alt="특정 줄에 대한 인라인 피드백과 이모지가 포함된 자동 리뷰 댓글이 표시된 pull request" data-og-width="1250" width="1250" data-og-height="704" height="704" data-path="images/cli/cookbook/code-review/github-actions.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/KODIqSiRh6LRGwl9/images/cli/cookbook/code-review/github-actions.png?w=280&fit=max&auto=format&n=KODIqSiRh6LRGwl9&q=85&s=9f2e324beb1cccb8052dcd0682323e47 280w, https://mintcdn.com/cursor/KODIqSiRh6LRGwl9/images/cli/cookbook/code-review/github-actions.png?w=560&fit=max&auto=format&n=KODIqSiRh6LRGwl9&q=85&s=f08497ddb17921f4bb4638ef4eec3379 560w, https://mintcdn.com/cursor/KODIqSiRh6LRGwl9/images/cli/cookbook/code-review/github-actions.png?w=840&fit=max&auto=format&n=KODIqSiRh6LRGwl9&q=85&s=3c869c0ed8eb8b5743dd3821e57cd406 840w, https://mintcdn.com/cursor/KODIqSiRh6LRGwl9/images/cli/cookbook/code-review/github-actions.png?w=1100&fit=max&auto=format&n=KODIqSiRh6LRGwl9&q=85&s=19e98ed953f4cc17b2c578ce543cf88d 1100w, https://mintcdn.com/cursor/KODIqSiRh6LRGwl9/images/cli/cookbook/code-review/github-actions.png?w=1650&fit=max&auto=format&n=KODIqSiRh6LRGwl9&q=85&s=4d9f47472af81254bd09b5f6234fc97f 1650w, https://mintcdn.com/cursor/KODIqSiRh6LRGwl9/images/cli/cookbook/code-review/github-actions.png?w=2500&fit=max&auto=format&n=KODIqSiRh6LRGwl9&q=85&s=f3af19e3edd7f8bbbb77ba6566d8e183 2500w" />
</Frame>

<div id="next-steps">
  ## 다음 단계
</div>

이제 자동 코드 리뷰 시스템이 잘 돌아가. 다음 개선을 고려해봐:

* [CI 실패 수정](/ko/cli/cookbook/fix-ci)을 위한 추가 워크플로 설정
* 브랜치별로 서로 다른 리뷰 레벨 구성
* 팀의 기존 코드 리뷰 프로세스와 통합
* 파일 유형이나 디렉터리별로 에이전트 동작 커스터마이즈

<Expandable title="고급: 차단형 리뷰">
  치명적인 이슈가 발견되면 워크플로를 실패로 처리해서, 해결될 때까지 pull request가 머지되지 않게 설정할 수 있어.

  **프롬프트에 차단 동작 추가**

  먼저, 리뷰 에이전트 단계에 `BLOCKING_REVIEW` 환경 변수를 포함하고, 이 차단 동작을 프롬프트에 추가해:

  ```
  Blocking behavior:
  - If BLOCKING_REVIEW is true and any 🚨 or 🔒 issues were posted: echo "CRITICAL_ISSUES_FOUND=true" >> $GITHUB_ENV
  - Otherwise: echo "CRITICAL_ISSUES_FOUND=false" >> $GITHUB_ENV
  - Always set CRITICAL_ISSUES_FOUND at the end
  ```

  **차단 확인 단계 추가**

  그다음 코드 리뷰 단계 뒤에 이 새 단계를 추가해:

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

← Previous: [Bugbot](./bugbot.md) | [Index](./index.md) | Next: [CI 실패 해결](./section-45.md) →