---
title: "Background Agents"
source: "https://docs.cursor.com/en/background-agent"
language: "en"
language_name: "English"
---

# Background Agents
Source: https://docs.cursor.com/en/background-agent

Asynchronous remote agents in Cursor

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

With background agents, spawn asynchronous agents that edit and run code in a remote environment. View their status, send follow-ups, or take over anytime.

## How to Use

You can access background agents in two ways:

1. **Background Agent Sidebar**: Use the background agent tab in the native Cursor sidebar to view all background agents associated with your account, search existing agents, and start new ones.
2. **Background Agent Mode**: Hit <Kbd tooltip="Trigger background agent mode">Cmd E</Kbd> to trigger background agent mode in the UI.

After submitting a prompt, select your agent from the list to view status and enter the machine.

<Note>
  <p className="!mb-0">
    Background agents require data retention on the order of a few days.
  </p>
</Note>

## Setup

Background agents run in an isolated ubuntu-based machine by default. Agents have internet access and can install packages.

#### GitHub connection

Background agents clone your repo from GitHub and work on a separate branch, pushing to your repo for easy handoff.

Grant read-write privileges to your repo (and any dependent repos or submodules). We'll support other providers (GitLab, BitBucket, etc) in the future.

##### IP Allow List Configuration

If your organization uses GitHub's IP allow list feature, you'll need to configure access for background agents. See the [GitHub integration documentation](/en/integrations/github#ip-allow-list-configuration) for complete setup instructions including contact information and IP addresses.

#### Base Environment Setup

For advanced cases, set up the environment yourself. Get an IDE instance connected to the remote machine. Set up your machine, install tools and packages, then take a snapshot. Configure runtime settings:

* Install command runs before an agent starts and installs runtime dependencies. This might mean running `npm install` or `bazel build`.
* Terminals run background processes while the agent works - like starting a web server or compiling protobuf files.

For the most advanced cases, use a Dockerfile for machine setup. The dockerfile lets you set up system-level dependencies: install specific compiler versions, debuggers, or switch the base OS image. Don't `COPY` the entire project - we manage the workspace and check out the correct commit. Still handle dependency installation in the install script.

Enter any required secrets for your dev environment - they're stored encrypted-at-rest (using KMS) in our database and provided in the background agent environment.

The machine setup lives in `.cursor/environment.json`, which can be committed in your repo (recommended) or stored privately. The setup flow guides you through creating `environment.json`.

#### Maintenance Commands

When setting up a new machine, we start from the base environment, then run the `install` command from your `environment.json`. This command is what a developer would run when switching branches - install any new dependencies.

For most people, the `install` command is `npm install` or `bazel build`.

To ensure fast machine startup, we cache disk state after the `install` command runs. Design it to run multiple times. Only disk state persists from the `install` command - processes started here won't be alive when the agent starts.

#### Startup Commands

After running `install`, the machine starts and we run the `start` command followed by starting any `terminals`. This starts processes that should be alive when the agent runs.

The `start` command can often be skipped. Use it if your dev environment relies on docker - put `sudo service docker start` in the `start` command.

`terminals` are for app code. These terminals run in a `tmux` session available to you and the agent. For example, many website repos put `npm run watch` as a terminal.

#### The `environment.json` Spec

The `environment.json` file can look like:

```json  theme={null}
{
  "snapshot": "POPULATED_FROM_SETTINGS",
  "install": "npm install",
  "terminals": [
    {
      "name": "Run Next.js",
      "command": "npm run dev"
    }
  ]
}
```

Formally, the spec is [defined here](https://www.cursor.com/schemas/environment.schema.json).

## Models

Only [Max Mode](/en/context/max-mode)-compatible models are available for background agents.

## Pricing

Learn more about [Background Agent pricing](/en/account/pricing#background-agent).

## Security

Background Agents are available in Privacy Mode. We never train on your code and only retain code for running the agent. [Learn more about Privacy mode](https://www.cursor.com/privacy-overview).

What you should know:

1. Grant read-write privileges to our GitHub app for repos you want to edit. We use this to clone the repo and make changes.
2. Your code runs inside our AWS infrastructure in isolated VMs and is stored on VM disks while the agent is accessible.
3. The agent has internet access.
4. The agent auto-runs all terminal commands, letting it iterate on tests. This differs from the foreground agent, which requires user approval for every command. Auto-running introduces data exfiltration risk: attackers could execute prompt injection attacks, tricking the agent to upload code to malicious websites. See [OpenAI's explanation about risks of prompt injection for background agents](https://platform.openai.com/docs/codex/agent-network#risks-of-agent-internet-access).
5. If privacy mode is disabled, we collect prompts and dev environments to improve the product.
6. If you disable privacy mode when starting a background agent, then enable it during the agent's run, the agent continues with privacy mode disabled until it completes.

## Dashboard settings

Workspace admins can configure additional settings from the Background Agents tab on the dashboard.

### Defaults Settings

* **Default model** – the model used when a run does not specify one. Pick any model that supports Max Mode.
* **Default repository** – when empty, agents ask the user to choose a repo. Supplying a repo here lets users skip that step.
* **Base branch** – the branch agents fork from when creating pull requests. Leave blank to use the repository’s default branch.

### Security Settings

All security options require admin privileges.

* **User restrictions** – choose *None* (all members can start background agents) or *Allow list*. When set to *Allow list* you specify exactly which teammates can create agents.
* **Team follow-ups** – when on, anyone in the workspace can add follow-up messages to an agent someone else started. Turn it off to restrict follow-ups to the agent owner and admins.
* **Display agent summary** – controls whether Cursor shows the agent’s file-diff images and code snippets. Disable this if you prefer not to expose file paths or code in the sidebar.
* **Display agent summary in external channels** – extends the previous toggle to Slack or any external channel you’ve connected.

Changes save instantly and affect new agents immediately.

---

← Previous: [Tools](./tools.md) | [Index](./index.md) | Next: [Add Follow-up](./add-follow-up.md) →