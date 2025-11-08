---
title: "Problèmes courants"
source: "https://docs.cursor.com/fr/troubleshooting/common-issues"
language: "fr"
language_name: "French"
---

# Problèmes courants
Source: https://docs.cursor.com/fr/troubleshooting/common-issues

Solutions aux problèmes fréquents et FAQ

Voici les problèmes courants et leurs solutions.

<div id="networking-issues">
  ### Problèmes réseau
</div>

Commence par vérifier ta connectivité réseau. Va dans `Cursor Settings` > `Network` et clique sur `Run Diagnostics`. Ça testera ta connexion aux serveurs de Cursor et aidera à identifier tout problème réseau pouvant affecter les fonctionnalités d'IA, les mises à jour ou d'autres fonctions en ligne.

Cursor s'appuie sur HTTP/2 pour les fonctionnalités d'IA, car il gère efficacement les réponses en streaming. Si ton réseau ne prend pas en charge HTTP/2, tu peux rencontrer des échecs d'indexation et des problèmes avec les fonctionnalités d'IA.

Ça arrive sur les réseaux d'entreprise, via des VPN, ou quand tu utilises des proxys comme Zscaler.

Pour résoudre ça, active le repli en HTTP/1.1 dans les paramètres de l'app (pas dans les paramètres de Cursor) : appuie sur `CMD/CTRL + ,`, cherche `HTTP/2`, puis active `Disable HTTP/2`. Ça force l'utilisation de HTTP/1.1 et règle le problème.

On prévoit d'ajouter une détection et un repli automatiques.

<div id="resource-issues-cpu-ram-etc">
  ### Problèmes de ressources (CPU, RAM, etc.)
</div>

Une forte utilisation du CPU ou de la RAM peut ralentir ta machine ou déclencher des alertes de ressources.

Même si les grands codebases nécessitent plus de ressources, une utilisation élevée provient généralement des extensions ou de certains réglages.

<Note>
  Si tu vois un avertissement de faible RAM sur **macOS**, sache qu'il existe un bug chez certains utilisateurs qui peut afficher des valeurs totalement incorrectes. Si tu vois ça, ouvre Moniteur d’activité et regarde l’onglet « Memory » pour voir l'utilisation réelle de la mémoire.
</Note>

Si tu constates une forte utilisation du CPU ou de la RAM, essaie ces étapes :

