---
title: "API Admin"
source: "https://docs.cursor.com/fr/account/teams/admin-api"
language: "fr"
language_name: "French"
---

# API Admin
Source: https://docs.cursor.com/fr/account/teams/admin-api

Accède aux métriques d’équipe, aux données d’usage et aux informations de dépenses via l’API

L’API Admin te permet d’accéder par programmation aux données de ton équipe, y compris les infos membres, les métriques d’usage et les détails de dépenses. Crée des tableaux de bord personnalisés, des outils de monitoring, ou intègre-la à tes workflows existants.

<Note>
  L’API en est à sa première version. On étend les capacités selon les retours — dis-nous quels endpoints il te faut !
</Note>

<div id="authentication">
  ## Authentification
</div>

Toutes les requêtes à l’API nécessitent une authentification au moyen d’une clé API. Seuls les administrateurs de l’équipe peuvent créer et gérer des clés API.

Les clés API sont liées à l’organisation, visibles par tous les administrateurs, et ne sont pas affectées par l’état du compte du créateur initial.

<div id="creating-an-api-key">
  ### Créer une clé API
</div>

1. Va sur **cursor.com/dashboard** → onglet **Settings** → **Cursor Admin API Keys**
2. Clique sur **Create New API Key**
3. Donne à ta clé un nom explicite (p. ex. « Usage Dashboard Integration »)
4. Copie la clé générée tout de suite — tu ne la verras plus après

Format : `key_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`

<div id="using-your-api-key">
  ### Utiliser ta clé API
</div>

Utilise ta clé API comme nom d’utilisateur dans l’authentification basique :

**Utiliser curl avec une authentification basique :**

```bash  theme={null}
curl https://api.cursor.com/{route} -u CLÉ_API:
```

**Ou définis directement l’en-tête Authorization :**

```bash  theme={null}
Authorization : Basic {base64_encode('API_KEY:')}
```

<div id="base-url">
  ## URL de base
</div>

Tous les points de terminaison de l’API utilisent :

```
https://api.cursor.com
```

<div id="endpoints">
  ## Points de terminaison
</div>

<div id="get-team-members">
  ### Obtenir les membres de l’équipe
</div>

Récupère tous les membres de l’équipe et leurs informations.

```
GET /teams/members
```

#### Réponse

Renvoie un tableau d’objets représentant des membres de l’équipe :

```typescript  theme={null}
{
  teamMembers: {
    name: string;
    email: string;
    role: 'owner' | 'member' | 'free-owner';
  }[];
}
```

#### Exemple de réponse

```json  theme={null}
{
  "teamMembers": [
    {
      "name": "Alex",
      "email": "developer@company.com",
      "role": "membre"
    },
    {
      "name": "Sam",
      "email": "admin@company.com",
      "role": "propriétaire"
    }
  ]
}

```

#### Exemple de demande

```bash  theme={null}
curl -X GET https://api.cursor.com/teams/members \
  -u TA_CLÉ_API:
```

### Obtenir les données d'utilisation quotidiennes

Récupère des métriques d'utilisation quotidiennes détaillées pour ton équipe sur une plage de dates. Fournit des informations sur les modifications de code, l'utilisation de l'assistance IA et les taux d'acceptation.

```
POST /teams/daily-usage-data
```

#### Corps de la requête

<div className="full-width-table">
  | Paramètre   | Type   | Obligatoire | Description                                    |
  | :---------- | :----- | :---------- | :--------------------------------------------- |
  | `startDate` | number | Oui         | Date de début en millisecondes depuis l'époque |
  | `endDate`   | number | Oui         | Date de fin en millisecondes depuis l'époque   |
</div>

<Note>
  L’intervalle de dates ne peut pas dépasser 90 jours. Fais plusieurs requêtes pour des périodes plus longues.
</Note>

#### Réponse

