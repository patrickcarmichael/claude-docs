---
title: "Model Context Protocol (MCP)"
source: "https://docs.cursor.com/fr/context/mcp"
language: "fr"
language_name: "French"
---

# Model Context Protocol (MCP)
Source: https://docs.cursor.com/fr/context/mcp

Connecte des outils externes et des sources de données à Cursor via MCP

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

<div id="what-is-mcp">
  ## C’est quoi MCP ?
</div>

[Model Context Protocol (MCP)](https://modelcontextprotocol.io/introduction) permet à Cursor de se connecter à des outils et des sources de données externes.

<Frame>
  <video src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/mcp/simple-mcp-call.mp4?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=08c642babc501c939ecbec9ef5124ce7" autoPlay loop muted playsInline controls data-path="images/context/mcp/simple-mcp-call.mp4" />
</Frame>

<div id="why-use-mcp">
  ### Pourquoi utiliser MCP ?
</div>

MCP relie Cursor à des systèmes et données externes. Au lieu de réexpliquer la structure de ton projet en boucle, connecte-toi directement à tes outils.

Écris des serveurs MCP dans n’importe quel langage capable d’écrire sur `stdout` ou d’exposer un endpoint HTTP — Python, JavaScript, Go, etc.

<div id="how-it-works">
  ### Comment ça marche
</div>

Les serveurs MCP exposent des fonctionnalités via le protocole, ce qui connecte Cursor à des outils externes ou à des sources de données.

Cursor prend en charge trois méthodes de transport :

<div className="full-width-table">
  | Transport                                                        | Environnement d’exécution | Déploiement                 | Utilisateurs           | Entrée                 | Authentification |
  | :--------------------------------------------------------------- | :------------------------ | :-------------------------- | :--------------------- | :--------------------- | :--------------- |
  | **<span className="whitespace-nowrap">`stdio`</span>**           | Local                     | Géré par Cursor             | Un seul utilisateur    | Commande shell         | Manuelle         |
  | **<span className="whitespace-nowrap">`SSE`</span>**             | Local/Remote              | Déployé en tant que serveur | Plusieurs utilisateurs | URL d’un endpoint SSE  | OAuth            |
  | **<span className="whitespace-nowrap">`Streamable HTTP`</span>** | Local/Remote              | Déployé en tant que serveur | Plusieurs utilisateurs | URL d’un endpoint HTTP | OAuth            |
</div>

<div id="protocol-support">
  ### Prise en charge du protocole
</div>

Cursor prend en charge les capacités suivantes du protocole MCP :

<div className="full-width-table">
  | Fonctionnalité  | Prise en charge | Description                                                                                                         |
  | :-------------- | :-------------- | :------------------------------------------------------------------------------------------------------------------ |
  | **Tools**       | Pris en charge  | Fonctions que le modèle d’IA peut exécuter                                                                          |
  | **Prompts**     | Pris en charge  | Messages et workflows paramétrés pour les utilisateurs                                                              |
  | **Resources**   | Pris en charge  | Sources de données structurées pouvant être lues et référencées                                                     |
  | **Roots**       | Pris en charge  | Requêtes initiées par le serveur pour déterminer les limites d’URI ou du système de fichiers dans lesquelles opérer |
  | **Elicitation** | Pris en charge  | Demandes initiées par le serveur pour obtenir des informations supplémentaires auprès des utilisateurs              |
</div>

<div id="installing-mcp-servers">
  ## Installation de serveurs MCP
</div>

<div id="one-click-installation">
  ### Installation en un clic
</div>

Installe des serveurs MCP depuis notre collection et authentifie-toi via OAuth.

<Columns cols={2}>
  <Card title="Parcourir les outils MCP" icon="table" horizontal href="/fr/tools">
    Parcours les serveurs MCP disponibles
  </Card>

  <Card title="Bouton « Ajouter à Cursor »" icon="plus" horizontal href="/fr/deeplinks">
    Crée un bouton « Ajouter à Cursor »
  </Card>
</Columns>

<div id="using-mcpjson">
  ### Utiliser `mcp.json`
</div>

Configure des serveurs MCP personnalisés avec un fichier JSON :

<CodeGroup>
  ```json CLI Server - Node.js theme={null}
  {
    "mcpServers": {
      "server-name": {
        "command": "npx",
        "args": ["-y", "mcp-server"],
        "env": {
          "API_KEY": "value"
        }
      }
    }
  }
  ```

  ```json CLI Server - Python theme={null}
  {
    "mcpServers": {
      "server-name": {
        "command": "python",
        "args": ["mcp-server.py"],
        "env": {
          "API_KEY": "value"
        }
      }
    }
  }
  ```

  ```json Remote Server theme={null}
  // Serveur MCP via HTTP ou SSE — s’exécute sur un serveur
  {
    "mcpServers": {
      "server-name": {
        "url": "http://localhost:3000/mcp",
        "headers": {
          "API_KEY": "value"
        }
      }
    }
  }
  ```
</CodeGroup>

<div id="stdio-server-configuration">
  ### Configuration du serveur STDIO
</div>

Pour les serveurs STDIO (serveurs locaux en ligne de commande), configure ces champs dans ton `mcp.json` :

<div className="full-width-table">
  | Champ       | Requis | Description                                                                                                             | Exemples                                  |
  | :---------- | :----- | :---------------------------------------------------------------------------------------------------------------------- | :---------------------------------------- |
  | **type**    | Oui    | Type de connexion du serveur                                                                                            | `"stdio"`                                 |
  | **command** | Oui    | Commande pour lancer l’exécutable du serveur. Doit être disponible dans ton PATH système ou inclure son chemin complet. | `"npx"`, `"node"`, `"python"`, `"docker"` |
  | **args**    | Non    | Tableau d’arguments passés à la commande                                                                                | `["server.py", "--port", "3000"]`         |
  | **env**     | Non    | Variables d’environnement pour le serveur                                                                               | `{"API_KEY": "${input:api-key}"}`         |
  | **envFile** | Non    | Chemin vers un fichier d’environnement pour charger d’autres variables                                                  | `".env"`, `"${workspaceFolder}/.env"`     |
</div>

<div id="using-the-extension-api">
  ### Utiliser l’API d’extension
</div>

Pour enregistrer des serveurs MCP par programmation, Cursor fournit une API d’extension qui permet une configuration dynamique sans modifier les fichiers `mcp.json`. C’est particulièrement utile dans les environnements d’entreprise et pour les workflows d’installation automatisés.

<Card title="Référence de l’API d’extension MCP" icon="code" href="/fr/context/mcp-extension-api">
  Découvre comment enregistrer des serveurs MCP par programmation avec `vscode.cursor.mcp.registerServer()`
</Card>

<div id="configuration-locations">
  ### Emplacements de configuration
</div>

<CardGroup cols={2}>
  <Card title="Configuration du projet" icon="folder-tree">
    Crée le fichier `.cursor/mcp.json` dans ton projet pour des outils spécifiques à ce projet.
  </Card>

  <Card title="Configuration globale" icon="globe">
    Crée le fichier `~/.cursor/mcp.json` dans ton dossier personnel pour des outils disponibles partout.
  </Card>
</CardGroup>

<div id="config-interpolation">
  ### Interpolation de configuration
</div>

Utilise des variables dans les valeurs de `mcp.json`. Cursor résout les variables dans ces champs : `command`, `args`, `env`, `url` et `headers`.

Syntaxe prise en charge :

* `${env:NAME}` variables d’environnement
* `${userHome}` chemin vers ton dossier personnel
* `${workspaceFolder}` racine du projet (le dossier qui contient `.cursor/mcp.json`)
* `${workspaceFolderBasename}` nom de la racine du projet
* `${pathSeparator}` et `${/}` séparateur de chemins du système d’exploitation

Exemples

```json  theme={null}
{
  "mcpServers": {
    "local-server": {
      "command": "python",
      "args": ["${workspaceFolder}/tools/mcp_server.py"],
      "env": {
        "API_KEY": "${env:API_KEY}"
      }
    }
  }
}
```

```json  theme={null}
{
  "mcpServers": {
    "remote-server": {
      "url": "https://api.example.com/mcp",
      "headers": {
        "Authorization": "Bearer ${env:MY_SERVICE_TOKEN}"
      }
    }
  }
}
```

<div id="authentication">
  ### Authentification
</div>

Les serveurs MCP utilisent des variables d’environnement pour l’authentification. Passe les clés d’API et les jetons via la config.

Cursor prend en charge OAuth pour les serveurs qui en ont besoin.

<div id="using-mcp-in-chat">
  ## Utiliser MCP dans le chat
</div>

Le Composer Agent utilise automatiquement les outils MCP répertoriés sous `Available Tools` quand c’est pertinent. Demande un outil précis par son nom ou décris ce dont tu as besoin. Active ou désactive des outils dans les paramètres.

<div id="toggling-tools">
  ### Activer/désactiver des outils
</div>

Active ou désactive des outils MCP directement depuis l’interface de chat. Clique sur le nom d’un outil dans la liste pour l’activer ou le désactiver. Les outils désactivés ne seront pas chargés dans le contexte et ne seront pas disponibles pour Agent.

<Frame>
  <video src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/mcp/tool-toggle.mp4?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=0fa3060f593cae3e5fb7c7d2f041a715" autoPlay loop muted playsInline controls data-path="images/context/mcp/tool-toggle.mp4" />
</Frame>

<div id="tool-approval">
  ### Approbation des outils
</div>

Par défaut, l’agent demande une approbation avant d’utiliser les outils MCP. Clique sur la flèche à côté du nom de l’outil pour afficher les arguments.

<Frame><img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/mcp/tool-confirm.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=bf9b19d5f23abc65914f712185b3ec72" alt="" data-og-width="1212" width="1212" data-og-height="902" height="902" data-path="images/context/mcp/tool-confirm.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/mcp/tool-confirm.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=e3f900fad0b8f2a469460c70fa1dd1dc 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/mcp/tool-confirm.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=de2f90138de39d75d70c5800f13be93a 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/mcp/tool-confirm.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=b9c616ce7a4080ea4088a0fdd0050c7c 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/mcp/tool-confirm.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=3f783e62a7a31957b8988edb97c139f9 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/mcp/tool-confirm.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=10bf2c1dbfd5c2a03aa95334f53cd571 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/mcp/tool-confirm.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=231c0e3cd60df5ad12455d5e8ef308d2 2500w" /></Frame>

<div id="auto-run">
  #### Exécution automatique
</div>

Active l’exécution automatique pour que Agent utilise les outils MCP sans te demander. Fonctionne comme des commandes de terminal. En savoir plus sur les paramètres d’exécution automatique [ici](/fr/agent/tools#auto-run).

<div id="tool-response">
  ### Réponse de l’outil
</div>

Cursor affiche la réponse dans le chat avec des volets déroulants pour les arguments et les réponses :

<Frame><img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/mcp/tool-call.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=30af3f35869e9a78781f455bdbc0e3b5" alt="" data-og-width="1212" width="1212" data-og-height="952" height="952" data-path="images/context/mcp/tool-call.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/mcp/tool-call.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=8821ac7bad00ad54a18abc614c2e3d5c 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/mcp/tool-call.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=d9d55f089ad53a89da99b8ddd524f6de 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/mcp/tool-call.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=a107d68a1fb05ed43851548b34fb4496 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/mcp/tool-call.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=b409b4941c2fd783043770fad0bd6390 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/mcp/tool-call.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=2a331b5e2bb9be0b9659393157454c2e 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/mcp/tool-call.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=585b769dfa2a5114b111eb901a969845 2500w" /></Frame>

<div id="images-as-context">
  ### Images comme contexte
</div>

Les serveurs MCP peuvent retourner des images — captures d’écran, schémas, etc. Retourne-les sous forme de chaînes encodées en base64 :

```js  theme={null}
const RED_CIRCLE_BASE64 = "/9j/4AAQSkZJRgABAgEASABIAAD/2w...";
// ^ base64 complet supprimé pour plus de lisibilité

server.tool("generate_image", async (params) => {
  return {
    content: [
      {
        type: "image",
        data: RED_CIRCLE_BASE64,
        mimeType: "image/jpeg",
      },
    ],
  };
});
```

Consulte cet [exemple de serveur](https://github.com/msfeldstein/mcp-test-servers/blob/main/src/image-server.js) pour les détails de l’implémentation. Cursor joint les images renvoyées à la conversation. Si le modèle prend en charge les images, il les analyse.

<div id="security-considerations">
  ## Considérations de sécurité
</div>

Quand t’installes des serveurs MCP, garde en tête ces bonnes pratiques :

* **Vérifie la source** : installe uniquement des serveurs MCP provenant de développeurs et de dépôts fiables
* **Passe en revue les autorisations** : regarde à quelles données et quelles API le serveur aura accès
* **Limite les clés API** : utilise des clés API restreintes avec le minimum d’autorisations nécessaire
* **Audit du code** : pour les intégrations critiques, examine le code source du serveur

Souviens-toi que les serveurs MCP peuvent accéder à des services externes et exécuter du code en ton nom. Assure-toi toujours de comprendre ce que fait un serveur avant de l’installer.

<div id="real-world-examples">
  ## Exemples concrets
</div>

Pour des exemples pratiques de MCP en action, consulte notre [guide de développement web](/fr/guides/tutorials/web-development), qui montre comment intégrer Linear, Figma et des outils de navigateur dans ton workflow de développement.

<div id="faq">
  ## FAQ
</div>

<AccordionGroup>
  <Accordion title="À quoi servent les serveurs MCP ?">
    Les serveurs MCP connectent Cursor à des outils externes comme Google Drive, Notion,
    et d'autres services pour intégrer des docs et des specs dans ton workflow de code.
  </Accordion>

  {" "}

  <Accordion title="Comment déboguer des problèmes de serveur MCP ?">
    Consulte les logs MCP de cette façon : 1. Ouvre le panneau Output dans Cursor (<Kbd>Cmd+Shift+U</Kbd>) 2. Sélectionne "MCP Logs" dans le menu déroulant 3. Vérifie les erreurs de connexion, les problèmes d'authentification ou les crashs serveur. Les logs affichent l'initialisation du serveur, les appels d'outils et les messages d'erreur.
  </Accordion>

  {" "}

  <Accordion title="Puis-je désactiver temporairement un serveur MCP ?">
    Oui ! Active/désactive des serveurs sans les supprimer : 1. Ouvre Settings (<Kbd>Cmd+Shift+J</Kbd>) 2. Va dans Features → Model Context Protocol 3. Clique sur le toggle à côté de n'importe quel serveur pour l'activer/désactiver. Les serveurs désactivés ne se chargent pas et n'apparaissent pas dans le chat. C'est utile pour dépanner ou réduire l'encombrement des outils.
  </Accordion>

  {" "}

  <Accordion title="Que se passe-t-il si un serveur MCP plante ou expire ?">
    Si un serveur MCP échoue : Cursor affiche un message d'erreur dans le chat. L'appel d'outil est marqué comme échoué. Tu peux réessayer l'opération ou consulter les logs pour plus de détails. Les autres serveurs MCP continuent de fonctionner normalement. Cursor isole les échecs des serveurs pour éviter qu'un serveur n'affecte les autres.
  </Accordion>

  {" "}

  <Accordion title="Comment mettre à jour un serveur MCP ?">
    Pour les serveurs basés sur npm : 1. Supprime le serveur dans les paramètres 2. Vide le cache npm : `npm cache clean --force` 3. Ajoute à nouveau le serveur pour obtenir la dernière version. Pour les serveurs custom, mets à jour tes fichiers locaux et redémarre Cursor.
  </Accordion>

  <Accordion title="Puis-je utiliser des serveurs MCP avec des données sensibles ?">
    Oui, mais suis les bonnes pratiques de sécu : utilise des variables d'environnement pour les secrets, ne les hard-code jamais ; exécute les serveurs sensibles en local avec le transport `stdio` ; limite les permissions des clés API au strict nécessaire ; passe en revue le code du serveur avant de le connecter à des systèmes sensibles ; et envisage d'exécuter les serveurs dans des environnements isolés.
  </Accordion>
</AccordionGroup>

---

← Previous: [Ignorer des fichiers](./ignorer-des-fichiers.md) | [Index](./index.md) | Next: [Memories](./memories.md) →