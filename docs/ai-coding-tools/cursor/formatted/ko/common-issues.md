---
title: "Common Issues"
source: "https://docs.cursor.com/ko/troubleshooting/common-issues"
language: "ko"
language_name: "Korean"
---

# Common Issues
Source: https://docs.cursor.com/ko/troubleshooting/common-issues

Solutions for common problems and FAQs

아래는 자주 겪는 문제와 해결 방법이야.

<div id="networking-issues">
  ### 네트워크 문제
</div>

먼저 네트워크 연결부터 확인해. `Cursor Settings` > `Network`로 가서 `Run Diagnostics`를 클릭해. Cursor 서버와의 연결을 점검하고, AI 기능, 업데이트, 기타 온라인 기능에 영향을 줄 수 있는 네트워크 문제를 찾아줘.

Cursor는 스트리밍 응답을 효율적으로 처리하기 위해 AI 기능에 HTTP/2를 사용해. 네트워크가 HTTP/2를 지원하지 않으면 인덱싱 실패나 AI 기능 장애가 생길 수 있어.

이런 상황은 기업 네트워크, VPN, Zscaler 같은 프록시를 사용할 때 자주 발생해.

해결하려면 앱 설정( Cursor 설정 아님 )에서 HTTP/1.1 폴백을 켜줘: `CMD/CTRL + ,`를 누르고 `HTTP/2`를 검색한 다음 `Disable HTTP/2`를 활성화해. 그러면 HTTP/1.1을 강제로 사용하게 되어 문제가 해결돼.

자동 감지와 폴백도 곧 추가할 거야.

<div id="resource-issues-cpu-ram-etc">
  ### 리소스 문제(CPU, RAM 등)
</div>

CPU나 RAM 사용량이 높으면 컴퓨터가 느려지거나 리소스 경고가 뜰 수 있어.

큰 코드베이스일수록 리소스를 더 쓰지만, 높은 사용량의 원인은 보통 익스텐션이나 설정 문제야.

<Note>
  **MacOS**에서 낮은 RAM 경고가 보이면, 일부 사용자에게 매우 부정확한 값이 표시되는 버그가 있어. 이런 경우 Activity Monitor를 열고 "Memory" 탭에서 실제 메모리 사용량을 확인해.
</Note>

CPU나 RAM 사용량이 높다면, 아래 단계를 시도해봐:

