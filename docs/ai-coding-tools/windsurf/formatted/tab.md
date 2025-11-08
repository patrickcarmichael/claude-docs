---
title: "Tab"
source: "https://docs.windsurf.com/tab/overview"
---

# Tab
Source: https://docs.windsurf.com/tab/overview

A powerful next-intent prediction experience routed to a single keystroke.

**Windsurf Tab** has evolved from a simple autocomplete tool into a contextually aware diff-suggestion and navigation engine for writing code.

It is powered by SWE-1-mini, our in-house model trained from scratch to optimize for speed and flow awareness.

<Frame>
  <video autoPlay muted loop playsInline src="https://mintcdn.com/codeium/bVGscI7v3lPUsThV/assets/windsurf/tabdemo.mp4?fit=max&auto=format&n=bVGscI7v3lPUsThV&q=85&s=eb7a88258f63bdedb0895c79dc251ba4" data-path="assets/windsurf/tabdemo.mp4" />
</Frame>

Suggestions are based on the context of your code, terminal, Cascade chat history, your prior actions around the editor, and even your clipboard (must opt in via advanced Settings).

Tab is able to make edits *both before and after* your current cursor position. You can press `esc` to cancel a suggestion.

Suggestions will also disappear if you continue typing or navigating without accepting them.

## Keyboard Shortcuts

* **Accept suggestion**: `tab`
* **Cancel suggestion**: `esc`
* **Accept suggestion word-by-word**: `⌘+→` (VS Code), `⌥+⇧+\` (JetBrains)
* **Next/previous suggestion**: `⌥+]`/`⌥+[`

## Tab to Jump

Windsurf can also anticipate your next cursor position and prompt you with a `Tab to Jump` label at a certain line in the editor, allowing you to easily navigate through your file.

If you accept by simply pressing `tab`, then you will be taken to that next position.

<Frame>
  <video style={{ transform: 'scale(1.12)' }} autoPlay muted loop playsInline src="https://mintcdn.com/codeium/bVGscI7v3lPUsThV/assets/windsurf/tab-to-jump.mp4?fit=max&auto=format&n=bVGscI7v3lPUsThV&q=85&s=5985dadc5b900d497e55946d6f429c91" data-path="assets/windsurf/tab-to-jump.mp4" />
</Frame>

## Tab to Import

After defining a new dependency to use in a file, just simply hit `tab` to import it at the top of the file once the hint shows. Your cursor will stay in the same position.

<Frame>
  <video autoPlay muted loop playsInline src="https://mintcdn.com/codeium/vRt4FQOyBeZpD2Pu/assets/tab-import.mp4?fit=max&auto=format&n=vRt4FQOyBeZpD2Pu&q=85&s=9e1a5dce9a510ea50295228011d93eab" data-path="assets/tab-import.mp4" />
</Frame>

## Settings

Windsurf Tab is split up into two main configurable parts: Autocomplete and Supercomplete.

Autocompletes typically appear at your cursor, and Supercompletes appear either in small windows around your cursor, which can suggest both deletions and additions.

Autocomplete and Supercomplete can be toggled on and off. Autocomplete speeds can also be configured between Slow, Default, and Fast modes.

You can also opt-in to using your clipboard as context. This means if you copy something to your clipboard, Windsurf will be able to use it as context.

You can also toggle Tab to Import and Tab to Jump functionalities, and choose whether or not you want to highlight the code after an accepted Tab suggestion.

<Frame>
  <img src="https://mintcdn.com/codeium/bVGscI7v3lPUsThV/assets/windsurf/tab-settings.png?fit=max&auto=format&n=bVGscI7v3lPUsThV&q=85&s=1b86247d84676fc10f627af39905cd93" data-og-width="1018" width="1018" data-og-height="1166" height="1166" data-path="assets/windsurf/tab-settings.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/codeium/bVGscI7v3lPUsThV/assets/windsurf/tab-settings.png?w=280&fit=max&auto=format&n=bVGscI7v3lPUsThV&q=85&s=16b8411f418af07bae750c84464306c3 280w, https://mintcdn.com/codeium/bVGscI7v3lPUsThV/assets/windsurf/tab-settings.png?w=560&fit=max&auto=format&n=bVGscI7v3lPUsThV&q=85&s=06dd67ed7ceae54a24192a3974e6bec5 560w, https://mintcdn.com/codeium/bVGscI7v3lPUsThV/assets/windsurf/tab-settings.png?w=840&fit=max&auto=format&n=bVGscI7v3lPUsThV&q=85&s=ab33f2279f4e4935ff878207ac6dfd56 840w, https://mintcdn.com/codeium/bVGscI7v3lPUsThV/assets/windsurf/tab-settings.png?w=1100&fit=max&auto=format&n=bVGscI7v3lPUsThV&q=85&s=042f119119f55a8102f870c4911a8113 1100w, https://mintcdn.com/codeium/bVGscI7v3lPUsThV/assets/windsurf/tab-settings.png?w=1650&fit=max&auto=format&n=bVGscI7v3lPUsThV&q=85&s=fe460dc8d3ffece1513964774185995b 1650w, https://mintcdn.com/codeium/bVGscI7v3lPUsThV/assets/windsurf/tab-settings.png?w=2500&fit=max&auto=format&n=bVGscI7v3lPUsThV&q=85&s=4c013b3f283b515e7309937a91c3a4c4 2500w" />
</Frame>

## Fill In The Middle (FIM)

Windsurf Tab can Fill In The Middle (FIM), meaning it can make suggestions while your cursor is in the middle of a line of code.

<Frame>
  <video autoPlay muted loop playsInline src="https://mintcdn.com/codeium/bVGscI7v3lPUsThV/assets/windsurf/inline-fim.mp4?fit=max&auto=format&n=bVGscI7v3lPUsThV&q=85&s=5526ce74678d75590b1c8182bcaa2125" data-path="assets/windsurf/inline-fim.mp4" />
</Frame>

Read more about in-line FIM on our blog [here](https://windsurf.com/blog/inline-fim-code-suggestions).

## Terminal Context Awareness

Windsurf Tab is also context aware of your the content of your terminal.

<Frame>
  <video autoPlay muted loop playsInline src="https://mintcdn.com/codeium/bVGscI7v3lPUsThV/assets/windsurf/tab-terminal-context.mp4?fit=max&auto=format&n=bVGscI7v3lPUsThV&q=85&s=8f567165363a508e416d08c7bb30773c" data-path="assets/windsurf/tab-terminal-context.mp4" />
</Frame>

---

← Previous: [Reporting Security Concerns](./reporting-security-concerns.md) | [Index](./index.md) | Next: [General Issues](./general-issues.md) →