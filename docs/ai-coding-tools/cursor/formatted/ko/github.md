---
title: "GitHub"
source: "https://docs.cursor.com/ko/integrations/github"
language: "ko"
language_name: "Korean"
---

# GitHub
Source: https://docs.cursor.com/ko/integrations/github

백그라운드 에이전트를 위한 공식 Cursor GitHub 앱

[Background Agents](/ko/background-agent)와 [Bugbot](/ko/bugbot)은 리포지토리를 클론하고 변경 사항을 푸시하려면 Cursor GitHub 앱이 필요해.

<div id="installation">
  ## 설치
</div>

1. [Dashboard의 Integrations](https://cursor.com/dashboard?tab=integrations)로 이동
2. GitHub 옆의 **Connect** 클릭
3. 리포지토리를 **All repositories** 또는 **Selected repositories** 중에서 선택

GitHub 계정을 연결 해제하려면 Integrations 대시보드로 돌아가 **Disconnect Account**를 클릭해.

<div id="using-agent-in-github">
  ## GitHub에서 Agent 사용하기
</div>

GitHub 통합을 통해 풀 리퀘스트와 이슈에서 바로 백그라운드 에이전트 워크플로를 실행할 수 있어. 어떤 PR이나 이슈에 `@cursor [prompt]`라고 댓글을 달면, 에이전트가 컨텍스트를 읽고, 수정 사항을 적용하고, 커밋을 푸시하도록 트리거할 수 있어.

[Bugbot](/ko/bugbot)을 켜놨다면, `@cursor fix`라고 댓글을 달아서 Bugbot이 제안한 수정안을 읽고 이슈를 해결할 백그라운드 에이전트를 트리거할 수 있어.

<div id="permissions">
  ## 권한
</div>

GitHub 앱이 백그라운드 에이전트랑 함께 작동하려면 특정 권한이 필요해:

<div className="full-width-table">
  | 권한                        | 목적                           |
  | ------------------------- | ---------------------------- |
  | **Repository access**     | 코드를 클론하고 작업 브랜치를 만들어         |
  | **Pull requests**         | 네 리뷰를 위해 에이전트 변경을 담은 PR을 만들어 |
  | **Issues**                | 에이전트가 찾거나 고친 버그와 작업을 추적해     |
  | **Checks and statuses**   | 코드 품질과 테스트 결과를 보고해           |
  | **Actions and workflows** | CI/CD 파이프라인과 배포 상태를 모니터링해    |
</div>

모든 권한은 백그라운드 에이전트 기능에 필요한 최소 권한 원칙을 따르고 있어.

<div id="ip-allow-list-configuration">
  ## IP 허용 목록 구성
</div>

조직에서 GitHub의 IP 허용 목록 기능으로 리포지토리 접근을 제한하고 있다면, 팀에 IP 허용 목록 기능을 켜 달라고 먼저 지원팀에 연락해야 해.

<div id="contact-support">
  ### 지원팀에 문의
</div>

IP 허용 목록을 설정하기 전에, 이 기능을 팀에 활성화하려면 [hi@cursor.com](mailto:hi@cursor.com)으로 먼저 연락해 줘. 아래 두 가지 구성 방식 모두에 필요한 절차야.

<div id="enable-ip-allow-list-configuration-for-installed-github-apps-recommended">
  ### 설치된 GitHub 앱에 대해 IP 허용 목록 구성 활성화(권장)
</div>

Cursor GitHub 앱에는 IP 목록이 이미 미리 설정돼 있어. 설치된 앱에 대해 허용 목록을 활성화하면 이 목록을 자동으로 승계할 수 있어. 이게 가장 권장되는 방법이야. 우리가 목록을 업데이트하면 조직도 자동으로 최신 목록을 받게 되거든.

활성화 방법:

1. 조직의 Security 설정으로 이동
2. IP 허용 목록 설정으로 이동
3. **"Allow access by GitHub Apps"** 체크

자세한 안내는 [GitHub 문서](https://docs.github.com/en/enterprise-cloud@latest/organizations/keeping-your-organization-secure/managing-security-settings-for-your-organization/managing-allowed-ip-addresses-for-your-organization#allowing-access-by-github-apps)를 참고해 줘.

<div id="add-ips-directly-to-your-allowlist">
  ### 허용 목록에 IP를 직접 추가
</div>

조직이 GitHub에서 IdP로 정의한 허용 목록을 사용하거나, 미리 구성된 허용 목록을 사용할 수 없다면 IP 주소를 직접 수동으로 추가하면 돼:

```
184.73.225.134
3.209.66.12
52.44.113.131
```

<Note>
  IP 주소 목록은 가끔 변경될 수 있어. IP allowlist를 사용하는 팀에는 IP 주소가 추가되거나 제거되기 전에 미리 알려줄게.
</Note>

<div id="troubleshooting">
  ## 문제 해결
</div>

<AccordionGroup>
  <Accordion title="에이전트가 리포지토리에 접근할 수 없음">
    * 리포지토리 접근 권한으로 GitHub 앱 설치하기
    * 비공개 리포지토리의 권한 설정 확인하기
    * GitHub 계정 권한 확인하기
  </Accordion>

  <Accordion title="풀 리퀘스트 권한 거부됨">
    * 앱에 풀 리퀘스트 쓰기 권한 부여하기
    * 브랜치 보호 규칙 확인하기
    * 앱 설치가 만료됐다면 재설치하기
  </Accordion>

  <Accordion title="GitHub 설정에서 앱이 보이지 않음">
    * 조직 단위로 설치됐는지 확인하기
    * [github.com/apps/cursor](https://github.com/apps/cursor)에서 재설치하기
    * 설치가 손상된 경우 지원팀에 문의하기
  </Accordion>
</AccordionGroup>

---

← Previous: [Git](./git.md) | [Index](./index.md) | Next: [Linear](./linear.md) →