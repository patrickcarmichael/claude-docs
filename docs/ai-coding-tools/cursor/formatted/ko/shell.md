---
title: "Shell 모드"
source: "https://docs.cursor.com/ko/cli/shell-mode"
language: "ko"
language_name: "Korean"
---

# Shell 모드
Source: https://docs.cursor.com/ko/cli/shell-mode

대화 흐름을 유지한 채 CLI에서 바로 셸 명령을 실행해

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

Shell Mode는 대화를 떠나지 않고 CLI에서 셸 명령을 바로 실행해. 안전 검사를 거치고, 출력은 대화에 표시되니까 빠른 비대화형 명령에 써봐.

<Frame>
  <video src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/cli/shell-mode/cli-shell-mode.mp4?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=5194392f1189eb1eba340d731e86bd5f" autoPlay loop muted playsInline controls data-path="images/cli/shell-mode/cli-shell-mode.mp4" />
</Frame>

<div id="command-execution">
  ## 명령 실행
</div>

명령은 로그인 셸(`$SHELL`)에서, CLI의 작업 디렉터리와 환경을 그대로 사용해 실행돼. 다른 디렉터리에서 실행하려면 명령을 체인으로 이어서 실행해:

```bash  theme={null}
cd subdir && npm test
```

<div id="output">
  ## 출력
</div>

<product_visual type="screenshot">
  종료 코드가 표시된 헤더, stdout/stderr 표시, 그리고 잘림 제어가 있는 명령 출력
</product_visual>

큰 출력은 자동으로 잘리고, 오래 실행되는 프로세스는 성능 유지를 위해 타임아웃돼.

<div id="limitations">
  ## 제한 사항
</div>

* 명령은 30초 후에 타임아웃돼
* 장시간 실행 프로세스, 서버, 대화형 프롬프트는 지원하지 않아
* 최상의 결과를 위해 짧은 비대화형 명령을 사용해

<div id="permissions">
  ## 권한
</div>

명령은 실행 전에 너의 권한과 팀 설정에 맞춰 확인돼. 자세한 설정은 [Permissions](/ko/cli/reference/permissions)를 참고해.

<product_visual type="screenshot">
  승인 옵션을 보여주는 결정 배너: Run, Reject/Propose, Add to allowlist, Auto-run
</product_visual>

관리자 정책이 특정 명령을 막을 수 있고, 리디렉션이 있는 명령은 인라인으로 allowlist에 추가할 수 없어.

<div id="usage-guidelines">
  ## 사용 가이드라인
</div>

Shell Mode는 상태 확인, 빠른 빌드, 파일 작업, 환경 점검에 잘 맞아.

오래 돌아가는 서버, 대화형 앱, 입력이 필요한 명령은 피해.

각 명령은 독립적으로 실행돼 — 다른 디렉터리에서 실행하려면 `cd <dir> && ...`를 써.

<div id="troubleshooting">
  ## 문제 해결
</div>

* 명령이 멈추면 <Kbd>Ctrl+C</Kbd>로 취소하고 비대화형 플래그를 추가해
* 권한 요청이 뜨면 한 번 승인하거나 <Kbd>Tab</Kbd>으로 allowlist에 추가해
* 출력이 잘리면 <Kbd>Ctrl+O</Kbd>로 펼쳐
* 다른 디렉터리에서 실행하려면 변경 사항이 유지되지 않으니까 `cd <dir> && ...`를 써
* Shell Mode는 `$SHELL` 변수에 설정된 zsh와 bash를 지원해

<div id="faq">
  ## FAQ
</div>

<AccordionGroup>
  <Accordion title="`cd`는 실행 사이에 유지돼?">
    아니. 각 명령은 독립적으로 실행돼. 다른 디렉터리에서 명령을 실행하려면 `cd &lt;dir&gt; &amp;&amp; ...`를 써.
  </Accordion>

  <Accordion title="타임아웃을 바꿀 수 있어?">
    아니. 명령은 30초로 제한돼 있고 이건 설정할 수 없어.
  </Accordion>

  <Accordion title="권한은 어디에서 설정해?">
    권한은 CLI와 팀 설정으로 관리돼. 허용 목록에 명령을 추가하려면 결정 배너를 써.
  </Accordion>

  <Accordion title="Shell Mode는 어떻게 종료해?">
    입력이 비어 있을 때 <Kbd>Escape</Kbd>를 누르거나, 비어 있는 상태에서 <Kbd>Backspace</Kbd>/<Kbd>Delete</Kbd>를 누르거나, <Kbd>Ctrl+C</Kbd>로 지우고 종료해.
  </Accordion>
</AccordionGroup>

---

← Previous: [Slash commands](./slash-commands.md) | [Index](./index.md) | Next: [CLI에서 에이전트 사용하기](./cli.md) →