```typescript  theme={null}
{
  data: {
    date: number;
    isActive: boolean;
    totalLinesAdded: number;
    totalLinesDeleted: number;
    acceptedLinesAdded: number;
    acceptedLinesDeleted: number;
    totalApplies: number;
    totalAccepts: number;
    totalRejects: number;
    totalTabsShown: number;
    totalTabsAccepted: number;
    composerRequests: number;
    chatRequests: number;
    agentRequests: number;
    cmdkUsages: number;
    subscriptionIncludedReqs: number;
    apiKeyReqs: number;
    usageBasedReqs: number;
    bugbotUsages: number;
    mostUsedModel: string;
    applyMostUsedExtension?: string;
    tabMostUsedExtension?: string;
    clientVersion?: string;
    email?: string;
  }[];
  period: {
    startDate: number;
    endDate: number;
  };
}
```

<div id="response-fields">
  #### Champs de réponse
</div>

<div className="full-width-table">
  | Champ                      | Description                                            |
  | :------------------------- | :----------------------------------------------------- |
  | `date`                     | Date en millisecondes Unix                             |
  | `isActive`                 | Utilisateur actif ce jour-là                           |
  | `totalLinesAdded`          | Lignes de code ajoutées                                |
  | `totalLinesDeleted`        | Lignes de code supprimées                              |
  | `acceptedLinesAdded`       | Lignes ajoutées à partir de suggestions IA acceptées   |
  | `acceptedLinesDeleted`     | Lignes supprimées à partir de suggestions IA acceptées |
  | `totalApplies`             | Opérations d’application                               |
  | `totalAccepts`             | Suggestions acceptées                                  |
  | `totalRejects`             | Suggestions rejetées                                   |
  | `totalTabsShown`           | Autocomplétions d’onglet affichées                     |
  | `totalTabsAccepted`        | Autocomplétions d’onglet acceptées                     |
  | `composerRequests`         | Requêtes du Composer                                   |
  | `chatRequests`             | Requêtes de chat                                       |
  | `agentRequests`            | Requêtes de l’agent                                    |
  | `cmdkUsages`               | Utilisations de la palette de commandes (Cmd+K)        |
  | `subscriptionIncludedReqs` | Requêtes incluses dans l’abonnement                    |
  | `apiKeyReqs`               | Requêtes via clé API                                   |
  | `usageBasedReqs`           | Requêtes à l’usage                                     |
  | `bugbotUsages`             | Utilisations de Bugbot                                 |
  | `mostUsedModel`            | Modèle d’IA le plus utilisé                            |
  | `applyMostUsedExtension`   | Extension de fichier la plus utilisée pour les apply   |
  | `tabMostUsedExtension`     | Extension de fichier la plus utilisée pour les tabs    |
  | `clientVersion`            | Version de Cursor                                      |
  | `email`                    | E-mail de l’utilisateur                                |
</div>

#### Exemple de réponse

```json  theme={null}
{
  "data": [
    {
      "date": 1710720000000,
      "isActive": true,
      "totalLinesAdded": 1543,
      "totalLinesDeleted": 892,
      "acceptedLinesAdded": 1102,
      "acceptedLinesDeleted": 645,
      "totalApplies": 87,
      "totalAccepts": 73,
      "totalRejects": 14,
      "totalTabsShown": 342,
      "totalTabsAccepted": 289,
      "composerRequests": 45,
      "chatRequests": 128,
      "agentRequests": 12,
      "cmdkUsages": 67,
      "subscriptionIncludedReqs": 180,
      "apiKeyReqs": 0,
      "usageBasedReqs": 5,
      "bugbotUsages": 3,
      "mostUsedModel": "gpt-4",
      "applyMostUsedExtension": ".tsx",
      "tabMostUsedExtension": ".ts",
      "clientVersion": "0.25.1",
      "email": "developer@company.com"
    },
    {
      "date": 1710806400000,
      "isActive": true,
      "totalLinesAdded": 2104,
      "totalLinesDeleted": 1203,
      "acceptedLinesAdded": 1876,
      "acceptedLinesDeleted": 987,
      "totalApplies": 102,
      "totalAccepts": 91,
      "totalRejects": 11,
      "totalTabsShown": 456,
      "totalTabsAccepted": 398,
      "composerRequests": 67,
      "chatRequests": 156,
      "agentRequests": 23,
      "cmdkUsages": 89,
      "subscriptionIncludedReqs": 320,
      "apiKeyReqs": 15,
      "usageBasedReqs": 0,
      "bugbotUsages": 5,
      "mostUsedModel": "claude-3-opus",
      "applyMostUsedExtension": ".py",
      "tabMostUsedExtension": ".py",
      "clientVersion": "0.25.1",
      "email": "developer@company.com"
    }
  ],
  "period": {
    "startDate": 1710720000000,
    "endDate": 1710892800000
  }
}
```

