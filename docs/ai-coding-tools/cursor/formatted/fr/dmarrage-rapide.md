---
title: "Démarrage rapide"
source: "https://docs.cursor.com/fr/get-started/quickstart"
language: "fr"
language_name: "French"
---

# Démarrage rapide
Source: https://docs.cursor.com/fr/get-started/quickstart

Prends en main Cursor en 5 minutes

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

Ce guide de démarrage rapide te fera parcourir un projet qui utilise les fonctionnalités clés de Cursor. À la fin, tu seras à l’aise avec Tab, Inline Edit et Agent.

<div id="open-a-project-in-cursor">
  ## Ouvre un projet dans Cursor
</div>

Utilise un projet existant ou clone notre exemple :

<Tabs>
  <Tab title="Cloner le projet d’exemple">
    1. Assure-toi que git est installé
    2. Clone le projet d’exemple :

    ```bash  theme={null}
    git clone git@github.com:voxelize/voxelize.git && \
    cd voxelize && \
    cursor .
    ```
  </Tab>

  <Tab title="Utiliser un projet existant">
    1. Ouvre Cursor
    2. Ouvre un dossier de projet avec <Kbd>Cmd O</Kbd> ou `cursor <path-to-project>`
  </Tab>
</Tabs>

On va montrer l’exemple avec le projet d’exemple, mais tu peux utiliser n’importe quel projet que tu as en local.

<div id="autocomplete-with-tab">
  ## Autocomplete avec [Tab](/fr/kbd#tab)
</div>

Tab est le modèle d'autocomplétion qu'on a entraîné en interne. C'est un super moyen d'entrer en douceur dans le codage assisté par l'IA si t'y es pas encore habitué. Avec Tab, tu peux :

* Autocompléter **plusieurs lignes et blocs** de code
* Passer **dans** et **entre** les fichiers jusqu'à la prochaine suggestion d'autocomplétion

1. Commence à taper le début d'une fonction :
   ```javascript  theme={null}
   function calculate
   ```
2. Les suggestions Tab apparaissent automatiquement
3. Appuie sur Tab pour accepter la suggestion
4. Cursor propose des paramètres et des corps de fonction

<div id="inline-edit-a-selection">
  ## [Inline Edit](/fr/inline-edit) d’une sélection
</div>

1. Sélectionne la fonction que tu viens de créer
2. Appuie sur <Kbd>Cmd K</Kbd>
3. Tape « make this function calculate fibonacci numbers »
4. Appuie sur <Kbd>Return</Kbd> pour appliquer les modifications
5. Cursor ajoute les imports et la documentation

<div id="chat-with-agent">
  ## Discuter avec [Agent](/fr/agent)
</div>

1. Ouvre le panneau Chat (<Kbd>Cmd I</Kbd>)
2. Demande : « Ajoute des tests pour cette fonction et exécute-les »
3. Agent va créer un fichier de test, écrire des tests et les lancer pour toi

<div id="bonus">
  ## Bonus
</div>

Fonctionnalités avancées :

<AccordionGroup>
  <Accordion title="Confier le travail au Background Agent">
    1. Ouvre le panneau de contrôle du Background Agent (<Kbd>Cmd E</Kbd>)
    2. Demande : « Find and fix a bug in this project »
    3. [Background Agent](/fr/background-agent) va :
       * Créer une machine virtuelle (VM) distante
       * Explorer ton projet
       * Détecter des bugs
       * Proposer des correctifs

    Passe en revue et applique les modifications.
  </Accordion>

  {" "}

  <Accordion title="Écrire une règle">
    1. Ouvre la palette de commandes (<Kbd>Cmd Shift P</Kbd>) 2. Recherche : « New Cursor
       Rule » 3. Donne-lui un nom (p. ex. : `style-guide`) 4. Sélectionne le type de règle « Always » 5. Définis
       ton style : `Prefer using camelCase for variable names`
  </Accordion>

  <Accordion title="Configurer un serveur MCP">
    1. Va sur notre [répertoire MCP](https://docs.cursor.com/tools)
    2. Choisis un outil
    3. Clique sur « Install »

    Les serveurs peuvent aussi être installés manuellement :

    1. Ouvre les paramètres de Cursor (<Kbd>Cmd Shift J</Kbd>)
    2. Va dans « Tools & Integrations »
    3. Clique sur « New MCP Server »
  </Accordion>
</AccordionGroup>

<div id="next-steps">
  ## Prochaines étapes
</div>

Parcours ces guides pour en savoir plus :

<CardGroup cols={2}>
  <Card title="Working with Context" href="/fr/guides/working-with-context">
    Fournis un contexte pertinent pour de meilleurs résultats
  </Card>

  <Card title="Selecting Models" href="/fr/guides/selecting-models">
    Choisis le bon modèle pour ta tâche
  </Card>
</CardGroup>

Découvre tous les [concepts de Cursor](/fr/get-started/concepts) et lance-toi !

---

← Previous: [Installation](./installation.md) | [Index](./index.md) | Next: [Data Science](./data-science.md) →