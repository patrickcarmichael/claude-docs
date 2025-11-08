---
title: "在 CLI 中使用 Agent"
source: "https://docs.cursor.com/zh/cli/using"
language: "zh"
language_name: "Chinese"
---

# 在 CLI 中使用 Agent
Source: https://docs.cursor.com/zh/cli/using

使用 Cursor CLI 高效地进行提示、审阅与迭代

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
  ## 提示编写
</div>

清晰表达意图能带来更好的结果。比如，可以用提示词“do not write any code”来确保代理不会修改任何文件。这在动手实现前做任务规划时很有帮助。

Agent 目前具备文件操作、搜索和运行 shell 命令的工具。我们正在不断加入更多工具，类似 IDE agent。

<div id="mcp">
  ## MCP
</div>

Agent 支持 [MCP（Model Context Protocol）](/zh/tools/mcp)，用于扩展功能和集成。CLI 会自动检测并遵循你的 `mcp.json` 配置文件，从而启用你在 IDE 中配置的同一套 MCP 服务器和工具。

<div id="rules">
  ## 规则
</div>

CLI 代理支持与 IDE 相同的[规则系统](/zh/context/rules)。你可以在 `.cursor/rules` 目录中创建规则，为代理提供上下文和指导。这些规则会根据其配置自动加载并应用，让你可以针对项目的不同部分或特定文件类型自定义代理的行为。

<Note>
  CLI 还会读取项目根目录下的 `AGENTS.md` 和 `CLAUDE.md`（如果存在），并将其与 `.cursor/rules` 一并作为规则生效。
</Note>

<div id="working-with-agent">
  ## 使用 Agent
</div>

<div id="navigation">
  ### 导航
</div>

按向上箭头（<Kbd>ArrowUp</Kbd>）查看之前的消息，并在它们之间循环切换。

<div id="review">
  ### 审查
</div>

用 <Kbd>Cmd+R</Kbd> 审查更改。按 <Kbd>i</Kbd> 添加后续指令。用 <Kbd>ArrowUp</Kbd>/<Kbd>ArrowDown</Kbd> 滚动，用 <Kbd>ArrowLeft</Kbd>/<Kbd>ArrowRight</Kbd> 切换文件。

<div id="selecting-context">
  ### 选择上下文
</div>

按 <Kbd>@</Kbd> 选择要包含在上下文中的文件和文件夹。运行 `/compress` 释放上下文窗口的空间。详见 [Summarization](/zh/agent/chat/summarization)。

<div id="history">
  ## 历史
</div>

使用 `--resume [thread id]` 从现有线程继续，以加载先前的上下文。

要恢复最近的对话，使用 `cursor-agent resume`。

你也可以运行 `cursor-agent ls` 查看以往对话的列表。

<div id="command-approval">
  ## 命令确认
</div>

在运行终端命令前，CLI 会提示你确认（<Kbd>y</Kbd>）或取消（<Kbd>n</Kbd>）执行。

<div id="non-interactive-mode">
  ## 非交互模式
</div>

使用 `-p` 或 `--print` 以非交互模式运行 Agent。它会把响应打印到控制台。

开启非交互模式后，可以以非交互方式调用 Agent，便于集成到脚本、CI 流水线等。

你也可以配合 `--output-format` 控制输出格式。比如，用 `--output-format json` 获取更易在脚本中解析的结构化输出，或者用 `--output-format text` 获取纯文本输出。

<Note>
  在非交互模式下，Cursor 具有完整的写入权限。
</Note>

---

← Previous: [Shell 模式](./shell.md) | [Index](./index.md) | Next: [键盘快捷键](./section.md) →