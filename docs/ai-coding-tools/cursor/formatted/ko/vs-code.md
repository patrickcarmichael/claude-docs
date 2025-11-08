---
title: "VS Code"
source: "https://docs.cursor.com/ko/guides/migration/vscode"
language: "ko"
language_name: "Korean"
---

# VS Code
Source: https://docs.cursor.com/ko/guides/migration/vscode

클릭 한 번으로 VS Code 설정과 확장 프로그램 가져오기

Cursor는 VS Code 코드베이스를 기반으로 만들어져, 익숙한 편집 환경을 유지하면서 최고의 AI 기반 코딩 경험을 만드는 데 집중할 수 있어. 덕분에 기존 VS Code 설정을 Cursor로 쉽게 마이그레이션할 수 있어.

<div id="profile-migration">
  ## 프로필 마이그레이션
</div>

<div id="one-click-import">
  ### 원클릭 가져오기
</div>

클릭 한 번으로 VS Code 설정 전체를 가져오는 방법:

1. Cursor 설정 열기 (<kbd>⌘</kbd>/<kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>J</kbd>)
2. General > Account로 이동
3. "VS Code Import"에서 Import 버튼 클릭

<Frame>
  <img src="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/vscode-import.png?fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=b7288403921047910fed69f1ae19b3d4" data-og-width="1307" width="1307" data-og-height="359" height="359" data-path="images/get-started/vscode-import.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/vscode-import.png?w=280&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=2bb1ffd673292810c7f271f224ee1937 280w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/vscode-import.png?w=560&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=f431f47576e4f9767eb062ca5a2e5f82 560w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/vscode-import.png?w=840&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=a67b7c2e6f8150207350875f27ccf0a1 840w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/vscode-import.png?w=1100&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=6a08000a573992f18a90b07c4a62adb4 1100w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/vscode-import.png?w=1650&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=e1ad4cd3868fba54ef75f84894a03797 1650w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/vscode-import.png?w=2500&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=4335d8732c6c0b9039da434e9deac267 2500w" />
</Frame>

다음이 전부 옮겨져:

* Extensions
* Themes
* Settings
* Keybindings

<div id="manual-profile-migration">
  ### 수동 프로필 마이그레이션
</div>

기기를 바꾸거나 설정을 더 세밀하게 컨트롤하고 싶다면, 프로필을 수동으로 마이그레이션해도 돼.

<div id="exporting-a-profile">
  #### 프로필 내보내기
</div>

1. VS Code에서 Command Palette 열기 (<kbd>⌘</kbd>/<kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd>)
2. "Preferences: Open Profiles (UI)" 검색
3. 왼쪽 사이드바에서 내보낼 프로필 찾기
4. 점 3개 메뉴를 클릭하고 "Export Profile" 선택
5. 로컬 머신이나 GitHub Gist로 내보내기 선택

<div id="importing-a-profile">
  #### 프로필 가져오기
</div>

1. Cursor에서 Command Palette 열기 (<kbd>⌘</kbd>/<kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd>)
2. "Preferences: Open Profiles (UI)" 검색
3. 'New Profile' 옆 드롭다운 메뉴를 클릭하고 'Import Profile' 클릭
4. GitHub Gist URL을 붙여넣거나 'Select File'을 선택해 로컬 파일 업로드
5. 대화상자 하단의 'Import'를 클릭해 프로필 저장
6. 마지막으로 사이드바에서 새 프로필을 선택하고 체크 아이콘을 클릭해 활성화

<div id="settings-and-interface">
  ## 설정 및 인터페이스
</div>

<div id="settings-menus">
  ### 설정 메뉴
</div>

<CardGroup>
  <Card title="Cursor Settings" icon="gear">
    Command Palette (<kbd>⌘</kbd>/<kbd>Ctrl</kbd> + <kbd>Shift</kbd>{" "}

    * <kbd>P</kbd>)를 열고 "Cursor Settings"를 입력해
  </Card>

  <Card title="VS Code Settings" icon="code">
    Command Palette (<kbd>⌘</kbd>/<kbd>Ctrl</kbd> + <kbd>Shift</kbd>{" "}

    * <kbd>P</kbd>)를 열고 "Preferences: Open Settings (UI)"를 입력해
  </Card>
</CardGroup>

<div id="version-updates">
  ### 버전 업데이트
</div>

<Card title="Version Updates" icon="code-merge">
  최신 VS Code의 기능과 수정 사항을 반영하기 위해 Cursor를 정기적으로 최신 버전에 리베이스해.
  안정성을 위해 Cursor는 가끔 약간 이전의 VS Code 버전을 사용해.
</Card>

<div id="activity-bar-orientation">
  ### Activity Bar 방향
</div>

<Frame>
  <img src="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/activity-bar.png?fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=7115db4ad44e29bf50cbb93d4a6766e6" data-og-width="478" width="478" data-og-height="186" height="186" data-path="images/get-started/activity-bar.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/activity-bar.png?w=280&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=f6690aff02f6b23ec1c44d9b3addb0f5 280w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/activity-bar.png?w=560&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=6ad8ce9e58f8f5e2bc40cbae481b738b 560w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/activity-bar.png?w=840&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=a93ec8cd4ecedb992a3c7775f5156095 840w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/activity-bar.png?w=1100&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=8cb513a6c916bb3164af6fc14451a0fa 1100w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/activity-bar.png?w=1650&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=149cef381de2fc65580dcaabd11cd5dd 1650w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/activity-bar.png?w=2500&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=d77ca2579d38947010f406a7558a7380 2500w" />
</Frame>

AI 채팅 인터페이스 공간을 최적화하려고 가로 배치를 기본으로 했어. 세로가 더 좋다면:

1. Command Palette (<kbd>⌘</kbd>/<kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd>) 열기
2. "Preferences: Open Settings (UI)" 검색
3. `workbench.activityBar.orientation` 검색
4. 값을 `vertical`로 설정
5. Cursor 재시작

---

← Previous: [JetBrains](./jetbrains.md) | [Index](./index.md) | Next: [아키텍처 다이어그램](./section.md) →