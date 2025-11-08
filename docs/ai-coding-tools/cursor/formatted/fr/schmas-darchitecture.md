---
title: "Schémas d’architecture"
source: "https://docs.cursor.com/fr/guides/tutorials/architectural-diagrams"
language: "fr"
language_name: "French"
---

# Schémas d’architecture
Source: https://docs.cursor.com/fr/guides/tutorials/architectural-diagrams

Apprends à générer des schémas d’architecture avec Mermaid pour visualiser la structure du système et les flux de données

Les schémas d’architecture t’aident à comprendre le fonctionnement de ton système. Tu peux t’en servir pour explorer la logique, suivre les données et communiquer la structure. Cursor permet de générer ces schémas directement avec des outils comme Mermaid, pour passer du code au visuel en seulement quelques prompts.

<Frame>
  <img alt="Exemple de schéma d’architecture" src="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/tutorials/architectural-diagrams/postgres-flowchart.png?fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=3d8dcd292e919c4640c03456a0959057" data-og-width="2048" width="2048" data-og-height="1326" height="1326" data-path="images/guides/tutorials/architectural-diagrams/postgres-flowchart.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/tutorials/architectural-diagrams/postgres-flowchart.png?w=280&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=b95ed20c23aff9fccf62cd209e817719 280w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/tutorials/architectural-diagrams/postgres-flowchart.png?w=560&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=bdb7d7390be1d8d71a1b560a4fc892ca 560w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/tutorials/architectural-diagrams/postgres-flowchart.png?w=840&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=b171506e9be3be4845966f61515c09de 840w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/tutorials/architectural-diagrams/postgres-flowchart.png?w=1100&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=aeaee70dede56db5b6c6dc92df7ba19e 1100w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/tutorials/architectural-diagrams/postgres-flowchart.png?w=1650&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=89513a2959f659f60f06c68891f89d45 1650w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/tutorials/architectural-diagrams/postgres-flowchart.png?w=2500&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=bdaf6ee66520c0e8b8b53b60f66f0b86 2500w" />
</Frame>

<div id="why-diagrams-matter">
  ## Pourquoi les diagrammes comptent
</div>

Les diagrammes clarifient comment les données circulent et comment les composants interagissent. Ils sont utiles quand tu :

* Veux comprendre le contrôle de flux dans ton codebase
* Dois retracer la lignée des données de l’entrée à la sortie
* Fais l’onboarding d’autres personnes ou documentes ton système

Ils sont aussi super pour déboguer et poser de meilleures questions. Les visuels t’aident (toi et le modèle) à voir l’ensemble.

<div id="two-dimensions-to-consider">
  ## Deux dimensions à prendre en compte
</div>

Il y a plusieurs angles à considérer :

* **Objectif** : Est-ce que tu représentes la logique, le flux de données, l’infrastructure, ou autre chose ?
* **Format** : Tu veux quelque chose de rapide (comme un diagramme Mermaid) ou de plus formel (comme UML) ?

<div id="how-to-prompt">
  ## Comment formuler une requête
</div>

Commence avec un objectif clair. Voici quelques façons courantes de demander :

* **Contrôle du flux** : « Montre-moi comment les requêtes passent du contrôleur à la base de données. »
* **Traçabilité des données** : « Retrace cette variable depuis son point d’entrée jusqu’à sa destination. »
* **Structure** : « Donne-moi une vue au niveau des composants de ce service. »

Tu peux inclure des points de départ et d’arrivée, ou demander à Cursor de retrouver le chemin complet.

<div id="working-with-mermaid">
  ## Travailler avec Mermaid
</div>

Mermaid est facile à apprendre et se rend directement dans Markdown (avec la bonne extension). Cursor peut générer des diagrammes comme :

* `flowchart` pour la logique et les séquences
* `sequenceDiagram` pour les interactions
* `classDiagram` pour la structure des objets
* `graph TD` pour des graphes directionnels simples

```mermaid  theme={null}
sequenceDiagram
    participant Utilisateur
    participant Serveur
    participant Base de données

    Utilisateur->>Serveur: Envoyer le formulaire
    Serveur->>Base de données: Enregistrer l’entrée
    Base de données-->>Serveur: Succès
    Serveur-->>Utilisateur: Confirmation

```

Tu peux installer l’[extension Mermaid](https://marketplace.cursorapi.com/items?itemName=bierner.markdown-mermaid) pour afficher un aperçu des diagrammes.

1. Va dans l’onglet Extensions
2. Cherche « Mermaid »
3. Clique sur Installer

<Frame>
  <img alt="Installation de l’extension Mermaid" src="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/tutorials/architectural-diagrams/installing-mermaid.png?fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=8d5ee8d972dcc3d3789696a6d383efe6" data-og-width="1365" width="1365" data-og-height="884" height="884" data-path="images/guides/tutorials/architectural-diagrams/installing-mermaid.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/tutorials/architectural-diagrams/installing-mermaid.png?w=280&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=bcb03e9519816da6bf4a8220fea8a319 280w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/tutorials/architectural-diagrams/installing-mermaid.png?w=560&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=52805242ed097f948b7da2b078c9ee02 560w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/tutorials/architectural-diagrams/installing-mermaid.png?w=840&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=5e2405e72459b4c099be1b3439b2bbd9 840w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/tutorials/architectural-diagrams/installing-mermaid.png?w=1100&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=296d1022a39afa4b2016425347901452 1100w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/tutorials/architectural-diagrams/installing-mermaid.png?w=1650&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=88bdac627e50291bb0550eb9313f8d1f 1650w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/tutorials/architectural-diagrams/installing-mermaid.png?w=2500&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=a9d3d7539bf41b023f1d53d68abc2dea 2500w" />
</Frame>

<div id="diagram-strategy">
  ## Stratégie de diagramme
</div>

Commence petit. N’essaie pas de tout modéliser d’un coup.

* Choisis une fonction, une route ou un processus
* Demande à Cursor de diagrammer cette partie avec Mermaid
* Une fois que t’en as quelques-uns, demande-lui de les combiner

Ça reprend le **modèle C4** — où tu pars d’un niveau bas (code ou composants) et tu montes vers des vues de plus haut niveau.

<div id="recommended-flow">
  ### Parcours recommandé
</div>

1. Commence par un diagramme détaillé de bas niveau
2. Résume-le en une vue de niveau intermédiaire
3. Répète jusqu’à atteindre le niveau d’abstraction que tu veux
4. Demande à Cursor de les fusionner en un seul diagramme ou une carte du système

```mermaid  theme={null}
graph TD
    subgraph Niveau 1 : Composants bas niveau
        A1[AuthService] --> A2[TokenValidator]
        A1 --> A3[UserDB]
        B1[PaymentService] --> B2[BillingEngine]
        B1 --> B3[InvoiceDB]
    end

    subgraph Niveau 2 : Systèmes de niveau intermédiaire
        A[Système utilisateur] --> A1
        B[Système de facturation] --> B1
    end

    subgraph Niveau 3 : Application de haut niveau
        App[Application principale] --> A
        App --> B
    end

```

<div id="takeaways">
  ## Points clés
</div>

* Utilise des diagrammes pour comprendre les flux, la logique et les données
* Commence avec de petits prompts et fais évoluer ton diagramme à partir de là
* Mermaid est le format le plus simple à utiliser dans Cursor
* Pars du bas niveau et abstrais vers le haut, comme dans le modèle C4
* Cursor peut t’aider à générer, affiner et combiner des diagrammes facilement

---

← Previous: [VS Code](./vs-code.md) | [Index](./index.md) | Next: [Créer un serveur MCP](./crer-un-serveur-mcp.md) →