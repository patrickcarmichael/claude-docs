---
title: "GitHub"
source: "https://docs.cursor.com/fr/integrations/github"
language: "fr"
language_name: "French"
---

# GitHub
Source: https://docs.cursor.com/fr/integrations/github

Application GitHub officielle de Cursor pour les agents en arrière-plan

[Background Agents](/fr/background-agent) et [Bugbot](/fr/bugbot) requièrent l’application GitHub de Cursor pour cloner des dépôts et pousser des modifications.

<div id="installation">
  ## Installation
</div>

1. Va sur [Intégrations dans le tableau de bord](https://cursor.com/dashboard?tab=integrations)
2. Clique sur **Connect** à côté de GitHub
3. Choisis le dépôt : **All repositories** ou **Selected repositories**

Pour déconnecter ton compte GitHub, retourne sur le tableau de bord des intégrations et clique sur **Disconnect Account**.

<div id="using-agent-in-github">
  ## Utiliser Agent dans GitHub
</div>

L’intégration GitHub permet d’exécuter des workflows d’agent en arrière‑plan directement depuis les pull requests et les issues. Tu peux déclencher un agent pour lire le contexte, appliquer des correctifs et pousser des commits en commentant `@cursor [prompt]` sur n’importe quel PR ou issue.

Si tu as [Bugbot](/fr/bugbot) activé, tu peux commenter `@cursor fix` pour lire la correction suggérée par Bugbot et déclencher un agent en arrière‑plan pour traiter le problème.

<div id="permissions">
  ## Permissions
</div>

L’appli GitHub a besoin d’autorisations spécifiques pour fonctionner avec les agents en arrière-plan :

<div className="full-width-table">
  | Permission                | Purpose                                                                     |
  | ------------------------- | --------------------------------------------------------------------------- |
  | **Repository access**     | Cloner ton code et créer des branches de travail                            |
  | **Pull requests**         | Créer des PR avec les changements des agents pour que tu puisses les relire |
  | **Issues**                | Suivre les bugs et les tâches que les agents découvrent ou corrigent        |
  | **Checks and statuses**   | Rendre compte de la qualité du code et des résultats de tests               |
  | **Actions and workflows** | Surveiller les pipelines CI/CD et l’état des déploiements                   |
</div>

Toutes les autorisations respectent le principe du moindre privilège nécessaire au fonctionnement des agents en arrière-plan.

<div id="ip-allow-list-configuration">
  ## Configuration de la liste d’autorisation d’IP
</div>

Si ton organisation utilise la fonctionnalité de liste d’autorisation d’IP de GitHub pour restreindre l’accès à tes dépôts, tu dois d’abord contacter le support pour activer la fonctionnalité de liste d’autorisation d’IP pour ton équipe.

<div id="contact-support">
  ### Contacter le support
</div>

Avant de configurer des listes d’autorisation d’IP, contacte [hi@cursor.com](mailto:hi@cursor.com) pour activer cette fonctionnalité pour ton équipe. C’est requis pour les deux méthodes de configuration ci-dessous.

<div id="enable-ip-allow-list-configuration-for-installed-github-apps-recommended">
  ### Activer la configuration de la liste d’autorisation d’IP pour les applications GitHub installées (recommandé)
</div>

L’application GitHub Cursor a déjà la liste d’IP préconfigurée. Tu peux activer la liste d’autorisation pour les applications installées afin d’hériter automatiquement de cette liste. C’est l’approche **recommandée**, car elle nous permet de mettre à jour la liste et ton organisation reçoit les mises à jour automatiquement.

Pour l’activer :

1. Va dans les paramètres de sécurité de ton organisation
2. Accède aux paramètres de la liste d’autorisation d’IP
3. Coche **« Allow access by GitHub Apps »**

Pour des instructions détaillées, consulte [la documentation de GitHub](https://docs.github.com/en/enterprise-cloud@latest/organizations/keeping-your-organization-secure/managing-security-settings-for-your-organization/managing-allowed-ip-addresses-for-your-organization#allowing-access-by-github-apps).

<div id="add-ips-directly-to-your-allowlist">
  ### Ajouter des IP directement à ta liste d’autorisation
</div>

Si ton organisation utilise des listes d’autorisation définies par un IdP dans GitHub ou ne peut pas utiliser la liste d’autorisation préconfigurée, tu peux ajouter les adresses IP manuellement :

```
184.73.225.134
3.209.66.12
52.44.113.131
```

<Note>
  La liste d’adresses IP peut occasionnellement changer. Les équipes utilisant des listes d’autorisation d’IP seront prévenues à l’avance avant tout ajout ou suppression d’adresses IP.
</Note>

<div id="troubleshooting">
  ## Dépannage
</div>

<AccordionGroup>
  <Accordion title="L'agent ne peut pas accéder au dépôt">
    * Installe l'app GitHub avec accès au dépôt
    * Vérifie les permissions du dépôt pour les dépôts privés
    * Vérifie les permissions de ton compte GitHub
  </Accordion>

  <Accordion title="Accès refusé pour les pull requests">
    * Accorde à l'app l'accès en écriture aux pull requests
    * Vérifie les règles de protection de branches
    * Réinstalle si l'installation de l'app a expiré
  </Accordion>

  <Accordion title="App non visible dans les paramètres GitHub">
    * Vérifie si elle est installée au niveau de l'organisation
    * Réinstalle depuis [github.com/apps/cursor](https://github.com/apps/cursor)
    * Contacte le support si l'installation est corrompue
  </Accordion>
</AccordionGroup>

---

← Previous: [Git](./git.md) | [Index](./index.md) | Next: [Linear](./linear.md) →