---
title: "Diffs & Review"
source: "https://docs.cursor.com/fr/agent/review"
language: "fr"
language_name: "French"
---

# Diffs & Review
Source: https://docs.cursor.com/fr/agent/review

Examiner et gérer les modifications de code générées par l’agent IA

Quand Agent génère des modifications de code, elles s’affichent dans une interface de revue qui montre ajouts et suppressions avec des lignes colorées. Ça te permet d’examiner et de contrôler quelles modifications sont appliquées à ton codebase.

L’interface de revue affiche les modifications de code dans un format diff familier :

<div id="diffs">
  ## Diffs
</div>

<div className="full-width-table">
  | Type              | Signification             | Exemple                                                                                               |
  | :---------------- | :------------------------ | :---------------------------------------------------------------------------------------------------- |
  | **Added lines**   | Ajouts de code            | <code className="bg-green-100 text-green-800 px-2 py-1 rounded">+ const newVariable = 'hello';</code> |
  | **Deleted lines** | Suppressions de code      | <code className="bg-red-100 text-red-800 px-2 py-1 rounded">- const oldVariable = 'goodbye';</code>   |
  | **Context lines** | Code de contexte inchangé | <code className="bg-gray-100 text-gray-600 px-2 py-1 rounded"> function example() {}</code>           |
</div>

<div id="review">
  ## Revue
</div>

Une fois la génération terminée, tu verras une invite pour passer en revue tous les changements avant de continuer. Ça te donne un aperçu de ce qui va être modifié.

<Frame>
  <img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/review/input-review.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=10633167c76c24c1e69748ef93dc3888" alt="Interface de revue de l'entrée" data-og-width="2095" width="2095" data-og-height="1178" height="1178" data-path="images/chat/review/input-review.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/review/input-review.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=f462337898ca48f71cd2b570b140d30d 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/review/input-review.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=07c91dfc92110cce444da8bbf3d0b3b5 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/review/input-review.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=492522862dabae6243fa8d33f6fd77f2 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/review/input-review.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=c897e19ce7f508bad4e24fcf8efb2512 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/review/input-review.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=3956c2d2c5c9156181b19e262e301b5b 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/review/input-review.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=907f90b1db432128964a7f4e59523bb6 2500w" />
</Frame>

<div id="file-by-file">
  ### Fichier par fichier
</div>

Une barre de revue flottante apparaît en bas de ton écran, te permettant de :

* **Accepter** ou **rejeter** les changements pour le fichier en cours
* Passer au **fichier suivant** avec des changements en attente
  <Frame>
    <video src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/review/review-bar.mp4?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=5dca0fe7aba3c79e6760cb264821a617" autoPlay loop muted playsInline controls data-path="images/chat/review/review-bar.mp4">
      Your browser does not support the video tag.
    </video>
  </Frame>

<div id="selective-acceptance">
  ### Acceptation sélective
</div>

Pour un contrôle fin :

* Pour accepter la plupart des changements : rejette les lignes indésirables, puis clique sur **Tout accepter**
* Pour rejeter la plupart des changements : accepte les lignes souhaitées, puis clique sur **Tout rejeter**

<div id="review-changes">
  ## Passer en revue les modifications
</div>

À la fin de la réponse de l’agent, clique sur le bouton **Review changes** pour afficher le diff complet des modifications.

<Frame>
  <video src="https://www.cursor.com/changelog/049/review-ui.mp4" autoPlay loop muted playsInline controls />
</Frame>

---

← Previous: [Planification](./planification.md) | [Index](./index.md) | Next: [Terminal](./terminal.md) →