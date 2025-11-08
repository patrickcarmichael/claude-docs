---
title: "Agents en arrière-plan"
source: "https://docs.cursor.com/fr/background-agent"
language: "fr"
language_name: "French"
---

# Agents en arrière-plan
Source: https://docs.cursor.com/fr/background-agent

Agents distants asynchrones dans Cursor

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

Avec les background agents, lance des agents asynchrones qui éditent et exécutent du code dans un environnement distant. Consulte leur état, envoie des relances ou reprends la main à tout moment.

## Comment l'utiliser

Tu peux accéder aux background agents de deux façons :

1. **Barre latérale des background agents** : utilise l'onglet des background agents dans la barre latérale native de Cursor pour voir tous les background agents associés à ton compte, rechercher des agents existants et en démarrer de nouveaux.
2. **Mode background agent** : appuie sur <Kbd tooltip="Trigger background agent mode">Cmd E</Kbd> pour activer le mode background agent dans l’UI.

Après avoir soumis un prompt, sélectionne ton agent dans la liste pour voir l’état et entrer dans la machine.

<Note>
  <p className="!mb-0">
    Les background agents nécessitent une conservation des données de l’ordre de quelques jours.
  </p>
</Note>

<div id="setup">
  ## Configuration
</div>

Par défaut, les agents d’arrière-plan s’exécutent dans une machine Ubuntu isolée. Ils ont accès à Internet et peuvent installer des packages.

<div id="github-connection">
  #### Connexion à GitHub
</div>

Les agents en arrière-plan clonent ton repo depuis GitHub et bossent sur une branche dédiée, puis poussent vers ton repo pour un handoff facile.

Accorde des droits en lecture/écriture à ton repo (et à tous les repos ou sous-modules dépendants). On prendra en charge d’autres fournisseurs (GitLab, Bitbucket, etc.) à l’avenir.

<div id="ip-allow-list-configuration">
  ##### Configuration de la liste d’autorisation IP
</div>

