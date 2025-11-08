# Paramètres Enterprise

**Navigation:** [← Previous](./11-desarrolladores.md) | [Index](./index.md) | [Next →](./13-mode-shell.md)

---

# Paramètres Enterprise
Source: https://docs.cursor.com/fr/account/teams/enterprise-settings

Gère de façon centralisée les paramètres de Cursor pour ton organisation

<div id="enterprise-settings">
  # Paramètres d’entreprise
</div>

Tu peux gérer de façon centralisée certaines fonctionnalités de Cursor via des solutions de gestion d’appareils pour t’assurer qu’il répond aux besoins de ton organisation. Quand tu définis une règle Cursor, sa valeur remplace le paramètre Cursor correspondant sur les appareils des utilisateurs.

Éditeur de paramètres indiquant que le paramètre « Extensions : autorisées » est géré par l’organisation.

Cursor propose actuellement des règles pour contrôler les fonctionnalités suivantes administrées par les équipes IT :

| Règle             | Description                                                                                                                                | Paramètre Cursor         | Disponible depuis |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------ | ----------------- |
| AllowedExtensions | Contrôle quelles extensions peuvent être installées.                                                                                       | extensions.allowed       | 1.2               |
| AllowedTeamId     | Contrôle quels IDs d’équipe sont autorisés à se connecter. Les utilisateurs avec des IDs d’équipe non autorisés sont déconnectés de force. | cursorAuth.allowedTeamId | 1.3               |

<div id="configure-allowed-extensions">
  ## Configurer les extensions autorisées
</div>

Le paramètre Cursor `extensions.allowed` contrôle quelles extensions peuvent être installées. Ce paramètre accepte un objet JSON dont les clés sont des noms d’éditeurs et les valeurs des booléens indiquant si les extensions de cet éditeur sont autorisées.

Par exemple, définir `extensions.allowed` sur `{"anysphere": true, "github": true}` autorise les extensions des éditeurs Anysphere et GitHub, tandis que le définir sur `{"anysphere": false}` bloque les extensions d’Anysphere.

Pour gérer de façon centralisée les extensions autorisées pour ton organisation, configure la stratégie `AllowedExtensions` via ta solution de gestion des appareils. Cette stratégie remplace le paramètre `extensions.allowed` sur les appareils des utilisateurs. La valeur de cette stratégie est une chaîne JSON qui définit les éditeurs autorisés.

Si tu veux en savoir plus sur les extensions dans Cursor, consulte la documentation des extensions.

<div id="configure-allowed-team-ids">
  ## Configurer les IDs d’équipe autorisés
</div>

Le paramètre Cursor `cursorAuth.allowedTeamId` détermine quels IDs d’équipe sont autorisés à se connecter à Cursor. Ce paramètre accepte une liste d’IDs d’équipe, séparés par des virgules, qui sont autorisés à accéder.

Par exemple, définir `cursorAuth.allowedTeamId` sur `"1,3,7"` permet aux utilisateurs appartenant à ces IDs d’équipe spécifiques de se connecter.

Quand un utilisateur essaie de se connecter avec un ID d’équipe qui n’est pas dans la liste autorisée :

* Il est immédiatement déconnecté de force
* Un message d’erreur s’affiche
* L’application bloque toute nouvelle tentative d’authentification jusqu’à l’utilisation d’un ID d’équipe valide

Pour gérer de manière centralisée les IDs d’équipe autorisés pour ton organisation, configure la stratégie `AllowedTeamId` via ta solution de gestion des appareils. Cette stratégie remplace le paramètre `cursorAuth.allowedTeamId` sur les appareils des utilisateurs. La valeur de cette stratégie est une chaîne contenant la liste, séparée par des virgules, des IDs d’équipe autorisés.

<div id="group-policy-on-windows">
  ## Stratégie de groupe sur Windows
</div>

Cursor prend en charge la stratégie de groupe basée sur le Registre Windows. Lorsque les définitions de stratégie sont installées, les admins peuvent utiliser l’Éditeur de stratégie de groupe locale pour gérer les valeurs de stratégie.

Pour ajouter une stratégie :

1. Copie les fichiers ADMX et ADML de stratégie depuis `AppData\Local\Programs\cursor\policies`.
2. Colle le fichier ADMX dans le répertoire `C:\Windows\PolicyDefinitions`, et le fichier ADML dans le répertoire `C:\Windows\PolicyDefinitions\<your-locale>\`.
3. Redémarre l’Éditeur de stratégie de groupe locale.
4. Définit les valeurs de stratégie appropriées (p. ex. `{"anysphere": true, "github": true}` pour la stratégie `AllowedExtensions`) dans l’Éditeur de stratégie de groupe locale.

Les stratégies peuvent être définies à la fois au niveau Ordinateur et au niveau Utilisateur. Si les deux sont définies, le niveau Ordinateur a la priorité. Lorsqu’une valeur de stratégie est définie, elle remplace la valeur du paramètre Cursor configurée à n’importe quel niveau (par défaut, utilisateur, espace de travail, etc.).

<div id="configuration-profiles-on-macos">
  ## Profils de configuration sur macOS
</div>

Les profils de configuration gèrent les paramètres sur les appareils macOS. Un profil est un fichier XML avec des paires clé/valeur correspondant aux stratégies disponibles. Ces profils peuvent être déployés via des solutions de gestion des appareils mobiles (MDM) ou installés manuellement.

<Accordion title="Exemple de fichier .mobileconfig">
  Un exemple de fichier `.mobileconfig` pour macOS est présenté ci-dessous :

  ```
  <?xml version="1.0" encoding="UTF-8"?>
  <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
  <plist version="1.0">
  	<dict>
  		<key>PayloadContent</key>
  		<array>
  			<dict>
  				<key>PayloadDisplayName</key>
  				<string>Cursor</string>
  				<key>PayloadIdentifier</key>
  				<string>com.todesktop.230313mzl4w4u92.J6B5723A-6539-4F31-8A4E-3CC96E51F48C</string>
  				<key>PayloadType</key>
  				<string>com.todesktop.230313mzl4w4u92</string>
  				<key>PayloadUUID</key>
  				<string>J6B5723A-6539-4F31-8A4E-3CC96E51F48C</string>
  				<key>PayloadVersion</key>
  				<integer>1</integer>
  				<key>AllowedExtensions</key>
  				<string>{"anysphere":true}</string>
  				<key>AllowedTeamId</key>
  				<string>1,2</string>
  			</dict>
  		</array>
  		<key>PayloadDescription</key>
  		<string>This profile manages Cursor.</string>
  		<key>PayloadDisplayName</key>
  		<string>Cursor</string>
  		<key>PayloadIdentifier</key>
  		<string>com.todesktop.230313mzl4w4u92</string>
  		<key>PayloadOrganization</key>
  		<string>Anysphere</string>
  		<key>PayloadType</key>
  		<string>Configuration</string>
  		<key>PayloadUUID</key>
  		<string>F2C1A7B3-9D4E-4B2C-8E1F-7A6C5D4B3E2F</string>
  		<key>PayloadVersion</key>
  		<integer>1</integer>
  		<key>TargetDeviceType</key>
  		<integer>5</integer>
  	</dict>
  </plist>
  ```
</Accordion>

<div id="string-policies">
  ### Stratégies de type chaîne
</div>

L’exemple ci-dessous illustre la configuration de la stratégie `AllowedExtensions`. La valeur de la stratégie est vide dans le fichier d’exemple (aucune extension n’est autorisée).

```
<key>ExtensionsAutorisées</key>
<string></string>
```

Ajoute la chaîne JSON appropriée qui définit ta politique entre les balises `<string>`.

```
<key>AllowedExtensions</key>
<string>{"anysphere": true, "github": true}</string>
```

Pour la règle `AllowedTeamId`, ajoute la liste des IDs d’équipe séparés par des virgules :

```
<key>AllowedTeamId</key>
<string>1,3,7</string>
```

**Important :** Le fichier `.mobileconfig` fourni initialise **toutes** les stratégies disponibles dans cette version de Cursor. Supprime toutes celles dont t’as pas besoin.

Si tu n’édites pas ou ne supprimes pas une stratégie dans l’exemple `.mobileconfig`, elle sera appliquée avec sa valeur par défaut (restrictive).

Installe manuellement un profil de configuration en double-cliquant sur le fichier `.mobileconfig` dans le Finder, puis active-le dans Réglages Système sous **Général** > **Gestion des appareils**. Supprimer le profil depuis Réglages Système retirera les stratégies de Cursor.

Pour en savoir plus sur les profils de configuration, consulte la documentation d’Apple.

<div id="additional-policies">
  ## Politiques supplémentaires
</div>

L’objectif est d’élever les réglages actuels de Cursor au rang de politiques et de s’aligner étroitement sur les réglages existants, afin que la nomenclature et le comportement restent cohérents. Si tu veux proposer davantage de politiques, ouvre une issue sur le dépôt GitHub de Cursor. L’équipe déterminera s’il existe déjà un réglage correspondant pour ce comportement ou s’il faut créer un nouveau réglage pour contrôler le comportement souhaité.

<div id="frequently-asked-questions">
  ## Foire aux questions
</div>

<div id="does-cursor-support-configuration-profiles-on-linux">
  ### Cursor prend-il en charge les profils de configuration sous Linux ?
</div>

La prise en charge de Linux n’est pas prévue sur la feuille de route. Si t’es intéressé par les profils de configuration sous Linux, ouvre une issue sur le dépôt GitHub de Cursor et partage les détails de ton cas d’usage.



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



# Bien démarrer
Source: https://docs.cursor.com/fr/account/teams/setup

Créer et configurer une équipe Cursor

<div id="cursor-for-teams">
  ## Cursor pour les équipes
</div>

Cursor marche aussi bien pour les personnes solo que pour les équipes. L’offre Teams propose des outils pour les organisations : SSO, gestion d’équipe, contrôles d’accès et analytics d’utilisation.

<div id="creating-a-team">
  ## Créer une équipe
</div>

Crée une équipe en suivant ces étapes :

<Steps>
  <Step title="Configurer l’offre Teams">
    Pour créer une équipe, suis ces étapes :

    1. **Nouveaux utilisateurs** : rends-toi sur [cursor.com/team/new-team](https://cursor.com/team/new-team) pour créer un nouveau compte et une équipe
    2. **Utilisateurs existants** : va sur ton [dashboard](/fr/account/dashboard) et clique sur « Upgrade to Teams »
  </Step>

  <Step title="Renseigner les informations de l’équipe">
    Choisis un nom d’équipe et un cycle de facturation

    <Frame>
      <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/new-team.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=3b9df20d032b544dcbc0343d9ddf056f" data-og-width="3456" width="3456" data-og-height="2158" height="2158" data-path="images/account/team/new-team.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/new-team.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=b81f3241069a8a0fb9278b6a2e246057 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/new-team.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=c26976bf06297d36ec9224ec1496a630 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/new-team.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=fed5c7c95914ff47cfceae81f1441208 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/new-team.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=0dc5986368419ef54f45803547741cfe 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/new-team.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=4eb38a9618399ddadbf7596b185d2732 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/new-team.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=1c7d720a1e20d2aa23463a1b9001d545 2500w" />
    </Frame>
  </Step>

  <Step title="Inviter des membres">
    Invite des membres de l’équipe. Le nombre d’utilisateurs est calculé au prorata : tu ne paies que pour la période où ils font partie de l’équipe.

    <Frame>
      <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/invite-members.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=bbd84dd96a7003415c2d2f038b1aaa77" style={{ paddingLeft: 16, paddingRight: 16, backgroundColor: '#0c0c0c' }} data-og-width="880" width="880" data-og-height="422" height="422" data-path="images/account/invite-members.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/invite-members.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=988e36ee874f704dfaae1b0a69ed2f84 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/invite-members.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=c0f85aacd3be59e11b1bfd05f9e5d6cd 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/invite-members.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=411456e375f8c406ad2972965e0b549e 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/invite-members.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=57ae04799be300a7e61464490344146f 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/invite-members.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=2faa0cf8ed56865c19916e33fde97900 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/invite-members.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=0bdb5040f44338e748246b4f1ddf2ddf 2500w" />
    </Frame>
  </Step>

  <Step title="Activer le SSO (optionnel)">
    Active le [SSO](/fr/account/teams/sso) pour plus de sécurité et un onboarding automatisé.

    <Frame>
      <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=76608c26daf1f9ab2bbc2c4ccb156c0e" data-og-width="802" width="802" data-og-height="440" height="440" data-path="images/account/sso-settings.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=334dc1fc107338d19ec7b0052e7ea0e4 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=543b3d868c19960a5fb4c526d9895bd3 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=a06655178ba10f6a72919e9f7d598191 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=e280fc911306fe8d3b8e90b7221b0c11 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=ffd8f2c0168e2ac4f95431062b226021 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=1c17e4eac666b663d676ce874f1c4ba5 2500w" />
    </Frame>
  </Step>
</Steps>

<div id="faq">
  ## FAQ
</div>

<AccordionGroup>
  <Accordion title="Mon équipe utilise Zscaler / un proxy / un VPN, est-ce que Cursor va marcher ?">
    Cursor utilise HTTP/2 par défaut. Certains proxies et VPN le bloquent.

    Active l’option de repli en HTTP/1.1 dans les paramètres pour utiliser HTTP/1.1 à la place.
  </Accordion>

  <Accordion title="Comment acheter des licences pour mon entreprise ?">
    Cursor facture par utilisateur actif, pas par siège. Ajoute ou retire des utilisateurs à tout moment — les nouveaux membres sont facturés au prorata pour le temps restant. Si un utilisateur retiré a utilisé des crédits, son siège reste occupé jusqu’à la fin du cycle de facturation.

    Ta date de renouvellement ne change pas.
  </Accordion>

  <Accordion title="Comment configurer une équipe quand j’utilise pas Cursor ?">
    Définis-toi comme [Unpaid Admin](/fr/account/teams/members) pour gérer sans licence.

    <Warning>
      Les équipes doivent avoir au moins un membre payant. Tu peux faire la configuration, inviter un membre, puis changer ton rôle avant la facturation.
    </Warning>
  </Accordion>

  <Accordion title="Comment ajouter Cursor au MDM de mon entreprise ?">
    Les liens de téléchargement pour toutes les plateformes sont dispo sur [cursor.com/downloads](https://cursor.com/downloads).

    Instructions MDM :

    * [Omnissa Workspace ONE](https://docs.omnissa.com/bundle/MobileApplicationManagementVSaaS/page/DeployInternalApplications.html) (anciennement VMware)
    * [Microsoft Intune (Windows)](https://learn.microsoft.com/en-us/mem/intune-service/apps/apps-win32-app-management)
    * [Microsoft Intune (Mac)](https://learn.microsoft.com/en-us/mem/intune-service/apps/lob-apps-macos-dmg)
    * [Kandji MDM](https://support.kandji.io/kb/custom-apps-overview)
  </Accordion>
</AccordionGroup>



# SSO
Source: https://docs.cursor.com/fr/account/teams/sso

Configure l’authentification unique pour ton équipe

<div id="overview">
  ## Vue d’ensemble
</div>

Le SSO SAML 2.0 est disponible sans frais supplémentaires sur les plans Business. Utilise ton fournisseur d’identité (IdP) existant pour authentifier les membres de ton équipe sans créer de comptes Cursor séparés.

<Frame>
  <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=76608c26daf1f9ab2bbc2c4ccb156c0e" style={{ padding: 32, backgroundColor: "#0c0c0c" }} data-og-width="802" width="802" data-og-height="440" height="440" data-path="images/account/sso-settings.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=334dc1fc107338d19ec7b0052e7ea0e4 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=543b3d868c19960a5fb4c526d9895bd3 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=a06655178ba10f6a72919e9f7d598191 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=e280fc911306fe8d3b8e90b7221b0c11 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=ffd8f2c0168e2ac4f95431062b226021 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=1c17e4eac666b663d676ce874f1c4ba5 2500w" />
</Frame>

<div id="prerequisites">
  ## Prérequis
</div>

* Forfait Cursor Team
* Accès admin à ton fournisseur d’identité (p. ex. Okta)
* Accès admin à ton organisation Cursor

<div id="configuration-steps">
  ## Étapes de configuration
</div>

<Steps>
  <Step title="Connecte-toi à ton compte Cursor">
    Va sur [cursor.com/dashboard?tab=settings](https://www.cursor.com/dashboard?tab=settings) avec un compte admin.
  </Step>

  <Step title="Trouve la configuration SSO">
    Repère la section « Single Sign-On (SSO) » et déplie-la.
  </Step>

  <Step title="Lance la configuration">
    Clique sur le bouton « SSO Provider Connection settings » pour démarrer la config SSO et suis l’assistant.
  </Step>

  <Step title="Configure ton fournisseur d’identité">
    Dans ton fournisseur d’identité (p. ex. Okta) :

    * Crée une nouvelle application SAML
    * Configure les paramètres SAML en utilisant les informations de Cursor
    * Mets en place le provisioning Just-in-Time (JIT)
  </Step>

  <Step title="Vérifie le domaine">
    Vérifie le domaine de tes utilisateurs dans Cursor en cliquant sur le bouton « Domain verification settings ».
  </Step>
</Steps>

<div id="identity-provider-setup-guides">
  ### Guides de configuration des fournisseurs d’identité
</div>

Pour des instructions de configuration propres à chaque fournisseur :

<Card title="Guides des fournisseurs d’identité" icon="book" href="https://workos.com/docs/integrations">
  Instructions de configuration pour Okta, Azure AD, Google Workspace et plus encore.
</Card>

<div id="additional-settings">
  ## Paramètres supplémentaires
</div>

* Gère l’application du SSO depuis le tableau de bord admin
* Les nouveaux utilisateurs sont inscrits automatiquement lorsqu’ils se connectent via SSO
* Gère les utilisateurs depuis ton fournisseur d’identité

<div id="troubleshooting">
  ## Dépannage
</div>

Si tu rencontres des problèmes :

* Vérifie que le domaine est validé dans Cursor
* Assure-toi que les attributs SAML sont correctement mis en correspondance
* Vérifie que le SSO est activé dans le tableau de bord admin
* Assure la correspondance des prénoms et noms entre le fournisseur d’identité et Cursor
* Consulte les guides spécifiques au fournisseur ci-dessus
* Contacte [hi@cursor.com](mailto:hi@cursor.com) si le problème persiste



# Accès aux mises à jour
Source: https://docs.cursor.com/fr/account/update-access

Choisis à quelle fréquence tu reçois des mises à jour

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

Cursor propose deux canaux de mise à jour.

<Tabs>
  <Tab title="Default">
    Le canal de mise à jour par défaut avec des versions testées.

    * Versions stables
    * Corrections de bugs issues des tests préversion
    * Par défaut pour tous les utilisateurs
    * Seule option pour les utilisateurs d’équipe

    <Note>
      Les comptes Team et Business utilisent le mode Default.
    </Note>
  </Tab>

  <Tab title="Early Access">
    Versions préversion avec de nouvelles fonctionnalités.

    <Warning>
      Les versions Early Access peuvent comporter des bugs ou des problèmes de stabilité.
    </Warning>

    * Accès aux fonctionnalités en cours de développement
    * Peut contenir des bugs
    * Non disponible pour les comptes d’équipe
  </Tab>
</Tabs>

<div id="change-update-channel">
  ## Changer de canal de mise à jour
</div>

1. **Ouvre les paramètres** : Appuie sur <Kbd>Cmd+Shift+J</Kbd>
2. **Va dans Beta** : Sélectionne Beta dans la barre latérale
3. **Sélectionne le canal** : Choisis Default ou Early Access

<Frame>
  <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/early-access.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=36c55c2deb93bc734b6ee0099a0d184c" data-og-width="1798" width="1798" data-og-height="442" height="442" data-path="images/account/early-access.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/early-access.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=624bfea7b3643f55afaa85b38b1c56e1 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/early-access.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=f32c8e59596f024223735b4f929949e0 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/early-access.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=bd8c4bf3265ab802b6188aa81a620244 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/early-access.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=e8600f42cc363c61377f158972187e01 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/early-access.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=32c83b2109587d299959c2d46ce67353 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/early-access.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=b2c4032824d39c62a7cbada5578b1a98 2500w" />
</Frame>

Signale les problèmes liés à Early Access sur le [forum](https://forum.cursor.com).



# Apply
Source: https://docs.cursor.com/fr/agent/apply

Découvre comment appliquer, accepter ou refuser des suggestions de code depuis le chat avec Apply

<div id="how-apply-works">
  ## Comment fonctionne Apply
</div>

Apply est un modèle Cursor spécialisé qui prend le code généré par le chat et l’intègre dans tes fichiers. Il traite les blocs de code issus des conversations et applique les modifications à ton codebase.

Apply ne génère pas de code lui-même. Le modèle de chat génère le code, et Apply se charge de l’intégration dans les fichiers existants. Il peut traiter des modifications sur plusieurs fichiers et de grands codebases.

<div id="apply-code-blocks">
  ## Appliquer des blocs de code
</div>

Pour appliquer une suggestion de bloc de code, appuie sur le bouton lecture en haut à droite du bloc.

<Frame>
  <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/apply.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=634492fa2f63b4f6eada08b2a1ded47e" data-og-width="1032" width="1032" data-og-height="410" height="410" data-path="images/chat/apply.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/apply.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=7dbc88cfe20429c73e627a289b17c964 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/apply.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=721e2d51bdb16dbb817e19d96d93c9d9 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/apply.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=8faea188ca903e58d347ddfec2c9bf6e 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/apply.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=f3bc38701cab63602b54374dfaa9e024 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/apply.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=fddad51f5b12c32493e2370ed326712d 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/apply.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=1584d431007b33a595905e23b5e1b453 2500w" />
</Frame>



# Points de contrôle
Source: https://docs.cursor.com/fr/agent/chat/checkpoints

Enregistrer et restaurer des états antérieurs après des changements de l’Agent

Les points de contrôle sont des instantanés automatiques des changements de l’Agent dans ta base de code. Ils te permettent d’annuler les modifications de l’Agent si besoin.

<Frame>
  <video src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/restore-checkpoint.mp4?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=7cededf7892f15a6342a81953ea0aa38" autoPlay loop muted playsInline controls data-path="images/chat/restore-checkpoint.mp4" />
</Frame>

<div id="restoring-checkpoints">
  ## Restauration des checkpoints
</div>

Deux façons de restaurer :

1. **Depuis la zone de saisie** : clique sur le bouton `Restore Checkpoint` sur les requêtes précédentes
2. **Depuis un message** : clique sur le bouton + en survolant un message

<Warning>
  Les checkpoints ne remplacent pas le contrôle de version. Utilise Git pour conserver un historique permanent.
</Warning>

<div id="how-they-work">
  ## Comment ça fonctionne
</div>

* Stockés localement, séparément de Git
* Ne suivent que les changements de l’Agent (pas les modifications manuelles)
* Nettoyés automatiquement

<Note>
  Les modifications manuelles ne sont pas suivies. Utilise les checkpoints uniquement pour les changements de l’Agent.
</Note>

<div id="faq">
  ## FAQ
</div>

<AccordionGroup>
  <Accordion title="Les checkpoints affectent-ils Git ?">
    Non. Ils sont distincts de l’historique Git.
  </Accordion>

  {" "}

  <Accordion title="Combien de temps sont-ils conservés ?">
    Pendant la session en cours et l’historique récent. Nettoyage automatique.
  </Accordion>

  <Accordion title="Puis-je les créer manuellement ?">
    Non. Cursor les crée automatiquement.
  </Accordion>
</AccordionGroup>

{" "}



# Commandes
Source: https://docs.cursor.com/fr/agent/chat/commands

Définir des commandes pour des flux de travail réutilisables

Les commandes personnalisées te permettent de créer des workflows réutilisables, déclenchables avec un simple préfixe « / » dans la zone de saisie du chat. Elles aident à standardiser les processus au sein de ton équipe et rendent les tâches courantes plus efficaces.

<Frame>
    <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/commands/input.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=0d25ac517b091210da1c6eff4c8e3098" alt="Commands input example" data-og-width="1689" width="1689" data-og-height="1079" height="1079" data-path="images/chat/commands/input.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/commands/input.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=680f0cbf1491ef1303171dbd18115288 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/commands/input.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=d6a5397e565ab2c90435e6fdd2b7b27a 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/commands/input.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=ae074e2f2b26741544fd8c8ecfa529e3 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/commands/input.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=564aad432affcc04e51b624725f386ad 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/commands/input.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=5c1bd5d49babc2f08eb0efcd24ba7783 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/commands/input.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=3244c3be31c9bc704468a706c6e6b38e 2500w" />
</Frame>

<Info>
  Les commandes sont actuellement en bêta. La fonctionnalité et la syntaxe peuvent évoluer au fur et à mesure que nous les améliorons.
</Info>

<div id="how-commands-work">
  ## Comment fonctionnent les commandes
</div>

Les commandes sont définies comme de simples fichiers Markdown et peuvent être stockées à deux emplacements :

1. **Commandes de projet** : stockées dans le répertoire `.cursor/commands` de ton projet
2. **Commandes globales** : stockées dans le répertoire `~/.cursor/commands` de ton dossier personnel

Quand tu tapes `/` dans le champ de saisie du chat, Cursor détecte et affiche automatiquement les commandes disponibles dans les deux répertoires, ce qui les rend instantanément accessibles dans tout ton workflow.

<div id="creating-commands">
  ## Créer des commandes
</div>

1. Crée un répertoire `.cursor/commands` à la racine de ton projet
2. Ajoute des fichiers `.md` avec des noms explicites (p. ex. `review-code.md`, `write-tests.md`)
3. Écris du contenu Markdown simple décrivant ce que la commande doit faire
4. Les commandes s’afficheront automatiquement dans le chat quand tu tapes `/`

Voici un exemple de la structure que pourrait avoir ton répertoire de commandes :

```
.cursor/
└── commands/
    ├── traiter-les-commentaires-des-PR-GitHub.md
    ├── liste-de-contrôle-revue-de-code.md
    ├── créer-une-PR.md
    ├── revue-rapide-des-diffs-existants.md
    ├── onboard-un-nouveau-développeur.md
    ├── exécuter-tous-les-tests-et-corriger.md
    ├── audit-de-sécurité.md
    └── configurer-une-nouvelle-fonctionnalité.md
