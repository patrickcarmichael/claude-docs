---
title: "Format de sortie"
source: "https://docs.cursor.com/fr/cli/reference/output-format"
language: "fr"
language_name: "French"
---

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

---

← Previous: [Configuration](./configuration.md) | [Index](./index.md) | Next: [Paramètres](./paramtres.md) →