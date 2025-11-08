---
title: "Travailler avec le contexte"
source: "https://docs.cursor.com/fr/guides/working-with-context"
language: "fr"
language_name: "French"
---

# Travailler avec le contexte
Source: https://docs.cursor.com/fr/guides/working-with-context

Comment travailler avec le contexte dans Cursor

D’abord, c’est quoi une fenêtre de contexte ? Et quel rapport avec le fait de coder efficacement avec Cursor ?

Pour prendre un peu de recul, un large language model (LLM) est un modèle d’IA entraîné à prédire et générer du texte en apprenant des motifs à partir d’énormes jeux de données. Il alimente des outils comme Cursor en comprenant ce que tu saisis et en suggérant du code ou du texte en fonction de ce qu’il a déjà vu.

Les tokens sont les entrées et sorties de ces modèles. Ce sont des morceaux de texte, souvent des fragments de mots, qu’un LLM traite un par un. Les modèles ne lisent pas des phrases entières d’un coup ; ils prédisent le token suivant à partir de ceux qui le précèdent.

Pour voir comment du texte est tokenisé, tu peux utiliser un tokenizer comme [celui-ci](https://tiktokenizer.vercel.app/).

<img src="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/working-with-context/tokenizer.png?fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=29ce8eb4d2c29f254b3757304859d196" alt="Tokenizer" data-og-width="2048" width="2048" data-og-height="1259" height="1259" data-path="images/guides/working-with-context/tokenizer.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/working-with-context/tokenizer.png?w=280&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=4320774dd92cd5ac7c009a20df3c4a63 280w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/working-with-context/tokenizer.png?w=560&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=1a9f636c945c3b6a7d0b7a99408addb6 560w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/working-with-context/tokenizer.png?w=840&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=15c8d4e2cc11dd79179de20312e177cc 840w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/working-with-context/tokenizer.png?w=1100&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=551647ef3c0fa17f5b6bc0c998b9bd2e 1100w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/working-with-context/tokenizer.png?w=1650&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=b1be1180c2a9b94b7230e02d7b9be2ad 1650w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/working-with-context/tokenizer.png?w=2500&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=1af46c0197c8c23e6dbe913c44d90f08 2500w" />

<div id="what-is-context">
  # C’est quoi le contexte ?
</div>

Quand on génère une suggestion de code dans Cursor, le « contexte » désigne les informations fournies au modèle (sous forme de « jetons d’entrée ») que le modèle utilise ensuite pour prédire la suite (sous forme de « jetons de sortie »).

Il existe deux types de contexte :

1. **Contexte d’intention**: ce que tu veux obtenir du modèle. Par exemple, un system prompt sert généralement d’instructions de haut niveau sur la façon dont tu veux que le modèle se comporte. La plupart du « prompting » dans Cursor relève du contexte d’intention. « Passe ce bouton du bleu au vert » est un exemple d’intention explicite ; c’est prescriptif.
2. **Contexte d’état**: l’état du monde à l’instant T. Fournir à Cursor des messages d’erreur, des logs de console, des images ou des extraits de code sont des exemples de contexte lié à l’état. C’est descriptif, pas prescriptif.

Ensemble, ces deux types de contexte fonctionnent de concert en décrivant l’état actuel et l’état futur souhaité, ce qui permet à Cursor de proposer des suggestions de code pertinentes.

```mermaid  theme={null}
flowchart LR
    A["Intention (ce que tu veux)"] --> C[Modèle]
    B["État (ce qui est vrai)"] --> C
    C -- Prédire --> D["Action (ce qu’il fait)"]
```

<div id="providing-context-in-cursor">
  # Fournir du contexte dans Cursor
</div>

Plus tu fournis de contexte pertinent à un modèle, plus il sera utile. Si le contexte donné dans Cursor est insuffisant, le modèle va tenter de résoudre le problème sans les infos nécessaires. Ça mène généralement à :

1. Des hallucinations où le modèle essaie de faire du pattern matching (alors qu’il n’y a pas de pattern), entraînant des résultats inattendus. Ça peut arriver souvent avec des modèles comme `claude-3.5-sonnet` quand ils n’ont pas assez de contexte.
2. L’Agent qui cherche à réunir le contexte par lui-même en explorant la codebase, en lisant des fichiers et en appelant des outils. Un modèle avec de fortes capacités de raisonnement (comme `claude-3.7-sonnet`) peut aller assez loin avec cette stratégie, et fournir le bon contexte initial va en déterminer la trajectoire.

La bonne nouvelle, c’est que Cursor est conçu avec la conscience du contexte au cœur et vise à nécessiter un minimum d’intervention de ta part. Cursor récupère automatiquement les parties de ta codebase que le modèle estime pertinentes, comme le fichier en cours, des patterns sémantiquement similaires dans d’autres fichiers, et d’autres infos de ta session.

Cependant, il y a énormément de contexte possible à exploiter, donc préciser manuellement le contexte que tu sais pertinent pour la tâche est une bonne façon d’orienter les modèles dans la bonne direction.

<div id="symbol">
  ## Symbole @
</div>

La façon la plus simple de fournir un contexte explicite, c’est d’utiliser le symbole @. C’est idéal quand tu sais précisément quel fichier, dossier, site web ou autre élément de contexte tu veux inclure. Plus tu es précis, mieux c’est. Voici comment affiner le contexte de manière plus ciblée :

| Symbole   | Exemple              | Cas d’usage                                                                             | Inconvénient                                                                             |
| --------- | -------------------- | --------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `@code`   | `@LRUCachedFunction` | Tu sais quelle fonction, constante ou quel symbole est pertinent pour la sortie générée | Nécessite une bonne connaissance de la base de code                                      |
| `@file`   | `cache.ts`           | Tu sais quel fichier doit être lu ou modifié, mais pas exactement où dans le fichier    | Peut inclure beaucoup de contexte non pertinent pour la tâche selon la taille du fichier |
| `@folder` | `utils/`             | Tous ou la majorité des fichiers d’un dossier sont pertinents                           | Peut inclure beaucoup de contexte non pertinent pour la tâche                            |

<img src="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/working-with-context/context-menu.png?fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=dd9cf0c3dc55465132421c7f4c63321a" alt="Context Menu" data-og-width="1956" width="1956" data-og-height="1266" height="1266" data-path="images/guides/working-with-context/context-menu.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/working-with-context/context-menu.png?w=280&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=bc3b241ff39cf6afd967f86dd8543dc6 280w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/working-with-context/context-menu.png?w=560&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=943522dab894b52ae922d0ba8d370f8e 560w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/working-with-context/context-menu.png?w=840&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=2fc3123a4388b5eab2b288e5c68301da 840w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/working-with-context/context-menu.png?w=1100&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=7ae7698ac325cab31376964994f7cecb 1100w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/working-with-context/context-menu.png?w=1650&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=04f2e442f95b59f2f11191b2f6f9222c 1650w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/working-with-context/context-menu.png?w=2500&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=d24a426d894174534501c6d0ddbbc5ba 2500w" />

<div id="rules">
  ## Règles
</div>

Pense aux règles comme à une mémoire à long terme à laquelle toi ou les autres membres de ton équipe pouvez accéder. Capturer le contexte spécifique à ton domaine — workflows, formatage et autres conventions — est un excellent point de départ pour rédiger des règles.

Tu peux aussi générer des règles à partir de conversations existantes avec `/Generate Cursor Rules`. Si tu as eu une longue conversation en aller-retour avec beaucoup de prompts, il y a probablement des directives utiles ou des règles générales que tu voudras réutiliser plus tard.

<img src="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/working-with-context/rules.png?fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=7100fd32cff4f24b90910642cd96a31a" alt="Règles" data-og-width="2048" width="2048" data-og-height="1326" height="1326" data-path="images/guides/working-with-context/rules.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/working-with-context/rules.png?w=280&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=181822aa329fa5f575f502f91485411f 280w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/working-with-context/rules.png?w=560&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=e21ae2ff2794ad9a697cd87345670a9d 560w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/working-with-context/rules.png?w=840&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=c5a67c106c0846abb8c970feac85a463 840w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/working-with-context/rules.png?w=1100&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=84b6bcbea6d0950c2edf177a34e5398b 1100w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/working-with-context/rules.png?w=1650&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=682fca965fbaeac3e24b1aeadc22e5d1 1650w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/working-with-context/rules.png?w=2500&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=eb35dfa5784add7c1325429e797ed80f 2500w" />

<div id="mcp">
  ## MCP
</div>

Le [Model Context Protocol](https://modelcontextprotocol.io/introduction) est une couche d’extensibilité qui permet à Cursor d’exécuter des actions et d’ingérer du contexte externe.

Selon ta config de développement, tu peux t’appuyer sur différents types de serveurs, mais deux catégories qu’on trouve particulièrement utiles sont :

* **Documentation interne** : p. ex. Notion, Confluence, Google Docs
* **Gestion de projet** : p. ex. Linear, Jira

Si tu as déjà des outils pour accéder au contexte et exécuter des actions via une API, tu peux créer un serveur MCP pour ça. Voici un court guide pour construire des [serveurs MCP](https://modelcontextprotocol.io/tutorials/building-mcp-with-llms).

<img src="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/working-with-context/mcp.png?fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=220979c9c6d2d2df274f4e6569f36a65" alt="MCP" data-og-width="2048" width="2048" data-og-height="1326" height="1326" data-path="images/guides/working-with-context/mcp.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/working-with-context/mcp.png?w=280&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=109502940ebd0566ba4aae7973f4ee55 280w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/working-with-context/mcp.png?w=560&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=02b169068621a0260c13aaaebc85988f 560w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/working-with-context/mcp.png?w=840&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=5b78292cbc00f791ec4431130c289e2e 840w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/working-with-context/mcp.png?w=1100&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=2bb9323e56965bdfff44949847dae0ea 1100w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/working-with-context/mcp.png?w=1650&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=f0dc65099b6478a735e451cacdc3f2c3 1650w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/working-with-context/mcp.png?w=2500&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=b7865a098b75bccb25bb93d90e7232ac 2500w" />

<div id="self-gathering-context">
  ## Auto-collecte de contexte
</div>

Un modèle d’utilisation puissant que beaucoup d’utilisateurs adoptent consiste à laisser l’Agent écrire de petits outils temporaires qu’il peut ensuite exécuter pour rassembler plus de contexte. C’est particulièrement efficace dans des workflows avec humain dans la boucle, où tu passes en revue le code avant son exécution.

Par exemple, ajouter des instructions de débogage à ton code, l’exécuter, puis laisser le modèle inspecter la sortie lui donne accès à un contexte dynamique qu’il ne pourrait pas déduire de manière statique.

En Python, tu peux faire ça en demandant à l’Agent de :

1. Ajouter des print("debugging: ...") aux endroits pertinents du code
2. Exécuter le code ou les tests via le terminal

L’Agent lira la sortie du terminal et décidera de la suite. L’idée centrale est de donner à l’Agent accès au comportement réel à l’exécution, pas seulement au code statique.

<img src="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/working-with-context/self-gathering.png?fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=a90ba6d4d4f17148c95f3a4f0d6b382e" alt="Auto-collecte de contexte" data-og-width="2048" width="2048" data-og-height="1325" height="1325" data-path="images/guides/working-with-context/self-gathering.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/working-with-context/self-gathering.png?w=280&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=234f5240c4f4a74abeccd4d10d79df0b 280w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/working-with-context/self-gathering.png?w=560&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=dfa67903d8d44bbdcaa766533809fd21 560w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/working-with-context/self-gathering.png?w=840&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=ebe9b89eea9e2b942094e57105c79b94 840w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/working-with-context/self-gathering.png?w=1100&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=b4381b453dc4f852885f0229d189f131 1100w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/working-with-context/self-gathering.png?w=1650&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=c5981136bf7465465ac3cc0cc38c897e 1650w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/working-with-context/self-gathering.png?w=2500&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=132bc18e9994be819af3e24a22c7e814 2500w" />

<div id="takeaways">
  # Points clés
</div>

* Le contexte est la base d’un codage IA efficace. Il se compose de l’intention (ce que tu veux) et de l’état (ce qui existe). Fournir les deux aide Cursor à faire des prédictions précises.
* Utilise un contexte chirurgical avec les symboles @ (@code, @file, @folder) pour guider Cursor avec précision, plutôt que de te reposer uniquement sur la collecte automatique de contexte.
* Capture les connaissances récurrentes dans des règles pour les réutiliser à l’échelle de l’équipe, et étends les capacités de Cursor avec le Model Context Protocol pour connecter des systèmes externes.
* Un contexte insuffisant mène à des hallucinations ou à de l’inefficacité, tandis qu’un excès de contexte non pertinent dilue le signal. Trouve le bon équilibre pour des résultats optimaux.

---

← Previous: [Développement web](./dveloppement-web.md) | [Index](./index.md) | Next: [Modification en ligne](./modification-en-ligne.md) →