```

<div id="examples">
  ## Exemples
</div>

Essaie ces commandes dans tes projets pour te faire une idée de leur fonctionnement.

<AccordionGroup>
  <Accordion title="Liste de contrôle pour la revue de code">
    ```markdown  theme={null}
    # Checklist de revue de code

    ## Vue d’ensemble
    Checklist complète pour mener des revues de code approfondies afin de garantir la qualité, la sécurité et la maintenabilité.

    ## Catégories de revue

    ### Fonctionnalité
    - [ ] Le code fait ce qu’il est censé faire
    - [ ] Les cas limites sont correctement gérés
    - [ ] La gestion des erreurs est appropriée
    - [ ] Pas de bugs évidents ni d’erreurs logiques

    ### Qualité du code
    - [ ] Le code est lisible et bien structuré
    - [ ] Les fonctions sont courtes et ciblées
    - [ ] Les noms de variables sont explicites
    - [ ] Pas de duplication de code
    - [ ] Respecte les conventions du projet

    ### Sécurité
    - [ ] Pas de vulnérabilités de sécurité évidentes
    - [ ] La validation des entrées est en place
    - [ ] Les données sensibles sont correctement traitées
    - [ ] Pas de secrets codés en dur
    ```
  </Accordion>

  <Accordion title="Audit de sécurité">
    ```markdown  theme={null}
    # Audit de sécurité

    ## Vue d’ensemble
    Revue de sécurité complète pour identifier et corriger les vulnérabilités dans la base de code.

    ## Étapes
    1. **Audit des dépendances**
       - Vérifier les vulnérabilités connues
       - Mettre à jour les paquets obsolètes
       - Passer en revue les dépendances tierces

    2. **Revue de la sécurité du code**
       - Rechercher les vulnérabilités courantes
       - Passer en revue l’authentification et l’autorisation
       - Auditer les pratiques de gestion des données

    3. **Sécurité de l’infrastructure**
       - Passer en revue les variables d’environnement
       - Vérifier les contrôles d’accès
       - Auditer la sécurité réseau

    ## Liste de vérification de sécurité
    - [ ] Dépendances à jour et sécurisées
    - [ ] Aucun secret en dur dans le code
    - [ ] Validation des entrées mise en œuvre
    - [ ] Authentification sécurisée
    - [ ] Autorisation correctement configurée
    ```
  </Accordion>

  <Accordion title="Configurer une nouvelle fonctionnalité">
    ```markdown  theme={null}
    # Configurer une nouvelle fonctionnalité

    ## Vue d’ensemble
    Mettre en place une nouvelle fonctionnalité de façon systématique, de la planification initiale jusqu’à la structure d’implémentation.

    ## Étapes
    1. **Définir les exigences**
       - Clarifier le périmètre et les objectifs de la fonctionnalité
       - Identifier les user stories et les critères d’acceptation
       - Planifier l’approche technique

    2. **Créer une branche de fonctionnalité**
       - Partir de main/develop
       - Configurer l’environnement de développement local
       - Configurer toute nouvelle dépendance

    3. **Concevoir l’architecture**
       - Concevoir les modèles de données et les API
       - Planifier les composants UI et les flux
       - Définir la stratégie de test

    ## Liste de contrôle de configuration de la fonctionnalité
    - [ ] Exigences documentées
    - [ ] User stories rédigées
    - [ ] Approche technique définie
    - [ ] Branche de fonctionnalité créée
    - [ ] Environnement de développement prêt
    ```
  </Accordion>

  <Accordion title="Créer une pull request">
    ```markdown  theme={null}
    # Créer une PR

    ## Vue d’ensemble
    Créer une pull request bien structurée avec une description claire, des labels et des reviewers.

    ## Étapes
    1. **Préparer la branche**
       - S’assurer que toutes les modifications sont commitées
       - Pousser la branche vers le dépôt distant
       - Vérifier que la branche est à jour avec main

    2. **Rédiger la description de la PR**
       - Résumer clairement les changements
       - Inclure le contexte et la motivation
       - Lister toute modification cassante
       - Ajouter des captures d’écran si l’UI change

    3. **Configurer la PR**
       - Créer la PR avec un titre descriptif
       - Ajouter les labels appropriés
       - Assigner des reviewers
       - Lier les issues associées

    ## Modèle de PR
    - [ ] Fonctionnalité A
    - [ ] Correction de bug B
    - [ ] Les tests unitaires passent
    - [ ] Tests manuels terminés
    ```
  </Accordion>

  <Accordion title="Lance les tests et corrige les échecs">
    ```markdown  theme={null}
    # Exécuter tous les tests et corriger les échecs

    ## Vue d’ensemble
    Exécuter l’ensemble de la suite de tests et corriger systématiquement tous les échecs afin de garantir la qualité et la fonctionnalité du code.

    ## Étapes
    1. **Exécuter la suite de tests**
       - Exécuter tous les tests du projet
       - Capturer la sortie et identifier les échecs
       - Vérifier les tests unitaires et d’intégration

    2. **Analyser les échecs**
       - Catégoriser par type : instables, cassés, nouveaux échecs
       - Prioriser les correctifs selon l’impact
       - Vérifier si les échecs sont liés aux changements récents

    3. **Corriger les problèmes de manière systématique**
       - Commencer par les échecs les plus critiques
       - Corriger un problème à la fois
       - Relancer les tests après chaque correctif
    ```
  </Accordion>

  <Accordion title="Intégrer un·e nouveau·elle développeur·euse">
    ```markdown  theme={null}
    # Intégrer un·e nouveau·elle développeur·euse

    ## Vue d’ensemble
    Processus d’onboarding complet pour permettre à un·e nouveau·elle développeur·euse d’être opérationnel·le rapidement.

    ## Étapes
    1. **Configuration de l’environnement**
       - Installer les outils requis
       - Configurer l’environnement de développement
       - Configurer l’IDE et les extensions
       - Configurer Git et les clés SSH

    2. **Prise en main du projet**
       - Passer en revue la structure du projet
       - Comprendre l’architecture
       - Lire la documentation principale
       - Configurer la base de données locale

    ## Checklist d’onboarding
    - [ ] Environnement de développement prêt
    - [ ] Tous les tests passent
    - [ ] Peut exécuter l’application en local
    - [ ] Base de données configurée et fonctionnelle
    - [ ] Première PR soumise
    ```
  </Accordion>
</AccordionGroup>



# Compact
Source: https://docs.cursor.com/fr/agent/chat/compact

Gagne de la place dans le chat avec l’interface du mode compact

Le mode compact propose une interface de chat épurée en réduisant le bruit visuel et en maximisant l’espace disponible pour les conversations.

<div id="overview">
  ## Aperçu
</div>

Une fois activé, le mode compact transforme l’interface de chat en :

* **Masquant les icônes** pour une apparence plus épurée et minimaliste
* **Repliant automatiquement les diffs** pour réduire le bruit visuel
* **Repliant automatiquement le champ de saisie** pour maximiser l’espace de conversation

Ce réglage est particulièrement utile sur les petits écrans ou quand tu préfères une expérience de chat focalisée et sans distractions.

<div id="before-and-after">
  ## Avant/après
</div>

<div id="default-mode">
  ### Mode par défaut
</div>

<Frame>
  <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/compact/off.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=e0f8b97ecd5201be396fcd09cec54de6" alt="Interface de chat en mode par défaut, avec toutes les icônes visibles et les éléments développés" data-og-width="2048" width="2048" data-og-height="2350" height="2350" data-path="images/chat/compact/off.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/compact/off.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=9395c8d1f324033631508dc9cdfd6f3e 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/compact/off.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=5d8025ef65ad2fc9fe8c30e5c4fcda32 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/compact/off.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=28050b27b683af948bc1ed939f31786c 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/compact/off.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=dc443705188da9d3368acefd917cc890 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/compact/off.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=be6603e2cedb7e88e7c20d797b18599c 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/compact/off.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=3afe563c9cd4576623adce5dcaaccddf 2500w" />
</Frame>

<div id="compact-mode">
  ### Mode compact
</div>

<Frame>
  <img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/compact/on.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=e9f068889026827422b2a9d943b55ded" alt="Interface de chat en mode compact, avec icônes masquées et éléments repliés" data-og-width="2048" width="2048" data-og-height="2350" height="2350" data-path="images/chat/compact/on.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/compact/on.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=44e86a79eb893b4de6c57c65487bbe9a 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/compact/on.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=539b71c72ed2fb3508e3aec0624429c1 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/compact/on.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=2c0da715a5daf93e94dbf2a5eefbb7eb 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/compact/on.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=b5bddca39109779c9d91bb6bc8bb42e9 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/compact/on.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=8bb334bb055e49d4d51cd137d2396db0 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/compact/on.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=70730d151a24440eeb6dc31e18189c7d 2500w" />
</Frame>

<div id="enabling-compact-mode">
  ## Activer le mode compact
</div>

Pour activer le mode compact :

1. Ouvre les paramètres de Cursor
2. Va dans **Chat**
3. Active **Mode compact**

L’interface se met à jour instantanément avec une vue épurée, te laissant plus d’espace pour te concentrer sur tes conversations.



# Dupliquer
Source: https://docs.cursor.com/fr/agent/chat/duplicate

Crée des branches à partir de n'importe quel point d'une conversation

Duplique ou crée un fork de chats pour explorer des pistes alternatives sans perdre ta conversation actuelle.

<Frame>
  <video src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/duplicate-chat.mp4?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=29fdb23214ba3e2c5b94ccefc01f7615" autoPlay loop muted playsInline controls data-path="images/chat/duplicate-chat.mp4" />
</Frame>

<div id="how-to-duplicate">
  ## Comment dupliquer
</div>

1. Trouve l’endroit où tu veux créer une branche
2. Clique sur les trois points du message
3. Sélectionne « Duplicate Chat »

<div id="what-happens">
  ## Ce qui se passe
</div>

* Le contexte jusqu’à ce point est conservé
* La conversation d’origine reste inchangée
* Les deux discussions conservent des historiques séparés



# Export
Source: https://docs.cursor.com/fr/agent/chat/export

Exporter des chats au format Markdown

Exporte les chats d’Agent en fichiers Markdown pour les partager ou les documenter.

<Frame>
  <video src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/export-chat.mp4?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=c6aa9d23a6a80ffae5864cd494907961" autoPlay loop muted playsInline controls data-path="images/chat/export-chat.mp4" />
</Frame>

<div id="whats-exported">
  ## Ce qui est exporté
</div>

* Tous les messages et les réponses
* Blocs de code avec surlignage syntaxique
* Références de fichiers et contexte
* Déroulé chronologique de la conversation

<div id="how-to-export">
  ## Comment exporter
</div>

1. Va sur le chat à exporter
2. Clique sur le menu contextuel → « Export Chat »
3. Enregistre le fichier en local

<Warning>
  Vérifie les exports pour des données sensibles : clés d’API, URL internes, code propriétaire,
  informations personnelles
</Warning>



# Historique
Source: https://docs.cursor.com/fr/agent/chat/history

Voir et gérer les conversations de chat

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

Accède aux conversations de l’Agent dans le panneau Historique.

<Frame>
  <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/chat-history.jpeg?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=d9ec96fad0c8c2fb132bbf5ce8ea35f7" alt="Historique des discussions" data-og-width="2048" width="2048" data-og-height="1317" height="1317" data-path="images/chat/chat-history.jpeg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/chat-history.jpeg?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=a3ad71e9891c3c9642f4288953a78e97 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/chat-history.jpeg?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=76139a177ebfeb0c55add7fb955f9000 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/chat-history.jpeg?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=1af22180859c017542777ab36b434b7a 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/chat-history.jpeg?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=751e7fa0888e5790f841432ef7521337 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/chat-history.jpeg?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=86b447c18601a9d44af8866d0042719e 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/chat-history.jpeg?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=88c84a8fb1b764ad3070e3211f539408 2500w" />
</Frame>

<div id="opening-history">
  ## Ouvrir l’historique
</div>

* Clique sur l’icône Historique dans le panneau latéral Agent
* Appuie sur <Kbd tooltip="Open chat history">Opt Cmd '</Kbd>

<div id="managing-chats">
  ## Gérer les chats
</div>

* **Modifier les titres** : Clique pour renommer
* **Supprimer** : Supprime les chats inutiles
* **Ouvrir** : Clique pour afficher toute la conversation

L’historique des chats est stocké localement dans une base de données SQLite sur ta machine.

<Note>
  Pour conserver les chats, [exporte-les](/fr/agent/chats/export) au format Markdown.
</Note>

<div id="background-agents">
  ## Agents en arrière-plan
</div>

Les conversations des agents en arrière-plan n’apparaissent pas dans l’historique habituel, elles sont stockées dans une base de données distante. Utilise <Kbd tooltip="Open background agent control panel">Cmd E</Kbd> pour les afficher.

<div id="referencing-past-chats">
  ## Référencer des discussions passées
</div>

Utilise [@Past Chats](/fr/context/@-symbols/@-past-chats) pour ajouter du contexte de conversations précédentes à ton chat actuel.



# Synthèse
Source: https://docs.cursor.com/fr/agent/chat/summarization

Gestion du contexte pour les longues conversations de chat

<div id="message-summarization">
  ## Résumé des messages
</div>

À mesure que les conversations s’allongent, Cursor résume automatiquement et gère le contexte pour que tes chats restent efficaces. Découvre comment utiliser le menu contextuel et comment les fichiers sont condensés pour tenir dans les fenêtres de contexte du modèle.

<div id="using-the-summarize-command">
  ### Utiliser la commande /summarize
</div>

Tu peux lancer manuellement un résumé avec la commande `/summarize` dans le chat. Cette commande aide à gérer le contexte quand les conversations deviennent trop longues, te permettant de continuer à travailler efficacement sans perdre d’informations importantes.

<Info>
  Pour aller plus loin sur le fonctionnement du contexte dans Cursor, consulte notre guide [Working with
  Context](/fr/guides/working-with-context).
</Info>

<div id="how-summarization-works">
  ### Comment fonctionne la synthèse
</div>

Quand les conversations s’allongent, elles finissent par dépasser la limite de la fenêtre de contexte du modèle :

<Frame>
  <div className="font-mono text-xs w-full bg-neutral-100 p-4 rounded-lg">
    <div className="relative">
      <div className="bg-white px-3 py-2 mb-2 rounded border border-dashed border-neutral-400 w-full">
        <div className="text-xs text-neutral-700 font-medium">User</div>
      </div>

      <div className="bg-white px-3 py-2 mb-2 rounded border border-dashed border-neutral-400 w-full">
        <div className="text-xs text-neutral-700 font-medium">Cursor</div>
      </div>

      <div className="bg-white px-3 py-2 mb-2 rounded border border-dashed border-neutral-400 w-full">
        <div className="text-xs text-neutral-700 font-medium">User</div>
      </div>

      <div className="relative my-4">
        <div className="absolute top-0 left-1/2 transform -translate-x-1/2 -translate-y-1/2 text-center text-xs text-black bg-neutral-100 px-2">Limite de la fenêtre de contexte</div>

        <div className="w-full h-px bg-black" />
      </div>

      <div className="bg-white px-3 py-2 mb-2 rounded border border-neutral-400 w-full">
        <div className="text-xs text-neutral-700 font-medium">Cursor</div>
      </div>

      <div className="bg-white px-3 py-2 mb-2 rounded border border-neutral-400 w-full">
        <div className="text-xs text-neutral-700 font-medium">User</div>
      </div>

      <div className="bg-white px-3 py-2 mb-2 rounded border border-neutral-400 w-full">
        <div className="text-xs text-neutral-700 font-medium">Cursor</div>
      </div>
    </div>
  </div>
</Frame>

Pour gérer ça, Cursor résume les anciens messages pour faire de la place aux nouvelles discussions.

<Frame>
  <div className="font-mono text-xs w-full bg-neutral-100 p-4 rounded-lg">
    <div className="relative">
      <div className="relative my-4">
        <div className="absolute top-0 left-1/2 transform -translate-x-1/2 -translate-y-1/2 text-center text-xs text-black bg-neutral-100 px-2">
          Limite de la fenêtre de contexte
        </div>

        <div className="w-full h-px bg-black" />
      </div>

      <div className="bg-neutral-100 px-3 py-2 mb-2 rounded border border-dashed border-neutral-400 w-full">
        <div className="text-xs text-neutral-700 font-medium">
          Messages synthétisés
        </div>
      </div>

      <div className="bg-white px-3 py-2 mb-2 rounded border border-neutral-400 w-full">
        <div className="text-xs text-neutral-700 font-medium">Cursor</div>
      </div>

      <div className="bg-white px-3 py-2 mb-2 rounded border border-neutral-400 w-full">
        <div className="text-xs text-neutral-700 font-medium">User</div>
      </div>

      <div className="bg-white px-3 py-2 mb-2 rounded border border-neutral-400 w-full">
        <div className="text-xs text-neutral-700 font-medium">Cursor</div>
      </div>
    </div>
  </div>
</Frame>

<div id="file-folder-condensation">
  ## Condensation des fichiers et des dossiers
</div>

Tandis que le résumé de chat gère les longues conversations, Cursor utilise une autre stratégie pour traiter les fichiers et dossiers volumineux : la **condensation intelligente**. Quand tu ajoutes des fichiers à ta conversation, Cursor détermine la meilleure façon de les présenter en fonction de leur taille et de l’espace de contexte disponible.

Voici les différents états possibles pour un fichier ou un dossier :

<div id="condensed">
  ### Condensé
</div>

Quand des fichiers ou des dossiers sont trop volumineux pour tenir dans la fenêtre de contexte, Cursor les condense automatiquement. Le condensé expose au modèle les éléments structurants clés comme les signatures de fonctions, les classes et les méthodes. Depuis cette vue condensée, le modèle peut choisir d’agrandir des fichiers précis si besoin. Cette approche optimise l’usage de la fenêtre de contexte disponible.

<Frame>
  <img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/context-management/condensed.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=0c3a07b6fef6402945138f7ee38b44c1" alt="Menu contextuel" data-og-width="1226" width="1226" data-og-height="793" height="793" data-path="images/context/context-management/condensed.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/context-management/condensed.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=4cc08626f9cfce1d186cdd6aa96c7d09 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/context-management/condensed.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=fa49ce9605bdb0186c98712f4c0a32cc 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/context-management/condensed.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=84874b2f40bff0a2cd54796865469914 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/context-management/condensed.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=050290a85c154e92f9298883afcdf892 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/context-management/condensed.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=f953aa28f11926b2d6fdf734cf928402 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/context-management/condensed.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=50aa9973ccf2027814860f3d97a2b031 2500w" />
</Frame>

<div id="significantly-condensed">
  ### Fortement condensé
</div>

Quand un nom de fichier apparaît avec la mention « Fortement condensé », le fichier est trop volumineux pour être inclus en entier, même sous forme condensée. Seul le nom du fichier sera affiché au modèle.

<div id="not-included">
  ### Non inclus
</div>

Lorsqu’une icône d’avertissement apparaît à côté d’un fichier ou d’un dossier, l’élément est trop volumineux pour être inclus dans la fenêtre de contexte, même sous forme condensée. Ça t’aide à voir quelles parties de ta base de code sont accessibles au modèle.

<Frame>
  <img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/context-management/not-included.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=06df9854c74c257d1ceb7d18b1864ceb" alt="Menu de contexte" data-og-width="1090" width="1090" data-og-height="346" height="346" data-path="images/context/context-management/not-included.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/context-management/not-included.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=072e75878f27a151f1310007d0e5e534 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/context-management/not-included.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=c6f3f71351ddf8e367096651b455bf9d 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/context-management/not-included.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=c407f7870412007549f8eb2871f9ca12 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/context-management/not-included.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=b0d17023b5734c8d7584c56f5419bd1a 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/context-management/not-included.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=f1bedff398cee6c957fe62877f7d2012 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/context-management/not-included.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=8b00fbaff658c384f69bfddf3f3a4cfe 2500w" />
</Frame>



# Onglets
Source: https://docs.cursor.com/fr/agent/chat/tabs

Exécuter plusieurs conversations avec l’Agent simultanément

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

<Frame>
  <video src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/chat-tabs.mp4?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=57fd5305279dc0a3139055b353ce4b7a" autoPlay loop muted playsInline controls data-path="images/chat/chat-tabs.mp4" />
</Frame>

<div id="overview">
  ## Vue d’ensemble
</div>

Appuie sur <Kbd>Cmd+T</Kbd> pour créer de nouveaux onglets. Chaque onglet conserve séparément l’historique de conversation, le contexte et le modèle sélectionné.

<Tip>
  Pour des workflows parallèles, essaie [Background Agents](/fr/background-agents)
</Tip>

<div id="managing-tabs">
  ## Gérer les onglets
</div>

* Crée de nouveaux onglets avec <Kbd>Cmd+T</Kbd>. Chaque onglet démarre une nouvelle conversation et conserve son propre contexte.

* Passe d’un onglet à l’autre en cliquant sur leur en-tête ou en utilisant <Kbd>Ctrl+Tab</Kbd> pour les parcourir.

* Les titres des onglets sont générés automatiquement après le premier message, mais tu peux les renommer en faisant un clic droit sur l’en-tête de l’onglet.

<Tip>
  Utilise une tâche par onglet, fournis des descriptions initiales claires et ferme les
  onglets terminés pour garder ton espace de travail organisé.
</Tip>

<div id="conflicts">
  ### Conflits
</div>

Cursor empêche plusieurs onglets de modifier les mêmes fichiers. Tu devras résoudre les conflits lorsqu’ils surviennent.

## Référencer d'autres chats

Utilise [@Past Chats](/fr/context/@-symbols/@-past-chats) pour inclure du contexte provenant d'autres onglets ou de sessions précédentes.



# Modes
Source: https://docs.cursor.com/fr/agent/modes

Choisis le mode adapté à ta tâche – du codage autonome aux éditions ciblées

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

Agent propose différents modes optimisés pour des tâches spécifiques. Chaque mode offre des capacités et des outils différents, activés pour s’adapter à ton workflow.

<div className="full-width-table">
  | Mode                  | Pour                                    | Capacités                                                  | Outils                         |
  | :-------------------- | :-------------------------------------- | :--------------------------------------------------------- | :----------------------------- |
  | **[Agent](#agent)**   | Fonctionnalités complexes, refactoring  | Exploration autonome, modifications multi‑fichiers         | Tous les outils activés        |
  | **[Ask](#ask)**       | Apprentissage, planification, questions | Exploration en lecture seule, aucun changement automatique | Outils de recherche uniquement |
  | **[Custom](#custom)** | Workflows spécialisés                   | Capacités définies par l’utilisateur                       | Configurable                   |
</div>

<div id="agent">
  ## Agent
</div>

Le mode par défaut pour les tâches de codage complexes. Agent explore ta base de code de manière autonome, modifie plusieurs fichiers, exécute des commandes et corrige les erreurs pour répondre à tes demandes.

<Frame>
  <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/agent.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=9cd06dd9f59e019b3d76aa0fd9f934ba" data-og-width="3600" width="3600" data-og-height="2025" height="2025" data-path="images/chat/agent.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/agent.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=d979435c61e2112ebcb784f16a49327f 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/agent.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=1a88e2085ffe80f02daea9a523887282 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/agent.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=de98a8bf766c3f35a6187e87190e30f9 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/agent.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=8648638c4240b718e0512a6ec2274171 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/agent.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=45b9898d65f5b425d276eaa44d4e1940 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/agent.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=30fef2b190d453ee0166e554a4005bd1 2500w" />
</Frame>

<div id="ask">
  ## Ask
</div>

Mode lecture seule pour apprendre et explorer. Ask parcourt ton code et fournit des réponses sans rien modifier — parfait pour comprendre le code avant d’y toucher.

<Frame>
  <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/ask.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=15e531cb84f0a18228723870fd84fa4f" data-og-width="3600" width="3600" data-og-height="2025" height="2025" data-path="images/chat/ask.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/ask.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=592ac5a681910a075ae88dec89bee25d 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/ask.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=74b98cce3b5bb83c79d0566cd3c65c34 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/ask.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=c4d80f50e20e7ca28db5a3ee71718979 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/ask.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=a4a6e017fd64149cf68d997114bbf6b6 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/ask.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=7354479ecd644b86ddbcb9fe1131f100 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/ask.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=274125e614eadd17522e0dacfcc6a38e 2500w" />
</Frame>

<div id="custom">
  ## Personnalisé
</div>

Crée tes propres modes avec des combinaisons d’outils et des instructions spécifiques. Combine les capacités pour les adapter à ton workflow.

<Note>
  Les modes personnalisés sont en bêta. Active-les dans `Cursor Settings` → `Chat` → `Custom
      Modes`
</Note>

<div id="examples">
  ### Exemples
</div>

<AccordionGroup>
  <Accordion title="Learn">
    **Outils :** All Search\
    **Instructions :** Explique les concepts en profondeur et pose des questions pour clarifier
  </Accordion>

  {" "}

  <Accordion title="Refactor">
    **Outils :** Edit & Reapply **Instructions :** Améliore la structure du code sans
    ajouter de nouvelles fonctionnalités
  </Accordion>

  {" "}

  <Accordion title="Plan">
    **Outils :** Codebase, Read file, Terminal **Instructions :** Crée des plans d’implémentation détaillés dans `plan.md`
  </Accordion>

  <Accordion title="Debug">
    **Outils :** All Search, Terminal, Edit & Reapply\
    **Instructions :** Analyse les problèmes en profondeur avant de proposer des correctifs
  </Accordion>
</AccordionGroup>

<div id="switching-modes">
  ## Changer de mode
</div>

* Utilise le sélecteur de mode (menu déroulant) dans Agent
* Appuie sur <Kbd>Cmd+.</Kbd> pour basculer rapidement
* Configure des raccourcis clavier dans les [réglages](#settings)

<div id="settings">
  ## Paramètres
</div>

Tous les modes partagent des options de configuration communes :

<div className="full-width-table">
  | Paramètre          | Description                                |
  | :----------------- | :----------------------------------------- |
  | Modèle             | Choisir le modèle d’IA à utiliser          |
  | Raccourcis clavier | Définir des raccourcis pour passer de mode |
</div>

Paramètres propres à chaque mode :

<div className="full-width-table">
  | Mode       | Paramètres                        | Description                                                           |
  | :--------- | :-------------------------------- | :-------------------------------------------------------------------- |
  | **Agent**  | Exécution auto et correction auto | Exécuter automatiquement les commandes et corriger les erreurs        |
  | **Ask**    | Recherche dans le codebase        | Trouver automatiquement les fichiers pertinents                       |
  | **Custom** | Sélection d’outils & instructions | Configurer les [outils](/fr/agent/tools) et des prompts personnalisés |
</div>



# Vue d’ensemble
Source: https://docs.cursor.com/fr/agent/overview

Assistant pour les tâches de code autonomes, les commandes du terminal et l’édition de code

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

Agent est l’assistant de Cursor qui peut accomplir de façon autonome des tâches de code complexes, exécuter des commandes dans le terminal et modifier du code. Accès dans le panneau latéral avec <Kbd>Cmd+I</Kbd>.

<Frame caption="Agent dans le panneau latéral">
  <video src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/overview.mp4?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=b17d6a1225b4992ea19978b6a6c259e1" autoPlay loop muted playsInline data-path="images/chat/overview.mp4" />
</Frame>

<div className="mt-24 flex flex-col gap-12">
  <Columns className="gap-4">
    <div>
      <h2 className="text-lg font-medium mb-2">
        <a href="/fr/agent/modes" className="hover:text-primary transition-colors">
          Modes
        </a>
      </h2>

      <p className="text-sm">
        Choisis entre Agent, Ask, ou crée des modes personnalisés. Chaque mode offre
        des fonctionnalités et des outils différents pour s’adapter à ton workflow.
      </p>
    </div>

    <Frame>
      <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/agent.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=9cd06dd9f59e019b3d76aa0fd9f934ba" alt="Modes de l’Agent" data-og-width="3600" width="3600" data-og-height="2025" height="2025" data-path="images/chat/agent.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/agent.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=d979435c61e2112ebcb784f16a49327f 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/agent.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=1a88e2085ffe80f02daea9a523887282 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/agent.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=de98a8bf766c3f35a6187e87190e30f9 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/agent.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=8648638c4240b718e0512a6ec2274171 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/agent.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=45b9898d65f5b425d276eaa44d4e1940 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/agent.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=30fef2b190d453ee0166e554a4005bd1 2500w" />
    </Frame>
  </Columns>

  <Columns className="gap-4">
    <div>
      <h3 className="text-lg font-medium mb-2">
        <a href="/fr/agent/tools" className="hover:text-primary transition-colors">
          Outils
        </a>
      </h3>

      <p className="text-sm">
        Agent s’appuie sur des outils pour chercher, modifier et exécuter des commandes. De la recherche sémantique dans le code à l’exécution dans le terminal, ces outils permettent d’accomplir des tâches de façon autonome.
      </p>
    </div>

    <div>
      <Frame>
        <img src="https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=3135722076a5aa636d27dbedec665bae" alt="Outils d’Agent" data-og-width="1624" width="1624" data-og-height="1012" height="1012" data-path="images/agent/auto-run.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=280&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=9f2e2bed8f634201adc51ccb2bd96cd2 280w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=560&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=51704cac2f270a04856fffbeaccf9700 560w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=840&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=01a5034975497a8dff4f41dca0d19f2e 840w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=1100&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=5f19026a0c6e5fb28c935ce795edb706 1100w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=1650&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=a108fc86f8ee7c0db6e5b7ab80ede738 1650w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=2500&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=9ce5f45879c29049640bb5a1494db11e 2500w" />
      </Frame>
    </div>
  </Columns>

  <Columns className="gap-4">
    <div>
      <h3 className="text-lg font-medium mb-2">
        <a href="/fr/agent/apply" className="hover:text-primary transition-colors">
          Appliquer les modifications
        </a>
      </h3>

      <p className="text-sm">
        Intègre des blocs de code proposés par l’IA à ta base de code. Apply gère
        les modifications à grande échelle avec efficacité tout en restant précis.
      </p>
    </div>

    <div>
      <Frame>
        <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/apply.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=634492fa2f63b4f6eada08b2a1ded47e" alt="Appliquer les modifications" data-og-width="1032" width="1032" data-og-height="410" height="410" data-path="images/chat/apply.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/apply.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=7dbc88cfe20429c73e627a289b17c964 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/apply.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=721e2d51bdb16dbb817e19d96d93c9d9 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/apply.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=8faea188ca903e58d347ddfec2c9bf6e 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/apply.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=f3bc38701cab63602b54374dfaa9e024 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/apply.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=fddad51f5b12c32493e2370ed326712d 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/apply.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=1584d431007b33a595905e23b5e1b453 2500w" />
      </Frame>
    </div>
  </Columns>

  <Columns className="gap-4">
    <div>
      <h3 className="text-lg font-medium mb-2">
        <a href="/fr/agent/review" className="hover:text-primary transition-colors">
          Examiner les diffs
        </a>
      </h3>

      <p className="text-sm">
        Examine les changements avant de les accepter. L’interface de revue affiche les ajouts
        et les suppressions avec un code couleur pour garder le contrôle sur les modifications.
      </p>
    </div>

    <div>
      <Frame>
        <video src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/review/review-bar.mp4?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=5dca0fe7aba3c79e6760cb264821a617" autoPlay loop muted playsInline controls data-path="images/chat/review/review-bar.mp4" />
      </Frame>
    </div>
  </Columns>

  <Columns className="gap-4">
    <div>
      <h3 className="text-lg font-medium mb-2">
        <a href="/fr/agent/chats/tabs" className="hover:text-primary transition-colors">
          Onglets de chat
        </a>
      </h3>

      <p className="text-sm">
        Lance plusieurs conversations en parallèle avec <Kbd>Cmd+T</Kbd>. Chaque onglet
        garde son propre contexte, son historique et son modèle sélectionné.
      </p>
    </div>

    <div>
      <Frame>
        <video src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/chat-tabs.mp4?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=57fd5305279dc0a3139055b353ce4b7a" autoPlay loop muted playsInline controls data-path="images/chat/chat-tabs.mp4" />
      </Frame>
    </div>
  </Columns>

  <Columns className="gap-4">
    <div>
      <h3 className="text-lg font-medium mb-2">
        <a href="/fr/agent/chats/checkpoints" className="hover:text-primary transition-colors">
          Points de contrôle
        </a>
      </h3>

      <p className="text-sm">
        Des captures automatiques suivent les modifications de l’Agent. Restaure un état précédent si
        les changements ne fonctionnent pas comme prévu, ou pour essayer d’autres approches.
      </p>
    </div>

    <div>
      <Frame>
        <video src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/restore-checkpoint.mp4?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=7cededf7892f15a6342a81953ea0aa38" autoPlay loop muted playsInline controls data-path="images/chat/restore-checkpoint.mp4" />
      </Frame>
    </div>
  </Columns>

  <Columns className="gap-4">
    <div>
      <h3 className="text-lg font-medium mb-2">
        <a href="/fr/agent/terminal" className="hover:text-primary transition-colors">
          Intégration au terminal
        </a>
      </h3>

      <p className="text-sm">
        Agent exécute des commandes dans le terminal, suit la sortie et gère les
        processus en plusieurs étapes. Configure l’exécution auto pour les workflows de confiance ou demande
        une confirmation pour plus de sécurité.
      </p>
    </div>

    <div>
      <Frame>
        <img src="https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=3135722076a5aa636d27dbedec665bae" alt="Intégration au terminal" data-og-width="1624" width="1624" data-og-height="1012" height="1012" data-path="images/agent/auto-run.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=280&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=9f2e2bed8f634201adc51ccb2bd96cd2 280w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=560&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=51704cac2f270a04856fffbeaccf9700 560w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=840&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=01a5034975497a8dff4f41dca0d19f2e 840w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=1100&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=5f19026a0c6e5fb28c935ce795edb706 1100w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=1650&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=a108fc86f8ee7c0db6e5b7ab80ede738 1650w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=2500&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=9ce5f45879c29049640bb5a1494db11e 2500w" />
      </Frame>
    </div>
  </Columns>

  <Columns className="gap-4">
    <div>
      <h3 className="text-lg font-medium mb-2">
        <a href="/fr/agent/chats/history" className="hover:text-primary transition-colors">
          Historique des conversations
        </a>
      </h3>

      <p className="text-sm">
        Accède aux conversations précédentes avec <Kbd>Opt Cmd '</Kbd>. Passe en revue
        les discussions passées, suis tes sessions de code et retrouve le contexte des
        échanges antérieurs.
      </p>
    </div>

    <div>
      <Frame>
        <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/chat-history.jpeg?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=d9ec96fad0c8c2fb132bbf5ce8ea35f7" alt="Historique des conversations" data-og-width="2048" width="2048" data-og-height="1317" height="1317" data-path="images/chat/chat-history.jpeg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/chat-history.jpeg?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=a3ad71e9891c3c9642f4288953a78e97 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/chat-history.jpeg?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=76139a177ebfeb0c55add7fb955f9000 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/chat-history.jpeg?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=1af22180859c017542777ab36b434b7a 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/chat-history.jpeg?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=751e7fa0888e5790f841432ef7521337 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/chat-history.jpeg?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=86b447c18601a9d44af8866d0042719e 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/chat-history.jpeg?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=88c84a8fb1b764ad3070e3211f539408 2500w" />
      </Frame>
    </div>
  </Columns>

  <Columns className="gap-4">
    <div>
      <h3 className="text-lg font-medium mb-2">
        <a href="/fr/agent/chats/export" className="hover:text-primary transition-colors">
          Exporter des chats
        </a>
      </h3>

      <p className="text-sm">
        Exporte des conversations au format Markdown. Partage des solutions avec ton équipe,
        documente des décisions ou crée des bases de connaissances à partir de sessions de code.
      </p>
    </div>

    <div>
      <Frame>
        <video src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/export-chat.mp4?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=c6aa9d23a6a80ffae5864cd494907961" autoPlay loop muted playsInline controls data-path="images/chat/export-chat.mp4" />
      </Frame>
    </div>
  </Columns>

  <Columns className="gap-4">
    <div>
      <h3 className="text-lg font-medium mb-2">
        <a href="/fr/context/rules" className="hover:text-primary transition-colors">
          Règles
        </a>
      </h3>

      <p className="text-sm">
        Définis des instructions personnalisées pour le comportement d’Agent. Les règles aident à maintenir
        les normes de code, à faire respecter des patterns, et à personnaliser la façon dont Agent t’aide sur
        ton projet.
      </p>
    </div>

    <div>
      <Frame>
        <img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rules-applied.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=e637bab83cfd5dcc8a3b15ed6fd9fc15" alt="Règles d’Agent" data-og-width="1198" width="1198" data-og-height="674" height="674" data-path="images/context/rules/rules-applied.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rules-applied.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=78e3c392987c6f95a02fc106753c5f98 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rules-applied.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=9d3a8b76ba99ada5ca302cba9fb63810 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rules-applied.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=f5ab7fb374a1a4c5fe2f50e2e50d233a 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rules-applied.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=5d25394a29c1da4172a3e673ee384c07 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rules-applied.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=0fc125bd3c2a93551674252c0523d3ec 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rules-applied.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=c576ea053ee18c30d2781c6bdd394a70 2500w" />
      </Frame>
    </div>
  </Columns>
</div>



# Planification
Source: https://docs.cursor.com/fr/agent/planning

Comment Agent planifie et gère des tâches complexes avec des tâches à faire et la mise en file d’attente

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

Agent peut anticiper et gérer des tâches complexes grâce à des listes de tâches structurées et à la mise en file d’attente des messages, ce qui rend les tâches de longue haleine plus faciles à comprendre et à suivre.

<div id="agent-to-dos">
  ## To-dos de l’Agent
</div>

Agent peut découper des tâches longues en étapes gérables avec des dépendances et créer un plan structuré qui se met à jour au fur et à mesure de l’avancement.

<video autoPlay loop muted playsInline controls>
  <source src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/agent/planning/agent-todo.mp4?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=b0285913832a3ef123fe149516ee37ea" type="video/mp4" data-path="images/agent/planning/agent-todo.mp4" />
</video>

<div id="how-it-works">
  ### Comment ça marche
</div>

* Agent génère automatiquement des listes de to-dos pour les tâches complexes
* Chaque élément peut dépendre d’autres tâches
* La liste se met à jour en temps réel à mesure que le travail progresse
* Les tâches terminées sont automatiquement cochées

<div id="visibility">
  ### Visibilité
</div>

* Les to-dos apparaissent dans l’interface de chat
* Si l’intégration [Slack](/fr/slack) est configurée, les to-dos y sont visibles aussi
* Tu peux consulter le découpage complet de la tâche à tout moment

<Tip>
  Pour une meilleure planification, décris clairement ton objectif final. Agent créera des
  découpages de tâches plus précis quand il comprend l’ensemble du périmètre.
</Tip>

<Note>La planification et les to-dos ne sont pas pris en charge pour le mode auto pour le moment.</Note>

## Messages en file d'attente

Mets en file d'attente des messages de suivi pendant qu'Agent travaille sur la tâche en cours. Tes instructions attendent leur tour et s'exécutent automatiquement dès qu'elles sont prêtes.

<video autoPlay loop muted playsInline controls>
  <source src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/agent/planning/agent-queue.mp4?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=4cdd6a7d1e12c67e520bc3ba67a42e0d" type="video/mp4" data-path="images/agent/planning/agent-queue.mp4" />
</video>

### Utiliser la file d'attente

1. Pendant qu'Agent travaille, tape ta prochaine instruction
2. Appuie sur <Kbd>Ctrl+Enter</Kbd> pour l’ajouter à la file d’attente
3. Les messages apparaissent dans l’ordre sous la tâche active
4. Réorganise les messages en file d’attente en cliquant sur la flèche
5. Agent les traite séquentiellement après avoir terminé

### Outrepasser la file d'attente

Pour mettre ton message en file d’attente au lieu d’utiliser la messagerie par défaut, utilise <Kbd>Ctrl+Enter</Kbd>. Pour envoyer un message immédiatement sans le mettre en file d’attente, utilise <Kbd>Cmd+Enter</Kbd>. Cela force l’envoi de ton message, en contournant la file d’attente pour l’exécuter tout de suite.

<div id="default-messaging">
  ## Messagerie par défaut
</div>

Par défaut, les messages sont envoyés aussi vite que possible et apparaissent généralement juste après qu’Agent a terminé un appel d’outil. Ça offre l’expérience la plus réactive.

<div id="how-default-messaging-works">
  ### Comment fonctionne la messagerie par défaut
</div>

* Ton message est ajouté au dernier message de l’utilisateur dans le chat
* Les messages se rattachent généralement aux résultats d’outil et s’envoient immédiatement dès qu’ils sont prêts
* Ça crée un flux de conversation plus naturel sans interrompre le travail en cours d’Agent
* Par défaut, ça se produit quand tu appuies sur Entrée pendant qu’Agent travaille



# Diffs & Review
Source: https://docs.cursor.com/fr/agent/review

Examiner et gérer les modifications de code générées par l’agent IA

Quand Agent génère des modifications de code, elles s’affichent dans une interface de revue qui montre ajouts et suppressions avec des lignes colorées. Ça te permet d’examiner et de contrôler quelles modifications sont appliquées à ton codebase.

L’interface de revue affiche les modifications de code dans un format diff familier :

<div id="diffs">
  ## Diffs
</div>

<div className="full-width-table">
  | Type              | Signification             | Exemple                                                                                               |
  | :---------------- | :------------------------ | :---------------------------------------------------------------------------------------------------- |
  | **Added lines**   | Ajouts de code            | <code className="bg-green-100 text-green-800 px-2 py-1 rounded">+ const newVariable = 'hello';</code> |
  | **Deleted lines** | Suppressions de code      | <code className="bg-red-100 text-red-800 px-2 py-1 rounded">- const oldVariable = 'goodbye';</code>   |
  | **Context lines** | Code de contexte inchangé | <code className="bg-gray-100 text-gray-600 px-2 py-1 rounded"> function example() {}</code>           |
</div>

<div id="review">
  ## Revue
</div>

Une fois la génération terminée, tu verras une invite pour passer en revue tous les changements avant de continuer. Ça te donne un aperçu de ce qui va être modifié.

<Frame>
  <img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/review/input-review.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=10633167c76c24c1e69748ef93dc3888" alt="Interface de revue de l'entrée" data-og-width="2095" width="2095" data-og-height="1178" height="1178" data-path="images/chat/review/input-review.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/review/input-review.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=f462337898ca48f71cd2b570b140d30d 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/review/input-review.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=07c91dfc92110cce444da8bbf3d0b3b5 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/review/input-review.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=492522862dabae6243fa8d33f6fd77f2 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/review/input-review.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=c897e19ce7f508bad4e24fcf8efb2512 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/review/input-review.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=3956c2d2c5c9156181b19e262e301b5b 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/review/input-review.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=907f90b1db432128964a7f4e59523bb6 2500w" />
</Frame>

<div id="file-by-file">
  ### Fichier par fichier
</div>

Une barre de revue flottante apparaît en bas de ton écran, te permettant de :

* **Accepter** ou **rejeter** les changements pour le fichier en cours
* Passer au **fichier suivant** avec des changements en attente
  <Frame>
    <video src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/review/review-bar.mp4?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=5dca0fe7aba3c79e6760cb264821a617" autoPlay loop muted playsInline controls data-path="images/chat/review/review-bar.mp4">
      Your browser does not support the video tag.
    </video>
  </Frame>

<div id="selective-acceptance">
  ### Acceptation sélective
</div>

Pour un contrôle fin :

* Pour accepter la plupart des changements : rejette les lignes indésirables, puis clique sur **Tout accepter**
* Pour rejeter la plupart des changements : accepte les lignes souhaitées, puis clique sur **Tout rejeter**

<div id="review-changes">
  ## Passer en revue les modifications
</div>

À la fin de la réponse de l’agent, clique sur le bouton **Review changes** pour afficher le diff complet des modifications.

<Frame>
  <video src="https://www.cursor.com/changelog/049/review-ui.mp4" autoPlay loop muted playsInline controls />
</Frame>



# Terminal
Source: https://docs.cursor.com/fr/agent/terminal

Exécuter automatiquement des commandes du terminal dans le cadre des opérations de l’agent

L’agent exécute des commandes dans le terminal natif de Cursor en conservant l’historique. Clique sur Skip pour envoyer <kbd>Ctrl+C</kbd> et interrompre les commandes.

<div id="troubleshooting">
  ## Dépannage
</div>

<Info>
  Certains thèmes de shell (par exemple Powerlevel9k/Powerlevel10k) peuvent perturber
  l’affichage du terminal intégré. Si la sortie de ta commande paraît tronquée ou
  mal mise en forme, désactive le thème ou passe à une invite plus simple pendant l’exécution d’Agent.
</Info>

<div id="disable-heavy-prompts-for-agent-sessions">
  ### Désactiver les invites lourdes pour les sessions Agent
</div>

Utilise la variable d’environnement `CURSOR_AGENT` dans ta config shell pour détecter quand
Agent tourne et ignorer l’initialisation des invites/thèmes sophistiqués.

```zsh  theme={null}