<AccordionGroup>
  <Accordion title="Vérifie tes extensions">
    Les extensions peuvent impacter les performances.

    L’Extension Monitor affiche la consommation de ressources de toutes tes extensions installées et intégrées.

    Active l’Extension Monitor depuis `Settings` > `Application` > `Experimental` et bascule `Extension Monitor: Enabled`. Tu devras redémarrer Cursor.

    Ouvre-le : `Cmd/Ctrl + Shift + P` → `Developer: Open Extension Monitor`.

    Cursor exécute tes extensions dans un ou plusieurs **extension hosts**. En général, la plupart de tes extensions s’exécutent dans le même extension host, ce qui signifie qu’une extension qui consomme beaucoup de temps CPU peut étouffer ses voisines !

    L’Extension Monitor affiche :

    * Chaque processus de longue durée lancé par une extension (macOS et Linux uniquement).
    * **% Ext Host** : le pourcentage du temps total de l’extension host consommé par cette extension. Aide à identifier quelles extensions utilisent le plus de temps par rapport aux autres.
    * **Max Blocking** : le plus long blocage continu d’une extension, par intervalle de surveillance.
    * **% CPU** :
      * Pour les extensions : le pourcentage de l’utilisation CPU totale attribuée au code de l’extension.
      * Pour les processus : le pourcentage de l’utilisation CPU totale attribuée au processus lancé (macOS et Linux uniquement).
    * **Memory** :
      * Pour les extensions : la quantité de mémoire de tas JS utilisée par le code de l’extension (allocations externes non comptabilisées).
      * Pour les processus : la quantité de mémoire système utilisée par le processus lancé (macOS et Linux uniquement).

    Tu peux aussi tester en lançant `cursor --disable-extensions` depuis la ligne de commande. Si les performances s’améliorent, réactive les extensions une par une pour trouver celles qui posent problème.

    Essaie Extension Bisect pour identifier les extensions problématiques. En savoir plus [ici](https://code.visualstudio.com/blogs/2021/02/16/extension-bisect#_welcome-extension-bisect). Remarque : ça marche mieux pour les problèmes immédiats, pas pour une dégradation progressive des performances.
  </Accordion>

  <Accordion title="Utilise le Process Explorer">
    Le Process Explorer montre quels processus consomment des ressources.

    Ouvre-le : Command Palette (`Cmd/Ctrl + Shift + P`) → `Developer: Open Process Explorer`.

    Examine les processus suivants :

    * **`extensionHost`** : problèmes liés aux extensions
    * **`ptyHost`** : consommation de ressources du terminal

    Le Process Explorer affiche chaque terminal et ses commandes en cours d’exécution pour le diagnostic.

    Pour les autres processus très gourmands, rapporte-les sur le [forum](https://forum.cursor.com/).
  </Accordion>

  <Accordion title="Surveille les ressources système">
    Utilise les outils de monitoring de ton système d’exploitation pour déterminer si le problème est spécifique à Cursor ou global au système.
  </Accordion>

  <Accordion title="Teste une installation minimale">
    Si les problèmes persistent, teste une installation minimale de Cursor.
  </Accordion>
</AccordionGroup>

<div id="general-faqs">
  ## FAQ générales
</div>

<AccordionGroup>
  <Accordion title="Je vois une mise à jour dans le changelog mais Cursor ne se met pas à jour">
    Les nouvelles versions sont déployées progressivement — des utilisateurs choisis aléatoirement les reçoivent en premier. Ta mise à jour devrait arriver d'ici quelques jours.
  </Accordion>

  <Accordion title="J'ai des problèmes avec ma connexion GitHub dans Cursor / Comment me déconnecter de GitHub dans Cursor ?">
    Utilise `Sign Out of GitHub` depuis la palette de commandes `Ctrl/⌘ + Shift + P`.
  </Accordion>

  <Accordion title="Je ne peux pas utiliser GitHub Codespaces">
    GitHub Codespaces n'est pas encore pris en charge.
  </Accordion>

  <Accordion title="J'ai des erreurs lors de la connexion à Remote SSH">
    La connexion SSH aux machines Mac ou Windows n'est pas prise en charge. Pour d'autres problèmes, signale-les sur le [forum](https://forum.cursor.com/) avec des logs.
  </Accordion>

  <Accordion title="Problèmes de connexion SSH sur Windows">
    Si tu vois "SSH is only supported in Microsoft versions of VS Code":

    1. Désinstalle Remote-SSH :
       * Ouvre la vue Extensions (`Ctrl + Shift + X`)
       * Cherche "Remote-SSH"
       * Clique sur l'icône d'engrenage → "Uninstall"

    2. Installe Anysphere Remote SSH :

    * Ouvre le marketplace de Cursor
    * Cherche "SSH"
    * Installe l'extension Anysphere Remote SSH

    3. Après l'installation :

    * Ferme toutes les instances de VS Code avec des connexions SSH actives
    * Redémarre Cursor
    * Reconnecte-toi via SSH

    Vérifie que ta configuration SSH et tes clés sont correctement configurées.
  </Accordion>

  <Accordion title="Cursor Tab et Inline Edit ne fonctionnent pas derrière mon proxy d'entreprise">
    Cursor Tab et Inline Edit utilisent HTTP/2 pour réduire la latence et l'utilisation des ressources. Certains proxies d'entreprise (p. ex. Zscaler) bloquent HTTP/2. Corrige en définissant `"cursor.general.disableHttp2": true` dans les paramètres (`Cmd/Ctrl + ,`, recherche `http2`).
  </Accordion>

  <Accordion title="Je viens de m'abonner à Pro mais je suis toujours sur le plan gratuit dans l'app">
    Déconnecte-toi puis reconnecte-toi depuis les paramètres de Cursor.
  </Accordion>

  <Accordion title="Quand mon utilisation sera-t-elle réinitialisée ?">
    Abonné·e Pro : Clique sur `Manage Subscription` dans le [Dashboard](https://cursor.com/dashboard) pour voir ta date de renouvellement.

    Utilisateur·rice gratuit·e : Vérifie la date de ton premier email de Cursor. L'utilisation est réinitialisée chaque mois à partir de cette date.
  </Accordion>

  <Accordion title="L'historique Chat/Composer a disparu après une mise à jour">
    Un espace disque insuffisant peut amener Cursor à effacer des données historiques lors des mises à jour. Pour éviter ça :

    1. Garde suffisamment d'espace disque libre avant les mises à jour
    2. Nettoie régulièrement les fichiers système inutiles
    3. Sauvegarde les conversations importantes avant de mettre à jour
  </Accordion>

  <Accordion title="Comment désinstaller Cursor ?">
    Suis [ce guide](https://code.visualstudio.com/docs/setup/uninstall). Remplace "VS Code" ou "Code" par "Cursor", et ".vscode" par ".cursor".
  </Accordion>

  <Accordion title="Comment supprimer mon compte ?">
    Clique sur `Delete Account` dans le [Dashboard](https://cursor.com/dashboard). Ça supprime définitivement ton compte et toutes les données associées.
  </Accordion>

  <Accordion title="Comment ouvrir Cursor depuis la ligne de commande ?">
    Exécute `cursor` dans ton terminal. Si la commande est absente :

    1. Ouvre la palette de commandes `⌘⇧P`
    2. Tape `install command`
    3. Sélectionne `Install 'cursor' command` (tu peux aussi installer la commande `code` pour remplacer celle de VS Code)
  </Accordion>

  <Accordion title="Impossible de se connecter à Cursor">
    Si cliquer sur Sign In te redirige vers cursor.com sans te connecter, désactive ton pare-feu ou ton antivirus — ils peuvent bloquer le processus d'authentification.
  </Accordion>

  <Accordion title="Message d'activité suspecte">
    Suite à une récente augmentation des abus, ta requête a pu être bloquée par mesure de sécurité. Voici comment résoudre ça :

    D'abord, vérifie ton VPN. Si tu en utilises un, essaie de le désactiver, car les VPN peuvent parfois déclencher nos systèmes de sécurité.

    Si ça ne résout pas le problème, tu peux essayer :

    * Créer un nouveau chat
    * Attendre un peu et réessayer plus tard
    * Créer un nouveau compte en utilisant l'authentification Google ou GitHub
    * Passer à Cursor Pro
  </Accordion>
</AccordionGroup>

---

← Previous: [Serveurs MCP](./serveurs-mcp.md) | [Index](./index.md) | Next: [Récupérer un ID de requête](./rcuprer-un-id-de-requte.md) →