#### Exemple de demande

```bash  theme={null}
curl -X POST https://api.cursor.com/teams/daily-usage-data \
  -u YOUR_API_KEY: \
  -H "Content-Type: application/json" \
  -d '{
    "startDate": 1710720000000,
    "endDate": 1710892800000
  }'
```

<div id="get-spending-data">
  ### Récupérer les données de dépenses
</div>

Récupère les informations de dépenses pour le mois calendaire en cours, avec recherche, tri et pagination.

```
POST /teams/spend
```

#### Corps de la requête

<div className="full-width-table">
  | Paramètre       | Type   | Obligatoire | Description                                               |
  | :-------------- | :----- | :---------- | :-------------------------------------------------------- |
  | `searchTerm`    | string | Non         | Recherche dans les noms d’utilisateur et les e-mails      |
  | `sortBy`        | string | Non         | Trier par : `amount`, `date`, `user`. Par défaut : `date` |
  | `sortDirection` | string | Non         | Ordre de tri : `asc`, `desc`. Par défaut : `desc`         |
  | `page`          | number | Non         | Numéro de page (indexé à partir de 1). Par défaut : `1`   |
  | `pageSize`      | number | Non         | Résultats par page                                        |
</div>

#### Réponse

```typescript  theme={null}
{
  teamMemberSpend: {
    spendCents: number;
    fastPremiumRequests: number;
    name: string;
    email: string;
    role: 'owner' | 'member' | 'free-owner';
    hardLimitOverrideDollars: number;
  }[];
  subscriptionCycleStart: number;
  totalMembers: number;
  totalPages: number;
}
```

<div id="response-fields">
  #### Champs de réponse
</div>

<div className="full-width-table">
  | Champ                      | Description                                       |
  | :------------------------- | :------------------------------------------------ |
  | `spendCents`               | Dépense totale en centimes                        |
  | `fastPremiumRequests`      | Requêtes du modèle premium rapide                 |
  | `name`                     | Nom du membre                                     |
  | `email`                    | E-mail du membre                                  |
  | `role`                     | Rôle dans l’équipe                                |
  | `hardLimitOverrideDollars` | Dérogation personnalisée à la limite de dépense   |
  | `subscriptionCycleStart`   | Début du cycle d’abonnement (millisecondes epoch) |
  | `totalMembers`             | Nombre total de membres de l’équipe               |
  | `totalPages`               | Nombre total de pages                             |
</div>

#### Exemple de réponse

```json  theme={null}
{
  "teamMemberSpend": [
    {
      "spendCents": 2450,
      "fastPremiumRequests": 1250,
      "name": "Alex",
      "email": "developer@company.com",
      "role": "membre",
      "hardLimitOverrideDollars": 100
    },
    {
      "spendCents": 1875,
      "fastPremiumRequests": 980,
      "name": "Sam",
      "email": "admin@company.com",
      "role": "propriétaire",
      "hardLimitOverrideDollars": 0
    },
  ],
  "subscriptionCycleStart": 1708992000000,
  "totalMembers": 15,
  "totalPages": 1
}
```

<div id="example-requests">
  #### Exemples de requêtes
</div>

**Données de dépenses de base :**

```bash  theme={null}
curl -X POST https://api.cursor.com/teams/spend \
  -u YOUR_API_KEY: \
  -H "Content-Type: application/json" \
  -d '{}'
```

**Rechercher un utilisateur précis avec pagination :**

```bash  theme={null}
curl -X POST https://api.cursor.com/teams/spend \
  -u YOUR_API_KEY: \
  -H "Content-Type: application/json" \
  -d '{
    "searchTerm": "alex@company.com",
    "page": 2,
    "pageSize": 25
  }'
```

<div id="get-usage-events-data">
  ### Obtenir les données d’événements d’usage
</div>

