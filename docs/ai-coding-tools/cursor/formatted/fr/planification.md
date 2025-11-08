---
title: "Planification"
source: "https://docs.cursor.com/fr/agent/planning"
language: "fr"
language_name: "French"
---

# Planification
Source: https://docs.cursor.com/fr/agent/planning

Comment Agent planifie et gère des tâches complexes avec des tâches à faire et la mise en file d’attente

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

Agent peut anticiper et gérer des tâches complexes grâce à des listes de tâches structurées et à la mise en file d’attente des messages, ce qui rend les tâches de longue haleine plus faciles à comprendre et à suivre.

<div id="agent-to-dos">
  ## To-dos de l’Agent
</div>

Agent peut découper des tâches longues en étapes gérables avec des dépendances et créer un plan structuré qui se met à jour au fur et à mesure de l’avancement.

<video autoPlay loop muted playsInline controls>
  <source src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/agent/planning/agent-todo.mp4?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=b0285913832a3ef123fe149516ee37ea" type="video/mp4" data-path="images/agent/planning/agent-todo.mp4" />
</video>

<div id="how-it-works">
  ### Comment ça marche
</div>

* Agent génère automatiquement des listes de to-dos pour les tâches complexes
* Chaque élément peut dépendre d’autres tâches
* La liste se met à jour en temps réel à mesure que le travail progresse
* Les tâches terminées sont automatiquement cochées

<div id="visibility">
  ### Visibilité
</div>

* Les to-dos apparaissent dans l’interface de chat
* Si l’intégration [Slack](/fr/slack) est configurée, les to-dos y sont visibles aussi
* Tu peux consulter le découpage complet de la tâche à tout moment

<Tip>
  Pour une meilleure planification, décris clairement ton objectif final. Agent créera des
  découpages de tâches plus précis quand il comprend l’ensemble du périmètre.
</Tip>

<Note>La planification et les to-dos ne sont pas pris en charge pour le mode auto pour le moment.</Note>

## Messages en file d'attente

Mets en file d'attente des messages de suivi pendant qu'Agent travaille sur la tâche en cours. Tes instructions attendent leur tour et s'exécutent automatiquement dès qu'elles sont prêtes.

<video autoPlay loop muted playsInline controls>
  <source src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/agent/planning/agent-queue.mp4?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=4cdd6a7d1e12c67e520bc3ba67a42e0d" type="video/mp4" data-path="images/agent/planning/agent-queue.mp4" />
</video>

### Utiliser la file d'attente

1. Pendant qu'Agent travaille, tape ta prochaine instruction
2. Appuie sur <Kbd>Ctrl+Enter</Kbd> pour l’ajouter à la file d’attente
3. Les messages apparaissent dans l’ordre sous la tâche active
4. Réorganise les messages en file d’attente en cliquant sur la flèche
5. Agent les traite séquentiellement après avoir terminé

### Outrepasser la file d'attente

Pour mettre ton message en file d’attente au lieu d’utiliser la messagerie par défaut, utilise <Kbd>Ctrl+Enter</Kbd>. Pour envoyer un message immédiatement sans le mettre en file d’attente, utilise <Kbd>Cmd+Enter</Kbd>. Cela force l’envoi de ton message, en contournant la file d’attente pour l’exécuter tout de suite.

<div id="default-messaging">
  ## Messagerie par défaut
</div>

Par défaut, les messages sont envoyés aussi vite que possible et apparaissent généralement juste après qu’Agent a terminé un appel d’outil. Ça offre l’expérience la plus réactive.

<div id="how-default-messaging-works">
  ### Comment fonctionne la messagerie par défaut
</div>

* Ton message est ajouté au dernier message de l’utilisateur dans le chat
* Les messages se rattachent généralement aux résultats d’outil et s’envoient immédiatement dès qu’ils sont prêts
* Ça crée un flux de conversation plus naturel sans interrompre le travail en cours d’Agent
* Par défaut, ça se produit quand tu appuies sur Entrée pendant qu’Agent travaille

---

← Previous: [Vue d’ensemble](./vue-densemble.md) | [Index](./index.md) | Next: [Diffs & Review](./diffs-review.md) →