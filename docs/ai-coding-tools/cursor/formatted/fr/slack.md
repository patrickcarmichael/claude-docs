---
title: "Slack"
source: "https://docs.cursor.com/fr/integrations/slack"
language: "fr"
language_name: "French"
---

# Slack
Source: https://docs.cursor.com/fr/integrations/slack

Utiliser les Background Agents depuis Slack

export const SlackThread = ({messages = []}) => {
  const MessageWithMentions = ({text}) => {
    const parts = text.split(/(@\w+)/g);
    return <>
        {parts.map((part, index) => {
      if (part.startsWith('@')) {
        return <span key={index} className="text-[#1264A3] bg-[#1264A3]/10 dark:bg-[#1264A3]/25 px-0.5 py-0.5 rounded hover:bg-[#1264A3]/20 cursor-pointer transition-colors">
                {part}
              </span>;
      }
      return <span key={index}>{part}</span>;
    })}
      </>;
  };
  return <div className="border border-neutral-200 dark:border-neutral-700 rounded-lg bg-neutral-50 dark:bg-neutral-900/50 py-4 overflow-hidden">
      {messages.map((msg, index) => <div key={index} className={`group hover:bg-[#f0f0f0] dark:hover:bg-[#333] px-6 py-2 -mx-2 -my-1 transition-colors`}>
          <div className="flex items-start gap-3">
            <div className="w-9 h-9 rounded-md bg-neutral-300 dark:bg-neutral-800 flex items-center justify-center text-white text-sm font-semibold flex-shrink-0">
              {msg.name ? msg.name.charAt(0).toUpperCase() : 'U'}
            </div>

            <div className="flex-1 min-w-0">
              <div className="flex items-baseline gap-2">
                <span className="font-semibold text-neutral-900 dark:text-neutral-100 text-sm">
                  {msg.name || 'User'}
                </span>
                <span className="text-xs text-neutral-500 dark:text-neutral-400">
                  {msg.timestamp || ''}
                </span>
              </div>
              <div className="text-neutral-900 dark:text-neutral-100 text-[15px] leading-relaxed">
                <MessageWithMentions text={msg.message} />
              </div>

              {msg.reactions && msg.reactions.length > 0 && <div className="flex gap-1 mt-1">
                  {msg.reactions.map((reaction, rIndex) => <div key={rIndex} className="inline-flex items-center gap-0.5 px-1.5 py-0.5 bg-white dark:bg-neutral-800 border border-neutral-200 dark:border-neutral-700 rounded text-xs hover:bg-neutral-100 dark:hover:bg-neutral-700 transition-colors cursor-pointer">
                      <span>{reaction.emoji}</span>
                      <span className="text-neutral-600 dark:text-neutral-400">{reaction.count}</span>
                    </div>)}
                </div>}
            </div>
          </div>
        </div>)}
    </div>;
};

export const SlackInlineMessage = ({message}) => {
  const MessageWithMentions = ({text}) => {
    const parts = text.split(/(@\w+)/g);
    return <>
        {parts.map((part, index) => {
      if (part.startsWith('@')) {
        return <span key={index} className="text-[#1264A3] hover:bg-[#1264A3]/10 dark:hover:bg-[#1264A3]/25 px-0.5 rounded">
                {part}
              </span>;
      }
      return <span key={index}>{part}</span>;
    })}
      </>;
  };
  return <span className="inline rounded p-0.5 bg-neutral-50 dark:bg-neutral-800/30">
      <MessageWithMentions text={message} />
    </span>;
};