Si ton organisation utilise la fonctionnalité de liste d’autorisation IP de GitHub, tu dois configurer l’accès pour les agents en arrière-plan. Consulte la [documentation d’intégration GitHub](/fr/integrations/github#ip-allow-list-configuration) pour des instructions de configuration complètes, y compris les coordonnées et les adresses IP.

<div id="base-environment-setup">
  #### Configuration de l’environnement de base
</div>

Pour les cas avancés, configure l’environnement toi‑même. Ouvre une instance d’IDE connectée à la machine distante. Prépare ta machine, installe les outils et packages, puis prends un snapshot. Configure les paramètres d’exécution :

* La commande d’installation s’exécute avant le démarrage d’un agent et installe les dépendances d’exécution. Ça peut vouloir dire lancer `npm install` ou `bazel build`.
* Les terminaux exécutent des processus en arrière‑plan pendant que l’agent travaille — par exemple démarrer un serveur web ou compiler des fichiers protobuf.

Pour les cas les plus avancés, utilise un Dockerfile pour configurer la machine. Le Dockerfile te permet d’installer des dépendances au niveau système : versions spécifiques de compilateurs, débogueurs, ou changement de l’image OS de base. Ne fais pas de `COPY` de tout le projet — on gère l’espace de travail et on récupère le commit correct. Gère quand même l’installation des dépendances dans le script d’installation.

Saisis les secrets requis pour ton environnement de dev — ils sont stockés chiffrés au repos (via KMS) dans notre base de données et fournis dans l’environnement de l’agent en arrière‑plan.

La configuration de la machine se trouve dans `.cursor/environment.json`, qui peut être commit dans ton repo (recommandé) ou stocké en privé. Le flux de configuration te guide pour créer `environment.json`.

<div id="maintenance-commands">
  #### Commandes de maintenance
</div>

Lors de la configuration d’une nouvelle machine, on part de l’environnement de base, puis on exécute la commande `install` depuis ton `environment.json`. C’est la commande qu’un·e dev lancerait en changeant de branche — pour installer toutes les nouvelles dépendances.

Pour la plupart, la commande `install` est `npm install` ou `bazel build`.

Pour garantir un démarrage rapide, on met en cache l’état du disque après l’exécution de la commande `install`. Conçois-la pour pouvoir l’exécuter plusieurs fois. Seul l’état du disque persiste après la commande `install` — les processus démarrés ici ne seront pas en cours d’exécution quand l’agent démarrera.

<div id="startup-commands">
  #### Commandes de démarrage
</div>

Après avoir exécuté `install`, la machine démarre, on lance la commande `start`, puis on démarre les `terminals`. Ça lance les processus qui doivent rester actifs quand l’agent s’exécute.

La commande `start` peut souvent être sautée. Utilise-la si ton environnement de dev dépend de Docker — mets `sudo service docker start` dans la commande `start`.

Les `terminals` servent pour le code de l’app. Ces terminaux tournent dans une session `tmux` accessible pour toi et pour l’agent. Par exemple, beaucoup de dépôts de sites web mettent `npm run watch` comme terminal.

<div id="the-environmentjson-spec">
  #### La spécification de `environment.json`
</div>

Le fichier `environment.json` peut ressembler à :

```json  theme={null}
{
  "snapshot": "RÉCUPÉRÉ_DEPUIS_LES_PARAMÈTRES",
  "install": "npm install",
  "terminals": [
    {
      "name": "Exécuter Next.js",
      "command": "npm run dev"
    }
  ]
}
```

Formellement, la spec est [définie ici](https://www.cursor.com/schemas/environment.schema.json).

<div id="models">
  ## Modèles
</div>

Seuls les modèles compatibles avec le [mode Max](/fr/context/max-mode) sont disponibles pour les agents en arrière-plan.

<div id="pricing">
  ## Tarifs
</div>

En savoir plus sur les [tarifs de Background Agent](/fr/account/pricing#background-agent).

<div id="security">
  ## Sécurité
</div>

Les Background Agents sont disponibles en mode confidentialité. On n’entraîne jamais nos modèles sur ton code et on ne conserve ton code que pour exécuter l’agent. [En savoir plus sur le mode confidentialité](https://www.cursor.com/privacy-overview).

Ce que tu dois savoir :

1. Accorde des droits lecture/écriture à notre application GitHub pour les dépôts que tu veux modifier. On s’en sert pour cloner le dépôt et faire des changements.
2. Ton code s’exécute dans notre infrastructure AWS, dans des VM isolées, et reste stocké sur les disques des VM tant que l’agent est actif.
3. L’agent a accès à internet.
4. L’agent exécute automatiquement toutes les commandes du terminal, ce qui lui permet d’itérer sur les tests. Ça diffère de l’agent au premier plan, qui demande l’approbation de l’utilisateur pour chaque commande. L’exécution automatique introduit un risque d’exfiltration de données : des attaquants peuvent lancer des attaques par injection de prompt et tromper l’agent pour qu’il téléverse du code vers des sites malveillants. Voir [l’explication d’OpenAI sur les risques d’injection de prompt pour les agents en arrière-plan](https://platform.openai.com/docs/codex/agent-network#risks-of-agent-internet-access).
5. Si le mode confidentialité est désactivé, on collecte les prompts et les environnements de dev pour améliorer le produit.
6. Si tu désactives le mode confidentialité au démarrage d’un agent en arrière-plan puis que tu l’actives pendant son exécution, l’agent continue avec le mode confidentialité désactivé jusqu’à la fin.

<div id="dashboard-settings">
  ## Paramètres du tableau de bord
</div>

Les admins de l’espace de travail peuvent configurer des paramètres supplémentaires depuis l’onglet Background Agents du tableau de bord.

<div id="defaults-settings">
  ### Paramètres par défaut
</div>

* **Modèle par défaut** – le modèle utilisé lorsqu’une exécution n’en précise pas. Choisis n’importe quel modèle compatible avec Max Mode.
* **Dépôt par défaut** – s’il est vide, les agents te demanderont de choisir un dépôt. Renseigner un dépôt ici permet de passer cette étape.
* **Branche de base** – la branche à partir de laquelle les agents créent un fork lors de la création des pull requests. Laisse vide pour utiliser la branche par défaut du dépôt.

<div id="security-settings">
  ### Paramètres de sécurité
</div>

Toutes les options de sécurité nécessitent des privilèges d’admin.

* **Restrictions utilisateur** – choisis *Aucune* (tous les membres peuvent lancer des agents en arrière-plan) ou *Liste autorisée*. Quand *Liste autorisée* est activé, tu définis précisément quels équipiers peuvent créer des agents.
* **Relances d’équipe** – lorsqu’il est activé, n’importe qui dans l’espace de travail peut ajouter des messages de suivi à un agent lancé par quelqu’un d’autre. Désactive-le pour limiter les suivis au propriétaire de l’agent et aux admins.
* **Afficher le résumé de l’agent** – détermine si Cursor affiche les images de diff de fichiers et les extraits de code de l’agent. Désactive-le si tu préfères ne pas exposer les chemins de fichiers ou du code dans la barre latérale.
* **Afficher le résumé de l’agent dans les canaux externes** – étend le réglage précédent à Slack ou à tout canal externe que tu as connecté.

Les modifications sont enregistrées instantanément et s’appliquent immédiatement aux nouveaux agents.

---

← Previous: [Outils](./outils.md) | [Index](./index.md) | Next: [Ajouter un suivi](./ajouter-un-suivi.md) →