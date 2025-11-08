---
title: "Paramètres Enterprise"
source: "https://docs.cursor.com/fr/account/teams/enterprise-settings"
language: "fr"
language_name: "French"
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

---

← Previous: [Dashboard](./dashboard.md) | [Index](./index.md) | Next: [Membres et rôles](./membres-et-rles.md) →