export const SlackUserMessage = ({message, reactions = [], replies = null}) => {
  const MessageWithMentions = ({text}) => {
    const parts = text.split(/(@\w+)/g);
    return <>
        {parts.map((part, index) => {
      if (part.startsWith('@')) {
        return <span key={index} className="text-[#1264A3] bg-[#1264A3]/10 dark:bg-[#1264A3]/25 px-0.5 py-0.5 rounded hover:bg-[#1264A3]/20 cursor-pointer transition-colors">
                {part}
              </span>;
      }
      return <span key={index}>{part}</span>;
    })}
      </>;
  };
  return <div className="border border-neutral-200 dark:border-neutral-700 rounded-lg hover:bg-neutral-50 dark:hover:bg-neutral-800/50 transition-colors px-5 py-3 group">
      <div className="text-neutral-900 dark:text-neutral-100 text-[15px] leading-relaxed">
        <MessageWithMentions text={message} />
      </div>

      {reactions.length > 0 && <div className="flex gap-1 mt-1">
          {reactions.map((reaction, index) => <div key={index} className="inline-flex items-center gap-0.5 px-1.5 py-0.5 bg-neutral-100 dark:bg-neutral-800 rounded text-xs hover:bg-neutral-200 dark:hover:bg-neutral-700 transition-colors cursor-pointer">
              <span>{reaction.emoji}</span>
              <span className="text-neutral-600 dark:text-neutral-400">{reaction.count}</span>
            </div>)}
        </div>}

      {replies && <div className="flex items-center gap-1.5 mt-2 text-[#1264A3] hover:underline cursor-pointer">
          <svg className="w-4 h-4" fill="currentColor" viewBox="0 0 20 20">
            <path d="M7.707 10.293a1 1 0 10-1.414 1.414l3 3a1 1 0 001.414 0l3-3a1 1 0 00-1.414-1.414L11 11.586V6h5a2 2 0 012 2v7a2 2 0 01-2 2H4a2 2 0 01-2-2V8a2 2 0 012-2h5v5.586l-1.293-1.293z" />
          </svg>
          <span className="text-sm font-medium">{replies.count} {replies.count === 1 ? 'reply' : 'replies'}</span>
          {replies.lastReplyTime && <span className="text-xs text-neutral-500 dark:text-neutral-400">{replies.lastReplyTime}</span>}
        </div>}
    </div>;
};

Avec l’intégration de Cursor pour Slack, tu peux utiliser les [Background Agents](/fr/background-agent) pour bosser sur tes tâches directement depuis Slack en mentionnant <SlackInlineMessage message="@Cursor" /> avec un prompt.

<Frame>
  <video src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-agent.mp4?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=aa7aa2681db1e363047334c6a8e33f72" controls autoplay muted loop data-path="images/background-agent/slack/slack-agent.mp4" />
</Frame>

<div id="get-started">
  ## Bien démarrer
</div>

<div id="installation">
  ### Installation
</div>