# ~/.zshrc — désactiver Powerlevel10k lorsque Cursor Agent est en cours d’exécution
if [[ -n "$CURSOR_AGENT" ]]; then
  # Ignorer l’initialisation du thème pour une meilleure compatibilité
else
  [[ -r ~/.p10k.zsh ]] && source ~/.p10k.zsh
fi
```

```bash  theme={null}

# ~/.bashrc — revenir à une invite simple dans les sessions Agent
if [[ -n "$CURSOR_AGENT" ]]; then
  PS1='\u@\h \W \$ '
fi
```



# Outils
Source: https://docs.cursor.com/fr/agent/tools

Outils disponibles pour les agents pour rechercher, modifier et exécuter du code

La liste de tous les outils disponibles pour les modes de l’[Agent](/fr/agent/overview), que tu peux activer ou désactiver lorsque tu crées tes propres [modes personnalisés](/fr/agent/modes#custom).

<Note>
  Il n’y a aucune limite au nombre d’appels d’outils que l’Agent peut effectuer pendant une tâche. L’Agent continuera d’utiliser les outils nécessaires pour accomplir ta demande.
</Note>

<div id="search">
  ## Recherche
</div>

Outils pour explorer ta base de code et le web afin de trouver des infos pertinentes.

<AccordionGroup>
  <Accordion title="Read File" icon="file-lines">
    Lit jusqu’à 250 lignes (750 en mode max) d’un fichier.
  </Accordion>

  <Accordion title="List Directory" icon="folder-open">
    Lit la structure d’un répertoire sans lire le contenu des fichiers.
  </Accordion>

  <Accordion title="Codebase" icon="database">
    Effectue des recherches sémantiques dans ta [base de code
    indexée](/fr/context/codebase-indexing).
  </Accordion>

  <Accordion title="Grep" icon="magnifying-glass">
    Cherche des mots-clés ou des motifs exacts dans les fichiers.
  </Accordion>

  <Accordion title="Search Files" icon="file-magnifying-glass">
    Trouve des fichiers par nom via une correspondance approximative (fuzzy matching).
  </Accordion>

  <Accordion title="Web" icon="globe">
    Génère des requêtes et effectue des recherches sur le web.
  </Accordion>

  <Accordion title="Fetch Rules" icon="gavel">
    Récupère des [règles](/fr/context/rules) spécifiques selon le type et la description.
  </Accordion>
</AccordionGroup>

<div id="edit">
  ## Modification
</div>

Outils pour apporter des modifications ciblées à tes fichiers et à ton codebase.

<AccordionGroup>
  <Accordion title="Modifier et réappliquer" icon="pencil">
    Suggère des modifications aux fichiers et [applique](/fr/agent/apply) ces modifications automatiquement.
  </Accordion>

  <Accordion title="Supprimer des fichiers" icon="trash">
    Supprime des fichiers de façon autonome (désactivable dans les paramètres).
  </Accordion>
</AccordionGroup>

<div id="run">
  ## Exécution
</div>

Le chat peut interagir avec ton terminal.

<AccordionGroup>
  <Accordion title="Terminal" icon="terminal">
    Exécute des commandes dans le terminal et surveille la sortie.
  </Accordion>
</AccordionGroup>

<Note>Par défaut, Cursor utilise le premier profil de terminal disponible.</Note>

Pour définir ton profil de terminal préféré :

1. Ouvre la palette de commandes (`Cmd/Ctrl+Shift+P`)
2. Recherche « Terminal : Select Default Profile »
3. Choisis le profil que tu veux

<div id="mcp">
  ## MCP
</div>

Chat peut utiliser des serveurs MCP configurés pour interagir avec des services externes, comme des bases de données ou des API tierces.

<AccordionGroup>
  <Accordion title="Activer/désactiver les serveurs MCP" icon="server">
    Active ou désactive les serveurs MCP disponibles. Respecte la configuration d’exécution automatique.
  </Accordion>
</AccordionGroup>

En savoir plus sur le [Model Context Protocol](/fr/context/model-context-protocol) et explore les serveurs disponibles dans l’[annuaire MCP](/fr/tools).

<div id="advanced-options">
  ## Options avancées
</div>

<AccordionGroup>
  <Accordion title="Application auto des modifications" icon="check">
    Appliquer automatiquement les modifications sans confirmation manuelle.
  </Accordion>

  <Accordion title="Exécution auto" icon="play">
    Exécuter automatiquement les commandes du terminal et accepter les modifications. Pratique pour lancer des suites de tests et vérifier les changements.

    <Frame>
      <img src="https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=3135722076a5aa636d27dbedec665bae" data-og-width="1624" width="1624" data-og-height="1012" height="1012" data-path="images/agent/auto-run.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=280&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=9f2e2bed8f634201adc51ccb2bd96cd2 280w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=560&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=51704cac2f270a04856fffbeaccf9700 560w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=840&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=01a5034975497a8dff4f41dca0d19f2e 840w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=1100&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=5f19026a0c6e5fb28c935ce795edb706 1100w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=1650&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=a108fc86f8ee7c0db6e5b7ab80ede738 1650w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=2500&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=9ce5f45879c29049640bb5a1494db11e 2500w" />
    </Frame>
  </Accordion>

  <Accordion title="Garde-fous" icon="shield">
    Configurer des listes autorisées pour spécifier quels outils peuvent s’exécuter automatiquement. Les listes autorisées renforcent la sécurité en définissant explicitement les opérations permises.
  </Accordion>

  <Accordion title="Correction auto des erreurs" icon="wrench">
    Corriger automatiquement les erreurs et avertissements du linter lorsqu’Agent les rencontre.
  </Accordion>
</AccordionGroup>



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



# Ajouter un suivi
Source: https://docs.cursor.com/fr/background-agent/api/add-followup

en/background-agent/api/openapi.yaml post /v0/agents/{id}/followup
Envoyer une instruction supplémentaire à un agent d’arrière-plan en cours d’exécution.




# Conversation de l’agent
Source: https://docs.cursor.com/fr/background-agent/api/agent-conversation

en/background-agent/api/openapi.yaml get /v0/agents/{id}/conversation
Récupère l’historique de conversation d’un agent en arrière-plan.

Si l’agent en arrière-plan a été supprimé, tu ne peux pas accéder à la conversation.



# Statut de l’agent
Source: https://docs.cursor.com/fr/background-agent/api/agent-status

en/background-agent/api/openapi.yaml get /v0/agents/{id}
Récupère l’état actuel et les résultats d’un agent en arrière-plan spécifique.




# Infos sur la clé API
Source: https://docs.cursor.com/fr/background-agent/api/api-key-info

en/background-agent/api/openapi.yaml get /v0/me
Récupérer les métadonnées de la clé API utilisée pour l’authentification.




# Supprimer un agent
Source: https://docs.cursor.com/fr/background-agent/api/delete-agent

en/background-agent/api/openapi.yaml delete /v0/agents/{id}
Supprimer définitivement un agent d’arrière-plan et ses ressources associées.




# Lancer un agent
Source: https://docs.cursor.com/fr/background-agent/api/launch-an-agent

en/background-agent/api/openapi.yaml post /v0/agents
Lance un nouvel agent en arrière-plan pour travailler sur ton dépôt.




# Liste des agents
Source: https://docs.cursor.com/fr/background-agent/api/list-agents

en/background-agent/api/openapi.yaml get /v0/agents
Récupère la liste paginée de tous les agents en arrière-plan de l’utilisateur authentifié.




# Liste des modèles
Source: https://docs.cursor.com/fr/background-agent/api/list-models

en/background-agent/api/openapi.yaml get /v0/models
Récupère une liste de modèles recommandés pour les agents en arrière-plan.

Si tu veux définir le modèle de l’agent en arrière-plan lors de sa création, tu peux utiliser cet endpoint pour consulter la liste des modèles recommandés.

Dans ce cas, on te recommande aussi de proposer une option « Auto » : tu n’indiques pas de nom de modèle à l’endpoint de création, et on sélectionne le modèle le plus adapté.



# Lister les dépôts GitHub
Source: https://docs.cursor.com/fr/background-agent/api/list-repositories

en/background-agent/api/openapi.yaml get /v0/repositories
Récupère la liste des dépôts GitHub accessibles à l'utilisateur authentifié.

<Warning>
  **Cet endpoint a des limites de taux très strictes.**

  Limite les requêtes à **1 / utilisateur / minute** et **30 / utilisateur / heure**.

  Cette requête peut prendre plusieurs dizaines de secondes pour les utilisateurs ayant accès à de nombreux dépôts.

  Assure-toi de gérer correctement le cas où cette information n'est pas disponible.
</Warning>



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



# Webhooks
Source: https://docs.cursor.com/fr/background-agent/api/webhooks

Recevoir des notifications en temps réel sur les changements d’état de l’agent en arrière-plan

<div id="webhooks">
  # Webhooks
</div>

Quand tu crées un agent avec une URL de webhook, Cursor envoie des requêtes HTTP POST pour te notifier des changements d’état. Pour l’instant, seuls les événements `statusChange` sont pris en charge, notamment quand un agent passe en état `ERROR` ou `FINISHED`.

<div id="webhook-verification">
  ## Vérification du webhook
</div>

Pour t’assurer que les requêtes de webhook proviennent bien de Cursor, vérifie la signature incluse avec chaque requête :

<div id="headers">
  ### En-têtes
</div>

Chaque requête de webhook inclut les en-têtes suivants :

* **`X-Webhook-Signature`** – Contient la signature HMAC-SHA256 au format `sha256=<hex_digest>`
* **`X-Webhook-ID`** – Un identifiant unique pour cette livraison (utile pour les logs)
* **`X-Webhook-Event`** – Le type d’événement (actuellement uniquement `statusChange`)
* **`User-Agent`** – Toujours défini sur `Cursor-Agent-Webhook/1.0`

<div id="signature-verification">
  ### Vérification de la signature
</div>

Pour vérifier la signature du webhook, calcule la signature attendue et compare-la à la signature reçue :

```javascript  theme={null}
const crypto = require('crypto');

