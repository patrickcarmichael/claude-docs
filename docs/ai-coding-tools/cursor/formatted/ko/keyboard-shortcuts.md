---
title: "Keyboard Shortcuts"
source: "https://docs.cursor.com/ko/configuration/kbd"
language: "ko"
language_name: "Korean"
---

# Keyboard Shortcuts
Source: https://docs.cursor.com/ko/configuration/kbd

Cursor의 키보드 단축키와 키 바인딩

export const Kbd = ({children, tooltip, os}) => {
  const keysInput = typeof children === 'string' && children.trim() !== '' ? children : null;
  if (!keysInput) {
    return null;
  }
  const isModifier = key => {
    const modifiers = ['⌘', '⇧', '⌥', '⌃', '⏎', '⌫', '⌦', '⎋', '⇥', '⌁', '←', '→', '↑', '↓', 'Ctrl', 'Shift', 'Alt', 'Cmd', 'Opt', 'Return', 'Backspace', 'Delete', 'Escape', 'Tab', 'Space', 'Enter', 'Esc', 'ArrowLeft', 'ArrowRight', 'ArrowUp', 'ArrowDown', 'Left', 'Right', 'Up', 'Down'];
    return modifiers.includes(key.trim());
  };
  const capitalizeFirstLetter = string => {
    return string.charAt(0).toUpperCase() + string.slice(1);
  };
  const isMac = os ? os.toLowerCase() === 'mac' || os.toLowerCase() === 'macos' : typeof navigator !== 'undefined' && (navigator.platform.toUpperCase().indexOf('MAC') >= 0 || navigator.userAgent.toUpperCase().indexOf('MAC') >= 0);
  const convertToSymbols = shortcut => {
    if (isMac) {
      return shortcut.replace(/⌘|Cmd|CMD/gi, '⌘').replace(/⌥|Opt|OPT/gi, '⌥').replace(/⌃|Ctrl/gi, '⌃').replace(/⇧|Shift/gi, '⇧').replace(/⏎|Return/gi, '⏎').replace(/⌫|Backspace/gi, '⌫').replace(/⌦|Delete/gi, '⌦').replace(/␛|Escape/gi, '␛').replace(/⇥|Tab/gi, '⇥').replace(/⌁|Space/gi, '⌁').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, '←').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, '→').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, '↑').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, '↓');
    } else {
      const converted = shortcut.replace(/⌘|Cmd|CMD/gi, 'Ctrl').replace(/⌥|Opt|OPT/gi, 'Alt').replace(/⌃|Ctrl/gi, 'Ctrl').replace(/⇧|Shift/gi, 'Shift').replace(/⏎|Return/gi, 'Enter').replace(/⌫|Backspace/gi, 'Backspace').replace(/⌦|Delete/gi, 'Delete').replace(/⎋|Escape/gi, 'Esc').replace(/⇥|Tab/gi, 'Tab').replace(/⌁|Space/gi, 'Space').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, 'Arrow-Left').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, 'Arrow-Right').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, 'Arrow-Up').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, 'Arrow-Down');
      const keyList = converted.split(/[\+\s]+/).filter(key => key.trim());
      return keyList.join('+');
    }
  };
  const convertToReadableText = shortcut => {
    const converted = shortcut.replace(/⌘|Cmd|CMD/gi, 'Cmd').replace(/⌥|Opt|OPT/gi, 'Opt').replace(/⌃|Ctrl/gi, 'Ctrl').replace(/⇧|Shift/gi, 'Shift').replace(/⏎|Return/gi, 'Return').replace(/⌫|Backspace/gi, 'Backspace').replace(/⌦|Delete/gi, 'Delete').replace(/⎋|Escape/gi, 'Escape').replace(/⇥|Tab/gi, 'Tab').replace(/⌁|Space/gi, 'Space').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, 'Arrow-Left').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, 'Arrow-Right').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, 'Arrow-Up').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, 'Arrow-Down');
    const keyList = converted.split(/[\+\s]+/).filter(key => key.trim());
    return keyList.map(key => {
      const trimmedKey = key.trim();
      return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
    }).join('+');
  };
  const displayShortcut = convertToSymbols(keysInput);
  const tooltipText = isMac ? tooltip ? `${convertToReadableText(keysInput)}: ${tooltip}` : convertToReadableText(keysInput) : tooltip || null;
  const processedKeys = isMac ? displayShortcut.split(/[\+\s]+/).filter(key => key.trim()).map(key => {
    const trimmedKey = key.trim();
    return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
  }).join('') : displayShortcut.split('+').map(key => {
    const trimmedKey = key.trim();
    return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
  }).join('+');
  return tooltipText ? <Tooltip tip={tooltipText}>
      <kbd>
        {processedKeys}
      </kbd>
    </Tooltip> : <kbd>
      {processedKeys}
    </kbd>;
};

Cursor의 키보드 단축키 개요. 모든 키보드 단축키는 <Kbd>Cmd R</Kbd>을 누른 다음 <Kbd>Cmd S</Kbd>를 누르거나, 명령 팔레트 <Kbd>Cmd Shift P</Kbd>를 열고 `Keyboard Shortcuts`를 검색해서 확인할 수 있어.

