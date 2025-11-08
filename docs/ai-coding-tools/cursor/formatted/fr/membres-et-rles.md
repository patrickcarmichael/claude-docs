---
title: "Membres et rôles"
source: "https://docs.cursor.com/fr/account/teams/members"
language: "fr"
language_name: "French"
---

# Membres et rôles
Source: https://docs.cursor.com/fr/account/teams/members

Gérer les membres et les rôles de l’équipe

Les équipes Cursor ont trois rôles :

<div id="roles">
  ## Rôles
</div>

Les **Membres** sont le rôle par défaut avec accès aux fonctionnalités Pro de Cursor.

* Accès complet aux fonctionnalités Pro de Cursor
* Pas d’accès aux paramètres de facturation ni au tableau de bord d’admin
* Peuvent voir leur propre utilisation et leur budget restant basé sur l’utilisation

Les **Admins** gèrent la gestion d’équipe et les paramètres de sécurité.

* Accès complet aux fonctionnalités Pro
* Ajout/suppression de membres, modification des rôles, configuration du SSO
* Configuration de la tarification à l’usage et des plafonds de dépenses
* Accès aux analyses d’équipe

Les **Admins non payants** gèrent des équipes sans occuper de place payante — idéal pour le personnel IT ou finance qui n’a pas besoin d’accéder à Cursor.

* Non facturés, pas de fonctionnalités Pro
* Même périmètre administratif que les Admins

<Info>Les Admins non payants nécessitent au moins un utilisateur payant dans l’équipe.</Info>

<div id="role-comparison">
  ## Comparaison des rôles
</div>

<div className="full-width-table">
  | Fonctionnalité                         | Membre | Admin | Admin non payant |
  | -------------------------------------- | :----: | :---: | :--------------: |
  | Utiliser les fonctionnalités de Cursor |    ✓   |   ✓   |                  |
  | Inviter des membres                    |    ✓   |   ✓   |         ✓        |
  | Retirer des membres                    |        |   ✓   |         ✓        |
  | Modifier le rôle d’un utilisateur      |        |   ✓   |         ✓        |
  | Tableau de bord Admin                  |        |   ✓   |         ✓        |
  | Configurer le SSO/la sécurité          |        |   ✓   |         ✓        |
  | Gérer la facturation                   |        |   ✓   |         ✓        |
  | Consulter les analytics                |        |   ✓   |         ✓        |
  | Gérer les accès                        |        |   ✓   |         ✓        |
  | Définir les contrôles d’utilisation    |        |   ✓   |         ✓        |
  | Nécessite une licence payante          |    ✓   |   ✓   |                  |
</div>

<div id="managing-members">
  ## Gérer les membres
</div>

Tous les membres de l'équipe peuvent inviter d'autres personnes. Pour l’instant, on ne restreint pas les invitations.

<div id="add-member">
  ### Ajouter un membre
</div>

Ajoute des membres de trois façons :

1. **Invitation par e-mail**

   * Clique sur `Invite Members`
   * Saisis des adresses e-mail
   * Les utilisateurs reçoivent une invitation par e-mail

2. **Lien d'invitation**

   * Clique sur `Invite Members`
   * Copie `Invite Link`
   * Partage le lien avec les membres de l'équipe

3. **SSO**
   * Configure le SSO dans le [tableau de bord d’admin](/fr/account/teams/sso)
   * Les utilisateurs rejoignent automatiquement en se connectant avec leur e-mail SSO

<Warning>
  Les liens d'invitation expirent très tard — toute personne ayant le lien peut rejoindre.
  Révoque-les ou utilise le [SSO](/fr/account/teams/sso)
</Warning>

<div id="remove-member">
  ### Retirer un membre
</div>

Les admins peuvent retirer des membres à tout moment via le menu contextuel → "Remove". Si un membre a utilisé des crédits, son siège reste occupé jusqu'à la fin du cycle de facturation.

<div id="change-role">
  ### Changer le rôle
</div>

Les admins peuvent changer le rôle d'autres membres en cliquant sur le menu contextuel puis sur l'option "Change role".<br />

