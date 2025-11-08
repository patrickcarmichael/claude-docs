---
title: "SSO"
source: "https://docs.cursor.com/fr/account/teams/sso"
language: "fr"
language_name: "French"
---

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

---

← Previous: [Bien démarrer](./bien-dmarrer.md) | [Index](./index.md) | Next: [Accès aux mises à jour](./accs-aux-mises-jour.md) →