---
title: "SCIM"
source: "https://docs.cursor.com/fr/account/teams/scim"
language: "fr"
language_name: "French"
---

# SCIM
Source: https://docs.cursor.com/fr/account/teams/scim

Configurer l’approvisionnement SCIM pour la gestion automatisée des utilisateurs et des groupes

<div id="overview">
  ## Aperçu
</div>

Le provisionnement SCIM 2.0 gère automatiquement les membres de ton équipe et les groupes d’annuaire via ton fournisseur d’identité. Disponible sur les offres Enterprise avec SSO activé.

<product_visual type="screenshot">
  Tableau de bord des paramètres SCIM affichant la configuration de gestion d’Active Directory
</product_visual>

<div id="prerequisites">
  ## Prérequis
</div>

* Abonnement Cursor Enterprise
* Le SSO doit être configuré au préalable — **SCIM nécessite une connexion SSO active**
* Accès admin à ton fournisseur d’identité (Okta, Azure AD, etc.)
* Accès admin à ton organisation Cursor

<div id="how-it-works">
  ## Comment ça marche
</div>

<div id="user-provisioning">
  ### Provisioning des utilisateurs
</div>

Les utilisateurs sont automatiquement ajoutés à Cursor quand ils sont affectés à l’application SCIM dans ton fournisseur d’identité. Quand ils sont désaffectés, ils sont supprimés. Les changements se synchronisent en temps réel.

<div id="directory-groups">
  ### Groupes d’annuaire
</div>

Les groupes d’annuaire et leurs membres se synchronisent depuis ton fournisseur d’identité. La gestion des groupes et des utilisateurs doit se faire via ton fournisseur d’identité — Cursor affiche ces infos en lecture seule.

<div id="spend-management">
  ### Gestion des dépenses
</div>

Définis des limites de dépenses par utilisateur pour chaque groupe d’annuaire. Les limites des groupes d’annuaire priment sur les limites au niveau de l’équipe. Les utilisateurs appartenant à plusieurs groupes reçoivent la limite de dépenses la plus élevée applicable.

<div id="setup">
  ## Configuration
</div>

<Steps>
  <Step title="Vérifie que le SSO est configuré">
    SCIM nécessite que le SSO soit configuré en premier. Si t’as pas encore configuré le SSO,
    suis le [guide de configuration du SSO](/fr/account/teams/sso) avant de continuer.
  </Step>

  <Step title="Accède à Active Directory Management">
    Va sur
    [cursor.com/dashboard?tab=active-directory](https://www.cursor.com/dashboard?tab=active-directory)
    avec un compte admin, ou ouvre les paramètres de ton dashboard et sélectionne l’onglet
    « Active Directory Management ».
  </Step>

  <Step title="Lance la configuration SCIM">
    Une fois le SSO vérifié, tu verras un lien pour une configuration SCIM pas à pas. Clique
    dessus pour lancer l’assistant de configuration.
  </Step>

  <Step title="Configure SCIM dans ton fournisseur d’identité">
    Dans ton fournisseur d’identité : - Crée ou configure ton application SCIM - Utilise
    l’endpoint SCIM et le token fournis par Cursor - Active le provisioning des utilisateurs et la synchronisation des groupes - Teste la connexion
  </Step>

  <Step title="Configure les limites de dépenses (optionnel)">
    De retour sur la page Active Directory Management de Cursor : - Consulte tes groupes d’annuaire synchronisés - Défini des limites de dépenses par utilisateur pour des groupes spécifiques si nécessaire -
    Vérifie quelles limites s’appliquent aux utilisateurs appartenant à plusieurs groupes
  </Step>
</Steps>

<div id="identity-provider-setup">
  ### Configuration du fournisseur d’identité
</div>

Pour des instructions de configuration spécifiques au fournisseur :

<Card title="Guides des fournisseurs d’identité" icon="book" href="https://workos.com/docs/integrations">
  Instructions de configuration pour Okta, Azure AD, Google Workspace et plus encore.
</Card>

<div id="managing-users-and-groups">
  ## Gestion des utilisateurs et des groupes
</div>

<Warning>
  Toute la gestion des utilisateurs et des groupes doit être effectuée via ton fournisseur d'identité.
  Les modifications effectuées dans ton fournisseur d'identité se synchronisent automatiquement avec Cursor, mais
  tu ne peux pas modifier les utilisateurs ou les groupes directement dans Cursor.
</Warning>

<div id="user-management">
  ### Gestion des utilisateurs
</div>

* Ajoute des utilisateurs en les assignant à ton application SCIM dans ton fournisseur d'identité
* Supprime des utilisateurs en les retirant de l'application SCIM
* Les modifications du profil utilisateur (nom, e-mail) se synchronisent automatiquement depuis ton fournisseur d'identité

<div id="group-management">
  ### Gestion des groupes
</div>

* Les groupes de l'annuaire sont automatiquement synchronisés depuis ton fournisseur d'identité
* Les changements d'appartenance aux groupes sont pris en compte en temps réel
* Utilise les groupes pour organiser les utilisateurs et définir différents plafonds de dépenses

<div id="spend-limits">
  ### Plafonds de dépenses
</div>

* Définit des plafonds par utilisateur différents pour chaque groupe de l'annuaire
* Les utilisateurs héritent du plafond de dépenses le plus élevé parmi leurs groupes
* Les plafonds de groupe remplacent le plafond par utilisateur par défaut au niveau de l'équipe

<div id="faq">
  ## FAQ
</div>

<div id="why-isnt-scim-management-showing-up-in-my-dashboard">
  ### Pourquoi la gestion SCIM n’apparaît-elle pas dans mon tableau de bord ?
</div>

Assure-toi que le SSO est correctement configuré et opérationnel avant de configurer SCIM. SCIM nécessite une connexion SSO active pour fonctionner.

<div id="why-arent-users-syncing">
  ### Pourquoi les utilisateurs ne se synchronisent-ils pas ?
</div>

Vérifie que les utilisateurs sont affectés à l’application SCIM dans ton fournisseur d’identité. Les utilisateurs doivent être explicitement affectés pour apparaître dans Cursor.

<div id="why-arent-groups-appearing">
  ### Pourquoi les groupes n’apparaissent-ils pas ?
</div>

Vérifie que l’approvisionnement des groupes par push est activé dans les paramètres SCIM de ton fournisseur d’identité. La synchronisation des groupes doit être configurée séparément de celle des utilisateurs.

<div id="why-arent-spend-limits-applying">
  ### Pourquoi les limites de dépenses ne s’appliquent-elles pas ?
</div>

Confirme que les utilisateurs sont correctement affectés aux groupes attendus dans ton fournisseur d’identité. L’appartenance à un groupe détermine quelles limites de dépenses s’appliquent.

<div id="can-i-manage-scim-users-and-groups-directly-in-cursor">
  ### Puis-je gérer les utilisateurs et les groupes SCIM directement dans Cursor ?
</div>

Non. Toute la gestion des utilisateurs et des groupes doit se faire via ton fournisseur d’identité. Cursor affiche ces informations en lecture seule.

<div id="how-quickly-do-changes-sync">
  ### À quelle vitesse les modifications se synchronisent-elles ?
</div>

Les modifications effectuées dans ton fournisseur d’identité se synchronisent avec Cursor en temps réel. Il peut y avoir un léger délai pour les opérations en masse de grande taille.

---

← Previous: [Membres et rôles](./membres-et-rles.md) | [Index](./index.md) | Next: [Bien démarrer](./bien-dmarrer.md) →