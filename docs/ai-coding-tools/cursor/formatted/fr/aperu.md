---
title: "Aperçu"
source: "https://docs.cursor.com/fr/background-agent/api/overview"
language: "fr"
language_name: "French"
---

# Aperçu
Source: https://docs.cursor.com/fr/background-agent/api/overview

Crée et gère par programmation des agents en arrière-plan qui travaillent sur tes dépôts

<div id="background-agents-api">
  # API des Background Agents
</div>

<Badge variant="beta">Bêta</Badge>

L'API des Background Agents te permet de créer et de gérer par code des agents de programmation alimentés par l’IA, qui travaillent de façon autonome sur tes dépôts.
Tu peux utiliser l’API pour répondre automatiquement aux retours utilisateurs, corriger des bugs, mettre à jour la doc, et bien plus encore !

<Info>
  L’API des Background Agents est actuellement en bêta, on adorerait avoir ton retour !
</Info>

<div id="key-features">
  ## Fonctionnalités clés
</div>

* **Génération de code autonome** - Crée des agents qui comprennent ton prompt et apportent des modifications à ton codebase
* **Intégration aux dépôts** - Travaille directement avec des dépôts GitHub
* Prompts de suivi - Ajoute des instructions supplémentaires aux agents en cours d’exécution
* **Tarification à l’usage** - Ne paie que pour les tokens que tu utilises
* **Scalabilité** - Prise en charge de jusqu’à 256 agents actifs par clé d’API

<div id="quick-start">
  ## Démarrage rapide
</div>

<div id="1-get-your-api-key">
  ### 1. Récupère ta clé d’API
</div>

**Va** sur [Cursor Dashboard → Integrations](https://cursor.com/dashboard?tab=integrations) pour créer ta clé d’API.

<div id="2-start-using-the-api">
  ### 2. Commence à utiliser l’API
</div>

Tous les points de terminaison de l’API sont relatifs à :

```
https://api.cursor.com
```

Consulte la [référence de l’API](/fr/background-agent/api/launch-an-agent) pour la liste détaillée des points de terminaison.

<div id="authentication">
  ## Authentification
</div>

Toutes les requêtes à l’API nécessitent une authentification avec un jeton Bearer :

```
Authorization: Bearer VOTRE_CLEF_API
```

Les clés API sont créées dans le [tableau de bord Cursor](https://cursor.com/dashboard?tab=integrations). Elles sont propres à ton compte et te permettent de créer et de gérer des agents (dans les limites de ton abonnement et selon les accès à tes dépôts).

<div id="pricing">
  ## Tarification
</div>

L’API est actuellement en bêta avec la même tarification que les Background Agents. Les prix peuvent évoluer à mesure qu’on fait monter le service en charge. Voir la [tarification des Background Agents](/fr/account/pricing#background-agent).

<div id="next-steps">
  ## Prochaines étapes
</div>

* Lis la [présentation de Background Agents](/fr/background-agent) pour comprendre les environnements, les autorisations et les workflows.
* Essaie Background Agents sur le [web et mobile](/fr/background-agent/web-and-mobile).
* Rejoins la discussion sur [Discord #background-agent](https://discord.gg/jfgpZtYpmb) ou envoie un e-mail à [background-agent-feedback@cursor.com](mailto:background-agent-feedback@cursor.com).

---

← Previous: [Lister les dépôts GitHub](./lister-les-dpts-github.md) | [Index](./index.md) | Next: [Webhooks](./webhooks.md) →