---
title: "Analytics"
source: "https://docs.cursor.com/fr/account/teams/analytics"
language: "fr"
language_name: "French"
---

# Analytics
Source: https://docs.cursor.com/fr/account/teams/analytics

Suivre l’usage de l’équipe et les métriques d’activité

Les admins d’équipe peuvent suivre les métriques depuis le [dashboard](/fr/account/teams/dashboard).

<Frame>
  <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/analytics.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=a8a4a0ca334e5f5acac55307b2ebeadf" data-og-width="3456" width="3456" data-og-height="1944" height="1944" data-path="images/account/team/analytics.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/analytics.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=73c11df8fcb2862e5c1fd551e6399159 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/analytics.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=c3eaa0d4faa7d6fdf5e3c79dfd11fb5a 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/analytics.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=e9ee5fc554ae46e9d0e2cf53c19e652d 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/analytics.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=5f0afded72e0b02142c5a85e448f2d4e 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/analytics.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=3a6dec2a182ac88d7de75f7a42b1f5ff 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/analytics.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=7a8ac7dafe559da435f3f4974b04df52 2500w" />
</Frame>

<div id="total-usage">
  ### Utilisation totale
</div>

Consulte les métriques agrégées de ton équipe, dont le nombre total d’onglets et les requêtes premium. Pour les équipes de moins de 30 jours, les métriques reflètent l’usage depuis la création, y compris l’activité avant l’arrivée des membres.

<div id="per-active-user">
  ### Par utilisateur actif
</div>

Consulte les métriques moyennes par utilisateur actif : onglets acceptés, lignes de code et requêtes premium.

<div id="user-activity">
  ### Activité des utilisateurs
</div>

Suis les utilisateurs actifs hebdomadaires et mensuels.

<div id="analytics-report-headers">
  ## En-têtes du rapport d’analytics
</div>

Quand tu exportes des données d’analytics depuis le tableau de bord, le rapport inclut des métriques détaillées sur le comportement des utilisateurs et l’utilisation des fonctionnalités. Voici ce que signifie chaque en-tête :

<div id="user-information">
  ### Informations utilisateur
</div>

<ResponseField name="Date" type="ISO 8601 timestamp">
  La date à laquelle les données d’analytics ont été enregistrées (p. ex., 2024-01-15T04:30:00.000Z)
</ResponseField>

<ResponseField name="User ID" type="string">
  Identifiant unique de chaque utilisateur dans le système
</ResponseField>

<ResponseField name="Email" type="string">
  Adresse e-mail de l’utilisateur associée à son compte
</ResponseField>

<ResponseField name="Is Active" type="boolean">
  Indique si l’utilisateur était actif à cette date
</ResponseField>

<div id="ai-generated-code-metrics">
  ### Métriques de code généré par l’IA
</div>

<ResponseField name="Chat Suggested Lines Added" type="number">
  Nombre total de lignes de code suggérées par la fonctionnalité de chat IA
</ResponseField>

<ResponseField name="Chat Suggested Lines Deleted" type="number">
  Nombre total de lignes de code suggérées pour suppression par le chat IA
</ResponseField>

<ResponseField name="Chat Accepted Lines Added" type="number">
  Lignes suggérées par l’IA que l’utilisateur a acceptées et ajoutées à son code
</ResponseField>

<ResponseField name="Chat Accepted Lines Deleted" type="number">
  Suppressions suggérées par l’IA que l’utilisateur a acceptées
</ResponseField>

<div id="feature-usage-metrics">
  ### Métriques d’utilisation des fonctionnalités
</div>

<ResponseField name="Chat Total Applies" type="number">
  Nombre de fois où un utilisateur a appliqué des modifications générées par l’IA depuis le chat
</ResponseField>

<ResponseField name="Chat Total Accepts" type="number">
  Nombre de fois où un utilisateur a accepté des suggestions de l’IA
</ResponseField>

<ResponseField name="Chat Total Rejects" type="number">
  Nombre de fois où un utilisateur a rejeté des suggestions de l’IA
</ResponseField>

<ResponseField name="Chat Tabs Shown" type="number">
  Nombre de fois où des onglets de suggestions IA ont été affichés à l’utilisateur
</ResponseField>

<ResponseField name="Tabs Accepted" type="number">
  Onglets de suggestions IA acceptés par l’utilisateur
</ResponseField>

<div id="request-type-metrics">
  ### Métriques par type de requête
</div>

<ResponseField name="Edit Requests" type="number">
  Requêtes effectuées via la fonctionnalité composer/edit (Cmd+K, modifications inline)
</ResponseField>

<ResponseField name="Ask Requests" type="number">
  Requêtes de chat où les utilisateurs posent des questions à l’IA
</ResponseField>

<ResponseField name="Agent Requests" type="number">
  Requêtes envoyées aux agents IA (assistants IA spécialisés)
</ResponseField>

<ResponseField name="Cmd+K Usages" type="number">
  Nombre de fois où la palette de commandes Cmd+K (ou Ctrl+K) a été utilisée
</ResponseField>

<div id="subscription-and-api-metrics">
  ### Métriques d’abonnement et d’API
</div>

<ResponseField name="Subscription Included Reqs" type="number">
  Requêtes à l’IA couvertes par l’abonnement de l’utilisateur
</ResponseField>

<ResponseField name="API Key Reqs" type="number">
  Requêtes effectuées avec des clés d’API pour un accès programmatique
</ResponseField>

<ResponseField name="Usage-Based Reqs" type="number">
  Requêtes comptabilisées pour la facturation à l’usage
</ResponseField>

<div id="additional-features">
  ### Fonctionnalités supplémentaires
</div>

<ResponseField name="Bugbot Usages" type="number">
  Nombre de fois où la fonctionnalité IA de détection/correction de bugs a été utilisée
</ResponseField>

<div id="configuration-information">
  ### Informations de configuration
</div>

<ResponseField name="Most Used Model" type="string">
  Modèle d’IA le plus utilisé par l’utilisateur (p. ex., GPT-4, Claude)
</ResponseField>

<ResponseField name="Most Used Apply Extension" type="string">
  Extension de fichier la plus utilisée lors de l’application des suggestions de l’IA (p. ex., .ts,
  .py, .java)
</ResponseField>

<ResponseField name="Most Used Tab Extension" type="string">
  Extension de fichier la plus utilisée avec les fonctionnalités de complétion par tabulation
</ResponseField>

<ResponseField name="Client Version" type="string">
  Version de l’éditeur Cursor utilisée
</ResponseField>

<div id="calculated-metrics">
  ### Métriques calculées
</div>

Le rapport inclut aussi des données traitées qui aident à comprendre la contribution de l’IA au code :

* Total des lignes ajoutées/supprimées : comptage brut de toutes les modifications de code
* Lignes ajoutées/supprimées acceptées : lignes issues de suggestions de l’IA et acceptées
* Requêtes du composer : requêtes effectuées via la fonctionnalité de composer inline
* Requêtes de chat : requêtes effectuées via l’interface de chat

<Note>
  Toutes les valeurs numériques valent 0 par défaut si absentes, les valeurs booléennes valent
  false par défaut, et les chaînes de caractères valent par défaut des chaînes vides. Les métriques
  sont agrégées par utilisateur à la journée.
</Note>

---

← Previous: [API de suivi de code par IA](./api-de-suivi-de-code-par-ia.md) | [Index](./index.md) | Next: [Analytics V2](./analytics-v2.md) →