function verifyWebhook(secret, rawBody, signature) {
  const expectedSignature = 'sha256=' +
    crypto.createHmac('sha256', secret)
          .update(rawBody)
          .digest('hex');
  
  return signature === expectedSignature;
}
```

```python  theme={null}
import hmac
import hashlib

def verify_webhook(secret, raw_body, signature):
    signature_attendue = 'sha256=' + hmac.new(
        secret.encode(),
        raw_body,
        hashlib.sha256
    ).hexdigest()
    
    return signature == expected_signature
```

Utilise toujours le corps brut de la requête (avant toute analyse) pour calculer la signature.

<div id="payload-format">
  ## Format de la charge utile
</div>

La charge utile du webhook est envoyée au format JSON avec la structure suivante :

```json  theme={null}
{
  "event": "statusChange",
  "timestamp": "2024-01-15T10:30:00Z",
  "id": "bc_abc123",
  "status": "FINISHED",
  "source": {
    "repository": "https://github.com/your-org/your-repo",
    "ref": "main"
  },
  "target": {
    "url": "https://cursor.com/agents?id=bc_abc123",
    "branchName": "cursor/add-readme-1234",
    "prUrl": "https://github.com/your-org/your-repo/pull/1234"
  },
  "summary": "Ajout de README.md avec des instructions d’installation"
}
```

Note que certains champs sont facultatifs et ne seront inclus que s’ils sont disponibles.

<div id="best-practices">
  ## Bonnes pratiques
</div>

* **Vérifie les signatures** – Vérifie toujours la signature du webhook pour t’assurer que la requête vient de Cursor
* **Gère les retentatives** – Les webhooks peuvent être renvoyés si ton endpoint renvoie un code d’erreur
* **Réponds rapidement** – Renvoie un code de statut 2xx dès que possible
* **Utilise HTTPS** – Utilise toujours des URL HTTPS pour les endpoints de webhook en production
* **Stocke les payloads bruts** – Stocke le payload brut du webhook pour le débogage et de futures vérifications



# Web & Mobile
Source: https://docs.cursor.com/fr/background-agent/web-and-mobile

Lance des agents de code depuis n’importe quel appareil, avec un passage fluide vers le desktop

<div id="overview">
  ## Aperçu
</div>

L’agent de Cursor sur le web apporte un assistant de code puissant sur tous tes appareils. Que tu sois sur ton téléphone pendant une balade ou en train de bosser dans ton navigateur, tu peux maintenant lancer des agents de code performants qui tournent en arrière-plan.
Quand ils ont terminé, récupère leur travail dans Cursor, passe en revue et fusionne les modifications, ou partage des liens avec ton équipe pour collaborer.

Commence sur [cursor.com/agents](https://cursor.com/agents).

<Frame><img src="https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/webagent/cursor-web-1.png?fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=79c7d14df82cfcae369bccb8a1431cf3" alt="Interface de l’agent web de Cursor" data-og-width="4095" width="4095" data-og-height="2048" height="2048" data-path="images/webagent/cursor-web-1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/webagent/cursor-web-1.png?w=280&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=099c28633151e6c20eebc7fe03b3d420 280w, https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/webagent/cursor-web-1.png?w=560&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=452e0216c7e270d760072032f1e2b36d 560w, https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/webagent/cursor-web-1.png?w=840&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=baaa4a73d4822b5daa293814dc201d37 840w, https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/webagent/cursor-web-1.png?w=1100&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=8c5255fbf16aa60924e78a8285afb95d 1100w, https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/webagent/cursor-web-1.png?w=1650&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=7cc5a04ff6b24ad4ce0cfb4a35a9919c 1650w, https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/webagent/cursor-web-1.png?w=2500&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=f5f1b15fa508e20f89a4089f81417774 2500w" /></Frame>

<div id="getting-started">
  ## Prise en main
</div>

<div id="quick-setup">
  ### Configuration rapide
</div>

1. **Va sur l’app web** : Ouvre [cursor.com/agents](https://cursor.com/agents) depuis n’importe quel appareil
2. **Connecte-toi** : Connecte-toi avec ton compte Cursor
3. **Connecte GitHub** : Associe ton compte GitHub pour accéder aux dépôts
4. **Lance ton premier agent** : Saisis une tâche et regarde l’agent se mettre au travail

<div id="mobile-installation">
  ### Installation mobile
</div>

Pour une meilleure expérience mobile, installe Cursor en tant que Progressive Web App (PWA) :

* **iOS** : Ouvre [cursor.com/agents](https://cursor.com/agents) dans Safari, appuie sur le bouton de partage, puis « Ajouter à l’écran d’accueil »
* **Android** : Ouvre l’URL dans Chrome, appuie sur le menu, puis « Ajouter à l’écran d’accueil » ou « Installer l’app »

<Tip>
  Installer en PWA offre une expérience proche d’une app native avec : - Interface en plein écran

  * Démarrage plus rapide - Icône d’app sur ton écran d’accueil
</Tip>

<div id="working-across-devices">
  ## Travailler sur plusieurs appareils
</div>

Le Web and Mobile Agent est conçu pour s’intégrer à ton workflow sur desktop ; clique sur « Open in Cursor » pour poursuivre le travail de l’agent dans ton IDE.

<Frame><img src="https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/webagent/cursor-web-2.png?fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=352140fd4bf3f3d98a1e1b9f4a995cad" alt="Review and handoff" data-og-width="4095" width="4095" data-og-height="2048" height="2048" data-path="images/webagent/cursor-web-2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/webagent/cursor-web-2.png?w=280&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=eedd50318503fd3d3961b6da27a386d9 280w, https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/webagent/cursor-web-2.png?w=560&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=fd8c730cf62a0af6f873945a6a23b90b 560w, https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/webagent/cursor-web-2.png?w=840&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=ac537cc639471556f1afa0e09425ef30 840w, https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/webagent/cursor-web-2.png?w=1100&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=d512cddda6890c0749a7ad6396682def 1100w, https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/webagent/cursor-web-2.png?w=1650&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=e208297f414976bcfeea6850b39e8abb 1650w, https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/webagent/cursor-web-2.png?w=2500&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=54683ff7f25750fdc788e87c30bb6d6d 2500w" /></Frame>

<div id="team-collaboration">
  ### Collaboration en équipe
</div>

* **Accès partagé** : Partage des liens avec les membres de ton équipe pour collaborer sur les exécutions de l’agent.
* **Processus de revue** : Les collaborateurs peuvent passer en revue les diffs et donner leur feedback.
* **Gestion des pull requests** : Crée, review et fusionne des pull requests directement depuis l’interface web.

<div id="slack-integration">
  ### Intégration Slack
</div>

Déclenche des agents directement depuis Slack en mentionnant `@Cursor`, et, lorsque tu lances des agents depuis le web ou le mobile, choisis de recevoir des notifications Slack à la fin de l’exécution.

<Card title="Use Cursor in Slack" icon="slack" href="/fr/slack">
  En savoir plus sur la configuration et l’utilisation de l’intégration Slack, y compris
  le déclenchement d’agents et la réception de notifications.
</Card>

<div id="pricing">
  ## Tarification
</div>

Les agents web et mobiles utilisent le même modèle de tarification que les Background Agents.

En savoir plus sur la [tarification des Background Agents](/fr/account/pricing#background-agent).

<div id="troubleshooting">
  ## Dépannage
</div>

<AccordionGroup>
  <Accordion title="Les exécutions de l’agent ne démarrent pas">
    * Assure-toi d’être connecté et d’avoir associé ton compte GitHub. - Vérifie
      que tu as les autorisations nécessaires sur le dépôt. - Tu dois aussi être sur
      un essai Pro ou un abonnement payant avec la tarification à l’usage activée.
      Pour activer la tarification à l’usage, va dans l’onglet paramètres de ton
      [Dashboard](https://www.cursor.com/dashboard?tab=settings).
  </Accordion>

  <Accordion title="Impossible de voir les exécutions de l’agent sur mobile">
    Essaie d’actualiser la page ou de vider le cache de ton navigateur. Assure-toi
    d’utiliser le même compte sur tous tes appareils.
  </Accordion>

  <Accordion title="L’intégration Slack ne fonctionne pas">
    Vérifie que l’admin de ton espace de travail a installé l’app Slack de
    Cursor et que tu as les autorisations adéquates.
  </Accordion>
</AccordionGroup>



# Bugbot
Source: https://docs.cursor.com/fr/bugbot

Revue de code IA pour les pull requests

Bugbot passe en revue les pull requests et repère les bugs, les failles de sécurité et les problèmes de qualité du code.

<Tip>
  Bugbot inclut une offre gratuite : chaque utilisateur a droit à un nombre limité de revues de PR gratuites chaque mois. Quand tu atteins la limite, les revues sont mises en pause jusqu’à ton prochain cycle de facturation. Tu peux passer à tout moment à un essai Pro gratuit de 14 jours pour des revues illimitées (avec les garde‑fous anti‑abus standard).
</Tip>

<Frame>
  <video src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/bugbot/bugbot-report-cropped.mp4?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=013060fbd22f397ac81f2c32bb8b6b14" alt="Bugbot laisse des commentaires sur une PR" autoPlay loop muted playsInline controls data-path="images/bugbot/bugbot-report-cropped.mp4" />
</Frame>

<div id="how-it-works">
  ## Comment ça marche
</div>

Bugbot analyse les diffs de PR et laisse des commentaires avec des explications et des propositions de correction. Il s’exécute automatiquement à chaque mise à jour de PR ou manuellement quand tu le déclenches.

* Lance des **revues automatiques** à chaque mise à jour de PR
* **Déclenchement manuel** en commentant `cursor review` ou `bugbot run` sur n’importe quelle PR
* Les liens **Fix in Cursor** ouvrent les tickets directement dans Cursor
* Les liens **Fix in Web** ouvrent les tickets directement sur [cursor.com/agents](https://cursor.com/agents)

<div id="setup">
  ## Configuration
</div>

Nécessite des droits admin sur Cursor et sur l’org GitHub.

1. Va sur [cursor.com/dashboard](https://cursor.com/dashboard?tab=bugbot)
2. Ouvre l’onglet Bugbot
3. Clique sur `Connect GitHub` (ou `Manage Connections` si tu es déjà connecté·e)
4. Suis le processus d’installation GitHub
5. Reviens sur le dashboard pour activer Bugbot sur des dépôts spécifiques

<Frame>
  <video src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/bugbot/bugbot-install.mp4?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=75745d4464b183c306a44571db86a0c4" alt="Configuration GitHub de Bugbot" autoPlay loop muted playsInline controls data-path="images/bugbot/bugbot-install.mp4" />
</Frame>

<div id="setup">
  ## Configuration
</div>

<Tabs defaultValue="Team">
  <Tab title="Individual">
    ### Paramètres du dépôt

    Active ou désactive Bugbot par dépôt depuis ta liste d’installations. Bugbot ne s’exécute que sur les PR que tu ouvres.

    ### Paramètres personnels

    * S’exécuter **uniquement quand il est mentionné** en commentant `cursor review` ou `bugbot run`
    * S’exécuter **une seule fois** par PR, en ignorant les commits suivants
  </Tab>

  <Tab title="Team">
    ### Paramètres du dépôt

    Les admins d’équipe peuvent activer Bugbot par dépôt, configurer des listes d’autorisation/interdiction pour les reviewers et définir :

    * S’exécuter **une seule fois** par PR et par installation, en ignorant les commits suivants
    * **Désactiver les revues en ligne** pour empêcher Bugbot de laisser des commentaires directement sur les lignes de code

    Bugbot s’exécute pour tous les contributeurs des dépôts activés, quelle que soit leur appartenance à l’équipe.

    ### Paramètres personnels

    Les membres de l’équipe peuvent surcharger les paramètres pour leurs propres PR :

    * S’exécuter **uniquement quand il est mentionné** en commentant `cursor review` ou `bugbot run`
    * S’exécuter **une seule fois** par PR, en ignorant les commits suivants
    * **Activer les revues sur les PR en draft** pour inclure les pull requests en brouillon dans les revues automatiques
  </Tab>
</Tabs>

<div id="analytics">
  ### Analytics
</div>

<Frame>
  <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/bugbot/bugbot-dashboard.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=0b09bc0e61d1c92017c3ca42957c70e1" alt="Tableau de bord de Bugbot" data-og-width="1832" width="1832" data-og-height="2022" height="2022" data-path="images/bugbot/bugbot-dashboard.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/bugbot/bugbot-dashboard.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=fe3c6151118fa404a0a5a100968649cf 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/bugbot/bugbot-dashboard.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=7a602dfdaa6f737dc6d5010ea90a74b8 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/bugbot/bugbot-dashboard.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=6a21a6cb4b32248fb2b8cbea9afb8bcc 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/bugbot/bugbot-dashboard.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=27df9beda1ee9efc84e6f2c339ff1076 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/bugbot/bugbot-dashboard.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=80cb6507ca96d1c2aa74bcc30170b517 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/bugbot/bugbot-dashboard.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=ce35818f10c462b16b2d697519557019 2500w" />
</Frame>

<div id="rules">
  ## Règles
</div>

Crée des fichiers `.cursor/BUGBOT.md` pour fournir un contexte spécifique au projet lors des revues. Bugbot inclut toujours le fichier racine `.cursor/BUGBOT.md` ainsi que tous les fichiers supplémentaires trouvés en remontant l’arborescence à partir des fichiers modifiés.

```
project/
  .cursor/BUGBOT.md          # Toujours inclus (règles globales au projet)
  backend/
    .cursor/BUGBOT.md        # Inclus lors de la revue des fichiers backend
    api/
      .cursor/BUGBOT.md      # Inclus lors de la revue des fichiers API
  frontend/
    .cursor/BUGBOT.md        # Inclus lors de la revue des fichiers frontend
