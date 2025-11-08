---
title: "GitHub Actions"
source: "https://docs.cursor.com/ko/cli/github-actions"
language: "ko"
language_name: "Korean"
---

# GitHub Actions
Source: https://docs.cursor.com/ko/cli/github-actions

GitHub Actions 및 기타 지속적 통합 시스템에서 Cursor CLI를 사용하는 방법을 알아보자

GitHub Actions 및 기타 CI/CD 시스템에서 Cursor CLI를 사용해 개발 작업을 자동화하자.

<div id="github-actions-integration">
  ## GitHub Actions 통합
</div>

기본 구성:

```yaml  theme={null}
- name: Cursor CLI 설치
  run: |
    curl https://cursor.com/install -fsS | bash
    echo "$HOME/.cursor/bin" >> $GITHUB_PATH

- name: Cursor Agent 실행
  env:
    CURSOR_API_KEY: ${{ secrets.CURSOR_API_KEY }}
  run: |
    cursor-agent -p "여기에 프롬프트를 입력해" --model gpt-5
```

<div id="cookbook-examples">
  ## 쿠크북 예시
</div>

실무 워크플로에 도움이 되는 쿠크북 예시를 확인해봐: [문서 업데이트](/ko/cli/cookbook/update-docs)와 [CI 문제 해결](/ko/cli/cookbook/fix-ci).

<div id="other-ci-systems">
  ## 기타 CI 시스템
</div>

다음이 갖춰진 어떤 CI/CD 시스템에서도 Cursor CLI를 사용할 수 있어:

* **셸 스크립트 실행**(bash, zsh 등)
* API 키 구성을 위한 **환경 변수**
* Cursor API에 접근할 **인터넷 연결**

<div id="autonomy-levels">
  ## 자율성 수준
</div>

에이전트의 자율성 수준을 선택해:

<div id="full-autonomy-approach">
  ### 완전 자율 방식
</div>

에이전트가 git 작업, API 호출, 외부 상호작용을 모두 직접 제어하게 해. 설정은 더 간단하지만, 더 큰 신뢰가 필요해.

**예시:** 우리 [Update Documentation](/ko/cli/cookbook/update-docs) 쿠크북의 첫 번째 워크플로우에선 에이전트가 다음을 수행해:

* PR 변경 사항 분석
* git 브랜치 생성 및 관리
* 변경 사항 커밋 및 푸시
* 풀 리퀘스트에 댓글 작성
* 모든 오류 시나리오 처리

```yaml  theme={null}
- name: 문서 업데이트 (완전 자율)
  run: |
    cursor-agent -p "git, GitHub CLI, 그리고 PR 작업에 완전한 접근 권한이 있어.
    커밋, 푸시, 그리고 PR 댓글을 포함해 전체 문서 업데이트 워크플로우를 처리해."
```

<div id="restricted-autonomy-approach">
  ### 제한적 자율성 접근 방식
</div>

<Note>
  프로덕션 CI 워크플로에선 **권한 기반 제한**과 함께 이 접근 방식을 쓰는 걸 추천해. 이렇게 하면 두 가지 장점을 모두 챙길 수 있어: 에이전트가 복잡한 분석과 파일 수정을 똑똑하게 처리하면서도, 중요한 작업은 결정론적이고 감사 가능하게 유지돼.
</Note>

중요 단계를 별도의 워크플로 단계로 분리하면서 에이전트의 작업 범위를 제한해. 제어와 예측 가능성이 더 좋아져.

**예시:** 같은 쿠크북의 두 번째 워크플로는 에이전트를 파일 수정으로만 제한해:

```yaml  theme={null}
- name: 문서 업데이트 생성 (제한됨)
  run: |
    cursor-agent -p "중요: 브랜치 생성, 커밋, 푸시, PR 댓글 작성 금지.
    작업 디렉터리의 파일만 수정해. 게시 작업은 이후 워크플로 단계에서 처리돼."

- name: 문서 브랜치 게시 (결정적)
  run: |
    # CI에서 결정적 git 작업을 처리함
    git checkout -B "docs/${{ github.head_ref }}"
    git add -A
    git commit -m "docs: PR 업데이트"
    git push origin "docs/${{ github.head_ref }}"

- name: PR 댓글 게시 (결정적)  
  run: |
    # CI에서 결정적 PR 댓글 작성을 처리함
    gh pr comment ${{ github.event.pull_request.number }} --body "문서가 업데이트됨"
```

<div id="permission-based-restrictions">
  ### 권한 기반 제한
</div>

CLI 수준에서 제한을 적용하려면 [권한 구성](/ko/cli/reference/permissions)을 사용해.

```json  theme={null}
{
  "permissions": {
    "allow": [
      "Read(**/*.md)",
      "Write(docs/**/*)",
      "Shell(grep)",
      "Shell(find)"
    ],
    "deny": [
      "Shell(git)",
      "Shell(gh)", 
      "Write(.env*)",
      "Write(package.json)"
    ]
  }
}
```

<div id="authentication">
  ## 인증
</div>

<div id="generate-your-api-key">
  ### API 키 생성
</div>

먼저 Cursor 대시보드에서 [API 키를 생성](/ko/cli/reference/authentication#api-key-authentication)해.

<div id="configure-repository-secrets">
  ### 리포지토리 시크릿 설정
</div>

리포지토리에 Cursor API 키를 안전하게 저장해:

1. GitHub 리포지토리로 이동해
2. **Settings** → **Secrets and variables** → **Actions**를 클릭해
3. **New repository secret**을 클릭해
4. 이름을 `CURSOR_API_KEY`로 지정해
5. 값으로 API 키를 붙여 넣어
6. **Add secret**을 클릭해

<div id="use-in-workflows">
  ### 워크플로에서 사용
</div>

`CURSOR_API_KEY` 환경 변수를 설정해:

```yaml  theme={null}
env:
  CURSOR_API_KEY: ${{ secrets.CURSOR_API_KEY }}
```

---

← Previous: [문서 업데이트](./section.md) | [Index](./index.md) | Next: [Headless CLI 사용하기](./headless-cli.md) →