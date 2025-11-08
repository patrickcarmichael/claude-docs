---
title: "Revue de code"
source: "https://docs.cursor.com/fr/cli/cookbook/code-review"
language: "fr"
language_name: "French"
---

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

---

← Previous: [Bugbot](./bugbot.md) | [Index](./index.md) | Next: [Corriger les échecs CI](./corriger-les-checs-ci.md) →