```

<AccordionGroup>
  <Accordion title="Exemple .cursor/BUGBOT.md">
    ```markdown  theme={null}
    # Directives pour la revue de projet

    ## Points clés de sécurité

    - Valider les entrées utilisateur dans les endpoints d’API
    - Vérifier les vulnérabilités d’injection SQL dans les requêtes de base de données
    - Garantir une authentification correcte sur les routes protégées

    ## Modèles d’architecture

    - Utiliser l’injection de dépendances pour les services
    - Suivre le pattern Repository pour l’accès aux données
    - Mettre en place une gestion des erreurs robuste avec des classes d’erreurs personnalisées

    ## Problèmes fréquents

    - Fuites de mémoire dans les composants React (vérifier le nettoyage de useEffect)
    - Absence de Error Boundaries dans les composants UI
    - Conventions de nommage incohérentes (utiliser le camelCase pour les fonctions)

    ```
  </Accordion>
</AccordionGroup>

<div id="pricing">
  ## Tarifs
</div>

Bugbot propose deux offres : **Gratuit** et **Pro**.

<div id="free-tier">
  ### Offre gratuite
</div>

Chaque utilisateur a droit à un nombre limité de revues de PR gratuites chaque mois. Pour les équipes, chaque membre bénéficie de ses propres revues gratuites. Quand tu atteins la limite, les revues sont mises en pause jusqu’à ton prochain cycle de facturation. Tu peux passer à tout moment à l’essai Pro gratuit de 14 jours pour des revues illimitées.

<div id="pro-tier">
  ### Offre Pro
</div>

<Tabs defaultValue="Teams">
  <Tab title="Individuals">
    ### Forfait fixe

    40 \$ par mois pour des revues Bugbot illimitées sur jusqu’à 200 PR par mois, tous dépôts confondus.

    ### Pour commencer

    Abonne-toi depuis les paramètres de ton compte.
  </Tab>

  <Tab title="Teams">
    ### Facturation par utilisateur

    Les équipes paient 40 \$ par utilisateur et par mois pour des revues illimitées.

    On considère comme utilisateur toute personne ayant créé des PR examinées par Bugbot au cours d’un mois.

    Toutes les licences sont libérées au début de chaque cycle de facturation et sont attribuées selon le principe du premier arrivé, premier servi. Si un utilisateur ne crée aucune PR examinée par Bugbot au cours d’un mois, la place peut être utilisée par quelqu’un d’autre.

    ### Limites de places

    Les admins d’équipe peuvent définir un nombre maximal de places Bugbot par mois pour maîtriser les coûts.

    ### Pour commencer

    Abonne-toi depuis le tableau de bord de ton équipe pour activer la facturation.

    ### Garde-fous contre les abus

    Pour prévenir les abus, nous appliquons un plafond mutualisé de 200 pull requests par mois pour chaque licence Bugbot. Si tu as besoin de plus de 200 pull requests par mois, contacte-nous à [hi@cursor.com](mailto:hi@cursor.com) et on se fera un plaisir de t’aider.

    Par exemple, si ton équipe compte 100 utilisateurs, ton organisation pourra initialement examiner 20 000 pull requests par mois. Si tu atteins cette limite naturellement, contacte-nous et on sera ravis d’augmenter le plafond.
  </Tab>
</Tabs>

<div id="troubleshooting">
  ## Dépannage
</div>

Si Bugbot ne fonctionne pas :

1. **Active le mode verbeux** en laissant un commentaire `cursor review verbose=true` ou `bugbot run verbose=true` pour obtenir des logs détaillés et l’ID de requête
2. **Vérifie les autorisations** pour t’assurer que Bugbot a accès au dépôt
3. **Vérifie l’installation** pour confirmer que l’application GitHub est installée et activée

Inclue l’ID de requête obtenu en mode verbeux quand tu signales un problème.

<div id="faq">
  ## FAQ
</div>

<AccordionGroup>
  <Accordion title="Bugbot est-il conforme au mode confidentialité ?">
    Oui, Bugbot respecte les mêmes exigences de confidentialité que Cursor et traite les données de manière identique aux autres requêtes Cursor.
  </Accordion>

  <Accordion title="Que se passe-t-il quand j’atteins la limite du palier gratuit ?">
    Quand t’atteins ta limite mensuelle du palier gratuit, les revues Bugbot sont mises en pause jusqu’à ton prochain cycle de facturation. Tu peux passer à l’essai Pro gratuit de 14 jours pour des revues illimitées (avec les garde-fous standard contre les abus).
  </Accordion>
</AccordionGroup>

```
```



# Revue de code
Source: https://docs.cursor.com/fr/cli/cookbook/code-review

Crée un workflow GitHub Actions qui utilise Cursor CLI pour examiner automatiquement les pull requests et fournir des commentaires

Ce tutoriel te montre comment configurer une revue de code avec Cursor CLI dans GitHub Actions. Le workflow analysera les pull requests, identifiera les problèmes et publiera des commentaires.

<Tip>
  Pour la plupart des utilisateurs, on recommande plutôt d’utiliser [Bugbot](/fr/bugbot). Bugbot propose une revue de code automatisée gérée, sans aucune configuration. Cette approche via la CLI est utile pour explorer les capacités et pour des personnalisations avancées.
</Tip>

<div className="space-y-4">
  <Expandable title="fichier de workflow complet">
    ```yaml cursor-code-review.yml theme={null}
    name: Revue de code

    on:
      pull_request:
        types: [opened, synchronize, reopened, ready_for_review]

    permissions:
      pull-requests: write
      contents: read
      issues: write

    jobs:
      code-review:
        runs-on: ubuntu-latest
        # Ignorer la revue de code automatisée pour les PR en brouillon
        if: github.event.pull_request.draft == false
        steps:
          - name: Récupérer le dépôt
            uses: actions/checkout@v4
            with:
              fetch-depth: 0
              ref: ${{ github.event.pull_request.head.sha }}

          - name: Installer le CLI Cursor
            run: |
              curl https://cursor.com/install -fsS | bash
              echo "$HOME/.cursor/bin" >> $GITHUB_PATH

          - name: Configurer l’identité Git
            run: |
              git config user.name "Cursor Agent"
              git config user.email "cursoragent@cursor.com"

          - name: Effectuer une revue de code automatisée
            env:
              CURSOR_API_KEY: ${{ secrets.CURSOR_API_KEY }}
              MODEL: gpt-5
              GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
              BLOCKING_REVIEW: ${{ vars.BLOCKING_REVIEW || 'false' }}
            run: |
              cursor-agent --force --model "$MODEL" --output-format=text --print 'Tu tournes dans un runner GitHub Actions qui effectue une revue de code automatisée. Le CLI gh est disponible et authentifié via GH_TOKEN. Tu peux commenter les pull requests.

              Contexte :
              - Repo: ${{ github.repository }}
              - PR Number: ${{ github.event.pull_request.number }}
              - PR Head SHA: ${{ github.event.pull_request.head.sha }}
              - PR Base SHA: ${{ github.event.pull_request.base.sha }}
              - Blocking Review: ${{ env.BLOCKING_REVIEW }}

              Objectifs :
              1) Revérifie les commentaires de revue existants et réponds resolved quand c’est traité.
              2) Passe en revue le diff actuel de la PR et ne signale que les problèmes clairs et à haute gravité.
              3) Laisse des commentaires en ligne très courts (1–2 phrases) uniquement sur les lignes modifiées, plus un bref résumé à la fin.

              Procédure :
              - Récupérer les commentaires existants : gh pr view --json comments
              - Récupérer le diff : gh pr diff
              - Récupérer les fichiers modifiés avec leurs patchs pour calculer les positions en ligne : gh api repos/${{ github.repository }}/pulls/${{ github.event.pull_request.number }}/files --paginate --jq '.[] | {filename,patch}'
              - Calculer des ancres en ligne exactes pour chaque problème (chemin de fichier + position dans le diff). Les commentaires DOIVENT être placés en ligne sur la ligne modifiée du diff, pas en commentaires de niveau supérieur.
              - Détecter les commentaires précédents de niveau supérieur de type « no issues » rédigés par ce bot (correspondances de corps comme : "✅ no issues", "No issues found", "LGTM").
              - Si l’exécution ACTUELLE trouve des problèmes et que des commentaires « no issues » existent :
                - Privilégier leur suppression pour éviter toute confusion :
                  - Tenter de supprimer les commentaires de niveau supérieur via : gh api -X DELETE repos/${{ github.repository }}/issues/comments/<comment_id>
                  - Si la suppression n’est pas possible, les minimiser via GraphQL (minimizeComment) ou les éditer pour préfixer "[Superseded by new findings]".
                - Si ni la suppression ni la minimisation n’est possible, répondre à ce commentaire : "⚠️ Superseded: issues were found in newer commits".
              - Si un problème signalé précédemment semble corrigé par des changements proches, répondre : ✅ This issue appears to be resolved by the recent changes
              - Analyser UNIQUEMENT :
                - Déréférencements de null/undefined
                - Fuites de ressources (fichiers ou connexions non fermés)
                - Injections (SQL/XSS)
                - Problèmes de concurrence/conditions de course
                - Absence de gestion d’erreurs pour des opérations critiques
                - Erreurs logiques évidentes avec comportement incorrect
                - Anti‑patterns de performance clairs avec impact mesurable
                - Vulnérabilités de sécurité avérées
              - Éviter les doublons : ignorer si un retour similaire existe déjà sur ou près des mêmes lignes.

              Règles de commentaire :
              - Maximum 10 commentaires en ligne au total ; prioriser les problèmes les plus critiques
              - Un problème par commentaire ; placer le commentaire exactement sur la ligne modifiée
              - Tous les commentaires de problème DOIVENT être en ligne (ancrés à un fichier et à une ligne/position dans le diff de la PR)
              - Ton naturel, spécifique et actionnable ; ne mentionne pas l’automatisation ni le niveau de confiance
              - Utiliser des émojis : 🚨 Critique 🔒 Sécurité ⚡ Performance ⚠️ Logique ✅ Résolu ✨ Amélioration

              Soumission :
              - S’il n’y a AUCUN problème à signaler et qu’un commentaire de niveau supérieur indiquant "no issues" existe déjà (p. ex., "✅ no issues", "No issues found", "LGTM"), ne soumets PAS un autre commentaire. Passe la soumission pour éviter la redondance.
              - S’il n’y a AUCUN problème à signaler et qu’AUCUN commentaire « no issues » antérieur n’existe, soumets un bref commentaire récapitulatif indiquant qu’il n’y a pas de problème.
              - S’IL Y A des problèmes à signaler et qu’un commentaire « no issues » antérieur existe, assure-toi que ce commentaire est supprimé/minimisé/marqué comme remplacé avant de soumettre la nouvelle revue.
              - S’IL Y A des problèmes à signaler, soumets UNE revue contenant UNIQUEMENT des commentaires en ligne, plus un corps de résumé concis optionnel. Utilise l’API GitHub Reviews pour garantir que les commentaires sont en ligne :
                - Build a JSON array of comments like: [{ "path": "<file>", "position": <diff_position>, "body": "..." }]
                - Submit via: gh api repos/${{ github.repository }}/pulls/${{ github.event.pull_request.number }}/reviews -f event=COMMENT -f body="$SUMMARY" -f comments='[$COMMENTS_JSON]'
              - NE PAS utiliser : gh pr review --approve ou --request-changes

              Comportement bloquant :
              - Si BLOCKING_REVIEW est true et que des problèmes 🚨 ou 🔒 ont été postés : echo "CRITICAL_ISSUES_FOUND=true" >> $GITHUB_ENV
              - Sinon : echo "CRITICAL_ISSUES_FOUND=false" >> $GITHUB_ENV
              - Toujours définir CRITICAL_ISSUES_FOUND à la fin
              '

          - name: Vérifier les résultats de la revue bloquante
            if: env.BLOCKING_REVIEW == 'true'
            run: |
              echo "Vérification des problèmes critiques..."
              echo "CRITICAL_ISSUES_FOUND: ${CRITICAL_ISSUES_FOUND:-unset}"

              if [ "${CRITICAL_ISSUES_FOUND:-false}" = "true" ]; then
                echo "❌ Des problèmes critiques ont été trouvés et la revue bloquante est activée. Échec du workflow."
                exit 1
              else
                echo "✅ Aucun problème bloquant trouvé."
              fi
    ```
  </Expandable>

  <Frame>
    <img src="https://mintcdn.com/cursor/KODIqSiRh6LRGwl9/images/cli/cookbook/code-review/comment.png?fit=max&auto=format&n=KODIqSiRh6LRGwl9&q=85&s=31c7e4b54276532df8010645686ebbbc" alt="Exemple de revue de code automatisée avec des commentaires en ligne sur une pull request" data-og-width="2920" width="2920" data-og-height="1272" height="1272" data-path="images/cli/cookbook/code-review/comment.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/KODIqSiRh6LRGwl9/images/cli/cookbook/code-review/comment.png?w=280&fit=max&auto=format&n=KODIqSiRh6LRGwl9&q=85&s=25e552210fa8425a10ff459bf4cd6006 280w, https://mintcdn.com/cursor/KODIqSiRh6LRGwl9/images/cli/cookbook/code-review/comment.png?w=560&fit=max&auto=format&n=KODIqSiRh6LRGwl9&q=85&s=234bf271bc595e763549c4f04d2e6fbb 560w, https://mintcdn.com/cursor/KODIqSiRh6LRGwl9/images/cli/cookbook/code-review/comment.png?w=840&fit=max&auto=format&n=KODIqSiRh6LRGwl9&q=85&s=b6f6d1444de7fe0197e3d35fa35955e8 840w, https://mintcdn.com/cursor/KODIqSiRh6LRGwl9/images/cli/cookbook/code-review/comment.png?w=1100&fit=max&auto=format&n=KODIqSiRh6LRGwl9&q=85&s=300314314f5071b77f735460be33985f 1100w, https://mintcdn.com/cursor/KODIqSiRh6LRGwl9/images/cli/cookbook/code-review/comment.png?w=1650&fit=max&auto=format&n=KODIqSiRh6LRGwl9&q=85&s=10e4db857ee84c55d17222cef492611d 1650w, https://mintcdn.com/cursor/KODIqSiRh6LRGwl9/images/cli/cookbook/code-review/comment.png?w=2500&fit=max&auto=format&n=KODIqSiRh6LRGwl9&q=85&s=e65add70ffebfeb9ad05c9bb19a5f4e1 2500w" />
  </Frame>
</div>

<div id="configure-authentication">
  ## Configurer l’authentification
</div>

[Configure ta clé d’API et les secrets du dépôt](/fr/cli/github-actions#authentication) pour authentifier Cursor CLI dans GitHub Actions.

<div id="set-up-agent-permissions">
  ## Configurer les autorisations de l’agent
</div>

Crée un fichier de configuration pour contrôler les actions que l’agent peut effectuer. Ça évite des opérations non intentionnelles comme pousser du code ou créer des pull requests.

Crée `.cursor/cli.json` à la racine de ton dépôt :

```json  theme={null}
{
  "permissions": {
    "interdire": [
      "Shell(git push)",
      "Shell(gh pr create)",
      "Write(**)"
    ]
  }
}
```

Cette configuration permet à l’agent de lire des fichiers et d’utiliser l’outil en ligne de commande GitHub (CLI) pour les commentaires, mais l’empêche d’apporter des modifications à ton dépôt. Consulte la [référence des autorisations](/fr/cli/reference/permissions) pour davantage d’options de configuration.

<div id="build-the-github-actions-workflow">
  ## Créer le workflow GitHub Actions
</div>

Construisons maintenant le workflow étape par étape.

<div id="set-up-the-workflow-trigger">
  ### Configurer le déclencheur du workflow
</div>

Crée le fichier `.github/workflows/cursor-code-review.yml` et configure-le pour s’exécuter sur les pull requests :

```yaml  theme={null}
name: Revue de code Cursor

on:
  pull_request:
    types: [opened, synchronize, reopened, ready_for_review]

jobs:
  code-review:
    runs-on: ubuntu-latest
    permissions:
      contents: read
      pull-requests: write
    
    steps:
```

<div id="checkout-the-repository">
  ### Récupère le dépôt
</div>

Ajoute l’étape de checkout pour accéder au code de la pull request :

```yaml  theme={null}
- name: Récupérer le dépôt
  uses: actions/checkout@v4
  with:
    fetch-depth: 0
    ref: ${{ github.event.pull_request.head.sha }}
```

<div id="install-cursor-cli">
  ### Installer le CLI Cursor
</div>

Ajoute l’étape d’installation du CLI :

```yaml  theme={null}
- name: Installer l’interface CLI de Cursor
  run: |
    curl https://cursor.com/install -fsS | bash
    echo "$HOME/.cursor/bin" >> $GITHUB_PATH
```

<div id="configure-the-review-agent">
  ### Configurer l’agent de review
</div>

Avant d’implémenter l’étape de review complète, on va décortiquer l’anatomie de notre prompt de review. Cette section explique comment on veut que l’agent se comporte :

**Objectif** :
On veut que l’agent analyse le diff du PR actuel et ne signale que les problèmes clairs et à forte gravité, puis laisse de très courts commentaires inline (1–2 phrases) uniquement sur les lignes modifiées, avec un bref récap à la fin. Ça maintient un bon ratio signal/bruit.

**Format** :
On veut des commentaires courts et directs. On utilise des émojis pour faciliter le scan des commentaires, et on veut un récapitulatif global de la review complète à la fin.

**Soumission** :
Quand la review est terminée, on veut que l’agent ajoute un court commentaire basé sur ce qui a été trouvé pendant la review. L’agent doit soumettre une seule review contenant des commentaires inline plus un résumé concis.

**Cas limites** :
On doit gérer :

* Commentaires existants résolus : l’agent doit les marquer comme terminés quand ils ont été adressés
* Éviter les doublons : l’agent doit s’abstenir de commenter si un retour similaire existe déjà sur ou près des mêmes lignes

**Prompt final** :
Le prompt complet combine toutes ces exigences de comportement pour produire un feedback ciblé et exploitable

Maintenant, implémentons l’étape de l’agent de review :

```yaml  theme={null}
- name: Effectuer une revue de code
  env:
    CURSOR_API_KEY: ${{ secrets.CURSOR_API_KEY }}
    GH_TOKEN: ${{ github.token }}
  run: |
    cursor-agent --force --model "$MODEL" --output-format=text --print "Tu es en train d’exécuter un job GitHub Actions pour une revue de code automatisée. L’interface de ligne de commande gh est disponible et authentifiée via GH_TOKEN. Tu peux commenter les pull requests.
    
    Contexte :
    - Référentiel : ${{ github.repository }}
    - Numéro de PR : ${{ github.event.pull_request.number }}
    - SHA de tête de la PR : ${{ github.event.pull_request.head.sha }}
    - SHA de base de la PR : ${{ github.event.pull_request.base.sha }}
    
    Objectifs :
    1) Revoir les commentaires existants et répondre « Résolu » lorsqu’ils ont été pris en compte
    2) Examiner le diff actuel de la PR et ne relever que les problèmes évidents et de gravité élevée
    3) Laisser des commentaires en ligne très courts (1 à 2 phrases) uniquement sur les lignes modifiées, puis un bref résumé à la fin
    
    Procédure :
    - Récupérer les commentaires existants : gh pr view --json comments
    - Récupérer le diff : gh pr diff
    - Si un problème signalé précédemment semble corrigé par des changements proches, répondre : ✅ Ce problème semble avoir été résolu par les changements récents
    - Éviter les doublons : ignorer si un retour similaire existe déjà sur ou à proximité des mêmes lignes
    
    Règles de commentaire :
    - Maximum 10 commentaires en ligne au total ; prioriser les problèmes les plus critiques
    - Un seul problème par commentaire ; le placer exactement sur la ligne modifiée
    - Ton naturel, précis et exploitable ; ne pas mentionner l’automatisation ni un niveau de confiance élevé
    - Utiliser des émojis : 🚨 Critique 🔒 Sécurité ⚡ Performance ⚠️ Logique ✅ Résolu ✨ Amélioration
    
    Soumission :
    - Soumettre une seule revue contenant des commentaires en ligne plus un résumé concis
    - Utiliser uniquement : gh pr review --comment
    - Ne pas utiliser : gh pr review --approve ou --request-changes"
