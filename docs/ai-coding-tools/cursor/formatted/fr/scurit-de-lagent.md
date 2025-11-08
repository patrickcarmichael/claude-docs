---
title: "Sécurité de l’agent"
source: "https://docs.cursor.com/fr/account/agent-security"
language: "fr"
language_name: "French"
---

# Sécurité de l’agent
Source: https://docs.cursor.com/fr/account/agent-security

Considérations de sécurité pour l’utilisation de Cursor Agent

Les attaques par injection de prompt, les hallucinations de l’IA et d’autres problèmes peuvent amener une IA à se comporter de manière inattendue et potentiellement malveillante. Pendant qu’on continue de travailler à résoudre l’injection de prompt à un niveau plus fondamental, notre protection principale dans les produits Cursor repose sur des garde-fous autour de ce qu’un agent peut faire, notamment l’exigence, activée par défaut, d’une approbation manuelle pour les actions sensibles. L’objectif de ce document est d’expliquer ces garde-fous et ce à quoi tu peux t’attendre.

Tous les contrôles et comportements ci-dessous correspondent à nos paramètres par défaut et recommandés.

<div id="first-party-tool-calls">
  ## Appels d’outils first‑party
</div>

Cursor est livré avec des outils qui permettent à l’agent d’aider nos utilisateurs à écrire du code. Ceux‑ci incluent la lecture de fichiers, les modifications, l’exécution de commandes dans le terminal, la recherche de documentation sur le web, et d’autres.

Les outils de lecture ne nécessitent pas d’approbation (c.-à-d. lecture de fichiers, recherche dans le code). Les utilisateurs peuvent utiliser [.cursorignore](/fr/context/ignore-files) pour empêcher l’agent d’accéder à des fichiers spécifiques, mais sinon les lectures sont généralement autorisées sans approbation. Pour les actions présentant un risque d’exfiltration de données sensibles, nous exigeons une approbation explicite.

La modification de fichiers dans l’espace de travail actuel ne nécessite pas d’approbation explicite, avec quelques exceptions. Quand un agent modifie des fichiers, ils sont immédiatement enregistrés sur le disque. Nous recommandons d’exécuter Cursor dans des espaces de travail sous contrôle de version, afin que le contenu des fichiers puisse être rétabli à tout moment. Nous exigeons une approbation explicite avant de modifier des fichiers qui changent la configuration de notre IDE/CLI, comme le fichier de paramètres de l’éditeur pour l’espace de travail. Cependant, les utilisateurs dont l’application se recharge automatiquement à la modification de fichiers doivent savoir que les changements de l’agent peuvent déclencher une exécution automatique avant qu’ils aient eu la chance de les revoir.

Toute commande de terminal suggérée par les agents nécessite une approbation par défaut. Nous recommandons que les utilisateurs relisent chaque commande avant que l’agent ne l’exécute. Les utilisateurs qui acceptent le risque peuvent choisir d’autoriser l’agent à exécuter toutes les commandes sans approbation. Nous incluons une fonctionnalité d’[allowlist](/fr/agent/tools) dans Cursor, mais nous ne la considérons pas comme un contrôle de sécurité. Certains utilisateurs choisissent d’autoriser des commandes spécifiques, mais c’est un système best effort et des contournements restent possibles. Nous ne recommandons pas « Run Everything », qui contourne toute allowlist configurée.

<div id="third-party-tool-calls">
  ## Appels d’outils tiers
</div>

Cursor permet de connecter des outils externes via le [MCP](/fr/context/mcp). Toutes les connexions MCP tierces doivent être explicitement approuvées par l’utilisateur. Une fois qu’un utilisateur a approuvé un MCP, par défaut chaque appel d’outil suggéré en mode Agent pour chaque intégration MCP externe doit être explicitement approuvé avant exécution.

<div id="network-requests">
  ## Requêtes réseau
</div>

Des requêtes réseau peuvent être utilisées par un attaquant pour exfiltrer des données. À l’heure actuelle, nous ne prenons pas en charge d’outils propriétaires effectuant des requêtes réseau en dehors d’un ensemble très restreint d’hôtes (par ex. GitHub), de la récupération explicite de liens, ni de la recherche web qu’avec un nombre limité de fournisseurs. Les requêtes réseau arbitraires des agents sont bloquées avec les paramètres par défaut.

<div id="workspace-trust">
  ## Confiance de l’espace de travail
</div>

L’IDE Cursor prend en charge la fonctionnalité standard de [confiance de l’espace de travail](https://code.visualstudio.com/docs/editing/workspaces/workspace-trust), qui est désactivée par défaut. À l’ouverture d’un nouvel espace de travail, une invite te propose de choisir entre le mode normal ou le mode restreint. Le mode restreint désactive l’IA et d’autres fonctionnalités pour lesquelles les gens utilisent généralement Cursor. On recommande d’utiliser d’autres outils, comme un éditeur de texte simple, pour travailler avec des dépôts auxquels tu ne fais pas confiance.

Tu peux activer la confiance de l’espace de travail dans tes paramètres en suivant ces étapes :

1. Ouvre ton fichier user settings.json
2. Ajoute la configuration suivante :
   ```json  theme={null}
   "security.workspace.trust.enabled": true
   ```

Ce paramètre peut aussi être imposé à l’échelle de l’organisation via des solutions de Mobile Device Management (MDM).

<div id="responsible-disclosure">
  ## Divulgation responsable
</div>

Si tu penses avoir trouvé une vulnérabilité dans Cursor, suis le guide sur notre page GitHub Security et dépose ton rapport là-bas. Si tu peux pas utiliser GitHub, écris-nous aussi à [security@cursor.com](mailto:security@cursor.com).

On s’engage à accuser réception des signalements de vulnérabilité sous 5 jours ouvrables et à les traiter dès qu’on le peut. On publiera les résultats sous forme d’avis de sécurité sur notre page GitHub Security. Les incidents critiques seront communiqués à la fois sur la page GitHub Security et par e‑mail à tous les utilisateurs.

---

← Previous: [Index](./index.md) | [Index](./index.md) | Next: [Facturation](./facturation.md) →