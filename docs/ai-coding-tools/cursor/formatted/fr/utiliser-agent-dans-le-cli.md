---
title: "Utiliser Agent dans le CLI"
source: "https://docs.cursor.com/fr/cli/using"
language: "fr"
language_name: "French"
---

# Utiliser Agent dans le CLI
Source: https://docs.cursor.com/fr/cli/using

Exécute des prompts, révise et itère efficacement avec le CLI Cursor

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
  ## Prompting
</div>

Énoncer clairement ton intention est recommandé pour obtenir les meilleurs résultats. Par exemple, tu peux utiliser l’invite « do not write any code » pour t’assurer que l’agent n’éditera aucun fichier. C’est généralement utile quand tu planifies des tâches avant de les implémenter.

L’agent dispose actuellement d’outils pour les opérations sur les fichiers, la recherche et l’exécution de commandes shell. D’autres outils sont en cours d’ajout, similaires à ceux de l’agent IDE.

<div id="mcp">
  ## MCP
</div>

Agent prend en charge le [MCP (Model Context Protocol)](/fr/tools/mcp) pour des fonctionnalités étendues et des intégrations. Le CLI détecte automatiquement et respecte ton fichier de configuration `mcp.json`, ce qui active les mêmes serveurs et outils MCP que t’as configurés pour l’IDE.

<div id="rules">
  ## Règles
</div>

L’agent CLI prend en charge le même [système de règles](/fr/context/rules) que l’IDE. Tu peux créer des règles dans le répertoire `.cursor/rules` pour fournir du contexte et des indications à l’agent. Ces règles sont automatiquement chargées et appliquées selon leur configuration, ce qui te permet de personnaliser le comportement de l’agent pour différentes parties de ton projet ou pour des types de fichiers spécifiques.

<Note>
  Le CLI lit aussi `AGENTS.md` et `CLAUDE.md` à la racine du projet (s’ils sont présents) et les applique comme règles, en complément de `.cursor/rules`.
</Note>

<div id="working-with-agent">
  ## Travailler avec Agent
</div>

<div id="navigation">
  ### Navigation
</div>

Parcours les messages précédents avec la flèche haut (<Kbd>ArrowUp</Kbd>).

<div id="review">
  ### Relecture
</div>

Passe en revue les modifications avec <Kbd>Cmd+R</Kbd>. Appuie sur <Kbd>i</Kbd> pour ajouter des instructions complémentaires. Utilise <Kbd>ArrowUp</Kbd>/<Kbd>ArrowDown</Kbd> pour faire défiler, et <Kbd>ArrowLeft</Kbd>/<Kbd>ArrowRight</Kbd> pour changer de fichier.

<div id="selecting-context">
  ### Sélection du contexte
</div>

Sélectionne des fichiers et des dossiers à inclure dans le contexte avec <Kbd>@</Kbd>. Libère de l’espace dans la fenêtre de contexte en exécutant `/compress`. Consulte [Summarization](/fr/agent/chat/summarization) pour plus de détails.

<div id="history">
  ## Historique
</div>

Reprends un fil existant avec `--resume [thread id]` pour charger le contexte précédent.

Pour reprendre la conversation la plus récente, utilise `cursor-agent resume`.

Tu peux aussi lancer `cursor-agent ls` pour voir la liste des conversations précédentes.

<div id="command-approval">
  ## Validation des commandes
</div>

Avant d'exécuter des commandes dans le terminal, le CLI te demandera de valider (<Kbd>y</Kbd>) ou d'annuler (<Kbd>n</Kbd>) l'exécution.

<div id="non-interactive-mode">
  ## Mode non interactif
</div>

Utilise `-p` ou `--print` pour lancer Agent en mode non interactif. Ça affichera la réponse dans la console.

En mode non interactif, tu peux invoquer Agent sans interaction. Ça te permet de l’intégrer à des scripts, des pipelines CI, etc.

Tu peux combiner ça avec `--output-format` pour contrôler le format de la sortie. Par exemple, utilise `--output-format json` pour une sortie structurée plus simple à analyser dans des scripts, ou `--output-format text` pour une sortie en texte brut.

<Note>
  Cursor dispose d’un accès en écriture complet en mode non interactif.
</Note>

---

← Previous: [Mode Shell](./mode-shell.md) | [Index](./index.md) | Next: [Raccourcis clavier](./raccourcis-clavier.md) →