<AccordionGroup>
  <Accordion title="익스텐션 확인하기">
    익스텐션은 성능에 영향을 줄 수 있어.

    Extension Monitor는 설치된 익스텐션과 내장 익스텐션의 리소스 사용량을 보여줘.

    `Settings` > `Application` > `Experimental`에서 `Extension Monitor: Enabled`를 켜줘. 그러면 Cursor 재시작 안내가 뜰 거야.

    여는 방법: `Cmd/Ctrl + Shift + P` → `Developer: Open Extension Monitor`.

    Cursor는 익스텐션을 하나 이상의 **extension host**에서 실행해. 보통 대부분의 익스텐션이 같은 extension host에서 돌기 때문에, 어떤 익스텐션이 CPU 시간을 많이 잡아먹으면 다른 익스텐션까지 숨통이 막힐 수 있어!

    Extension Monitor에서 확인할 수 있어:

    * 익스텐션이 실행한 장기 실행 프로세스 전체(MacOS 및 Linux만).
    * **% Ext Host**: 해당 익스텐션이 사용한 전체 extension host 시간의 비율. 다른 익스텐션 대비 많이 쓰는 걸 파악하는 데 도움 돼.
    * **Max Blocking**: 모니터링 간격당 이 익스텐션의 최장 연속 실행 구간.
    * **% CPU**:
      * 익스텐션: 익스텐션 코드가 차지한 전체 CPU 사용량 비율.
      * 프로세스: 실행된 프로세스가 차지한 전체 CPU 사용량 비율(MacOS 및 Linux만).
    * **Memory**:
      * 익스텐션: 익스텐션 코드가 사용한 JS 힙 메모리(외부 할당 제외).
      * 프로세스: 실행된 프로세스가 사용한 시스템 메모리(MacOS 및 Linux만).

    커맨드 라인에서 `cursor --disable-extensions`를 실행해 테스트해봐. 성능이 좋아지면 문제 있는 익스텐션을 찾을 때까지 하나씩 다시 켜봐.

    Extension Bisect로 문제 익스텐션을 추려봐. 자세한 내용은 [여기](https://code.visualstudio.com/blogs/2021/02/16/extension-bisect#_welcome-extension-bisect)를 참고해. 참고: 점진적 성능 저하보다는 즉시 나타나는 이슈에서 더 효과적이야.
  </Accordion>

  <Accordion title="Process Explorer 사용하기">
    Process Explorer는 어떤 프로세스가 리소스를 쓰는지 보여줘.

    여는 방법: Command Palette(`Cmd/Ctrl + Shift + P`) → `Developer: Open Process Explorer`.

    아래 항목의 프로세스를 확인해:

    * **`extensionHost`**: 익스텐션 관련 이슈
    * **`ptyHost`**: 터미널 리소스 사용

    Process Explorer는 각 터미널과, 진단을 위한 실행 중인 명령을 표시해.

    그 외 고사용량 프로세스는 [forum](https://forum.cursor.com/)에 보고해줘.
  </Accordion>

  <Accordion title="시스템 리소스 모니터링">
    운영체제의 모니터링 도구로 문제가 Cursor에 국한된 건지, 시스템 전반 문제인지 확인해.
  </Accordion>

  <Accordion title="최소 설치로 테스트">
    문제가 계속되면, 최소 구성으로 Cursor를 설치해 테스트해봐.
  </Accordion>
</AccordionGroup>

<div id="general-faqs">
  ## 일반 FAQ
</div>

<AccordionGroup>
  <Accordion title="변경 로그에 업데이트가 보이는데 Cursor가 업데이트되지 않아">
    새 업데이트는 단계적 롤아웃을 사용해. 무작위로 선택된 사용자에게 먼저 배포돼. 며칠 안에 업데이트될 거야.
  </Accordion>

  <Accordion title="Cursor에서 GitHub 로그인에 문제가 있어 / Cursor에서 GitHub에서 어떻게 로그아웃해?">
    커맨드 팔레트 `Ctrl/⌘ + Shift + P`에서 `Sign Out of GitHub`를 실행해.
  </Accordion>

  <Accordion title="GitHub Codespaces를 사용할 수 없어">
    GitHub Codespaces는 아직 지원하지 않아.
  </Accordion>

  <Accordion title="Remote SSH 연결에 오류가 있어">
    Mac이나 Windows 머신으로의 SSH는 지원하지 않아. 다른 문제가 있으면 로그와 함께 [forum](https://forum.cursor.com/)에 보고해줘.
  </Accordion>

  <Accordion title="Windows에서 SSH 연결 문제">
    "SSH is only supported in Microsoft versions of VS Code" 메시지가 보이면:

    1. Remote-SSH 제거:
       * 확장 보기 열기 (`Ctrl + Shift + X`)
       * "Remote-SSH" 검색
       * 톱니바퀴 아이콘 클릭 → "Uninstall"

    2. Anysphere Remote SSH 설치:
       * Cursor 마켓플레이스 열기
       * "SSH" 검색
       * Anysphere Remote SSH 확장 설치

    3. 설치 후:
       * 활성 SSH 연결이 있는 모든 VS Code 인스턴스 종료
       * Cursor 재시작
       * SSH로 다시 연결

    SSH 설정과 키가 제대로 구성됐는지 확인해줘.
  </Accordion>

  <Accordion title="회사 프록시 뒤에서 Cursor Tab과 Inline Edit가 작동하지 않아">
    Cursor Tab과 Inline Edit는 지연 시간과 리소스 사용량을 줄이기 위해 HTTP/2를 사용해. 일부 기업 프록시(예: Zscaler)가 HTTP/2를 차단해. 설정에서 `"cursor.general.disableHttp2": true`로 바꾸면 해결돼 (`Cmd/Ctrl + ,` 누르고 `http2` 검색).
  </Accordion>

  <Accordion title="방금 Pro를 구독했는데 앱에서는 아직 무료 플랜이야">
    Cursor 설정에서 로그아웃했다가 다시 로그인해줘.
  </Accordion>

  <Accordion title="사용량은 언제 다시 리셋돼?">
    Pro 구독자: [Dashboard](https://cursor.com/dashboard)에서 `Manage Subscription`을 클릭해 갱신 날짜를 확인해.

    무료 사용자: 첫 번째 Cursor 이메일 수신 날짜를 확인해. 그 날짜를 기준으로 매월 사용량이 리셋돼.
  </Accordion>

  <Accordion title="업데이트 후 Chat/Composer 기록이 사라졌어">
    디스크 공간이 부족하면 업데이트 중에 Cursor가 과거 데이터를 정리할 수 있어. 예방하려면:

    1. 업데이트 전에 충분한 디스크 여유 공간 유지
    2. 불필요한 시스템 파일 정기적으로 정리
    3. 업데이트 전에 중요한 대화 백업
  </Accordion>

  <Accordion title="Cursor를 어떻게 제거해?">
    [이 가이드](https://code.visualstudio.com/docs/setup/uninstall)를 따라줘. "VS Code" 또는 "Code"는 "Cursor"로, ".vscode"는 ".cursor"로 바꿔 적용하면 돼.
  </Accordion>

  <Accordion title="내 계정을 어떻게 삭제해?">
    [Dashboard](https://cursor.com/dashboard)에서 `Delete Account`를 클릭해. 계정과 모든 관련 데이터가 영구적으로 삭제돼.
  </Accordion>

  <Accordion title="명령줄에서 Cursor를 어떻게 열어?">
    터미널에서 `cursor`를 실행해. 명령이 없다면:

    1. 커맨드 팔레트 열기 `⌘⇧P`
    2. `install command` 입력
    3. `Install 'cursor' command` 선택 (원하면 VS Code를 대체하도록 `code` 명령도 설치)
  </Accordion>

  <Accordion title="Cursor에 로그인할 수 없어">
    Sign In을 클릭하면 cursor.com으로 리디렉션되지만 로그인되지 않는다면, 방화벽이나 백신 소프트웨어를 비활성화해줘. 로그인 과정을 차단할 수 있어.
  </Accordion>

  <Accordion title="Suspicious Activity 메시지">
    최근 시스템 오남용 증가로 인해 보안 조치로 요청이 차단됐을 수 있어. 이렇게 해결해봐:

    먼저 VPN을 확인해줘. 사용 중이라면 꺼봐. VPN이 보안 시스템을 트리거할 때가 있어.

    그래도 안 되면 다음을 시도해봐:

    * 새 채팅 만들기
    * 잠시 기다렸다가 다시 시도
    * Google 또는 GitHub 인증으로 새 계정 만들기
    * Cursor Pro로 업그레이드
  </Accordion>
</AccordionGroup>

---

← Previous: [MCP 서버](./mcp.md) | [Index](./index.md) | Next: [요청 ID 가져오기](./section-110.md) →