```

```text  theme={null}
.
├── .cursor/
│   └── cli.json
├── .github/
│   └── workflows/
│       └── cursor-code-review.yml
```

<div id="test-your-reviewer">
  ## Teste ton reviewer
</div>

Crée une pull request de test pour vérifier que le workflow fonctionne et que l’agent publie des commentaires de review avec des retours en émojis.

<Frame>
  <img src="https://mintcdn.com/cursor/KODIqSiRh6LRGwl9/images/cli/cookbook/code-review/github-actions.png?fit=max&auto=format&n=KODIqSiRh6LRGwl9&q=85&s=aa989eb5b7520e6718a48afd8daa70d9" alt="Pull request affichant des commentaires de review automatisés avec des émojis et des retours inline sur des lignes spécifiques" data-og-width="1250" width="1250" data-og-height="704" height="704" data-path="images/cli/cookbook/code-review/github-actions.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/KODIqSiRh6LRGwl9/images/cli/cookbook/code-review/github-actions.png?w=280&fit=max&auto=format&n=KODIqSiRh6LRGwl9&q=85&s=9f2e324beb1cccb8052dcd0682323e47 280w, https://mintcdn.com/cursor/KODIqSiRh6LRGwl9/images/cli/cookbook/code-review/github-actions.png?w=560&fit=max&auto=format&n=KODIqSiRh6LRGwl9&q=85&s=f08497ddb17921f4bb4638ef4eec3379 560w, https://mintcdn.com/cursor/KODIqSiRh6LRGwl9/images/cli/cookbook/code-review/github-actions.png?w=840&fit=max&auto=format&n=KODIqSiRh6LRGwl9&q=85&s=3c869c0ed8eb8b5743dd3821e57cd406 840w, https://mintcdn.com/cursor/KODIqSiRh6LRGwl9/images/cli/cookbook/code-review/github-actions.png?w=1100&fit=max&auto=format&n=KODIqSiRh6LRGwl9&q=85&s=19e98ed953f4cc17b2c578ce543cf88d 1100w, https://mintcdn.com/cursor/KODIqSiRh6LRGwl9/images/cli/cookbook/code-review/github-actions.png?w=1650&fit=max&auto=format&n=KODIqSiRh6LRGwl9&q=85&s=4d9f47472af81254bd09b5f6234fc97f 1650w, https://mintcdn.com/cursor/KODIqSiRh6LRGwl9/images/cli/cookbook/code-review/github-actions.png?w=2500&fit=max&auto=format&n=KODIqSiRh6LRGwl9&q=85&s=f3af19e3edd7f8bbbb77ba6566d8e183 2500w" />
</Frame>

<div id="next-steps">
  ## Prochaines étapes
</div>

Tu as maintenant un système automatisé de revue de code opérationnel. Pense à ces améliorations :

* Mettre en place des workflows supplémentaires pour [corriger les échecs CI](/fr/cli/cookbook/fix-ci)
* Configurer différents niveaux de revue selon les branches
* Intégrer ça au processus de revue de code existant de ton équipe
* Personnaliser le comportement de l’agent selon les types de fichiers ou les répertoires

<Expandable title="Avancé : revues bloquantes">
  Tu peux configurer le workflow pour échouer en cas de problèmes critiques, empêchant la fusion de la pull request tant qu’ils ne sont pas résolus.

  **Ajouter un comportement bloquant au prompt**

  D’abord, mets à jour l’étape de ton agent de revue pour inclure la variable d’environnement `BLOCKING_REVIEW` et ajoute ce comportement bloquant au prompt :

  ```
  Blocking behavior:
  - If BLOCKING_REVIEW is true and any 🚨 or 🔒 issues were posted: echo "CRITICAL_ISSUES_FOUND=true" >> $GITHUB_ENV
  - Otherwise: echo "CRITICAL_ISSUES_FOUND=false" >> $GITHUB_ENV
  - Always set CRITICAL_ISSUES_FOUND at the end
  ```

  **Ajouter l’étape de vérification de blocage**

  Ajoute ensuite cette nouvelle étape après ton étape de revue de code :

  ```yaml  theme={null}
        - name: Check blocking review results
          if: env.BLOCKING_REVIEW == 'true'
          run: |
            echo "Checking for critical issues..."
            echo "CRITICAL_ISSUES_FOUND: ${CRITICAL_ISSUES_FOUND:-unset}"

            if [ "${CRITICAL_ISSUES_FOUND:-false}" = "true" ]; then
              echo "❌ Critical issues found and blocking review is enabled. Failing the workflow."
              exit 1
            else
              echo "✅ No blocking issues found."
            fi
  ```
</Expandable>



# Corriger les échecs CI
Source: https://docs.cursor.com/fr/cli/cookbook/fix-ci

Corrige les problèmes de CI d’un dépôt en utilisant Cursor CLI dans GitHub Actions

Corrige les échecs de CI avec Cursor CLI dans GitHub Actions. Ce workflow analyse les échecs, applique des correctifs ciblés et crée une branche de correctif avec un lien de PR à création rapide.

Ce workflow surveille un workflow spécifique par son nom. Mets à jour la liste `workflows` pour correspondre au nom réel de ton workflow de CI.

<CodeGroup>
  ```yaml auto-fix-ci.yml theme={null}
  name: Fix CI Failures

  on:
    workflow_run:
      workflows: [Test]
      types: [completed]

  permissions:
    contents: write
    pull-requests: write
    actions: read

  jobs:
    attempt-fix:
      if: >-
        ${{ github.event.workflow_run.conclusion == 'failure' && github.event.workflow_run.name != 'Fix CI Failures' }}
      runs-on: ubuntu-latest
      steps:
        - name: Checkout repository
          uses: actions/checkout@v4
          with:
            fetch-depth: 0

        - name: Install Cursor CLI
          run: |
            curl https://cursor.com/install -fsS | bash
            echo "$HOME/.cursor/bin" >> $GITHUB_PATH

        - name: Configure git identity
          run: |
            git config user.name "Cursor Agent"
            git config user.email "cursoragent@cursor.com"

        - name: Fix CI failure
          env:
            CURSOR_API_KEY: ${{ secrets.CURSOR_API_KEY }}
            MODEL: gpt-5
            GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
            BRANCH_PREFIX: ci-fix
          run: |
            cursor-agent -p "You are operating in a GitHub Actions runner.

            The GitHub CLI is available as `gh` and authenticated via `GH_TOKEN`. Git is available. You have write access to repository contents and can comment on pull requests, but you must not create or edit PRs directly.

            # Context:
            - Repo: ${{ github.repository }}
            - Owner: ${{ github.repository_owner }}
            - Workflow Run ID: ${{ github.event.workflow_run.id }}
            - Workflow Run URL: ${{ github.event.workflow_run.html_url }}
            - Fix Branch Prefix: ${{ env.BRANCH_PREFIX }}

            # Goal:
            - Implement an end-to-end CI fix flow driven by the failing PR, creating a separate persistent fix branch and proposing a quick-create PR back into the original PR's branch.

            # Requirements:
            1) Identify the PR associated with the failed workflow run and determine its base and head branches. Let HEAD_REF be the PR's head branch (the contributor/origin branch).
            2) Maintain a persistent fix branch for this PR head using the Fix Branch Prefix from Context. Create it if missing, update it otherwise, and push changes to origin.
            3) Attempt to resolve the CI failure by making minimal, targeted edits consistent with the repo's style. Keep changes scoped and safe.
            4) You do NOT have permission to create PRs. Instead, post or update a single natural-language PR comment (1–2 sentences) that briefly explains the CI fix and includes an inline compare link to quick-create a PR.

            # Inputs and conventions:
            - Use `gh api`, `gh run view`, `gh pr view`, `gh pr diff`, `gh pr list`, `gh run download`, and git commands as needed to discover the failing PR and branches.
            - Avoid duplicate comments; if a previous bot comment exists, update it instead of posting a new one.
            - If no actionable fix is possible, make no changes and post no comment.

            # Deliverables when updates occur:
            - Pushed commits to the persistent fix branch for this PR head.
            - A single natural-language PR comment on the original PR that includes the inline compare link above.
            " --force --model "$MODEL" --output-format=text

  ```
</CodeGroup>



# Audit des secrets
Source: https://docs.cursor.com/fr/cli/cookbook/secret-audit

Audite les secrets d’un dépôt avec Cursor CLI dans GitHub Actions

Analyse ton dépôt pour détecter des vulnérabilités de sécurité et des fuites de secrets avec Cursor CLI. Ce workflow recherche des secrets potentiels, repère des schémas de workflows à risque et propose des correctifs de sécurité.

<CodeGroup>
  ```yaml auto-secret-audit.yml theme={null}
  name: Secrets Audit

  on:
    schedule:
      - cron: "0 4 * * *"
    workflow_dispatch:

  permissions:
    contents: write
    pull-requests: write
    actions: read

  jobs:
    secrets-audit:
      runs-on: ubuntu-latest
      steps:
        - name: Checkout repository
          uses: actions/checkout@v4
          with:
            fetch-depth: 0

        - name: Install Cursor CLI
          run: |
            curl https://cursor.com/install -fsS | bash
            echo "$HOME/.cursor/bin" >> $GITHUB_PATH

        - name: Configure git identity
          run: |
            git config user.name "Cursor Agent"
            git config user.email "cursoragent@cursor.com"

        - name: Scan and propose hardening
          env:
            CURSOR_API_KEY: ${{ secrets.CURSOR_API_KEY }}
            MODEL: gpt-5
            GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
            BRANCH_PREFIX: audit
          run: |
            cursor-agent -p "You are operating in a GitHub Actions runner.

            The GitHub CLI is available as `gh` and authenticated via `GH_TOKEN`. Git is available. You have write access to repository contents and can comment on pull requests, but you must not create or edit PRs directly.

            # Context:
            - Repo: ${{ github.repository }}
             - Hardening Branch Prefix: ${{ env.BRANCH_PREFIX }}

            # Goal:
            - Perform a repository secrets exposure and workflow hardening audit on a schedule, and propose minimal safe fixes.

            # Requirements:
            1) Scan for potential secrets in tracked files and recent history; support allowlist patterns if present (e.g., .gitleaks.toml).
            2) Detect risky workflow patterns: unpinned actions, overbroad permissions, unsafe pull_request_target usage, secrets in forked PR contexts, deprecated insecure commands, missing permissions blocks.
            3) Maintain a persistent branch for this run using the Hardening Branch Prefix from Context. Create it if missing, update it otherwise, and push changes to origin.
            4) Propose minimal edits: redact literals where safe, add ignore rules, pin actions to SHA, reduce permissions, add guardrails to workflows, and add a SECURITY_LOG.md summarizing changes and remediation guidance.
            5) Push to origin.
            6) If there is at least one open PR in the repo, post or update a single natural-language comment (1–2 sentences) on the most recently updated open PR that briefly explains the hardening changes and includes an inline compare link to quick-create a PR.
            7) Avoid duplicate comments; update an existing bot comment if present. If no changes or no open PRs, post nothing.

            # Inputs and conventions:
            - Use `gh` to list PRs and to post comments. Avoid duplicate comments.

            # Deliverables when updates occur:
             - Pushed commits to the persistent hardening branch for this run.
            - A single natural-language PR comment with the compare link above (only if an open PR exists).
            " --force --model "$MODEL" --output-format=text

  ```
</CodeGroup>



# Traduire des clés
Source: https://docs.cursor.com/fr/cli/cookbook/translate-keys

Traduire les clés d’un dépôt avec Cursor CLI dans GitHub Actions

Gère les clés de traduction pour l’internationalisation avec Cursor CLI. Ce workflow détecte les nouvelles clés i18n ou celles modifiées dans les pull requests et complète les traductions manquantes sans écraser celles qui existent déjà.

<CodeGroup>
  ```yaml auto-translate-keys.yml theme={null}
  name: Translate Keys

  on:
    pull_request:
      types: [opened, synchronize, reopened, ready_for_review]

  permissions:
    contents: write
    pull-requests: write

  jobs:
    i18n:
      if: ${{ !startsWith(github.head_ref, 'translate/') }}
      runs-on: ubuntu-latest
      steps:
        - name: Checkout repository
          uses: actions/checkout@v4
          with:
            fetch-depth: 0

        - name: Install Cursor CLI
          run: |
            curl https://cursor.com/install -fsS | bash
            echo "$HOME/.cursor/bin" >> $GITHUB_PATH

        - name: Configure git identity
          run: |
            git config user.name "Cursor Agent"
            git config user.email "cursoragent@cursor.com"

        - name: Propose i18n updates
          env:
            CURSOR_API_KEY: ${{ secrets.CURSOR_API_KEY }}
            MODEL: gpt-5
            GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
            BRANCH_PREFIX: translate
          run: |
            cursor-agent -p "You are operating in a GitHub Actions runner.

            The GitHub CLI is available as `gh` and authenticated via `GH_TOKEN`. Git is available. You have write access to repository contents and can comment on pull requests, but you must not create or edit PRs directly.

            # Context:
            - Repo: ${{ github.repository }}
            - PR Number: ${{ github.event.pull_request.number }}
            - Head Ref: ${{ github.head_ref }}
            - Translate Branch Prefix: ${{ env.BRANCH_PREFIX }}

            # Goal:
            - Detect i18n keys added or changed in the PR and fill only missing locales in message files. Never overwrite existing translations.

            # Requirements:
            1) Determine changed keys by inspecting the PR diff (source files and messages files).
            2) Compute missing keys per locale using the source/canonical locale as truth.
            3) Add entries only for missing keys. Preserve all existing values untouched.
            4) Validate JSON formatting and schemas.
            5) Maintain a persistent translate branch for this PR head using the Translate Branch Prefix from Context. Create it if missing, update it otherwise, and push changes to origin.
            6) Post or update a single PR comment on the original PR written in natural language (1–2 sentences) that briefly explains what was updated and why, and includes an inline compare link to quick-create a PR.
            7) Avoid duplicate comments; update a previous bot comment if present.
            8) If no changes are necessary, make no commits and post no comment.

            # Inputs and conventions:
            - Use `gh pr diff` and git history to detect changes.

            # Deliverables when updates occur:
            - Pushed commits to the persistent translate branch for this PR head.
            - A single natural-language PR comment on the original PR with the compare link above.
            " --force --model "$MODEL" --output-format=text

  ```
</CodeGroup>



# Mettre à jour la doc
Source: https://docs.cursor.com/fr/cli/cookbook/update-docs

Mets à jour la doc d’un dépôt avec Cursor CLI dans GitHub Actions

Mets à jour la doc avec Cursor CLI dans GitHub Actions. Deux approches : autonomie complète de l’agent ou workflow déterministe où seul l’agent modifie les fichiers.

<CodeGroup>
  ```yaml auto-update-docs.yml theme={null}
  name: Mettre à jour la doc

  on:
    pull_request:
      types: [opened, synchronize, reopened, ready_for_review]

  permissions:
    contents: write
    pull-requests: write

  jobs:
    auto-docs:
      if: ${{ !startsWith(github.head_ref, 'docs/') }}
      runs-on: ubuntu-latest
      steps:
        - name: Cloner le dépôt
          uses: actions/checkout@v4
          with:
            fetch-depth: 0

        - name: Installer l’interface en ligne de commande Cursor
          run: |
            curl https://cursor.com/install -fsS | bash
            echo "$HOME/.cursor/bin" >> $GITHUB_PATH

        - name: Configurer Git
          run: |
            git config user.name "Cursor Agent"
            git config user.email "cursoragent@cursor.com"

        - name: Mettre à jour la doc
          env:
            MODEL: gpt-5
            CURSOR_API_KEY: ${{ secrets.CURSOR_API_KEY }}
            GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
            BRANCH_PREFIX: docs
          run: |
            cursor-agent -p "Tu tournes dans un runner GitHub Actions.

            Le CLI GitHub est disponible sous `gh` et authentifié via `GH_TOKEN`. Git est disponible. Tu as un accès en écriture au contenu du dépôt et tu peux commenter les pull requests, mais tu ne dois pas créer ni modifier de PR.

            # Contexte :
            - Repo: ${{ github.repository }}
            - Owner: ${{ github.repository_owner }}
            - PR Number: ${{ github.event.pull_request.number }}
            - Base Ref: ${{ github.base_ref }}
            - Head Ref: ${{ github.head_ref }}
            - Docs Branch Prefix: ${{ env.BRANCH_PREFIX }}

            # Objectif :
            - Mettre en place un flux de mise à jour de la doc de bout en bout, piloté par les changements incrémentaux de la PR d’origine.

            # Exigences :
            1) Déterminer ce qui a changé dans la PR d’origine et, s’il y a eu plusieurs pushs, calculer les diffs incrémentiels depuis la dernière mise à jour de la doc réussie.
            2) Mettre à jour uniquement la doc pertinente en fonction de ces changements incrémentiels.
            3) Maintenir la branche de doc persistante pour le head de cette PR en utilisant le préfixe de branche Docs indiqué dans le Contexte. La créer si elle est absente, sinon la mettre à jour, puis pousser les changements vers origin.
            4) Tu n’as PAS la permission de créer des PR. À la place, publie ou mets à jour un unique commentaire en langage naturel sur la PR (1–2 phrases) qui explique brièvement les mises à jour de la doc et inclut un lien de comparaison en ligne pour créer rapidement une PR.

            # Entrées et conventions :
            - Utilise `gh pr diff` et l’historique Git pour détecter les changements et dériver les plages incrémentielles depuis la dernière mise à jour de la doc.
            - N’essaie pas de créer ou de modifier des PR directement. Utilise le format de lien de comparaison ci-dessus.
            - Garde les changements minimaux et cohérents avec le style du dépôt. S’il n’y a pas de mises à jour de doc nécessaires, ne fais aucun changement et ne publie aucun commentaire.

            # Livrables en cas de mises à jour :
            - Commits poussés vers la branche de doc persistante pour le head de cette PR.
            - Un unique commentaire en langage naturel sur la PR d’origine qui inclut le lien de comparaison en ligne ci-dessus. Évite les doublons ; mets à jour un précédent commentaire du bot s’il existe.
            " --force --model "$MODEL" --output-format=text
  ```

  ```yaml auto-update-docs-deterministic.yml theme={null}
  name: Mettre à jour la doc

  on:
    pull_request:
      types: [opened, synchronize, reopened, ready_for_review]

  permissions:
    contents: write
    pull-requests: write

  jobs:
    auto-docs:
      if: ${{ !startsWith(github.head_ref, 'docs/') }}
      runs-on: ubuntu-latest
      steps:
        - name: Récupérer le dépôt
          uses: actions/checkout@v4
          with:
            fetch-depth: 0

        - name: Installer le CLI Cursor
          run: |
            curl https://cursor.com/install -fsS | bash
            echo "$HOME/.cursor/bin" >> $GITHUB_PATH

        - name: Configurer git
          run: |
            git config user.name "Cursor Agent"
            git config user.email "cursoragent@cursor.com"

        - name: Générer les mises à jour de la doc (pas de commit/push/commentaire)
          env:
            MODEL: gpt-5
            CURSOR_API_KEY: ${{ secrets.CURSOR_API_KEY }}
            GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
            BRANCH_PREFIX: docs
          run: |
            cursor-agent -p "Tu es en train d’exécuter dans un runner GitHub Actions.

            Le CLI GitHub est disponible sous `gh` et authentifié via `GH_TOKEN`. Git est disponible.

            IMPORTANT : Ne crée pas de branches, ne fais pas de commit, ne push pas et ne poste pas de commentaires sur la PR. Modifie uniquement les fichiers dans le répertoire de travail si nécessaire. Une étape ultérieure du workflow publiera les changements et commentera la PR.

            # Contexte :
            - Repo: ${{ github.repository }}
            - Owner: ${{ github.repository_owner }}
            - PR Number: ${{ github.event.pull_request.number }}
            - Base Ref: ${{ github.base_ref }}
            - Head Ref: ${{ github.head_ref }}

            # Objectif :
            - Mettre à jour la documentation du dépôt en fonction des changements incrémentaux introduits par cette PR.

            # Exigences :
            1) Détermine ce qui a changé dans la PR d’origine (utilise `gh pr diff` et l’historique git si nécessaire). Si une branche de doc persistante `${{ env.BRANCH_PREFIX }}/${{ github.head_ref }}` existe, tu peux l’utiliser comme point de référence en lecture seule pour comprendre les mises à jour précédentes.
            2) Mets à jour uniquement la doc pertinente en fonction de ces changements. Garde les modifications minimales et conformes au style du dépôt.
            3) Ne fais pas de commit, ne push pas, ne crée pas de branches et ne poste pas de commentaires sur la PR. Laisse l’arbre de travail avec uniquement les fichiers mis à jour ; une étape ultérieure publiera.

            # Entrées et conventions :
            - Utilise `gh pr diff` et l’historique git pour détecter les changements et cibler les modifications de la doc en conséquence.
            - Si aucune mise à jour de la doc n’est nécessaire, ne fais aucun changement et ne produis aucune sortie.

            # Livrables lorsque des mises à jour ont lieu :
            - Fichiers de doc modifiés dans le répertoire de travail uniquement (pas de commits/push/commentaires).
            " --force --model "$MODEL" --output-format=text

        - name: Publier la branche de doc
          id: publish_docs
          env:
            BRANCH_PREFIX: docs
            HEAD_REF: ${{ github.head_ref }}
            PR_NUMBER: ${{ github.event.pull_request.number }}
          run: |
            echo "changes_published=false" >> "$GITHUB_OUTPUT"

            DOCS_BRANCH="${BRANCH_PREFIX}/${HEAD_REF}"

            # Assure-toi d’être sur une branche locale que l’on peut pousser
            git fetch origin --prune

            # Crée/bascule vers la branche persistante de doc, en conservant les changements actuels de l’arborescence de travail
            git checkout -B "$DOCS_BRANCH"

            # Indexer et détecter les changements
            git add -A
            if git diff --staged --quiet; then
              echo "Aucun changement de doc à publier. On saute le commit/push."
              exit 0
            fi

            COMMIT_MSG="docs: update for PR #${PR_NUMBER} (${HEAD_REF} @ $(git rev-parse --short HEAD))"
            git commit -m "$COMMIT_MSG"
            git push --set-upstream origin "$DOCS_BRANCH"

            echo "changes_published=true" >> "$GITHUB_OUTPUT"

        - name: Publier ou mettre à jour le commentaire de la PR
          if: steps.publish_docs.outputs.changes_published == 'true'
          env:
            GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
            BRANCH_PREFIX: docs
            REPO: ${{ github.repository }}
            BASE_REF: ${{ github.base_ref }}
            HEAD_REF: ${{ github.head_ref }}
            PR_NUMBER: ${{ github.event.pull_request.number }}
          run: |

            DOCS_BRANCH="${BRANCH_PREFIX}/${HEAD_REF}"
            COMPARE_URL="https://github.com/${REPO}/compare/${BASE_REF}...${DOCS_BRANCH}?quick_pull=1&title=docs%3A+updates+for+PR+%23${PR_NUMBER}"

            COMMENT_FILE="${RUNNER_TEMP}/auto-docs-comment.md"
            {
              echo "Cursor a mis à jour la branche de doc : \`${DOCS_BRANCH}\`"
              echo "Tu peux maintenant [voir le diff et créer rapidement une PR pour fusionner ces mises à jour de doc](${COMPARE_URL})."
              echo
              echo "_Ce commentaire sera mis à jour lors des exécutions suivantes au fur et à mesure que la PR évolue._"
              echo
              echo "<!-- auto-update-docs-split -->"
            } > "$COMMENT_FILE"

            # Si la modification du dernier commentaire du bot échoue (gh plus ancien), on revient à la création d’un nouveau commentaire
            if gh pr comment "$PR_NUMBER" --body-file "$COMMENT_FILE" --edit-last; then
              echo "Commentaire de PR existant mis à jour."
            else
              gh pr comment "$PR_NUMBER" --body-file "$COMMENT_FILE"
              echo "Nouveau commentaire de PR publié."
            fi
  ```
</CodeGroup>



# GitHub Actions
Source: https://docs.cursor.com/fr/cli/github-actions

Découvre comment utiliser la CLI de Cursor dans GitHub Actions et d'autres systèmes d'intégration continue

Utilise la CLI de Cursor dans GitHub Actions et d'autres systèmes CI/CD pour automatiser des tâches de développement.

<div id="github-actions-integration">
  ## Intégration de GitHub Actions
</div>

Configuration de base :

```yaml  theme={null}
- name: Installer l’outil en ligne de commande Cursor
  run: |
    curl https://cursor.com/install -fsS | bash
    echo "$HOME/.cursor/bin" >> $GITHUB_PATH

