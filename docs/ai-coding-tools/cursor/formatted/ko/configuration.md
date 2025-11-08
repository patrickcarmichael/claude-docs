---
title: "Configuration"
source: "https://docs.cursor.com/ko/cli/reference/configuration"
language: "ko"
language_name: "Korean"
---

# Configuration
Source: https://docs.cursor.com/ko/cli/reference/configuration

cli-config.json용 Agent CLI 구성 레퍼런스

`cli-config.json` 파일로 Agent CLI를 구성해.

<div id="file-location">
  ## 파일 위치
</div>

<div class="full-width-table">
  | 유형   | 플랫폼         | 경로                                         |
  | :--- | :---------- | :----------------------------------------- |
  | 전역   | macOS/Linux | `~/.cursor/cli-config.json`                |
  | 전역   | Windows     | `$env:USERPROFILE\.cursor\cli-config.json` |
  | 프로젝트 | 전체          | `<project>/.cursor/cli.json`               |
</div>

<Note>프로젝트 수준에서는 권한만 설정할 수 있어. 나머지 CLI 설정은 전부 전역으로 설정해야 해.</Note>

환경 변수로 오버라이드:

* **`CURSOR_CONFIG_DIR`**: 커스텀 디렉터리 경로
* **`XDG_CONFIG_HOME`** (Linux/BSD): `$XDG_CONFIG_HOME/cursor/cli-config.json` 사용

<div id="schema">
  ## 스키마
</div>

<div id="required-fields">
  ### 필수 필드
</div>

<div class="full-width-table">
  | Field               | Type      | Description                                                   |
  | :------------------ | :-------- | :------------------------------------------------------------ |
  | `version`           | number    | 구성 스키마 버전(현재: `1`)                                            |
  | `editor.vimMode`    | boolean   | Vim 키바인딩 사용(기본값: `false`)                                     |
  | `permissions.allow` | string\[] | 허용되는 작업(자세한 내용: [Permissions](/ko/cli/reference/permissions)) |
  | `permissions.deny`  | string\[] | 금지되는 작업(자세한 내용: [Permissions](/ko/cli/reference/permissions)) |
</div>

<div id="optional-fields">
  ### 선택 필드
</div>

<div class="full-width-table">
  | Field                    | Type    | Description              |
  | :----------------------- | :------ | :----------------------- |
  | `model`                  | object  | 선택된 모델 설정                |
  | `hasChangedDefaultModel` | boolean | CLI에서 관리하는 기본 모델 재정의 플래그 |
</div>

<div id="examples">
  ## 예제
</div>

<div id="minimal-config">
  ### 최소 설정
</div>

```json  theme={null}
{
  "version": 1,
  "editor": { "vimMode": false },
  "permissions": { "allow": ["Shell(ls)"], "deny": [] }
}
```

<div id="enable-vim-mode">
  ### Vim 모드 켜기
</div>

```json  theme={null}
{
  "version": 1,
  "editor": { "vimMode": true },
  "permissions": { "allow": ["Shell(ls)"], "deny": [] }
}
```

<div id="configure-permissions">
  ### 권한 설정
</div>

```json  theme={null}
{
  "version": 1,
  "editor": { "vimMode": false },
  "permissions": {
    "allow": ["Shell(ls)", "Shell(echo)"],
    "deny": ["Shell(rm)"]
  }
}
```

사용 가능한 권한 유형과 예시는 [Permissions](/ko/cli/reference/permissions)에서 확인해.

<div id="troubleshooting">
  ## 문제 해결
</div>

**설정 오류**: 파일을 잠시 옮겨두고 다시 시작해.

```bash  theme={null}
mv ~/.cursor/cli-config.json ~/.cursor/cli-config.json.bad
```

**변경 사항이 유지되지 않음**: JSON이 유효한지, 쓰기 권한이 있는지 확인해. 일부 필드는 CLI에서 관리돼서 덮어쓰일 수 있어.

<div id="notes">
  ## 참고사항
</div>

* 순수 JSON 형식(주석 없음)
* CLI가 누락된 필드를 자동으로 복구함
* 손상된 파일은 `.bad`로 백업한 뒤 다시 생성됨
* 권한 항목은 정확한 문자열이어야 함(자세한 내용은 [Permissions](/ko/cli/reference/permissions) 참고)

---

← Previous: [인증](./section.md) | [Index](./index.md) | Next: [출력 형식](./section.md) →