Cursor의 키보드 단축키를 더 알아보려면, Cursor 키 바인딩의 기준이 되는 [Key Bindings for VS Code](https://code.visualstudio.com/docs/getstarted/keybindings)를 참고해.

Cursor 전용 기능을 포함한 모든 Cursor 키 바인딩은 Keyboard Shortcuts 설정에서 재매핑할 수 있어.

<div id="general">
  ## 일반
</div>

<div className="full-width-table equal-table-columns">
  | 단축키                    | 동작                          |
  | ---------------------- | --------------------------- |
  | <Kbd>Cmd I</Kbd>       | 사이드패널 토글(모드에 연결되어 있지 않은 경우) |
  | <Kbd>Cmd L</Kbd>       | 사이드패널 토글(모드에 연결되어 있지 않은 경우) |
  | <Kbd>Cmd E</Kbd>       | 백그라운드 에이전트 제어 패널            |
  | <Kbd>Cmd .</Kbd>       | 모드 메뉴                       |
  | <Kbd>Cmd /</Kbd>       | AI 모델 순환                    |
  | <Kbd>Cmd Shift J</Kbd> | Cursor 설정                   |
  | <Kbd>Cmd ,</Kbd>       | 일반 설정                       |
  | <Kbd>Cmd Shift P</Kbd> | 커맨드 팔레트                     |
</div>

<div id="chat">
  ## 채팅
</div>

채팅 입력창 단축키.

<div className="full-width-table equal-table-columns">
  | Shortcut                                             | Action           |
  | ---------------------------------------------------- | ---------------- |
  | <Kbd>Return</Kbd>                                    | 넛지(기본)           |
  | <Kbd>Ctrl Return</Kbd>                               | 메시지를 대기열에 추가     |
  | <Kbd>Cmd Return</Kbd> when typing                    | 강제로 전송           |
  | <Kbd>Cmd Shift Backspace</Kbd>                       | 생성 취소            |
  | <Kbd>Cmd Shift L</Kbd> with code selected            | 선택한 코드를 컨텍스트에 추가 |
  | <Kbd>Cmd V</Kbd> with code or log in clipboard       | 클립보드를 컨텍스트에 추가   |
  | <Kbd>Cmd Shift V</Kbd> with code or log in clipboard | 클립보드를 입력창에 추가    |
  | <Kbd>Cmd Return</Kbd> with suggested changes         | 제안된 변경 사항 모두 수락  |
  | <Kbd>Cmd Backspace</Kbd>                             | 제안된 변경 사항 모두 거부  |
  | <Kbd>Tab</Kbd>                                       | 다음 메시지로 이동       |
  | <Kbd>Shift Tab</Kbd>                                 | 이전 메시지로 이동       |
  | <Kbd>Cmd Opt /</Kbd>                                 | 모델 전환            |
  | <Kbd>Cmd N</Kbd> / <Kbd>Cmd R</Kbd>                  | 새 채팅             |
  | <Kbd>Cmd T</Kbd>                                     | 새 채팅 탭           |
  | <Kbd>Cmd \[</Kbd>                                    | 이전 채팅            |
  | <Kbd>Cmd ]</Kbd>                                     | 다음 채팅            |
  | <Kbd>Cmd W</Kbd>                                     | 채팅 닫기            |
  | <Kbd>Escape</Kbd>                                    | 필드 포커스 해제        |
</div>

<div id="inline-edit">
  ## 인라인 편집
</div>

<div className="full-width-table equal-table-columns">
  | 단축키                            | 작업        |
  | ------------------------------ | --------- |
  | <Kbd>Cmd K</Kbd>               | 열기        |
  | <Kbd>Cmd Shift K</Kbd>         | 입력 포커스 토글 |
  | <Kbd>Return</Kbd>              | 제출        |
  | <Kbd>Cmd Shift Backspace</Kbd> | 취소        |
  | <Kbd>Opt Return</Kbd>          | 빠른 질문     |
</div>

## 코드 선택 & 컨텍스트

<div className="full-width-table equal-table-columns">
  | Shortcut                                        | Action                              |
  | ----------------------------------------------- | ----------------------------------- |
  | <Kbd>@</Kbd>                                    | [@-symbols](/ko/context/@-symbols/) |
  | <Kbd>#</Kbd>                                    | 파일                                  |
  | <Kbd>/</Kbd>                                    | 단축어 명령                              |
  | <Kbd>Cmd Shift L</Kbd>                          | 선택 영역을 Chat에 추가                     |
  | <Kbd>Cmd Shift K</Kbd>                          | 선택 영역을 Edit에 추가                     |
  | <Kbd>Cmd L</Kbd>                                | 선택 영역으로 새 채팅 시작                     |
  | <Kbd>Cmd M</Kbd>                                | 파일 읽기 전략 토글                         |
  | <Kbd>Cmd →</Kbd>                                | 제안의 다음 단어 받아들이기                     |
  | <Kbd>Cmd Return</Kbd>                           | 채팅에서 코드베이스 검색                       |
  | 코드 선택, <Kbd>Cmd C</Kbd>, <Kbd>Cmd V</Kbd>       | 복사한 참조 코드를 컨텍스트로 추가                 |
  | 코드 선택, <Kbd>Cmd C</Kbd>, <Kbd>Cmd Shift V</Kbd> | 복사한 코드를 텍스트 컨텍스트로 추가                |
</div>

<div id="tab">
  ## Tab
</div>

<div className="full-width-table equal-table-columns">
  | Shortcut         | Action      |
  | ---------------- | ----------- |
  | <Kbd>Tab</Kbd>   | 제안 받아들이기    |
  | <Kbd>Cmd →</Kbd> | 다음 단어 받아들이기 |
</div>

<div id="terminal">
  ## 터미널
</div>

<div className="full-width-table equal-table-columns">
  | 단축키                   | 동작            |
  | --------------------- | ------------- |
  | <Kbd>Cmd K</Kbd>      | 터미널 프롬프트 바 열기 |
  | <Kbd>Cmd Return</Kbd> | 생성된 명령 실행     |
  | <Kbd>Escape</Kbd>     | 명령 확정         |
</div>

---

← Previous: [CLI에서 에이전트 사용하기](./cli.md) | [Index](./index.md) | Next: [Shell Commands](./shell-commands.md) →