- name: Exécuter Cursor Agent
  env:
    CURSOR_API_KEY: ${{ secrets.CURSOR_API_KEY }}
  run: |
    cursor-agent -p "Ton prompt ici" --model gpt-5
```

<div id="cookbook-examples">
  ## Exemples de recettes
</div>

Découvre nos exemples de recettes pour des workflows concrets : [mise à jour de la doc](/fr/cli/cookbook/update-docs) et [correction des problèmes de CI](/fr/cli/cookbook/fix-ci).

<div id="other-ci-systems">
  ## Autres systèmes CI
</div>

Utilise le CLI Cursor dans n’importe quel système CI/CD avec :

* **Exécution de scripts shell** (bash, zsh, etc.)
* **Variables d’environnement** pour configurer la clé API
* **Connexion Internet** pour accéder à l’API de Cursor

## Niveaux d'autonomie

Choisis le niveau d'autonomie de ton agent :

<div id="full-autonomy-approach">
  ### Autonomie totale
</div>

Donne à l'agent le contrôle complet des opérations Git, des appels API et des interactions externes. Configuration plus simple, mais nécessite davantage de confiance.

**Exemple :** Dans notre cookbook [Update Documentation](/fr/cli/cookbook/update-docs), le premier workflow permet à l'agent de :

* Analyser les changements du PR
* Créer et gérer des branches Git
* Commit et push des changements
* Publier des commentaires sur les pull requests
* Gérer tous les scénarios d’erreur

```yaml  theme={null}
- name: Mettre à jour la doc (autonomie totale)
  run: |
    cursor-agent -p "Tu as un accès complet à git, au CLI GitHub et aux opérations de PR. 
    Gère tout le workflow de mise à jour de la doc, y compris les commits, les push et les commentaires de PR."
```

<div id="restricted-autonomy-approach">
  ### Approche d’autonomie restreinte
</div>

<Note>
  On recommande d’utiliser cette approche avec des **restrictions fondées sur des permissions** pour les workflows CI en production. Ça te donne le meilleur des deux mondes : l’agent peut gérer intelligemment des analyses complexes et des modifications de fichiers, tandis que les opérations critiques restent déterministes et auditables.
</Note>

Limite les opérations de l’agent tout en traitant les étapes critiques dans des étapes de workflow séparées. Meilleur contrôle et meilleure prévisibilité.

**Exemple :** Le deuxième workflow du même cookbook restreint l’agent aux seules modifications de fichiers :

```yaml  theme={null}
- name: Générer des mises à jour de la doc (restreint)
  run: |
    cursor-agent -p "IMPORTANT : Ne crée pas de branches, ne fais pas de commit, ne fais pas de push et ne publie pas de commentaires sur les PR.
    Modifie uniquement les fichiers dans le répertoire de travail. Une étape ultérieure du workflow s’occupe de la publication."

- name: Publier la branche de doc (déterministe)
  run: |
    # Opérations git déterministes gérées par le CI
    git checkout -B "docs/${{ github.head_ref }}"
    git add -A
    git commit -m "docs: mise à jour pour la PR"
    git push origin "docs/${{ github.head_ref }}"

- name: Publier un commentaire de PR (déterministe)  
  run: |
    # Publication de commentaires de PR déterministe gérée par le CI
    gh pr comment ${{ github.event.pull_request.number }} --body "Docs mises à jour"
```

<div id="permission-based-restrictions">
  ### Restrictions basées sur les permissions
</div>

Utilise les [configurations d’autorisations](/fr/cli/reference/permissions) pour appliquer des restrictions au niveau du CLI :

```json  theme={null}
{
  "permissions": {
    "allow": [
      "Read(**/*.md)",
      "Write(docs/**/*)",
      "Shell(grep)",
      "Shell(find)"
    ],
    "deny": [
      "Shell(git)",
      "Shell(gh)", 
      "Write(.env*)",
      "Write(package.json)"
    ]
  }
}
```

<div id="authentication">
  ## Authentification
</div>

<div id="generate-your-api-key">
  ### Générer ta clé API
</div>

D’abord, [génère une clé API](/fr/cli/reference/authentication#api-key-authentication) depuis ton tableau de bord Cursor.

<div id="configure-repository-secrets">
  ### Configurer les secrets du dépôt
</div>

Stocke ta clé API Cursor en toute sécurité dans ton dépôt :

1. Va sur ton dépôt GitHub
2. Clique sur **Settings** → **Secrets and variables** → **Actions**
3. Clique sur **New repository secret**
4. Nomme-la `CURSOR_API_KEY`
5. Colle ta clé API comme valeur
6. Clique sur **Add secret**

<div id="use-in-workflows">
  ### Utiliser dans les workflows
</div>

Définis ta variable d’environnement `CURSOR_API_KEY` :

```yaml  theme={null}
env:
  CURSOR_API_KEY: ${{ secrets.CURSOR_API_KEY }}
```



# Utiliser le CLI en mode headless
Source: https://docs.cursor.com/fr/cli/headless

Découvre comment écrire des scripts avec Cursor CLI pour l’analyse, la génération et la modification automatisées de code

Utilise Cursor CLI dans des scripts et des workflows d’automatisation pour des tâches d’analyse de code, de génération et de refactorisation.

<div id="how-it-works">
  ## Comment ça marche
</div>

Utilise le [mode d’impression](/fr/cli/using#non-interactive-mode) (`-p, --print`) pour les scripts non interactifs et l’automatisation.

<div id="file-modification-in-scripts">
  ### Modification de fichiers dans des scripts
</div>

Combine `--print` avec `--force` pour modifier des fichiers dans des scripts :

```bash  theme={null}

# Autoriser les modifications de fichiers en mode impression
cursor-agent -p --force "Refactor this code to use modern ES6+ syntax"


# Sans --force, les modifications sont proposées mais non appliquées
cursor-agent -p "Ajouter des commentaires JSDoc à ce fichier"  # Ne modifiera pas les fichiers


# Traitement par lots avec modifications réelles des fichiers
find src/ -name "*.js" | while read file; do
  cursor-agent -p --force "Ajouter des commentaires JSDoc détaillés à $file"
done
```

<Warning>
  L’option `--force` permet à l’agent d’apporter des modifications directes aux fichiers sans confirmation
</Warning>

<div id="setup">
  ## Configuration
</div>

Consulte [Installation](/fr/cli/installation) et [Authentification](/fr/cli/reference/authentication) pour tous les détails de configuration.

```bash  theme={null}

# Installer l’interface en ligne de commande (CLI) de Cursor
curl https://cursor.com/install -fsS | bash


# Définir la clé d’API pour les scripts  
export CURSOR_API_KEY=your_api_key_here
cursor-agent -p "Analyse ce code"
```

<div id="example-scripts">
  ## Exemples de scripts
</div>

Utilise différents formats de sortie selon les besoins des scripts. Consulte la page [Format de sortie](/fr/cli/reference/output-format) pour plus de détails.

<div id="searching-the-codebase">
  ### Recherche dans la base de code
</div>

Utilise `--output-format text` pour obtenir des réponses lisibles :

```bash  theme={null}
#!/bin/bash

# Question simple sur le codebase

cursor-agent -p --output-format text "À quoi sert ce codebase ?"
```

<div id="automated-code-review">
  ### Revue de code automatisée
</div>

Utilise `--output-format json` pour obtenir une analyse structurée :

```bash  theme={null}
#!/bin/bash

# simple-code-review.sh - Script de revue de code simple

echo "Début de la revue de code..."


# Examiner les changements récents
cursor-agent -p --force --output-format text \
  "Passe en revue les derniers changements de code et donne un retour sur :
  - Qualité du code et lisibilité  
  - Bugs ou problèmes potentiels
  - Aspects de sécurité
  - Conformité aux bonnes pratiques

  Donne des suggestions d’amélioration concrètes et écris-les dans review.txt"

if [ $? -eq 0 ]; then
  echo "✅ Revue de code terminée avec succès"
else
  echo "❌ Échec de la revue de code"
  exit 1
fi
```

<div id="real-time-progress-tracking">
  ### Suivi de la progression en temps réel
</div>

Utilise `--output-format stream-json` pour un suivi de la progression en temps réel :

```bash  theme={null}
#!/bin/bash

# stream-progress.sh - Suivre la progression en temps réel

echo "🚀 Démarrage du traitement du stream..."


# Suivi de la progression en temps réel
accumulated_text=""
tool_count=0
start_time=$(date +%s)

cursor-agent -p --force --output-format stream-json \
  "Analyse la structure de ce projet et crée un rapport de synthèse dans analysis.txt" | \
  while IFS= read -r line; do
    
    type=$(echo "$line" | jq -r '.type // empty')
    subtype=$(echo "$line" | jq -r '.subtype // empty')
    
    case "$type" in
      "system")
        if [ "$subtype" = "init" ]; then
          model=$(echo "$line" | jq -r '.model // "unknown"')
          echo "🤖 Modèle utilisé : $model"
        fi
        ;;
        
      "assistant")
        # Accumuler les deltas de texte en streaming
        content=$(echo "$line" | jq -r '.message.content[0].text // empty')
        accumulated_text="$accumulated_text$content"
        
        # Afficher la progression en temps réel
        printf "\r📝 Génération : %d caractères" ${#accumulated_text}
        ;;
        
      "tool_call")
        if [ "$subtype" = "started" ]; then
          tool_count=$((tool_count + 1))
          
          # Extraire les informations de l’outil
          if echo "$line" | jq -e '.tool_call.writeToolCall' > /dev/null 2>&1; then
            path=$(echo "$line" | jq -r '.tool_call.writeToolCall.args.path // "unknown"')
            echo -e "\n🔧 Outil n°$tool_count : Création de $path"
          elif echo "$line" | jq -e '.tool_call.readToolCall' > /dev/null 2>&1; then
            path=$(echo "$line" | jq -r '.tool_call.readToolCall.args.path // "unknown"')
            echo -e "\n📖 Outil n°$tool_count : Lecture de $path"
          fi
          
        elif [ "$subtype" = "completed" ]; then
          # Extraire et afficher les résultats de l’outil
          if echo "$line" | jq -e '.tool_call.writeToolCall.result.success' > /dev/null 2>&1; then
            lines=$(echo "$line" | jq -r '.tool_call.writeToolCall.result.success.linesCreated // 0')
            size=$(echo "$line" | jq -r '.tool_call.writeToolCall.result.success.fileSize // 0')
            echo "   ✅ Création de $lines lignes ($size octets)"
          elif echo "$line" | jq -e '.tool_call.readToolCall.result.success' > /dev/null 2>&1; then
            lines=$(echo "$line" | jq -r '.tool_call.readToolCall.result.success.totalLines // 0')
            echo "   ✅ Lecture de $lines lignes"
          fi
        fi
        ;;
        
      "result")
        duration=$(echo "$line" | jq -r '.duration_ms // 0')
        end_time=$(date +%s)
        total_time=$((end_time - start_time))
        
        echo -e "\n\n🎯 Terminé en ${duration} ms (${total_time} s au total)"
        echo "📊 Statistiques finales : $tool_count outils, ${#accumulated_text} caractères générés"
        ;;
    esac
  done
```



# Installation
Source: https://docs.cursor.com/fr/cli/installation

Installer et mettre à jour l’interface en ligne de commande (CLI) Cursor

<div id="installation">
  ## Installation
</div>

<div id="macos-linux-and-windows-wsl">
  ### macOS, Linux et Windows (WSL)
</div>

Installe la CLI Cursor avec une seule commande :

```bash  theme={null}
curl https://cursor.com/install -fsS | bash
```

<div id="verification">
  ### Vérification
</div>

Après l’installation, vérifie que le CLI Cursor fonctionne correctement :

```bash  theme={null}
cursor-agent --version
```

<div id="post-installation-setup">
  ## Configuration après installation
</div>

1. **Ajoute \~/.local/bin à ton PATH :**

   Pour bash :

   ```bash  theme={null}
   echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
   source ~/.bashrc
   ```

   Pour zsh :

   ```bash  theme={null}
   echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc
   source ~/.zshrc
   ```

2. **Commence à utiliser Cursor Agent :**
   ```bash  theme={null}
   cursor-agent
   ```

<div id="updates">
  ## Mises à jour
</div>

Par défaut, Cursor CLI essaie de se mettre à jour automatiquement pour que t’aies toujours la dernière version.

Pour mettre à jour manuellement Cursor CLI vers la dernière version :

```bash  theme={null}
cursor-agent update

# ou 
cursor-agent upgrade
```

Les deux commandes mettront à jour Cursor Agent vers la version la plus récente.



# MCP
Source: https://docs.cursor.com/fr/cli/mcp

Utilise des serveurs MCP avec cursor-agent pour te connecter à des outils externes et à des sources de données

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

<div id="overview">
  ## Vue d’ensemble
</div>

La CLI de Cursor prend en charge les serveurs [Model Context Protocol (MCP)](/fr/context/mcp), te permettant de connecter des outils externes et des sources de données à `cursor-agent`. **MCP dans la CLI utilise la même configuration que l’éditeur** — tous les serveurs MCP que t’as configurés fonctionneront sans accroc avec les deux.

<Card title="Découvrir MCP" icon="link" href="/fr/context/mcp">
  Nouveau sur MCP ? Lis le guide complet sur la configuration, l’authentification et les serveurs disponibles
</Card>

<div id="cli-commands">
  ## Commandes CLI
</div>

Utilise la commande `cursor-agent mcp` pour gérer les serveurs MCP :

<div id="list-configured-servers">
  ### Lister les serveurs configurés
</div>

Affiche tous les serveurs MCP configurés et leur état actuel :

```bash  theme={null}
cursor-agent mcp list
```

Cela affiche :

* Noms et identifiants des serveurs
* État de la connexion (connecté/déconnecté)
* Source de la configuration (projet ou global)
* Méthode de transport (stdio, HTTP, SSE)

<div id="list-available-tools">
  ### Lister les outils disponibles
</div>

Voir les outils fournis par un serveur MCP donné :

```bash  theme={null}
cursor-agent mcp list-tools <identifiant>
```

Cela affiche :

* Noms et descriptions des outils
* Paramètres requis et facultatifs
* Types de paramètres et contraintes

<div id="login-to-mcp-server">
  ### Connexion au serveur MCP
</div>

Authentifie-toi auprès d’un serveur MCP configuré dans ton `mcp.json` :

```bash  theme={null}
cursor-agent mcp login <identifiant>
```

<div id="disable-mcp-server">
  ### Désactiver un serveur MCP
</div>

Retire un serveur MCP de la liste locale des serveurs approuvés :

```bash  theme={null}
cursor-agent mcp disable <ID>
```

<div id="using-mcp-with-agent">
  ## Utiliser MCP avec Agent
</div>

Une fois que tu as configuré des serveurs MCP (voir le [guide MCP principal](/fr/context/mcp) pour la configuration), `cursor-agent` détecte automatiquement et utilise les outils disponibles lorsqu’ils sont pertinents pour tes requêtes.

```bash  theme={null}

# Vérifier quels serveurs MCP sont disponibles
cursor-agent mcp list


# Voir quels outils un serveur donné fournit
cursor-agent mcp list-tools playwright


# Utiliser cursor-agent - il utilise automatiquement les outils MCP quand c’est pertinent
cursor-agent --prompt "Va sur google.com et prends une capture d’écran de la page de recherche"
```

La CLI suit la même priorité de configuration que l’éditeur (projet → global → imbriqué), et détecte automatiquement les configurations dans les répertoires parents.

<div id="related">
  ## Articles associés
</div>

<CardGroup cols={2}>
  <Card title="MCP Overview" icon="link" href="/fr/context/mcp">
    Guide complet de MCP : installation, configuration et authentification
  </Card>

  <Card title="Available MCP Tools" icon="table" href="/fr/tools">
    Parcours les serveurs MCP prêts à l’emploi que tu peux utiliser
  </Card>
</CardGroup>



# Cursor CLI
Source: https://docs.cursor.com/fr/cli/overview

Commence avec Cursor CLI pour coder dans ton terminal

Cursor CLI te permet d’interagir avec des agents IA directement depuis ton terminal pour écrire, relire et modifier du code. Que tu préfères une interface terminal interactive ou l’automatisation en sortie texte pour des scripts et des pipelines CI, la CLI t’apporte une aide puissante, là où tu travailles.

```bash  theme={null}

# Installation
curl https://cursor.com/install -fsS | bash


# Lancer une session interactive
cursor-agent
```

<Frame>
  <video src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/cli/cli-overview.mp4?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=b323547dd61e985df8c0d6179c1492bd" autoPlay loop muted playsInline controls data-path="images/cli/cli-overview.mp4" />
</Frame>

<Info>
  Cursor CLI est actuellement en bêta, on adorerait ton feedback !
</Info>

<div id="interactive-mode">
  ### Mode interactif
</div>

Démarre une session de discussion avec l’agent pour décrire tes objectifs, passer en revue les changements proposés et approuver les commandes :

```bash  theme={null}

# Démarrer une session interactive
cursor-agent


# Démarrer avec une invite initiale
cursor-agent "refactorise le module d'auth pour utiliser des tokens JWT"
```

<div id="non-interactive-mode">
  ### Mode non interactif
</div>

Utilise le mode print pour les scénarios non interactifs, comme les scripts, les pipelines CI ou l’automatisation :

```bash  theme={null}

# Exécuter avec une invite et un modèle spécifiques
cursor-agent -p "find and fix performance issues" --model "gpt-5"


# Utiliser avec les modifications Git incluses pour relecture
cursor-agent -p "review these changes for security issues" --output-format text
```

<div id="sessions">
  ### Sessions
</div>

Reprends des conversations précédentes pour garder le contexte sur plusieurs échanges :

```bash  theme={null}

# Lister toutes les discussions précédentes
cursor-agent ls


# Reprendre la dernière conversation
cursor-agent resume


# Reprendre une conversation précise
cursor-agent --resume="chat-id-here"
```



# Authentification
Source: https://docs.cursor.com/fr/cli/reference/authentication

Authentifie Cursor CLI via la connexion navigateur ou des clés API

Cursor CLI prend en charge deux méthodes d'authentification : la connexion via le navigateur (recommandée) et les clés API.

<div id="browser-authentication-recommended">
  ## Authentification via le navigateur (recommandé)
</div>

Utilise le parcours via le navigateur pour une expérience d’authentification ultra simple :

```bash  theme={null}

# Se connecter via le navigateur
cursor-agent login


# Vérifier l’état de l’authentification
cursor-agent status


