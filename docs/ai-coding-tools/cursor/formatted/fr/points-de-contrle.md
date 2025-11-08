---
title: "Points de contrôle"
source: "https://docs.cursor.com/fr/agent/chat/checkpoints"
language: "fr"
language_name: "French"
---

# Points de contrôle
Source: https://docs.cursor.com/fr/agent/chat/checkpoints

Enregistrer et restaurer des états antérieurs après des changements de l’Agent

Les points de contrôle sont des instantanés automatiques des changements de l’Agent dans ta base de code. Ils te permettent d’annuler les modifications de l’Agent si besoin.

<Frame>
  <video src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/restore-checkpoint.mp4?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=7cededf7892f15a6342a81953ea0aa38" autoPlay loop muted playsInline controls data-path="images/chat/restore-checkpoint.mp4" />
</Frame>

<div id="restoring-checkpoints">
  ## Restauration des checkpoints
</div>

Deux façons de restaurer :

1. **Depuis la zone de saisie** : clique sur le bouton `Restore Checkpoint` sur les requêtes précédentes
2. **Depuis un message** : clique sur le bouton + en survolant un message

<Warning>
  Les checkpoints ne remplacent pas le contrôle de version. Utilise Git pour conserver un historique permanent.
</Warning>

<div id="how-they-work">
  ## Comment ça fonctionne
</div>

* Stockés localement, séparément de Git
* Ne suivent que les changements de l’Agent (pas les modifications manuelles)
* Nettoyés automatiquement

<Note>
  Les modifications manuelles ne sont pas suivies. Utilise les checkpoints uniquement pour les changements de l’Agent.
</Note>

<div id="faq">
  ## FAQ
</div>

<AccordionGroup>
  <Accordion title="Les checkpoints affectent-ils Git ?">
    Non. Ils sont distincts de l’historique Git.
  </Accordion>

  {" "}

  <Accordion title="Combien de temps sont-ils conservés ?">
    Pendant la session en cours et l’historique récent. Nettoyage automatique.
  </Accordion>

  <Accordion title="Puis-je les créer manuellement ?">
    Non. Cursor les crée automatiquement.
  </Accordion>
</AccordionGroup>

{" "}

---

← Previous: [Apply](./apply.md) | [Index](./index.md) | Next: [Commandes](./commandes.md) →