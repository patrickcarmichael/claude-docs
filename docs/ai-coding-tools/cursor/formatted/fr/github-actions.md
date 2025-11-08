---
title: "GitHub Actions"
source: "https://docs.cursor.com/fr/cli/github-actions"
language: "fr"
language_name: "French"
---

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

---

← Previous: [Mettre à jour la doc](./mettre-jour-la-doc.md) | [Index](./index.md) | Next: [Utiliser le CLI en mode headless](./utiliser-le-cli-en-mode-headless.md) →