# Se déconnecter et effacer les informations d’authentification stockées
cursor-agent logout
```

La commande de connexion ouvrira ton navigateur par défaut et te demandera de t’authentifier avec ton compte Cursor. Une fois l’opération terminée, tes identifiants seront stockés localement de manière sécurisée.

<div id="api-key-authentication">
  ## Authentification par clé API
</div>

Pour l’automatisation, les scripts ou les environnements CI/CD, utilise l’authentification par clé API :

<div id="step-1-generate-an-api-key">
  ### Étape 1 : Générer une clé API
</div>

Génère une clé API dans ton tableau de bord Cursor, sous Integrations > User API Keys.

<div id="step-2-set-the-api-key">
  ### Étape 2 : Définir la clé API
</div>

Tu peux fournir la clé API de deux façons :

**Option 1 : Variable d’environnement (recommandé)**

```bash  theme={null}
export CURSOR_API_KEY=your_api_key_here
cursor-agent "implémenter l’authentification des utilisateurs"
```

**Option 2 : Drapeau de ligne de commande**

```bash  theme={null}
cursor-agent --api-key your_api_key_here "implémente l’authentification des utilisateurs"
```

<div id="authentication-status">
  ## État d’authentification
</div>

Vérifie ton statut d’authentification actuel :

```bash  theme={null}
cursor-agent status
```

Cette commande affichera :

* Si t’es authentifié
* Les infos de ton compte
* La configuration actuelle de l’endpoint

<div id="troubleshooting">
  ## Dépannage
</div>

* **Erreurs « Not authenticated » :** Exécute `cursor-agent login` ou vérifie que ta clé API est correctement définie
* **Erreurs de certificat SSL :** Utilise l’option `--insecure` pour les environnements de développement
* **Problèmes d’endpoint :** Utilise l’option `--endpoint` pour spécifier un endpoint d’API personnalisé



# Configuration
Source: https://docs.cursor.com/fr/cli/reference/configuration

Référence de configuration de l’Agent CLI pour cli-config.json

Configure l’Agent CLI à l’aide du fichier `cli-config.json`.

<div id="file-location">
  ## Emplacement du fichier
</div>

<div class="full-width-table">
  | Type   | Plateforme  | Chemin                                     |
  | :----- | :---------- | :----------------------------------------- |
  | Global | macOS/Linux | `~/.cursor/cli-config.json`                |
  | Global | Windows     | `$env:USERPROFILE\.cursor\cli-config.json` |
  | Projet | Tous        | `<project>/.cursor/cli.json`               |
</div>

<Note>Seules les autorisations peuvent être configurées au niveau du projet. Tous les autres réglages du CLI doivent être définis globalement.</Note>

Remplacer via des variables d’environnement :

* **`CURSOR_CONFIG_DIR`** : chemin de répertoire personnalisé
* **`XDG_CONFIG_HOME`** (Linux/BSD) : utilise `$XDG_CONFIG_HOME/cursor/cli-config.json`

<div id="schema">
  ## Schéma
</div>

<div id="required-fields">
  ### Champs requis
</div>

<div class="full-width-table">
  | Champ               | Type      | Description                                                               |
  | :------------------ | :-------- | :------------------------------------------------------------------------ |
  | `version`           | number    | Version du schéma de configuration (actuelle : `1`)                       |
  | `editor.vimMode`    | boolean   | Activer les raccourcis Vim (par défaut : `false`)                         |
  | `permissions.allow` | string\[] | Opérations autorisées (voir [Permissions](/fr/cli/reference/permissions)) |
  | `permissions.deny`  | string\[] | Opérations interdites (voir [Permissions](/fr/cli/reference/permissions)) |
</div>

<div id="optional-fields">
  ### Champs optionnels
</div>

<div class="full-width-table">
  | Champ                    | Type    | Description                                          |
  | :----------------------- | :------ | :--------------------------------------------------- |
  | `model`                  | object  | Configuration du modèle sélectionné                  |
  | `hasChangedDefaultModel` | boolean | Indicateur de remplacement du modèle géré par la CLI |
</div>

<div id="examples">
  ## Exemples
</div>

<div id="minimal-config">
  ### Configuration minimale
</div>

```json  theme={null}
{
  "version": 1,
  "editor": { "vimMode": false },
  "permissions": { "allow": ["Shell(ls)"], "deny": [] }
}
```

<div id="enable-vim-mode">
  ### Activer le mode Vim
</div>

```json  theme={null}
{
  "version": 1,
  "editor": { "vimMode": true },
  "permissions": { "allow": ["Shell(ls)"], "deny": [] }
}
```

<div id="configure-permissions">
  ### Configurer les permissions
</div>

```json  theme={null}
{
  "version": 1,
  "editor": { "vimMode": false },
  "permissions": {
    "allow": ["Shell(ls)", "Shell(echo)"],
    "deny": ["Shell(rm)"]
  }
}
```

Consulte [Permissions](/fr/cli/reference/permissions) pour les types d’autorisations disponibles et des exemples.

<div id="troubleshooting">
  ## Dépannage
</div>

**Erreurs de configuration** : Mets le fichier de côté et redémarre :

```bash  theme={null}
mv ~/.cursor/cli-config.json ~/.cursor/cli-config.json.bad
```

**Les modifications ne sont pas conservées** : Assure-toi que le JSON est valide et que tu as les autorisations d’écriture. Certains champs sont gérés par la CLI et peuvent être écrasés.

<div id="notes">
  ## Notes
</div>

* Format JSON pur (sans commentaires)
* La CLI répare automatiquement les champs manquants
* Les fichiers corrompus sont sauvegardés en `.bad` puis recréés
* Les entrées d’autorisations sont des chaînes exactes (voir [Permissions](/fr/cli/reference/permissions) pour plus de détails)



# Format de sortie
Source: https://docs.cursor.com/fr/cli/reference/output-format

Schéma de sortie pour les formats texte, JSON et stream-JSON

Le CLI Cursor Agent propose plusieurs formats de sortie via l’option `--output-format` lorsqu’elle est utilisée avec `--print`. Ces formats incluent des formats structurés pour un usage programmatique (`json`, `stream-json`) et un format texte simplifié pour suivre l’avancement de manière lisible.

<Note>
  Le `--output-format` par défaut est `stream-json`. Cette option n’est valable que lors de l’impression (`--print`) ou lorsque le mode impression est déduit (stdout non TTY ou stdin passé en pipe).
</Note>

<div id="json-format">
  ## Format JSON
</div>

Le format de sortie `json` émet un seul objet JSON (suivi d’un saut de ligne) lorsque l’exécution se termine avec succès. Aucune delta ni aucun événement d’outil n’est émis ; le texte est agrégé dans le résultat final.

En cas d’échec, le processus se termine avec un code non nul et écrit un message d’erreur sur stderr. Aucun objet JSON valide n’est émis en cas d’échec.

<div id="success-response">
  ### Réponse en cas de succès
</div>

En cas de réussite, la CLI affiche un objet JSON avec la structure suivante :

```json  theme={null}
{
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "duration_ms": 1234,
  "duration_api_ms": 1234,
  "result": "<texte intégral de l’assistant>",
  "session_id": "<uuid>",
  "request_id": "<ID de requête (optionnel)>"
}
```

<div class="full-width-table">
  | Champ             | Description                                                                            |
  | ----------------- | -------------------------------------------------------------------------------------- |
  | `type`            | Toujours `"result"` pour les résultats du terminal                                     |
  | `subtype`         | Toujours `"success"` pour les exécutions réussies                                      |
  | `is_error`        | Toujours `false` pour les réponses réussies                                            |
  | `duration_ms`     | Durée totale d’exécution en millisecondes                                              |
  | `duration_api_ms` | Durée de la requête API en millisecondes (actuellement égale à `duration_ms`)          |
  | `result`          | Texte complet de la réponse de l’assistant (concaténation de tous les deltas de texte) |
  | `session_id`      | Identifiant de session unique                                                          |
  | `request_id`      | Identifiant de requête facultatif (peut être omis)                                     |
</div>

<div id="stream-json-format">
  ## Format JSON de flux
</div>

Le format de sortie `stream-json` émet du JSON délimité par des retours à la ligne (NDJSON). Chaque ligne contient un unique objet JSON représentant un événement en temps réel pendant l'exécution.

Le flux se termine par un événement final `result` en cas de réussite. En cas d'échec, le processus se termine avec un code différent de zéro et le flux peut s'arrêter plus tôt sans événement final ; un message d'erreur est écrit sur stderr.

### Types d'événements

<div id="system-initialization">
  #### Initialisation du système
</div>

Émis une fois au début de chaque session :

```json  theme={null}
{
  "type": "system",
  "subtype": "init",
  "apiKeySource": "env|flag|login",
  "cwd": "/chemin/absolu",
  "session_id": "<uuid>",
  "model": "<nom d’affichage du modèle>",
  "permissionMode": "par défaut"
}
```

<Note>
  Des champs comme `tools` et `mcp_servers` pourraient être ajoutés à cet événement à l’avenir.
</Note>

<div id="user-message">
  #### Message utilisateur
</div>

Contient l’invite saisie par l’utilisateur :

```json  theme={null}
{
  "type": "user",
  "message": {
    "role": "user",
    "content": [{ "type": "text", "text": "<prompt>" }]
  },
  "session_id": "<uuid>"
}
```

<div id="assistant-text-delta">
  #### Delta de texte de l’assistant
</div>

Émis plusieurs fois pendant que l’assistant génère sa réponse. Ces événements contiennent des fragments de texte au fil de l’eau :

```json  theme={null}
{
  "type": "assistant",
  "message": {
    "role": "assistant",
    "content": [{ "type": "text", "text": "<fragment delta>" }]
  },
  "session_id": "<uuid>"
}
```

<Note>
  Concatène toutes les valeurs `message.content[].text`, dans l’ordre, pour reconstruire la réponse complète de l’assistant.
</Note>

<div id="tool-call-events">
  #### Événements d’appel d’outil
</div>

Les appels d’outil sont suivis par des événements de démarrage et d’achèvement :

**Appel d’outil démarré :**

```json  theme={null}
{
  "type": "tool_call",
  "subtype": "started",
  "call_id": "<string id>",
  "tool_call": {
    "readToolCall": {
      "args": { "path": "file.txt" }
    }
  },
  "session_id": "<uuid>"
}
```

**Appel d’outil terminé :**

```json  theme={null}
{
  "type": "tool_call",
  "subtype": "completed",
  "call_id": "<string id>",
  "tool_call": {
    "readToolCall": {
      "args": { "path": "file.txt" },
      "result": {
        "success": {
          "content": "contenu du fichier…",
          "isEmpty": false,
          "exceededLimit": false,
          "totalLines": 54,
          "totalChars": 1254
        }
      }
    }
  },
  "session_id": "<uuid>"
}
```

<div id="tool-call-types">
  #### Types d’appels d’outils
</div>

**Outil de lecture de fichier :**

* **Démarrage** : `tool_call.readToolCall.args` contient `{ "path": "file.txt" }`
* **Achèvement** : `tool_call.readToolCall.result.success` contient les métadonnées et le contenu du fichier

**Outil d’écriture de fichier :**

* **Démarrage** : `tool_call.writeToolCall.args` contient `{ "path": "file.txt", "fileText": "content...", "toolCallId": "id" }`
* **Achèvement** : `tool_call.writeToolCall.result.success` contient `{ "path": "/absolute/path", "linesCreated": 19, "fileSize": 942 }`

**Autres outils :**

* Peut utiliser la structure `tool_call.function` avec `{ "name": "tool_name", "arguments": "..." }`

<div id="terminal-result">
  #### Résultat du terminal
</div>

L’événement final émis en cas de réussite :

```json  theme={null}
{
  "type": "result",
  "subtype": "réussite",
  "duration_ms": 1234,
  "duration_api_ms": 1234,
  "is_error": false,
  "result": "<texte complet de l’assistant>",
  "session_id": "<uuid>",
  "request_id": "<ID de requête (optionnel)>"
}
```

<div id="example-sequence">
  ### Exemple de séquence
</div>

Voici une séquence NDJSON représentative illustrant le déroulement typique des événements :

```json  theme={null}
{"type":"system","subtype":"init","apiKeySource":"login","cwd":"/Users/user/project","session_id":"c6b62c6f-7ead-4fd6-9922-e952131177ff","model":"Claude 4 Sonnet","permissionMode":"default"}
{"type":"user","message":{"role":"user","content":[{"type":"text","text":"Lis README.md et fais un résumé"}]},"session_id":"c6b62c6f-7ead-4fd6-9922-e952131177ff"}
{"type":"assistant","message":{"role":"assistant","content":[{"type":"text","text":"Je vais "}]},"session_id":"c6b62c6f-7ead-4fd6-9922-e952131177ff"}
{"type":"assistant","message":{"role":"assistant","content":[{"type":"text","text":"lire le fichier README.md"}]},"session_id":"c6b62c6f-7ead-4fd6-9922-e952131177ff"}
{"type":"tool_call","subtype":"started","call_id":"toolu_vrtx_01NnjaR886UcE8whekg2MGJd","tool_call":{"readToolCall":{"args":{"path":"README.md"}}},"session_id":"c6b62c6f-7ead-4fd6-9922-e952131177ff"}
{"type":"tool_call","subtype":"completed","call_id":"toolu_vrtx_01NnjaR886UcE8whekg2MGJd","tool_call":{"readToolCall":{"args":{"path":"README.md"},"result":{"success":{"content":"# Project\n\nThis is a sample project...","isEmpty":false,"exceededLimit":false,"totalLines":54,"totalChars":1254}}}},"session_id":"c6b62c6f-7ead-4fd6-9922-e952131177ff"}
{"type":"assistant","message":{"role":"assistant","content":[{"type":"text","text":" et faire un résumé"}]},"session_id":"c6b62c6f-7ead-4fd6-9922-e952131177ff"}
{"type":"tool_call","subtype":"started","call_id":"toolu_vrtx_01Q3VHVnWFSKygaRPT7WDxrv","tool_call":{"writeToolCall":{"args":{"path":"summary.txt","fileText":"# README Summary\n\nThis project contains...","toolCallId":"toolu_vrtx_01Q3VHVnWFSKygaRPT7WDxrv"}}},"session_id":"c6b62c6f-7ead-4fd6-9922-e952131177ff"}
{"type":"tool_call","subtype":"completed","call_id":"toolu_vrtx_01Q3VHVnWFSKygaRPT7WDxrv","tool_call":{"writeToolCall":{"args":{"path":"summary.txt","fileText":"# README Summary\n\nThis project contains...","toolCallId":"toolu_vrtx_01Q3VHVnWFSKygaRPT7WDxrv"},"result":{"success":{"path":"/Users/user/project/summary.txt","linesCreated":19,"fileSize":942}}}},"session_id":"c6b62c6f-7ead-4fd6-9922-e952131177ff"}
{"type":"result","subtype":"success","duration_ms":5234,"duration_api_ms":5234,"is_error":false,"result":"Je vais lire le fichier README.md et faire un résumé","session_id":"c6b62c6f-7ead-4fd6-9922-e952131177ff","request_id":"10e11780-df2f-45dc-a1ff-4540af32e9c0"}
```

<div id="text-format">
  ## Format texte
</div>

Le format de sortie `text` fournit un flux simplifié et lisible des actions de l’agent. Au lieu d’événements JSON détaillés, il produit des descriptions concises de ce que fait l’agent en temps réel.

Ce format est utile pour suivre la progression de l’agent sans le coût d’analyse de données structurées, ce qui le rend idéal pour la journalisation, le débogage ou un simple suivi de l’avancement.

<div id="example-output">
  ### Exemple de sortie
</div>

```
Fichier lu
Fichier modifié
Commande de terminal exécutée
Nouveau fichier créé
```

Chaque action s’affiche sur une nouvelle ligne à mesure que l’agent l’exécute, offrant un retour immédiat sur l’avancement de l’agent dans la tâche.

<div id="implementation-notes">
  ## Notes d’implémentation
</div>

* Chaque événement est émis sur une seule ligne terminée par `\n`
* Les événements `thinking` sont masqués en mode impression et n’apparaissent dans aucun des formats de sortie
* Des champs peuvent être ajoutés au fil du temps de manière rétrocompatible (les consommateurs doivent ignorer les champs inconnus)
* Le format stream fournit des mises à jour en temps réel, tandis que le format JSON attend la fin avant d’afficher les résultats
* Concatène tous les deltas du message `assistant` pour reconstituer la réponse complète
* Les IDs d’appels d’outils peuvent être utilisés pour faire correspondre les événements de début et de fin
* Les IDs de session restent identiques tout au long d’une exécution unique de l’agent



# Paramètres
Source: https://docs.cursor.com/fr/cli/reference/parameters

Référence complète des commandes du CLI Cursor Agent

<div id="global-options">
  ## Options globales
</div>

Les options globales peuvent être utilisées avec n'importe quelle commande :

<div class="full-width-table">
  | Option                     | Description                                                                                                                            |
  | -------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
  | `-v, --version`            | Affiche le numéro de version                                                                                                           |
  | `-a, --api-key <key>`      | Clé API pour l'authentification (tu peux aussi utiliser la variable d'env `CURSOR_API_KEY`)                                            |
  | `-p, --print`              | Affiche les réponses dans la console (pour les scripts ou l'usage non interactif). A accès à tous les outils, y compris write et bash. |
  | `--output-format <format>` | Format de sortie (ne fonctionne qu'avec `--print`) : `text`, `json` ou `stream-json` (par défaut : `stream-json`)                      |
  | `-b, --background`         | Démarre en arrière-plan (ouvre le sélecteur de composition au lancement)                                                               |
  | `--fullscreen`             | Active le mode plein écran                                                                                                             |
  | `--resume [chatId]`        | Rétablit une session de chat                                                                                                           |
  | `-m, --model <model>`      | Modèle à utiliser                                                                                                                      |
  | `-f, --force`              | Force l'autorisation des commandes sauf refus explicite                                                                                |
  | `-h, --help`               | Affiche l'aide de la commande                                                                                                          |
</div>

<div id="commands">
  ## Commandes
</div>

<div class="full-width-table">
  | Commande          | Description                                            | Utilisation                                     |
  | ----------------- | ------------------------------------------------------ | ----------------------------------------------- |
  | `login`           | S’authentifier avec Cursor                             | `cursor-agent login`                            |
  | `logout`          | Se déconnecter et effacer les identifiants enregistrés | `cursor-agent logout`                           |
  | `status`          | Vérifier l’état de l’authentification                  | `cursor-agent status`                           |
  | `mcp`             | Gérer les serveurs MCP                                 | `cursor-agent mcp`                              |
  | `update\|upgrade` | Mettre à jour Cursor Agent vers la dernière version    | `cursor-agent update` ou `cursor-agent upgrade` |
  | `ls`              | Reprendre une session de chat                          | `cursor-agent ls`                               |
  | `resume`          | Reprendre la dernière session de chat                  | `cursor-agent resume`                           |
  | `help [command]`  | Afficher l’aide d’une commande                         | `cursor-agent help [command]`                   |
</div>

<Note>
  Si tu ne précises aucune commande, Cursor Agent démarre par défaut en mode chat interactif.
</Note>

<div id="mcp">
  ## MCP
</div>

Gère les serveurs MCP configurés pour Cursor Agent.

<div class="full-width-table">
  | Sous-commande             | Description                                                                   | Utilisation                                |
  | ------------------------- | ----------------------------------------------------------------------------- | ------------------------------------------ |
  | `login <identifier>`      | S’authentifie auprès d’un serveur MCP défini dans `.cursor/mcp.json`          | `cursor-agent mcp login <identifier>`      |
  | `list`                    | Liste les serveurs MCP configurés et leur état                                | `cursor-agent mcp list`                    |
  | `list-tools <identifier>` | Liste les outils disponibles et les noms de leurs arguments pour un MCP donné | `cursor-agent mcp list-tools <identifier>` |
</div>

Toutes les commandes MCP acceptent `-h, --help` pour obtenir l’aide spécifique à la commande.

<div id="arguments">
  ## Arguments
</div>

Quand tu démarres en mode chat (comportement par défaut), tu peux fournir un prompt initial :

**Arguments :**

* `prompt` — Prompt initial pour l’agent

<div id="getting-help">
  ## Obtenir de l’aide
</div>

Toutes les commandes prennent en charge l’option globale `-h, --help` pour afficher l’aide propre à chaque commande.



# Permissions
Source: https://docs.cursor.com/fr/cli/reference/permissions

Types d’autorisations pour contrôler l’accès de l’agent aux fichiers et aux commandes

Configure ce que l’agent est autorisé à faire en utilisant des jetons d’autorisation dans ta configuration CLI. Les autorisations se définissent dans `~/.cursor/cli-config.json` (global) ou `<project>/.cursor/cli.json` (spécifique au projet).

<div id="permission-types">
  ## Types d’autorisations
</div>

<div id="shell-commands">
  ### Commandes shell
</div>

**Format :** `Shell(commandBase)`

Contrôle l’accès aux commandes shell. Le `commandBase` est le premier jeton de la ligne de commande.

<div class="full-width-table">
  | Exemple      | Description                                                           |
  | ------------ | --------------------------------------------------------------------- |
  | `Shell(ls)`  | Autoriser l’exécution des commandes `ls`                              |
  | `Shell(git)` | Autoriser toutes les sous-commandes `git`                             |
  | `Shell(npm)` | Autoriser les commandes du gestionnaire de paquets npm                |
  | `Shell(rm)`  | Refuser la suppression destructrice de fichiers (souvent dans `deny`) |
</div>

<div id="file-reads">
  ### Lectures de fichiers
</div>

**Format :** `Read(pathOrGlob)`

Contrôle l’accès en lecture aux fichiers et aux répertoires. Prend en charge les motifs glob.

<div class="full-width-table">
  | Exemple             | Description                                             |
  | ------------------- | ------------------------------------------------------- |
  | `Read(src/**/*.ts)` | Autoriser la lecture des fichiers TypeScript dans `src` |
  | `Read(**/*.md)`     | Autoriser la lecture des fichiers Markdown partout      |
  | `Read(.env*)`       | Refuser la lecture des fichiers d’environnement         |
  | `Read(/etc/passwd)` | Refuser la lecture des fichiers système                 |
</div>

<div id="file-writes">
  ### Écritures de fichiers
</div>

**Format :** `Write(pathOrGlob)`

Contrôle l’accès en écriture aux fichiers et aux répertoires. Prend en charge les motifs glob. En mode impression, `--force` est requis pour écrire des fichiers.

<div class="full-width-table">
  | Exemple               | Description                                                 |
  | --------------------- | ----------------------------------------------------------- |
  | `Write(src/**)`       | Autoriser l’écriture dans n’importe quel fichier sous `src` |
  | `Write(package.json)` | Autoriser la modification de `package.json`                 |
  | `Write(**/*.key)`     | Refuser l’écriture de fichiers de clés privées              |
  | `Write(**/.env*)`     | Refuser l’écriture des fichiers d’environnement             |
</div>

<div id="configuration">
  ## Configuration
</div>

Ajoute des permissions à l’objet `permissions` dans ton fichier de configuration du CLI :

```json  theme={null}
{
  "permissions": {
    "allow": [
      "Shell(ls)",
      "Shell(git)", 
      "Read(src/**/*.ts)",
      "Write(package.json)"
    ],
    "deny": [
      "Shell(rm)",
      "Read(.env*)",
      "Write(**/*.key)"
    ]
  }
}
```

<div id="pattern-matching">
  ## Correspondance de motifs
</div>

* Les motifs glob utilisent les caractères génériques `**`, `*` et `?`
* Les chemins relatifs sont limités à l’espace de travail actuel
* Les chemins absolus peuvent cibler des fichiers en dehors du projet
* Les règles de refus priment sur les règles d’autorisation



# Commandes slash
Source: https://docs.cursor.com/fr/cli/reference/slash-commands

Actions rapides disponibles dans les sessions CLI de Cursor

<div class="full-width-table">
  | Commande              | Description                                                             |
  | --------------------- | ----------------------------------------------------------------------- |
  | `/model <model>`      | Définir ou lister les modèles                                           |
  | `/auto-run [state]`   | Activer/désactiver l’auto-run (par défaut) ou régler \[on\|off\|status] |
  | `/new-chat`           | Démarrer une nouvelle session de chat                                   |
  | `/vim`                | Activer/désactiver les touches Vim                                      |
  | `/help [command]`     | Afficher l’aide (/help \[cmd])                                          |
  | `/feedback <message>` | Envoyer un feedback à l’équipe                                          |
  | `/resume <chat>`      | Reprendre un chat précédent par nom de dossier                          |
  | `/copy-req-id`        | Copier le dernier ID de requête                                         |
  | `/logout`             | Se déconnecter de Cursor                                                |
  | `/quit`               | Quitter                                                                 |
</div>




---

**Navigation:** [← Previous](./11-desarrolladores.md) | [Index](./index.md) | [Next →](./13-mode-shell.md)