Il doit toujours y avoir au moins un Admin et au moins un membre payant dans l'équipe.

## Sécurité & SSO

Le Single Sign-On (SSO) SAML 2.0 est dispo sur les offres Team. Fonctionnalités clés :

* Configurer des connexions SSO ([en savoir plus](/fr/account/teams/sso))
* Mettre en place la vérification de domaine
* Inscription automatique des utilisateurs
* Options d’application du SSO
* Intégration avec un fournisseur d’identité (Okta, etc.)

<Note>
  <p className="!mb-0">La vérification de domaine est requise pour activer le SSO.</p>
</Note>

<Frame>
  <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=76608c26daf1f9ab2bbc2c4ccb156c0e" style={{ padding: `32px 64px`, backgroundColor: "#0c0c0c" }} data-og-width="802" width="802" data-og-height="440" height="440" data-path="images/account/sso-settings.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=334dc1fc107338d19ec7b0052e7ea0e4 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=543b3d868c19960a5fb4c526d9895bd3 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=a06655178ba10f6a72919e9f7d598191 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=e280fc911306fe8d3b8e90b7221b0c11 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=ffd8f2c0168e2ac4f95431062b226021 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=1c17e4eac666b663d676ce874f1c4ba5 2500w" />
</Frame>

<div id="usage-controls">
  ## Contrôles d’utilisation
</div>

Accède aux paramètres d’utilisation pour :

* Activer la tarification à l’usage
* Activer pour les modèles premium
* Limiter les modifications aux admins
* Définir des plafonds de dépense mensuels
* Suivre l’utilisation à l’échelle de l’équipe

<Frame>
  <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/usage-based-pricing.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=e8149f830c27308af1bcc329c25e38b5" style={{ backgroundColor: "#0c0c0c" }} data-og-width="1668" width="1668" data-og-height="1160" height="1160" data-path="images/account/usage-based-pricing.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/usage-based-pricing.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=bc308a967251694ad7b03189c1083c61 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/usage-based-pricing.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=ddc293e19fa993e65be8c09ced649b4f 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/usage-based-pricing.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=3a4df7d48d75c6166ab215550a641ca6 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/usage-based-pricing.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=f9051947c802ae54fd964196c50a3701 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/usage-based-pricing.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=ed775e3e98611ead1b938aedaf917f11 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/usage-based-pricing.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=b26f86bce94dc981d3cf71853a965374 2500w" />
</Frame>

<div id="billing">
  ## Facturation
</div>

Quand tu ajoutes des membres à l’équipe :

* Chaque membre ou admin occupe une place facturable (voir [tarifs](https://cursor.com/pricing))
* Les nouveaux membres sont facturés au prorata du temps restant dans la période de facturation
* Les places d’admin non payées ne sont pas comptabilisées

Les ajouts en cours de mois ne facturent que les jours utilisés. Quand tu retires des membres qui ont utilisé des crédits, leur place reste occupée jusqu’à la fin du cycle de facturation — aucun remboursement au prorata n’est accordé.

Les changements de rôle (p. ex. Admin vers Admin non payé) ajustent la facturation à partir de la date du changement. Choisis une facturation mensuelle ou annuelle.

Le renouvellement mensuel/annuel a lieu à ta date d’inscription initiale, quels que soient les changements de membres.

<div id="switch-to-yearly-billing">
  ### Passer à la facturation annuelle
</div>

Économise **20 %** en passant du mensuel à l’annuel :

1. Va sur le [Dashboard](https://cursor.com/dashboard)
2. Dans la section Compte, clique sur « Advanced » puis « Upgrade to yearly billing »

<Note>
  Tu peux uniquement passer du mensuel à l’annuel via le dashboard. Pour passer de
  l’annuel au mensuel, contacte [hi@cursor.com](mailto:hi@cursor.com).
</Note>

---

← Previous: [Paramètres Enterprise](./paramtres-enterprise.md) | [Index](./index.md) | Next: [SCIM](./scim.md) →