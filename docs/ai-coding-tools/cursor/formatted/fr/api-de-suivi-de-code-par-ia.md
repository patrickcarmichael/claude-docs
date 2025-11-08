---
title: "API de suivi de code par IA"
source: "https://docs.cursor.com/fr/account/teams/ai-code-tracking-api"
language: "fr"
language_name: "French"
---

# API de suivi de code par IA
Source: https://docs.cursor.com/fr/account/teams/ai-code-tracking-api

Accède aux analytics de code générées par l’IA pour les dépôts de ton équipe

Accède aux analytics de code générées par l’IA pour les dépôts de ton équipe. Ça inclut l’usage de l’IA par commit ainsi que le détail des modifications d’IA acceptées.

<Note>
  L’API est en première release. On étend les capacités selon les retours — dis-nous quels endpoints tu veux !
</Note>

* **Disponibilité**: Réservée aux équipes Enterprise
* **Statut**: Alpha (la structure des réponses et les champs peuvent changer)

<div id="authentication">
  ## Authentification
</div>

Toutes les requêtes à l’API nécessitent une authentification avec une clé d’API. Cette API utilise le même mécanisme d’authentification de l’Admin API que les autres endpoints.

Pour des instructions détaillées sur l’authentification, vois [Admin API authentication](/fr/account/teams/admin-api#authentication).

<div id="base-url">
  ## URL de base
</div>

Toutes les routes de l’API utilisent :

```
https://api.cursor.com
```

<div id="rate-limits">
  ## Limites de débit
</div>

* 5 requêtes par minute et par équipe, par endpoint

<div id="query-parameters">
  ## Paramètres de requête
</div>

Tous les endpoints ci-dessous acceptent les mêmes paramètres via la chaîne de requête :

<div className="full-width-table">
  | Paramètre   | Type   | Requis | Description                                                                                                                                                                                                |                                                                                                                                              |
  | :---------- | :----- | :----- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
  | `startDate` | string | date   | Non                                                                                                                                                                                                        | Chaîne de date ISO, le littéral "now", ou des jours relatifs comme "7d" (équivaut à maintenant - 7 jours). Par défaut : maintenant - 7 jours |
  | `endDate`   | string | date   | Non                                                                                                                                                                                                        | Chaîne de date ISO, le littéral "now", ou des jours relatifs comme "0d". Par défaut : maintenant                                             |
  | `page`      | number | Non    | Numéro de page (indexé à partir de 1). Par défaut : 1                                                                                                                                                      |                                                                                                                                              |
  | `pageSize`  | number | Non    | Résultats par page. Par défaut : 100, max : 1000                                                                                                                                                           |                                                                                                                                              |
  | `user`      | string | Non    | Filtre optionnel par un seul utilisateur. Accepte une adresse e-mail (p. ex. [developer@company.com](mailto:developer@company.com)), un ID encodé (p. ex. user\_abc123...), ou un ID numérique (p. ex. 42) |                                                                                                                                              |
</div>

<Note>
  Les réponses renvoient userId comme ID externe encodé avec le préfixe user\_. C’est stable pour une consommation via l’API.
</Note>

<div id="semantics-and-how-metrics-are-computed">
  ## Sémantique et calcul des métriques
</div>

* **Sources** : "TAB" correspond aux complétions en ligne acceptées ; "COMPOSER" correspond aux diffs acceptés depuis Composer
* **Métriques de lignes** : tabLinesAdded/Deleted et composerLinesAdded/Deleted sont comptées séparément ; nonAiLinesAdded/Deleted sont calculées comme max(0, totalLines - AI lines)
* **Mode confidentialité** : S’il est activé côté client, certaines métadonnées (comme fileName) peuvent être omises
* **Infos de branche** : isPrimaryBranch vaut true lorsque la branche actuelle est la branche par défaut du dépôt ; peut être undefined si les infos du dépôt ne sont pas disponibles

Tu peux parcourir ce fichier pour comprendre comment les commits et les modifications sont détectés et signalés.

<div id="endpoints">
  ## Endpoints
</div>

<div id="get-ai-commit-metrics-json-paginated">
  ### Récupérer les métriques de commits IA (JSON, paginées)
</div>

Récupère des métriques agrégées par commit attribuant les lignes à TAB, COMPOSER et au non-IA.

```
GET /analytics/ai-code/commits
```

<div id="response">
  #### Réponses
</div>

```typescript  theme={null}
{
  items: AiCommitMetric[];
  totalCount: number;
  page: number;
  pageSize: number;
}
```

<div id="aicommitmetric-fields">
  #### Champs AiCommitMetric
</div>

<div className="full-width-table">
  | Champ                  | Type    | Description                                      |                                              |
  | :--------------------- | :------ | :----------------------------------------------- | -------------------------------------------- |
  | `commitHash`           | string  | Hachage du commit Git                            |                                              |
  | `userId`               | string  | ID utilisateur encodé (p. ex. user\_abc123)      |                                              |
  | `userEmail`            | string  | Adresse e-mail de l’utilisateur                  |                                              |
  | `repoName`             | string  | null                                             | Nom du dépôt                                 |
  | `branchName`           | string  | null                                             | Nom de la branche                            |
  | `isPrimaryBranch`      | boolean | null                                             | Indique s’il s’agit de la branche principale |
  | `totalLinesAdded`      | number  | Nombre total de lignes ajoutées dans le commit   |                                              |
  | `totalLinesDeleted`    | number  | Nombre total de lignes supprimées dans le commit |                                              |
  | `tabLinesAdded`        | number  | Lignes ajoutées via des complétions Tab          |                                              |
  | `tabLinesDeleted`      | number  | Lignes supprimées via des complétions Tab        |                                              |
  | `composerLinesAdded`   | number  | Lignes ajoutées via Composer                     |                                              |
  | `composerLinesDeleted` | number  | Lignes supprimées via Composer                   |                                              |
  | `nonAiLinesAdded`      | number  | null                                             | Lignes non AI ajoutées                       |
  | `nonAiLinesDeleted`    | number  | null                                             | Lignes non AI supprimées                     |
  | `message`              | string  | null                                             | Message de commit                            |
  | `commitTs`             | string  | null                                             | Horodatage du commit (format ISO)            |
  | `createdAt`            | string  | Horodatage d’ingestion (format ISO)              |                                              |
</div>

<div id="example-response">
  #### Exemple de réponse
</div>

```json  theme={null}
{
  "items": [
    {
      "commitHash": "a1b2c3d4",
      "userId": "user_3k9x8q...",
      "userEmail": "developer@company.com",
      "repoName": "company/repo",
      "branchName": "main",
      "isPrimaryBranch": true,
      "totalLinesAdded": 120,
      "totalLinesDeleted": 30,
      "tabLinesAdded": 50,
      "tabLinesDeleted": 10,
      "composerLinesAdded": 40,
      "composerLinesDeleted": 5,
      "nonAiLinesAdded": 30,
      "nonAiLinesDeleted": 15,
      "message": "Refactor : extraire le client d’analytics"
      "commitTs": "2025-07-30T14:12:03.000Z",
      "createdAt": "2025-07-30T14:12:30.000Z"
    }
  ],
  "totalCount": 42,
  "page": 1,
  "pageSize": 100
}
```

<div id="example-requests">
  #### Exemples de demandes
</div>

**Demande simple :**

```bash  theme={null}
curl -X GET "https://api.cursor.com/analytics/ai-code/commits?startDate=7d&endDate=now&page=1&pageSize=100" \
  -u TA_CLÉ_API:
```

**Filtrer par utilisateur (e-mail) :**

```bash  theme={null}
curl -X GET "https://api.cursor.com/analytics/ai-code/commits?startDate=2025-06-01T00:00:00Z&endDate=now&user=developer@company.com" \
  -u TA_CLEF_API:
```

<div id="download-ai-commit-metrics-csv-streaming">
  ### Télécharger les métriques de commits IA (CSV, streaming)
</div>

Télécharge les métriques de commits au format CSV pour des extractions de données volumineuses.

```
GET /analytics/ai-code/commits.csv
```

#### Réponse

En-têtes :

* Content-Type: text/csv; charset=utf-8

<div id="csv-columns">
  #### Colonnes CSV
</div>

<div className="full-width-table">
  | Colonne                  | Type    | Description                                      |
  | :----------------------- | :------ | :----------------------------------------------- |
  | `commit_hash`            | string  | Hash de commit Git                               |
  | `user_id`                | string  | ID utilisateur encodé                            |
  | `user_email`             | string  | Adresse e-mail de l’utilisateur                  |
  | `repo_name`              | string  | Nom du dépôt                                     |
  | `branch_name`            | string  | Nom de la branche                                |
  | `is_primary_branch`      | boolean | Indique s’il s’agit de la branche par défaut     |
  | `total_lines_added`      | number  | Nombre total de lignes ajoutées dans le commit   |
  | `total_lines_deleted`    | number  | Nombre total de lignes supprimées dans le commit |
  | `tab_lines_added`        | number  | Lignes ajoutées via les complétions Tab          |
  | `tab_lines_deleted`      | number  | Lignes supprimées via les complétions Tab        |
  | `composer_lines_added`   | number  | Lignes ajoutées via Composer                     |
  | `composer_lines_deleted` | number  | Lignes supprimées via Composer                   |
  | `non_ai_lines_added`     | number  | Lignes non IA ajoutées                           |
  | `non_ai_lines_deleted`   | number  | Lignes non IA supprimées                         |
  | `message`                | string  | Message de commit                                |
  | `commit_ts`              | string  | Horodatage du commit (format ISO)                |
  | `created_at`             | string  | Horodatage d’ingestion (format ISO)              |
</div>

<div id="sample-csv-output">
  #### Exemple de sortie CSV
</div>

```csv  theme={null}
commit_hash,user_id,user_email,repo_name,branch_name,is_primary_branch,total_lines_added,total_lines_deleted,tab_lines_added,tab_lines_deleted,composer_lines_added,composer_lines_deleted,non_ai_lines_added,non_ai_lines_deleted,message,commit_ts,created_at
a1b2c3d4,user_3k9x8q...,developer@company.com,company/repo,main,true,120,30,50,10,40,5,30,15,"Refactorisation : extraction du client d’analytics",2025-07-30T14:12:03.000Z,2025-07-30T14:12:30.000Z
e5f6g7h8,user_3k9x8q...,developer@company.com,company/repo,feature-branch,false,85,15,30,5,25,3,30,7,"Ajout de la gestion des erreurs",2025-07-30T13:45:21.000Z,2025-07-30T13:45:45.000Z
```

<div id="example-request">
  #### Exemple de demande
</div>

```bash  theme={null}
curl -L "https://api.cursor.com/analytics/ai-code/commits.csv?startDate=2025-07-01T00:00:00Z&endDate=now&user=user_3k9x8q..." \
  -u TA_CLÉ_API: \
  -o commits.csv
```

<div id="get-ai-code-change-metrics-json-paginated">
  ### Obtenir des métriques sur les changements de code IA (JSON, paginées)
</div>

Récupère des changements IA acceptés à un niveau granulaire, regroupés par changeId déterministe. Utile pour analyser les événements IA acceptés indépendamment des commits.

```
GET /analytics/ai-code/changes
```

<div id="response">
  #### Réponses
</div>

```typescript  theme={null}
{
  items: AiCodeChangeMetric[];
  totalCount: number;
  page: number;
  pageSize: number;
}
```

<div id="aicodechangemetric-fields">
  #### Champs AiCodeChangeMetric
</div>

<div className="full-width-table">
  | Champ               | Type   | Description                                                              |                                     |
  | :------------------ | :----- | :----------------------------------------------------------------------- | ----------------------------------- |
  | `changeId`          | string | ID déterministe de la modification                                       |                                     |
  | `userId`            | string | ID utilisateur encodé (p. ex. user\_abc123)                              |                                     |
  | `userEmail`         | string | Adresse e-mail de l’utilisateur                                          |                                     |
  | `source`            | "TAB"  | "COMPOSER"                                                               | Origine de la modification par l’IA |
  | `model`             | string | null                                                                     | Modèle d’IA utilisé                 |
  | `totalLinesAdded`   | number | Nombre total de lignes ajoutées                                          |                                     |
  | `totalLinesDeleted` | number | Nombre total de lignes supprimées                                        |                                     |
  | `createdAt`         | string | Horodatage d’ingestion (format ISO)                                      |                                     |
  | `metadata`          | Array  | Métadonnées de fichier (fileName peut être omis en mode confidentialité) |                                     |
</div>

<div id="example-response">
  #### Exemple de réponse
</div>

```json  theme={null}
{
  "items": [
    {
      "changeId": "749356201",
      "userId": "user_3k9x8q...",
      "userEmail": "developer@company.com",
      "source": "COMPOSER",
      "model": null,
      "totalLinesAdded": 18,
      "totalLinesDeleted": 4,
      "createdAt": "2025-07-30T15:10:12.000Z",
      "metadata": [
        { "fileName": "src/analytics/report.ts", "fileExtension": "ts", "linesAdded": 12, "linesDeleted": 3 },
        { "fileName": "src/analytics/ui.tsx", "fileExtension": "tsx", "linesAdded": 6, "linesDeleted": 1 }
      ]
    }
  ],
  "totalCount": 128,
  "page": 1,
  "pageSize": 200
}
```

<div id="example-requests">
  #### Exemples de demandes
</div>

**Demande de base :**

```bash  theme={null}
curl -X GET "https://api.cursor.com/analytics/ai-code/changes?startDate=14d&endDate=now&page=1&pageSize=200" \
  -u VOTRE_CLÉ_API:
```

**Filtrer par utilisateur (ID encodé) :**

```bash  theme={null}
curl -X GET "https://api.cursor.com/analytics/ai-code/changes?user=user_3k9x8q..." \
  -u TA_CLÉ_API:
```

**Filtrer par utilisateur (e-mail) :**

```bash  theme={null}
curl -X GET "https://api.cursor.com/analytics/ai-code/changes?user=developer@company.com" \
  -u VOTRE_CLE_API:
```

<div id="download-ai-code-change-metrics-csv-streaming">
  ### Télécharger les métriques de modifications de code IA (CSV, streaming)
</div>

Télécharge les métriques de modifications au format CSV pour de larges extractions de données.

```
GET /analytics/ai-code/changes.csv
```

#### Réponse

En-têtes :

* Content-Type: text/csv; charset=utf-8

<div id="csv-columns">
  #### Colonnes CSV
</div>

<div className="full-width-table">
  | Colonne               | Type   | Description                                           |
  | :-------------------- | :----- | :---------------------------------------------------- |
  | `change_id`           | string | ID déterministe de la modification                    |
  | `user_id`             | string | ID utilisateur encodé                                 |
  | `user_email`          | string | Adresse e-mail de l’utilisateur                       |
  | `source`              | string | Origine de la modification par l’IA (TAB ou COMPOSER) |
  | `model`               | string | Modèle d’IA utilisé                                   |
  | `total_lines_added`   | number | Nombre total de lignes ajoutées                       |
  | `total_lines_deleted` | number | Nombre total de lignes supprimées                     |
  | `created_at`          | string | Horodatage d’ingestion (format ISO)                   |
  | `metadata_json`       | string | Tableau de métadonnées sérialisé en JSON              |
</div>

<div id="notes">
  #### Notes
</div>

* metadata\_json est un tableau de métadonnées sérialisé en JSON (peut omettre fileName en mode confidentialité)
* Lors de la lecture du CSV, pense à parser les champs entre guillemets

<div id="sample-csv-output">
  #### Exemple de sortie CSV
</div>

```csv  theme={null}
change_id,user_id,user_email,source,model,total_lines_added,total_lines_deleted,created_at,metadata_json
749356201,user_3k9x8q...,developer@company.com,COMPOSER,gpt-4o,18,4,2025-07-30T15:10:12.000Z,"[{""fileName"":""src/analytics/report.ts"",""fileExtension"":""ts"",""linesAdded"":12,""linesDeleted"":3},{""fileName"":""src/analytics/ui.tsx"",""fileExtension"":""tsx"",""linesAdded"":6,""linesDeleted"":1}]"
749356202,user_3k9x8q...,developer@company.com,TAB,,8,2,2025-07-30T15:08:45.000Z,"[{""fileName"":""src/utils/helpers.ts"",""fileExtension"":""ts"",""linesAdded"":8,""linesDeleted"":2}]"
```

<div id="example-request">
  #### Exemple de demande
</div>

```bash  theme={null}
curl -L "https://api.cursor.com/analytics/ai-code/changes.csv?startDate=30d&endDate=now" \
  -u TA_CLE_API: \
  -o changes.csv
```

<div id="tips">
  ## Conseils
</div>

* Utilise le paramètre `user` pour filtrer rapidement un utilisateur donné sur tous les endpoints
* Pour de larges extractions de données, privilégie les endpoints CSV — ils diffusent côté serveur par pages de 10 000 enregistrements
* `isPrimaryBranch` peut être indéfini si le client n’a pas pu déterminer la branche par défaut
* `commitTs` est l’horodatage du commit ; `createdAt` est l’heure d’ingestion sur nos serveurs
* Certains champs peuvent être absents lorsque le mode confidentialité est activé côté client

<div id="changelog">
  ## Journal des modifications
</div>

* **Version alpha** : Premiers endpoints pour les commits et les modifications. Les formats de réponse pourront évoluer en fonction des retours

---

← Previous: [API Admin](./api-admin.md) | [Index](./index.md) | Next: [Analytics](./analytics.md) →