Récupère des événements d’usage détaillés pour ton équipe avec des options complètes de filtrage, de recherche et de pagination. Cet endpoint fournit des informations granulaires sur les appels API individuels, l’usage des modèles, la consommation de jetons et les coûts.

```
POST /teams/filtered-usage-events
```

#### Corps de la requête

<div className="full-width-table">
  | Paramètre   | Type   | Requis | Description                                             |
  | :---------- | :----- | :----- | :------------------------------------------------------ |
  | `startDate` | number | Non    | Date de début en millisecondes depuis l’époque (epoch)  |
  | `endDate`   | number | Non    | Date de fin en millisecondes depuis l’époque (epoch)    |
  | `userId`    | number | Non    | Filtrer par ID utilisateur spécifique                   |
  | `page`      | number | Non    | Numéro de page (indexé à partir de 1). Par défaut : `1` |
  | `pageSize`  | number | Non    | Nombre de résultats par page. Par défaut : `10`         |
  | `email`     | string | Non    | Filtrer par adresse e-mail de l’utilisateur             |
</div>

#### Réponse

```typescript  theme={null}
{
  totalUsageEventsCount: number;
  pagination: {
    numPages: number;
    currentPage: number;
    pageSize: number;
    hasNextPage: boolean;
    hasPreviousPage: boolean;
  };
  usageEvents: {
    timestamp: string;
    model: string;
    kind: string;
    maxMode: boolean;
    requestsCosts: number;
    isTokenBasedCall: boolean;
    tokenUsage?: {
      inputTokens: number;
      outputTokens: number;
      cacheWriteTokens: number;
      cacheReadTokens: number;
      totalCents: number;
    };
    isFreeBugbot: boolean;
    userEmail: string;
  }[];
  period: {
    startDate: number;
    endDate: number;
  };
}
```

<div id="response-fields-explained">
  #### Explication des champs de réponse
</div>

<div className="full-width-table">
  | Champ                   | Description                                                                        |
  | :---------------------- | :--------------------------------------------------------------------------------- |
  | `totalUsageEventsCount` | Nombre total d’événements d’utilisation correspondant à la requête                 |
  | `pagination`            | Métadonnées de pagination pour naviguer dans les résultats                         |
  | `timestamp`             | Horodatage de l’événement en millisecondes Unix (epoch)                            |
  | `model`                 | Modèle d’IA utilisé pour la requête                                                |
  | `kind`                  | Catégorie d’utilisation (p. ex. « Usage-based », « Included in Business »)         |
  | `maxMode`               | Indique si le mode max était activé                                                |
  | `requestsCosts`         | Coût en unités de requête                                                          |
  | `isTokenBasedCall`      | true lorsque l’événement est facturé comme un événement à l’usage                  |
  | `tokenUsage`            | Détail de la consommation de jetons (disponible lorsque isTokenBasedCall est true) |
  | `isFreeBugbot`          | Indique s’il s’agissait d’une utilisation gratuite de bugbot                       |
  | `userEmail`             | E-mail de l’utilisateur ayant effectué la requête                                  |
  | `period`                | Intervalle de dates des données interrogées                                        |
</div>

#### Exemple de réponse

```json  theme={null}
{
  "totalUsageEventsCount": 113,
  "pagination": {
    "numPages": 12,
    "currentPage": 1,
    "pageSize": 10,
    "hasNextPage": true,
    "hasPreviousPage": false
  },
  "usageEvents": [
    {
      "timestamp": "1750979225854",
      "model": "claude-4-opus",
      "kind": "À l'usage",
      "maxMode": true,
      "requestsCosts": 5,
      "isTokenBasedCall": true,
      "tokenUsage": {
        "inputTokens": 126,
        "outputTokens": 450,
        "cacheWriteTokens": 6112,
        "cacheReadTokens": 11964,
        "totalCents": 20.18232
      },
      "isFreeBugbot": false,
      "userEmail": "developer@company.com"
    },
    {
      "timestamp": "1750979173824",
      "model": "claude-4-opus",
      "kind": "Usage-based",
      "maxMode": true,
      "requestsCosts": 10,
      "isTokenBasedCall": true,
      "tokenUsage": {
        "inputTokens": 5805,
        "outputTokens": 311,
        "cacheWriteTokens": 11964,
        "cacheReadTokens": 0,
        "totalCents": 40.16699999999999
      },
      "isFreeBugbot": false,
      "userEmail": "developer@company.com"
    },
    {
      "timestamp": "1750978339901",
      "model": "claude-4-sonnet-thinking",
      "kind": "Inclus dans l’offre Business"
      "maxMode": true,
      "requestsCosts": 1.4,
      "isTokenBasedCall": false,
      "isFreeBugbot": false,
      "userEmail": "admin@company.com"
    }
  ],
  "period": {
    "startDate": 1748411762359,
    "endDate": 1751003762359
  }
}
```

