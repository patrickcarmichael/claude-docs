---
title: "Shell 模式"
source: "https://docs.cursor.com/zh/cli/shell-mode"
language: "zh"
language_name: "Chinese"
---

# Shell 模式
Source: https://docs.cursor.com/zh/cli/shell-mode

在 CLI 中直接运行 shell 命令，无需离开对话

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

Shell 模式可在 CLI 中直接运行 shell 命令，无需离开对话。用它来执行快速、非交互式的命令；带有安全检查，输出会显示在对话中。

<Frame>
  <video src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/cli/shell-mode/cli-shell-mode.mp4?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=5194392f1189eb1eba340d731e86bd5f" autoPlay loop muted playsInline controls data-path="images/cli/shell-mode/cli-shell-mode.mp4" />
</Frame>

<div id="command-execution">
  ## 命令执行
</div>

命令会在你的登录 shell（`$SHELL`）中运行，并继承 CLI 的工作目录与环境。可通过串联命令在其他目录下运行：

```bash  theme={null}
cd subdir && npm test
```

<div id="output">
  ## 输出
</div>

<product_visual type="screenshot">
  命令输出显示带有退出码的页眉、stdout/stderr 面板，以及截断控制
</product_visual>

超大输出会自动截断，长时间运行的进程会超时以保证性能。

<div id="limitations">
  ## 限制
</div>

* 命令在 30 秒后会超时
* 不支持长时间运行的进程、服务器或交互式提示
* 建议使用简短且非交互式的命令以获得最佳效果

<div id="permissions">
  ## 权限
</div>

在执行之前，系统会根据你的权限和团队设置校验命令。查看 [Permissions](/zh/cli/reference/permissions) 了解详细配置。

<product_visual type="screenshot">
  决策横幅显示的审批选项：Run、Reject/Propose、Add to allowlist 和 Auto-run
</product_visual>

管理员策略可能会阻止某些命令，且带有重定向的命令无法在行内加入 allowlist。

<div id="usage-guidelines">
  ## 使用指南
</div>

Shell 模式适合用于状态检查、快速构建、文件操作和环境查看。

避免运行长时间驻留的服务器、交互式应用，以及需要用户输入的命令。

每条命令都是独立执行的——若要在其他目录下运行命令，请使用 `cd <dir> && ...`。

<div id="troubleshooting">
  ## 疑难排查
</div>

* 如果命令卡住，按 <Kbd>Ctrl+C</Kbd> 取消，并添加非交互式参数
* 当出现权限提示时，可批准一次，或按 <Kbd>Tab</Kbd> 将其加入允许列表
* 输出被截断时，按 <Kbd>Ctrl+O</Kbd> 展开
* 需要在不同目录运行时，使用 `cd <dir> && ...`，因为目录变更不会持久化
* Shell 模式会根据 `$SHELL` 变量使用 zsh 或 bash

<div id="faq">
  ## 常见问题
</div>

<AccordionGroup>
  <Accordion title="`cd` 会在多次运行之间保留吗？">
    不会。每条命令都是独立运行的。用 `cd <dir> && ...` 在不同目录里执行命令。
  </Accordion>

  <Accordion title="我可以更改超时时间吗？">
    不行。命令限定为 30 秒，且不可配置。
  </Accordion>

  <Accordion title="权限在哪里配置？">
    权限由 CLI 和团队配置一起管理。用决策横幅把命令加入允许列表。
  </Accordion>

  <Accordion title="怎么退出 Shell 模式？">
    当输入为空时按 <Kbd>Escape</Kbd>，在空输入时按 <Kbd>Backspace</Kbd>/<Kbd>Delete</Kbd>，或按 <Kbd>Ctrl+C</Kbd> 清除并退出。
  </Accordion>
</AccordionGroup>

---

← Previous: [斜杠命令](./section.md) | [Index](./index.md) | Next: [在 CLI 中使用 Agent](./cli-agent.md) →