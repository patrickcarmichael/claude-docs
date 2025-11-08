---
title: "MCP"
source: "https://docs.cursor.com/fr/cli/mcp"
language: "fr"
language_name: "French"
---

# MCP
Source: https://docs.cursor.com/fr/cli/mcp

Utilise des serveurs MCP avec cursor-agent pour te connecter à des outils externes et à des sources de données

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

<div id="overview">
  ## Vue d’ensemble
</div>

La CLI de Cursor prend en charge les serveurs [Model Context Protocol (MCP)](/fr/context/mcp), te permettant de connecter des outils externes et des sources de données à `cursor-agent`. **MCP dans la CLI utilise la même configuration que l’éditeur** — tous les serveurs MCP que t’as configurés fonctionneront sans accroc avec les deux.

<Card title="Découvrir MCP" icon="link" href="/fr/context/mcp">
  Nouveau sur MCP ? Lis le guide complet sur la configuration, l’authentification et les serveurs disponibles
</Card>

<div id="cli-commands">
  ## Commandes CLI
</div>

Utilise la commande `cursor-agent mcp` pour gérer les serveurs MCP :

<div id="list-configured-servers">
  ### Lister les serveurs configurés
</div>

Affiche tous les serveurs MCP configurés et leur état actuel :

```bash  theme={null}
cursor-agent mcp list
```

Cela affiche :

* Noms et identifiants des serveurs
* État de la connexion (connecté/déconnecté)
* Source de la configuration (projet ou global)
* Méthode de transport (stdio, HTTP, SSE)

<div id="list-available-tools">
  ### Lister les outils disponibles
</div>

Voir les outils fournis par un serveur MCP donné :

```bash  theme={null}
cursor-agent mcp list-tools <identifiant>
```

Cela affiche :

* Noms et descriptions des outils
* Paramètres requis et facultatifs
* Types de paramètres et contraintes

<div id="login-to-mcp-server">
  ### Connexion au serveur MCP
</div>

Authentifie-toi auprès d’un serveur MCP configuré dans ton `mcp.json` :

```bash  theme={null}
cursor-agent mcp login <identifiant>
```

<div id="disable-mcp-server">
  ### Désactiver un serveur MCP
</div>

Retire un serveur MCP de la liste locale des serveurs approuvés :

```bash  theme={null}
cursor-agent mcp disable <ID>
```

<div id="using-mcp-with-agent">
  ## Utiliser MCP avec Agent
</div>

Une fois que tu as configuré des serveurs MCP (voir le [guide MCP principal](/fr/context/mcp) pour la configuration), `cursor-agent` détecte automatiquement et utilise les outils disponibles lorsqu’ils sont pertinents pour tes requêtes.

```bash  theme={null}

---

← Previous: [Installation](./installation.md) | [Index](./index.md) | Next: [Cursor CLI](./cursor-cli.md) →