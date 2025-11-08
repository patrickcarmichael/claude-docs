---
title: "Auto-executed Cascade commands"
source: ""
---

# Auto-executed Cascade commands

Cascade has the ability to run terminal commands on its own with user permission. However, certain terminal commands can be accepted or rejected automatically through the Allow and Deny lists.

By enabling Auto mode, it will rely on Cascade's judgement on whether the command requires the user's permission to be executed. This feature is only available for messages sent with premium models.

### Turbo Mode

In Turbo mode, Cascade will always execute the command, unless it is in the deny list.

You can toggle this via the Windsurf - Settings panel in the bottom right hand corner of the editor.

<Frame>
  <img style={{ maxHeight: "500px" }} src="https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/cascade/cascade-turbo-mode.png?fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=8860ea8311000ae2cc440cef26560620" data-og-width="680" width="680" data-og-height="60" height="60" data-path="assets/windsurf/cascade/cascade-turbo-mode.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/cascade/cascade-turbo-mode.png?w=280&fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=dbcaa01fab58d7ba1fac05acc91ae12f 280w, https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/cascade/cascade-turbo-mode.png?w=560&fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=c5dc736ca3cd591d00f0c8b3b4f13f90 560w, https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/cascade/cascade-turbo-mode.png?w=840&fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=13ee4803cf3edcdaba2b9d76dcf109aa 840w, https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/cascade/cascade-turbo-mode.png?w=1100&fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=389cfcb06aec368986869bfd15a42553 1100w, https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/cascade/cascade-turbo-mode.png?w=1650&fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=e9829ad62b78b641213d472b4bca8683 1650w, https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/cascade/cascade-turbo-mode.png?w=2500&fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=db556ad06ddff8c4fbe5186569bf8334 2500w" />
</Frame>

### Allow list

An allow list defines a set of terminal commands that will always auto-execute. For example, if you add `git`, then Cascade will always accept `git add -A`.

The setting can be via Command Palette → Open Settings (UI) → Search for `windsurf.cascadeCommandsAllowList`.

<Frame>
  <img style={{ maxHeight: "500px" }} src="https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/cascade/allow-list.png?fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=be27cab4ada44ba016f41cf7d943ae20" data-og-width="2098" width="2098" data-og-height="770" height="770" data-path="assets/windsurf/cascade/allow-list.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/cascade/allow-list.png?w=280&fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=67d775a5a8dc5f74a9b1d743b265a9e1 280w, https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/cascade/allow-list.png?w=560&fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=fc3414e119592d5e9f7499e5e4e95d59 560w, https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/cascade/allow-list.png?w=840&fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=05dc8b80e975470b071eeefff32484e1 840w, https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/cascade/allow-list.png?w=1100&fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=19be334d151ab04ea1c32f1732c0ed60 1100w, https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/cascade/allow-list.png?w=1650&fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=7a16f9b1638e6a6b9cf4124460fdd308 1650w, https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/cascade/allow-list.png?w=2500&fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=e347583986d3f7cd0e220b87494263c2 2500w" />
</Frame>

### Deny list

A deny list defines a set of terminal commands that will never auto-execute. For example, if you add `rm`, then Cascade will always ask for permission to run `rm index.py`.

The setting can be via Command Palette → Open Settings (UI) → Search for `windsurf.cascadeCommandsDenyList`.

<Frame>
  <img style={{ maxHeight: "500px" }} src="https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/cascade/deny-list.png?fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=83f5c447deeb931e68781fbd6cb89733" data-og-width="2090" width="2090" data-og-height="624" height="624" data-path="assets/windsurf/cascade/deny-list.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/cascade/deny-list.png?w=280&fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=479a1b8b643adefbca8fcd08bbb2d4cd 280w, https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/cascade/deny-list.png?w=560&fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=fb60fb1ea1f66c2cd63eb62ae0513675 560w, https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/cascade/deny-list.png?w=840&fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=83520e9689fae159e121ccce1dc72901 840w, https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/cascade/deny-list.png?w=1100&fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=a4832324125ef273f72d41f315a434ca 1100w, https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/cascade/deny-list.png?w=1650&fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=28da77a6ed6fb67a2467df9bd95c7c90 1650w, https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/cascade/deny-list.png?w=2500&fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=01bc9a72d11a63527867a908cdace643 2500w" />
</Frame>

---

← Previous: [@-mention your terminal](./mention-your-terminal.md) | [Index](./index.md) | Next: [Vibe and Replace](./vibe-and-replace.md) →