<div id="example-requests">
  #### Exemples de requêtes
</div>

**Récupérer tous les événements d’utilisation avec la pagination par défaut :**

```bash  theme={null}
curl -X POST https://api.cursor.com/teams/filtered-usage-events \
  -u YOUR_API_KEY: \
  -H "Content-Type: application/json" \
  -d '{}'
```

**Filtrer par plage de dates et par utilisateur spécifique :**

```bash  theme={null}
curl -X POST https://api.cursor.com/teams/filtered-usage-events \
  -u YOUR_API_KEY: \
  -H "Content-Type: application/json" \
  -d '{
    "startDate": 1748411762359,
    "endDate": 1751003762359,
    "email": "developer@company.com",
    "page": 1,
    "pageSize": 25
  }'
```

**Récupérer les événements d’usage d’un utilisateur spécifique avec une pagination personnalisée :**

```bash  theme={null}
curl -X POST https://api.cursor.com/teams/filtered-usage-events \
  -u YOUR_API_KEY: \
  -H "Content-Type: application/json" \
  -d '{
    "userId": 12345,
    "page": 2,
    "pageSize": 50
  }'
```

<div id="set-user-spend-limit">
  ### Définir la limite de dépenses par utilisateur
</div>

Définis des limites de dépenses pour chaque membre de l'équipe. Ça te permet de contrôler combien chaque utilisateur peut dépenser pour l'utilisation de l'IA au sein de ton équipe.

```
POST /teams/user-spend-limit
```

<Note>
  **Limitation du débit :** 60 requêtes par minute et par équipe
</Note>

#### Corps de la requête

<div className="full-width-table">
  | Paramètre           | Type   | Obligatoire | Description                                                           |
  | :------------------ | :----- | :---------- | :-------------------------------------------------------------------- |
  | `userEmail`         | string | Oui         | Adresse e-mail du membre de l'équipe                                  |
  | `spendLimitDollars` | number | Oui         | Plafond de dépenses en dollars (entier uniquement, pas de décimales). |
</div>

<Note>
  * L'utilisateur doit déjà faire partie de ton équipe
  * Seules les valeurs entières sont acceptées (aucun montant décimal)
  * Définir `spendLimitDollars` sur 0 fixe la limite à 0 \$
</Note>

#### Réponse

Retourne une réponse normalisée indiquant un succès ou un échec :

```typescript  theme={null}
{
  outcome: 'success' | 'error';
  message: string;
}
```

<div id="example-responses">
  #### Exemples de réponses
</div>

**Limite définie avec succès :**

```json  theme={null}
{
  "outcome": "succès",
  "message": "Limite de dépenses définie à 100 $ pour l’utilisateur developer@company.com"
}
```

**Réponse d’erreur :**

```json  theme={null}
{
  "outcome": "error",
  "message": "Format d’e-mail invalide"
}
```

<div id="example-requests">
  #### Exemples de requêtes
</div>

**Définir une limite de dépenses :**

```bash  theme={null}
curl -X POST https://api.cursor.com/teams/user-spend-limit \
  -u YOUR_API_KEY: \
  -H "Content-Type: application/json" \
  -d '{
    "userEmail": "developer@company.com",
    "spendLimitDollars": 100
  }'
```

<div id="repo-blocklists-api">
  ### API des listes de blocage de dépôts
</div>

Ajoute des dépôts et des motifs pour empêcher l’indexation de certains fichiers ou répertoires, ou leur utilisation comme contexte pour ton équipe.

#### Obtenir les listes de blocage des dépôts de l'équipe

