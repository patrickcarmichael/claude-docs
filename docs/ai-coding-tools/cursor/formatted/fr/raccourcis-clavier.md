---
title: "Raccourcis clavier"
source: "https://docs.cursor.com/fr/configuration/kbd"
language: "fr"
language_name: "French"
---

# Raccourcis clavier
Source: https://docs.cursor.com/fr/configuration/kbd

Raccourcis clavier et raccourcis de touches dans Cursor

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

Aperçu des raccourcis clavier dans Cursor. Vois tous les raccourcis clavier en appuyant sur <Kbd>Cmd R</Kbd> puis <Kbd>Cmd S</Kbd>, ou en ouvrant la palette de commandes avec <Kbd>Cmd Shift P</Kbd> et en cherchant `Keyboard Shortcuts`.

Pour en savoir plus sur les raccourcis clavier dans Cursor, utilise [Key Bindings for VS Code](https://code.visualstudio.com/docs/getstarted/keybindings) comme référence de base pour les raccourcis de Cursor.

Tous les raccourcis de Cursor, y compris les fonctionnalités spécifiques à Cursor, peuvent être remappés dans les paramètres Keyboard Shortcuts.

<div id="general">
  ## Général
</div>

<div className="full-width-table equal-table-columns">
  | Raccourci              | Action                                                          |
  | ---------------------- | --------------------------------------------------------------- |
  | <Kbd>Cmd I</Kbd>       | Afficher/masquer le panneau latéral (sauf si associé à un mode) |
  | <Kbd>Cmd L</Kbd>       | Afficher/masquer le panneau latéral (sauf si associé à un mode) |
  | <Kbd>Cmd E</Kbd>       | Panneau de contrôle de l’agent en arrière-plan                  |
  | <Kbd>Cmd .</Kbd>       | Menu des modes                                                  |
  | <Kbd>Cmd /</Kbd>       | Basculer entre les modèles d’IA                                 |
  | <Kbd>Cmd Shift J</Kbd> | Paramètres de Cursor                                            |
  | <Kbd>Cmd ,</Kbd>       | Paramètres généraux                                             |
  | <Kbd>Cmd Shift P</Kbd> | Palette de commandes                                            |
</div>

<div id="chat">
  ## Chat
</div>

Raccourcis pour la zone de saisie du chat.

<div className="full-width-table equal-table-columns">
  | Raccourci                                            | Action                                                      |
  | ---------------------------------------------------- | ----------------------------------------------------------- |
  | <Kbd>Return</Kbd>                                    | Nudge (par défaut)                                          |
  | <Kbd>Ctrl Return</Kbd>                               | Mettre le message en file d’attente                         |
  | <Kbd>Cmd Return</Kbd> when typing                    | Forcer l’envoi du message                                   |
  | <Kbd>Cmd Shift Backspace</Kbd>                       | Annuler la génération                                       |
  | <Kbd>Cmd Shift L</Kbd> with code selected            | Ajouter le code sélectionné au contexte                     |
  | <Kbd>Cmd V</Kbd> with code or log in clipboard       | Ajouter le contenu du presse‑papiers au contexte            |
  | <Kbd>Cmd Shift V</Kbd> with code or log in clipboard | Ajouter le contenu du presse‑papiers dans la zone de saisie |
  | <Kbd>Cmd Return</Kbd> with suggested changes         | Accepter toutes les modifications                           |
  | <Kbd>Cmd Backspace</Kbd>                             | Rejeter toutes les modifications                            |
  | <Kbd>Tab</Kbd>                                       | Passer au message suivant                                   |
  | <Kbd>Shift Tab</Kbd>                                 | Revenir au message précédent                                |
  | <Kbd>Cmd Opt /</Kbd>                                 | Basculer de modèle                                          |
  | <Kbd>Cmd N</Kbd> / <Kbd>Cmd R</Kbd>                  | Nouveau chat                                                |
  | <Kbd>Cmd T</Kbd>                                     | Nouvel onglet de chat                                       |
  | <Kbd>Cmd \[</Kbd>                                    | Chat précédent                                              |
  | <Kbd>Cmd ]</Kbd>                                     | Chat suivant                                                |
  | <Kbd>Cmd W</Kbd>                                     | Fermer le chat                                              |
  | <Kbd>Escape</Kbd>                                    | Retirer le focus du champ                                   |
</div>

<div id="inline-edit">
  ## Édition en ligne
</div>

<div className="full-width-table equal-table-columns">
  | Raccourci                      | Action                        |
  | ------------------------------ | ----------------------------- |
  | <Kbd>Cmd K</Kbd>               | Ouvrir                        |
  | <Kbd>Cmd Shift K</Kbd>         | Basculer le focus de l’entrée |
  | <Kbd>Return</Kbd>              | Valider                       |
  | <Kbd>Cmd Shift Backspace</Kbd> | Annuler                       |
  | <Kbd>Opt Return</Kbd>          | Poser une question rapide     |
</div>

<div id="code-selection-context">
  ## Sélection de code et contexte
</div>

<div className="full-width-table equal-table-columns">
  | Raccourci                                                     | Action                                            |
  | ------------------------------------------------------------- | ------------------------------------------------- |
  | <Kbd>@</Kbd>                                                  | [Symboles @](/fr/context/@-symbols/)              |
  | <Kbd>#</Kbd>                                                  | Fichiers                                          |
  | <Kbd>/</Kbd>                                                  | Commandes rapides                                 |
  | <Kbd>Cmd Shift L</Kbd>                                        | Ajouter la sélection au chat                      |
  | <Kbd>Cmd Shift K</Kbd>                                        | Ajouter la sélection à Edit                       |
  | <Kbd>Cmd L</Kbd>                                              | Ajouter la sélection à une nouvelle discussion    |
  | <Kbd>Cmd M</Kbd>                                              | Basculer la stratégie de lecture des fichiers     |
  | <Kbd>Cmd →</Kbd>                                              | Accepter le mot suivant de la suggestion          |
  | <Kbd>Cmd Return</Kbd>                                         | Rechercher la base de code dans le chat           |
  | Sélectionne du code, <Kbd>Cmd C</Kbd>, <Kbd>Cmd V</Kbd>       | Ajouter le code de référence copié comme contexte |
  | Sélectionne du code, <Kbd>Cmd C</Kbd>, <Kbd>Cmd Shift V</Kbd> | Ajouter le code copié comme contexte texte        |
</div>

<div id="tab">
  ## Tab
</div>

<div className="full-width-table equal-table-columns">
  | Raccourci        | Action                  |
  | ---------------- | ----------------------- |
  | <Kbd>Tab</Kbd>   | Accepter la suggestion  |
  | <Kbd>Cmd →</Kbd> | Accepter le mot suivant |
</div>

<div id="terminal">
  ## Terminal
</div>

<div className="full-width-table equal-table-columns">
  | Raccourci             | Action                               |
  | --------------------- | ------------------------------------ |
  | <Kbd>Cmd K</Kbd>      | Ouvrir la barre d’invite du terminal |
  | <Kbd>Cmd Return</Kbd> | Exécuter la commande générée         |
  | <Kbd>Escape</Kbd>     | Valider la commande                  |
</div>

---

← Previous: [Utiliser Agent dans le CLI](./utiliser-agent-dans-le-cli.md) | [Index](./index.md) | Next: [Commandes shell](./commandes-shell.md) →