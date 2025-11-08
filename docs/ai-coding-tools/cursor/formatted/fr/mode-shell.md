---
title: "Mode Shell"
source: "https://docs.cursor.com/fr/cli/shell-mode"
language: "fr"
language_name: "French"
---

# Mode Shell
Source: https://docs.cursor.com/fr/cli/shell-mode

Exécute des commandes shell directement depuis le CLI sans quitter ta conversation

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

Le mode Shell exécute des commandes shell directement depuis le CLI sans quitter ta conversation. Utilise-le pour des commandes rapides et non interactives, avec des garde-fous et un affichage des résultats directement dans la conversation.

<Frame>
  <video src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/cli/shell-mode/cli-shell-mode.mp4?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=5194392f1189eb1eba340d731e86bd5f" autoPlay loop muted playsInline controls data-path="images/cli/shell-mode/cli-shell-mode.mp4" />
</Frame>

<div id="command-execution">
  ## Exécution des commandes
</div>

Les commandes s’exécutent dans ton shell de connexion (`$SHELL`) avec le répertoire de travail et l’environnement du CLI. Enchaîne les commandes pour les exécuter dans d’autres répertoires :

```bash  theme={null}
cd subdir && npm test
```

<div id="output">
  ## Sortie
</div>

<product_visual type="screenshot">
  Sortie de commande affichant un en-tête avec le code de retour, l’affichage de stdout/stderr et des contrôles de troncature
</product_visual>

Les sorties volumineuses sont automatiquement tronquées et les processus longue durée expirent pour maintenir les performances.

<div id="limitations">
  ## Limitations
</div>

* Les commandes expirent au bout de 30 secondes
* Les processus longue durée, les serveurs et les invites interactives ne sont pas pris en charge
* Utilise des commandes courtes et non interactives pour de meilleurs résultats

<div id="permissions">
  ## Permissions
</div>

Les commandes sont vérifiées par rapport à tes permissions et aux paramètres de ton équipe avant exécution. Consulte [Permissions](/fr/cli/reference/permissions) pour une configuration détaillée.

<product_visual type="screenshot">
  Bandeau de décision affichant les options d’approbation : Run, Reject/Propose, Add to allowlist et Auto‑run
</product_visual>

Les politiques d’admin peuvent bloquer certaines commandes, et les commandes avec redirection ne peuvent pas être ajoutées à la allowlist en ligne.

<div id="usage-guidelines">
  ## Recommandations d’utilisation
</div>

Le mode Shell est idéal pour les vérifications d’état, les builds rapides, les opérations sur les fichiers et l’inspection de l’environnement.

Évite les serveurs longue durée, les applications interactives et les commandes nécessitant une entrée.

Chaque commande s’exécute indépendamment — utilise `cd <dir> && ...` pour lancer des commandes dans d’autres répertoires.

<div id="troubleshooting">
  ## Dépannage
</div>

* Si une commande se fige, annule avec <Kbd>Ctrl+C</Kbd> et ajoute des options non interactives
* Quand on te demande des autorisations, approuve une fois ou ajoute à la allowlist avec <Kbd>Tab</Kbd>
* Si la sortie est tronquée, utilise <Kbd>Ctrl+O</Kbd> pour l’étendre
* Pour exécuter dans d’autres répertoires, utilise `cd <dir> && ...` car les changements ne persistent pas
* Le mode Shell prend en charge zsh et bash d’après ta variable `$SHELL`

<div id="faq">
  ## FAQ
</div>

<AccordionGroup>
  <Accordion title="Est-ce que `cd` persiste entre les exécutions ?">
    Non. Chaque commande s'exécute indépendamment. Utilise `cd <dir> && ...` pour lancer des commandes dans différents répertoires.
  </Accordion>

  <Accordion title="Puis-je changer le délai d'expiration ?">
    Non. Les commandes sont limitées à 30 secondes et ce n'est pas configurable.
  </Accordion>

  <Accordion title="Où configure-t-on les autorisations ?">
    Les autorisations sont gérées par la configuration du CLI et de l'équipe. Utilise la bannière de décision pour ajouter des commandes aux listes d'autorisation.
  </Accordion>

  <Accordion title="Comment quitter le mode Shell ?">
    Appuie sur <Kbd>Échap</Kbd> quand le champ est vide, sur <Kbd>Retour arrière</Kbd>/<Kbd>Suppr</Kbd> quand l'entrée est vide, ou <Kbd>Ctrl+C</Kbd> pour tout effacer et quitter.
  </Accordion>
</AccordionGroup>

---

← Previous: [Commandes slash](./commandes-slash.md) | [Index](./index.md) | Next: [Utiliser Agent dans le CLI](./utiliser-agent-dans-le-cli.md) →