Récupère toutes les listes de blocage de dépôts configurées pour ton équipe.

```
GET /settings/repo-blocklists/repos
```

<div id="response">
  ##### Réponse
</div>

Renvoie un tableau d’objets de liste de blocage de dépôt :

```typescript  theme={null}
{
  repos: {
    id: string;
    url: string;
    patterns: string[];
  }[];
}
```

<div id="example-response">
  ##### Exemple de réponse
</div>

```json  theme={null}
{
  "repos": [
    {
      "id": "repo_123",
      "url": "https://github.com/company/sensitive-repo",
      "patterns": ["*.env", "config/*", "secrets/**"]
    },
    {
      "id": "repo_456",
      "url": "https://github.com/company/internal-tools",
      "patterns": ["*"]
    }
  ]
}
```

<div id="example-request">
  ##### Exemple de demande
</div>

```bash  theme={null}
curl -X GET https://api.cursor.com/settings/repo-blocklists/repos \
  -u TA_CLE_API:
```

<div id="upsert-repo-blocklists">
  #### Upsert des listes de blocage de dépôts
</div>

Remplace les listes de blocage de dépôts existantes pour les dépôts fournis.
*Remarque : cet endpoint ne remplacera que les patterns pour les dépôts fournis. Tous les autres dépôts ne seront pas affectés.*

```
POST /settings/repo-blocklists/repos/upsert
```

<div id="request-body">
  ##### Corps de la requête
</div>

| Paramètre | Type  | Requis | Description                             |
| --------- | ----- | ------ | --------------------------------------- |
| repos     | array | Oui    | Tableau d’objets de blocklist de dépôts |

Chaque objet de dépôt doit contenir :

| Champ    | Type      | Requis | Description                                                           |
| -------- | --------- | ------ | --------------------------------------------------------------------- |
| url      | string    | Oui    | URL du dépôt à ajouter à la blocklist                                 |
| patterns | string\[] | Oui    | Tableau de modèles de fichiers à bloquer (motifs glob pris en charge) |

<div id="response">
  ##### Réponse
</div>

Renvoie la liste mise à jour des blocklists de dépôts :

```typescript  theme={null}
{
  repos: {
    id: string;
    url: string;
    patterns: string[];
  }[];
}
```

<div id="example-request">
  ##### Exemple de demande
</div>

```bash  theme={null}
curl -X POST https://api.cursor.com/settings/repo-blocklists/repos/upsert \
  -u YOUR_API_KEY: \
  -H "Content-Type: application/json" \
  -d '{
    "repos": [
      {
        "url": "https://github.com/company/sensitive-repo",
        "patterns": ["*.env", "config/*", "secrets/**"]
      },
      {
        "url": "https://github.com/company/internal-tools", 
        "patterns": ["*"]
      }
    ]
  }'
```

<div id="delete-repo-blocklist">
  #### Supprimer un dépôt de la blocklist
</div>

Supprime un dépôt spécifique de la blocklist.

```
DELETE /settings/repo-blocklists/repos/:repoId
```

<div id="parameters">
  ##### Paramètres
</div>

| Paramètre | Type   | Requis | Description                             |
| --------- | ------ | ------ | --------------------------------------- |
| repoId    | string | Oui    | ID de la blocklist du dépôt à supprimer |

<div id="response">
  ##### Réponse
</div>

Renvoie 204 No Content en cas de suppression réussie.

<div id="example-request">
  ##### Exemple de demande
</div>

```bash  theme={null}
curl -X DELETE https://api.cursor.com/settings/repo-blocklists/repos/repo_123 \
  -u TA_CLÉ_API:
```

<div id="pattern-examples">
  #### Exemples de modèles
</div>

Modèles courants de liste de blocage :

* `*` - Bloquer tout le dépôt
* `*.env` - Bloquer tous les fichiers .env
* `config/*` - Bloquer tous les fichiers du répertoire config
* `**/*.secret` - Bloquer tous les fichiers .secret dans n’importe quel sous-répertoire
* `src/api/keys.ts` - Bloquer un fichier spécifique

---

← Previous: [Tarification](./tarification.md) | [Index](./index.md) | Next: [API de suivi de code par IA](./api-de-suivi-de-code-par-ia.md) →