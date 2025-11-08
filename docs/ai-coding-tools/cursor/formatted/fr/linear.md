---
title: "Linear"
source: "https://docs.cursor.com/fr/integrations/linear"
language: "fr"
language_name: "French"
---

# Linear
Source: https://docs.cursor.com/fr/integrations/linear

Utilise des Background Agents depuis Linear

Utilise les [Background Agents](/fr/background-agent) directement depuis Linear en déléguant des tickets à Cursor ou en mentionnant `@Cursor` dans les commentaires.

<Frame>
  <video src="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-agent.mp4?fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=ac4bacf6bf42c541f45325ba72f8c25f" controls autoPlay muted loop playsInline data-path="images/integrations/linear/linear-agent.mp4" />
</Frame>

<div id="get-started">
  ## Pour commencer
</div>

<div id="installation">
  ### Installation
</div>

<Note>
  Tu dois être admin Cursor pour connecter l’intégration Linear. D’autres réglages d’équipe sont disponibles pour les membres non admins.
</Note>

1. Va sur [Cursor integrations](https://www.cursor.com/en/dashboard?tab=integrations)
2. Clique sur *Connect* à côté de Linear
3. Connecte ton espace de travail Linear et sélectionne l’équipe
4. Clique sur *Authorize*
5. Termine la configuration restante de Background Agent dans Cursor :
   * Connecte GitHub et sélectionne le dépôt par défaut
   * Active la tarification à l’usage
   * Confirme les paramètres de confidentialité

<div id="account-linking">
  ### Association de compte
</div>

La première utilisation déclenche l’association de compte entre Cursor et Linear. Connexion à GitHub requise pour créer des PR.

<div id="how-to-use">
  ## Comment l’utiliser
</div>

Délègue des tickets à Cursor ou mentionne `@Cursor` dans les commentaires. Cursor analyse les tickets et filtre automatiquement les tâches non liées au développement.

<div id="delegating-issues">
  ### Déléguer des tickets
</div>

1. Ouvre le ticket Linear
2. Clique sur le champ d’assignation
3. Sélectionne « Cursor »

<Frame>
  <img src="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-delegate.png?fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=c9a6536a083cfe4a7798c626360e53cc" alt="Déléguer un ticket à Cursor dans Linear" data-og-width="1637" width="1637" data-og-height="1046" height="1046" data-path="images/integrations/linear/linear-delegate.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-delegate.png?w=280&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=b30e2ccb68c4a15b921cf86721878676 280w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-delegate.png?w=560&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=1ac5dfd75e06451de0e688ff87e1ce4c 560w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-delegate.png?w=840&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=7393e80c07e1fe5c33690a970029fe31 840w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-delegate.png?w=1100&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=2a07cc74a1d65581a341cf2225b51a37 1100w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-delegate.png?w=1650&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=5684841fe823ef85472f74748730278c 1650w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-delegate.png?w=2500&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=9f7818cae47a652e14557eb20f20b04e 2500w" />
</Frame>

<div id="mentioning-cursor">
  ### Mentionner Cursor
</div>

Mentionne `@Cursor` dans un commentaire pour créer un nouvel agent ou fournir des instructions supplémentaires, par exemple : `@Cursor corrige le bug d’authentification décrit ci-dessus`.

<div id="workflow">
  ## Flux de travail
</div>

Les Background Agents affichent leur statut en temps réel dans Linear et créent des PR automatiquement une fois terminés. Suis l’avancement dans le [dashboard Cursor](https://www.cursor.com/dashboard?tab=background-agents).

<Frame>
  <img src="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-activity.png?fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=eecf562be6db4d44c397f4786b8ef273" alt="Mises à jour de statut des Background Agents dans Linear" data-og-width="3456" width="3456" data-og-height="2158" height="2158" data-path="images/integrations/linear/linear-activity.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-activity.png?w=280&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=238da245aee71392f22644cb85f7cee4 280w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-activity.png?w=560&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=e21f515fbd2e5917fcf63b8801f66307 560w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-activity.png?w=840&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=9f88441301e6d614ba47756cb886e023 840w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-activity.png?w=1100&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=4927a8d00768a3dbbc0bd5be1faad80e 1100w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-activity.png?w=1650&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=1707f8223126480c46639428ad5fc85a 1650w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-activity.png?w=2500&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=74ca2ad37e8158bbb86188821bf96299 2500w" />
</Frame>

<div id="follow-up-instructions">
  ### Instructions de suivi
</div>

Tu peux répondre dans la session de l’agent et ton message sera envoyé comme suivi à l’agent. Mentionne simplement `@Cursor` dans un commentaire Linear pour donner des indications supplémentaires à un Background Agent en cours d’exécution.

<div id="configuration">
  ## Configuration
</div>

Configure les paramètres de Background Agents depuis [Dashboard → Background Agents](https://www.cursor.com/dashboard?tab=background-agents).

<div className="full-width-table">
  | Paramètre             | Emplacement      | Description                                                                  |
  | :-------------------- | :--------------- | :--------------------------------------------------------------------------- |
  | **Dépôt par défaut**  | Cursor Dashboard | Dépôt principal lorsqu’aucun dépôt de projet n’est configuré                 |
  | **Modèle par défaut** | Cursor Dashboard | Modèle d’IA pour les Background Agents                                       |
  | **Branche de base**   | Cursor Dashboard | Branche à partir de laquelle créer les PR (généralement `main` ou `develop`) |
</div>

<div id="configuration-options">
  ### Options de configuration
</div>

Tu peux configurer le comportement de Background Agents via plusieurs méthodes :

**Description de l’issue ou commentaires** : utilise la syntaxe `[key=value]`, par exemple :

* `@cursor please fix [repo=anysphere/everysphere]`
* `@cursor implement feature [model=claude-3.5-sonnet] [branch=feature-branch]`

**Labels d’issue** : utilise une structure parent-enfant où le label parent est la clé de configuration et le label enfant est la valeur.

**Labels de projet** : même structure parent-enfant que les labels d’issue, appliquée au niveau du projet.

Clés de configuration prises en charge :

* `repo` : spécifie le dépôt cible (p. ex. `owner/repository`)
* `branch` : spécifie la branche de base pour la création de PR
* `model` : spécifie le modèle d’IA à utiliser

<div id="repository-selection">
  ### Sélection du dépôt
</div>

Cursor détermine sur quel dépôt travailler selon cet ordre de priorité :

1. **Description/commentaires de l’issue** : syntaxe `[repo=owner/repository]` dans le texte de l’issue ou les commentaires
2. **Labels d’issue** : labels de dépôt attachés à l’issue Linear concernée
3. **Labels de projet** : labels de dépôt attachés au projet Linear
4. **Dépôt par défaut** : dépôt spécifié dans les paramètres du dashboard Cursor

<div id="setting-up-repository-labels">
  #### Configuration des labels de dépôt
</div>

Pour créer des labels de dépôt dans Linear :

1. Va dans **Settings** de ton workspace Linear
2. Clique sur **Labels**
3. Clique sur **New group**
4. Nomme le groupe "repo" (insensible à la casse — doit être exactement "repo", pas "Repository" ni d’autres variantes)
5. Dans ce groupe, crée des labels pour chaque dépôt au format `owner/repo`

Ces labels peuvent ensuite être assignés aux issues ou aux projets pour indiquer sur quel dépôt les Background Agents doivent travailler.

<Frame>
  <img src="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-project-labels.png?fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=6e2b90ce09957a72fdef3c1ed4ef93aa" alt="Configuration des labels de dépôt dans Linear" data-og-width="3456" width="3456" data-og-height="2158" height="2158" data-path="images/integrations/linear/linear-project-labels.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-project-labels.png?w=280&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=1933d2112631527116bd1d817f1a6153 280w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-project-labels.png?w=560&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=93f344ff848172ce6bd97ef652ab03de 560w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-project-labels.png?w=840&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=ea9f19d7248f39086a20606c6ec14ac6 840w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-project-labels.png?w=1100&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=55bfa5cf5b87def6cbe51c3345579eee 1100w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-project-labels.png?w=1650&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=d99c0f06c5fbf33794408350b143f655 1650w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-project-labels.png?w=2500&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=b1f731d1978dc5e60c545b745bb9d8ad 2500w" />
</Frame>

{/* ### Getting help

  Check [agent activity](https://www.cursor.com/dashboard?tab=background-agents) and include request IDs when contacting support.

  ## Feedback

  Share feedback through Linear comments or your Cursor dashboard support channels. */}

---

← Previous: [GitHub](./github.md) | [Index](./index.md) | Next: [Slack](./slack.md) →