---
title: "CLI에서 에이전트 사용하기"
source: "https://docs.cursor.com/ko/cli/using"
language: "ko"
language_name: "Korean"
---

# CLI에서 에이전트 사용하기
Source: https://docs.cursor.com/ko/cli/using

Cursor CLI로 효과적으로 프롬프트하고, 리뷰하고, 반복하기

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

<div id="prompting">
  ## 프롬프트 작성
</div>

의도를 명확하게 밝히면 가장 좋은 결과를 얻을 수 있어. 예를 들어, 에이전트가 어떤 파일도 수정하지 않게 하려면 "코드를 작성하지 마" 같은 프롬프트를 쓰면 돼. 구현에 들어가기 전에 작업을 계획할 때 특히 유용해.

에이전트는 현재 파일 작업, 검색, 셸 명령 실행을 위한 도구를 갖추고 있어. IDE 에이전트처럼 더 많은 도구가 계속 추가되고 있어.

<div id="mcp">
  ## MCP
</div>

Agent는 확장 기능과 통합을 위해 [MCP(Model Context Protocol)](/ko/tools/mcp)을 지원해. CLI가 `mcp.json` 구성 파일을 자동으로 감지하고 따르니까, IDE에서 설정해 둔 MCP 서버와 도구를 그대로 쓸 수 있어.

<div id="rules">
  ## 규칙
</div>

CLI 에이전트는 IDE와 동일한 [규칙 시스템](/ko/context/rules)을 지원해. `.cursor/rules` 디렉터리에 규칙을 만들어 에이전트에 컨텍스트와 가이드라인을 제공할 수 있어. 이 규칙들은 설정에 따라 자동으로 로드되고 적용되니까, 프로젝트의 다양한 부분이나 특정 파일 유형에 맞춰 에이전트 동작을 커스터마이즈할 수 있어.

<Note>
  CLI는 프로젝트 루트에 있는(있다면) `AGENTS.md`와 `CLAUDE.md`도 읽어서 `.cursor/rules`와 함께 규칙으로 적용해.
</Note>

<div id="working-with-agent">
  ## Agent 사용하기
</div>

<div id="navigation">
  ### 탐색
</div>

이전 메시지는 위쪽 화살표(<Kbd>ArrowUp</Kbd>)로 불러와서 순환할 수 있어.

<div id="review">
  ### 검토
</div>

<Kbd>Cmd+R</Kbd>로 변경 사항을 검토해. 후속 지시를 추가하려면 <Kbd>i</Kbd>를 눌러. 스크롤은 <Kbd>ArrowUp</Kbd>/<Kbd>ArrowDown</Kbd>, 파일 전환은 <Kbd>ArrowLeft</Kbd>/<Kbd>ArrowRight</Kbd>를 써.

<div id="selecting-context">
  ### 컨텍스트 선택
</div>

<Kbd>@</Kbd>로 컨텍스트에 포함할 파일과 폴더를 선택해. `/compress`를 실행해 컨텍스트 창의 공간을 확보해. 자세한 내용은 [Summarization](/ko/agent/chat/summarization)을 확인해.

<div id="history">
  ## 기록
</div>

이전 컨텍스트를 불러오려면 `--resume [thread id]`로 기존 스레드에서 이어가.

가장 최근 대화를 다시 시작하려면 `cursor-agent resume`를 써.

이전 대화 목록을 보려면 `cursor-agent ls`를 실행해.

<div id="command-approval">
  ## 명령 승인
</div>

터미널 명령을 실행하기 전에 CLI가 실행을 승인(<Kbd>y</Kbd>)할지 거부(<Kbd>n</Kbd>)할지 물어봐.

<div id="non-interactive-mode">
  ## 비대화형 모드
</div>

`-p` 또는 `--print`를 사용해 Agent를 비대화형 모드로 실행해. 그러면 콘솔에 응답이 출력돼.

비대화형 모드에선 Agent를 대화 없이 호출할 수 있어. 스크립트, CI 파이프라인 등에 통합하기 좋아.

출력 형식을 제어하려면 `--output-format`과 함께 써. 예를 들어, 스크립트에서 파싱하기 쉬운 구조화된 출력을 원하면 `--output-format json`을, 일반 텍스트 출력을 원하면 `--output-format text`를 사용해.

<Note>
  비대화형 모드에서 Cursor는 전체 쓰기 권한을 가지고 있어.
</Note>

---

← Previous: [Shell 모드](./shell.md) | [Index](./index.md) | Next: [Keyboard Shortcuts](./keyboard-shortcuts.md) →