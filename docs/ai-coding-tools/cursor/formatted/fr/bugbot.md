---
title: "Bugbot"
source: "https://docs.cursor.com/fr/bugbot"
language: "fr"
language_name: "French"
---

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

---

← Previous: [Web & Mobile](./web-mobile.md) | [Index](./index.md) | Next: [Revue de code](./revue-de-code.md) →