1. Va sur [Cursor integrations](https://www.cursor.com/en/dashboard?tab=integrations)

2. Clique sur *Connect* à côté de Slack ou ouvre la [page d’installation](https://cursor.com/api/install-slack-app) depuis ici

3. On te demandera d’installer l’app Cursor pour Slack dans ton espace de travail.

4. Après l’installation dans Slack, tu seras redirigé vers Cursor pour finaliser la configuration

   1. Connecte GitHub (si ce n’est pas déjà fait) et choisis un dépôt par défaut
   2. Active la tarification à l’usage
   3. Confirme les paramètres de confidentialité

5. Commence à utiliser les Background Agents dans Slack en mentionnant <SlackInlineMessage message="@Cursor" />

<Frame>
  <video src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/cursor-slack-install.mp4?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=bd5b3c65b1a0de08b46c90515b6056a6" controls autoplay muted loop data-path="images/background-agent/slack/cursor-slack-install.mp4" />
</Frame>

<div id="how-to-use">
  ## Comment utiliser
</div>

Mentionne <SlackInlineMessage message="@Cursor" /> et donne ton prompt. Ça couvre la plupart des cas d’usage, mais tu peux aussi utiliser les commandes ci-dessous pour personnaliser ton agent.

Par exemple, mentionne <SlackInlineMessage message="@Cursor fix the login bug" /> directement dans la conversation, ou utilise des commandes spécifiques comme <SlackInlineMessage message="@Cursor [repo=torvalds/linux] fix bug" /> pour cibler un dépôt particulier.

<div id="commands">
  ### Commandes
</div>

Lance <SlackInlineMessage message="@Cursor help" /> pour obtenir la liste de commandes à jour.

<div className="full-width-table">
  | Commande                                                    | Description                                                                                            |
  | :---------------------------------------------------------- | :----------------------------------------------------------------------------------------------------- |
  | <SlackInlineMessage message="@Cursor [prompt]" />           | Démarre un Background Agent. Dans les fils avec des agents existants, ajoute des instructions de suivi |
  | <SlackInlineMessage message="@Cursor settings" />           | Configure les paramètres par défaut et le dépôt par défaut du canal                                    |
  | <SlackInlineMessage message="@Cursor [options] [prompt]" /> | Utilise des options avancées : `branch`, `model`, `repo`                                               |
  | <SlackInlineMessage message="@Cursor agent [prompt]" />     | Force la création d’un nouvel agent dans un fil                                                        |
  | <SlackInlineMessage message="@Cursor list my agents" />     | Affiche tes agents en cours d’exécution                                                                |
</div>

<div id="options">
  #### Options
</div>

Personnalise le comportement du Background Agent avec ces options :

<div className="full-width-table">
  | Option   | Description                                    | Exemple           |
  | :------- | :--------------------------------------------- | :---------------- |
  | `branch` | Spécifie la branche de base                    | `branch=main`     |
  | `model`  | Choisis le modèle d’IA                         | `model=o3`        |
  | `repo`   | Cible un dépôt spécifique                      | `repo=owner/repo` |
  | `autopr` | Active/désactive la création automatique de PR | `autopr=false`    |
</div>

<div id="syntax-formats">
  ##### Formats de syntaxe
</div>

Utilise les options de plusieurs manières :

1. Format entre crochets

   <SlackInlineMessage message="@Cursor [branch=dev, model=o3, repo=owner/repo, autopr=false] Fix the login bug" />

2. Format inline
   <SlackInlineMessage message="@Cursor branch=dev model=o3 repo=owner/repo autopr=false Fix the login bug" />

<div id="option-precedence">
  ##### Priorité des options
</div>

Quand tu combines des options :

* Les valeurs explicites remplacent les valeurs par défaut
* Les valeurs plus tardives remplacent les précédentes en cas de duplication
* Les options inline priment sur les valeurs par défaut du modal de paramètres

Le bot analyse les options où qu’elles se trouvent dans le message, ce qui permet d’écrire des commandes naturellement.

<div id="using-thread-context">
  #### Utiliser le contexte du fil
</div>

Les Background Agents comprennent et utilisent le contexte des discussions existantes du fil. Pratique quand ton équipe discute d’un problème et que tu veux que l’agent implémente la solution en se basant sur cette conversation.

<SlackThread
  messages={[
{
  message:
    "Hey team, we're getting reports that users can't log in after the latest deploy",
  timestamp: "2:30 PM",
  name: "Sarah",
},
{
  message:
    "I checked the logs - looks like the auth token validation is failing on line 247 of auth.js",
  timestamp: "2:32 PM",
  name: "Mike",
},
{
  message:
    "Oh, I think it's because we changed the token format but didn't update the validation regex",
  timestamp: "2:33 PM",
  name: "Alex",
},
{
  message:
    "Yeah, the regex still expects the old format. We need to update it to handle both old and new formats for backwards compatibility",
  timestamp: "2:35 PM",
  name: "Sarah",
},
{
  message: "@Cursor fix this",
  timestamp: "2:36 PM",
  name: "You",
  reactions: [{ emoji: "⏳", count: 1 }],
},
]}
/>

<Note>
  Les Background Agents lisent l’intégralité du fil pour le contexte lors de l’invocation
  et comprennent puis implémentent des solutions en se basant sur la discussion de l’équipe.
</Note>

<div id="when-to-use-force-commands">
  #### Quand utiliser les commandes de forçage
</div>

Quand ai-je besoin de <SlackInlineMessage message="@Cursor agent" /> ?

Dans les fils avec des agents existants, <SlackInlineMessage message="@Cursor [prompt]" /> ajoute des instructions de suivi (ne fonctionne que si tu es propriétaire de l’agent). Utilise <SlackInlineMessage message="@Cursor agent [prompt]" /> pour lancer un agent distinct.

Quand ai-je besoin de Add follow-up (depuis le menu contextuel) ?

Utilise le menu contextuel (⋯) sur la réponse d’un agent pour ajouter des instructions de suivi. Pratique quand plusieurs agents existent dans un fil et que tu dois préciser lequel relancer.

<div id="status-updates-handoff">
  ### Mises à jour de statut et passation
</div>

Quand le Background Agent s’exécute, tu vois d’abord l’option Open in Cursor.

<Frame>
  <img className="p-2" src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-open-in-cursor.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=496d3775ca5cc1e20dd1dc34952f76fd" style={{ backgroundColor: "#1b1d21" }} data-og-width="1236" width="1236" data-og-height="258" height="258" data-path="images/background-agent/slack/slack-open-in-cursor.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-open-in-cursor.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=9136ecf72e3f7e75b2178a2922878fbd 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-open-in-cursor.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=5d6977f43055c3e8cb69071fe7b48367 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-open-in-cursor.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=5264cb584c1160bd8ac3cdeaae320777 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-open-in-cursor.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=a065e6c1a08d4413464e1251eab1b2a6 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-open-in-cursor.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=e067f0dc80ed77bce7843f777f2d7970 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-open-in-cursor.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=fbcb8e474fd1681219964c558ea2952d 2500w" />
</Frame>

Quand Background Agent a fini, tu reçois une notif dans Slack et tu peux ouvrir la PR créée sur GitHub.

<Frame>
  <img className="p-2" src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-view-pr.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=d0f5f15094f682a5617c936bea88db3d" style={{ backgroundColor: "#1b1d21" }} data-og-width="1272" width="1272" data-og-height="496" height="496" data-path="images/background-agent/slack/slack-view-pr.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-view-pr.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=a51c98f13fef794ba8f54a28ad42e99d 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-view-pr.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=bbde7fe552a04a8ed44b1771bbc3f55c 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-view-pr.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=616811c969184b9061435e9753f63ddb 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-view-pr.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=90fe4582797d75782019c7d0c3232ea8 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-view-pr.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=ffe4d6a78cad700f82e770418c7f6e13 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-view-pr.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=ec4dac244e5982d0150d058ddac0d205 2500w" />
</Frame>

<div id="managing-agents">
  ### Gérer les agents
</div>

Pour voir tous les agents en cours, lance <SlackInlineMessage message="@Cursor list my agents" />.

Gère les Background Agents via le menu contextuel en cliquant sur les trois points (⋯) d’un message de l’agent.

<Frame>
  <img className="p-2" src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-context-menu.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=9a92748d0f4d3450d51a2c2cdd989eb1" style={{ backgroundColor: "#1b1d21" }} data-og-width="1982" width="1982" data-og-height="1498" height="1498" data-path="images/background-agent/slack/slack-context-menu.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-context-menu.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=6af034b2f0c1b510510622b111c8d4e7 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-context-menu.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=7d28c9785328aa414eba66704d7f4f08 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-context-menu.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=810f99ed15ec100cdfee183ef9b7f827 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-context-menu.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=f4c00c380996793b50d31ef3ac95219c 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-context-menu.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=94bccdd7d7a9f1301fdb4e832e008efa 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-context-menu.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=90e628735b628ec71d5a78547db2441c 2500w" />
</Frame>

Options disponibles :

* **Add follow-up**: Ajouter des instructions à un agent existant
* **Delete**: Arrêter et archiver le Background Agent
* **View request ID**: Afficher l’ID de requête unique pour le dépannage (à inclure quand tu contactes le support)
* **Give feedback**: Donner un feedback sur les performances de l’agent

<div id="configuration">
  ## Configuration
</div>

Gère les paramètres par défaut et les options de confidentialité depuis [Dashboard → Background Agents](https://www.cursor.com/dashboard?tab=background-agents).

<div id="settings">
  ### Paramètres
</div>

<div id="default-model">
  #### Modèle par défaut
</div>

Utilisé quand aucun modèle n’est explicitement spécifié avec <SlackInlineMessage message="@Cursor [model=...]" />. Consulte les [paramètres](https://www.cursor.com/dashboard?tab=background-agents) pour les options disponibles.

<div id="default-repository">
  #### Dépôt par défaut
</div>

Utilisé quand aucun dépôt n’est spécifié. Utilise ces formats :

* `https://github.com/org/repository`
* `org/repository`

<Note>
  Si tu fais référence à un dépôt inexistant, ça peut donner l’impression que tu n’as pas
  accès. L’erreur s’affiche quand Background Agent ne parvient pas à démarrer.
</Note>

<div id="base-branch">
  #### Branche de base
</div>

Branche de départ pour Background Agent. Laisse vide pour utiliser la branche par défaut du dépôt (souvent `main`)

<div id="channel-settings">
  ### Paramètres de canal
</div>

Configure des paramètres par défaut au niveau du canal avec <SlackInlineMessage message="@Cursor settings" />. Ces paramètres sont définis par équipe et remplacent tes valeurs par défaut personnelles pour ce canal.

Particulièrement utile quand :

* Différents canaux travaillent sur différents dépôts
* Les équipes veulent des paramètres cohérents pour tous les membres
* Tu veux éviter de spécifier le dépôt dans chaque commande

Pour configurer les paramètres du canal :

1. Exécute <SlackInlineMessage message="@Cursor settings" /> dans le canal souhaité
2. Définit le dépôt par défaut pour ce canal
3. Tous les membres de l’équipe qui utilisent Background Agents dans ce canal utilisent ces valeurs par défaut

<Note>
  Les paramètres du canal priment sur les paramètres personnels mais peuvent être remplacés
  par des options explicites comme{" "}

  <SlackInlineMessage message="@Cursor [repo=...] [prompt]" />
</Note>

<div id="privacy">
  ### Confidentialité
</div>

Les Background Agents prennent en charge le mode Confidentialité.

En savoir plus sur le [mode Confidentialité](https://www.cursor.com/privacy-overview) ou gère tes [paramètres de confidentialité](https://www.cursor.com/dashboard?tab=background-agents).

<Warning>
  Le mode Confidentialité (héritage) n’est pas pris en charge. Les Background Agents nécessitent
  un stockage temporaire du code pendant l’exécution.
</Warning>

<div id="display-agent-summary">
  #### Afficher le résumé de l’agent
</div>

Affiche les résumés d’agent et les images de diff. Peut contenir des chemins de fichiers ou des extraits de code. Peut être activé/désactivé.

<div id="display-agent-summary-in-external-channels">
  #### Afficher le résumé de l’agent dans les canaux externes
</div>

Pour Slack Connect avec d’autres espaces de travail ou des canaux avec des membres externes comme des invités, choisis d’afficher les résumés d’agent dans les canaux externes.

<div id="permissions">
  ## Permissions
</div>

Cursor demande ces permissions Slack pour que les Background Agents fonctionnent dans ton espace de travail :

<div className="full-width-table">
  | Permission          | Description                                                                                                     |
  | :------------------ | :-------------------------------------------------------------------------------------------------------------- |
  | `app_mentions:read` | Détecte les @mentions pour lancer les Background Agents et répondre aux demandes                                |
  | `channels:history`  | Lit les messages précédents dans les fils pour le contexte lors de l’ajout d’instructions de suivi              |
  | `channels:join`     | Rejoint automatiquement les canaux publics lorsqu’il est invité ou sollicité                                    |
  | `channels:read`     | Accède aux métadonnées des canaux (ID et noms) pour publier des réponses et des mises à jour                    |
  | `chat:write`        | Envoie des mises à jour de statut, des notifications d’achèvement et des liens de PR quand les agents ont fini  |
  | `files:read`        | Télécharge les fichiers partagés (journaux, captures d’écran, extraits de code) pour un contexte supplémentaire |
  | `files:write`       | Met en ligne des résumés visuels des changements des agents pour une revue rapide                               |
  | `groups:history`    | Lit les messages précédents dans les canaux privés pour le contexte des conversations multi‑tours               |
  | `groups:read`       | Accède aux métadonnées des canaux privés pour publier des réponses et maintenir le flux de conversation         |
  | `im:history`        | Accède à l’historique des messages directs pour le contexte des conversations en continu                        |
  | `im:read`           | Lit les métadonnées des MD pour identifier les participants et maintenir le bon fil de discussion               |
  | `im:write`          | Démarre des messages directs pour des notifications privées ou une communication individuelle                   |
  | `mpim:history`      | Accède à l’historique des MD de groupe pour des conversations multi‑participants                                |
  | `mpim:read`         | Lit les métadonnées des MD de groupe pour s’adresser aux participants et assurer une bonne livraison            |
  | `reactions:read`    | Observe les réactions émoji pour les retours utilisateur et les signaux de statut                               |
  | `reactions:write`   | Ajoute des réactions émoji pour marquer le statut : ⏳ en cours, ✅ terminé, ❌ échec                              |
  | `team:read`         | Identifie les détails de l’espace de travail pour séparer les installations et appliquer les paramètres         |
  | `users:read`        | Fait correspondre les utilisateurs Slack aux comptes Cursor pour les permissions et un accès sécurisé           |
</div>

---

← Previous: [Linear](./linear.md) | [Index](./index.md) | Next: [Modèles](./modles.md) →