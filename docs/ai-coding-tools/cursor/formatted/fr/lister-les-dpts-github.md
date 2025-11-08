---
title: "Lister les dépôts GitHub"
source: "https://docs.cursor.com/fr/background-agent/api/list-repositories"
language: "fr"
language_name: "French"
---

# Lister les dépôts GitHub
Source: https://docs.cursor.com/fr/background-agent/api/list-repositories

en/background-agent/api/openapi.yaml get /v0/repositories
Récupère la liste des dépôts GitHub accessibles à l'utilisateur authentifié.

<Warning>
  **Cet endpoint a des limites de taux très strictes.**

  Limite les requêtes à **1 / utilisateur / minute** et **30 / utilisateur / heure**.

  Cette requête peut prendre plusieurs dizaines de secondes pour les utilisateurs ayant accès à de nombreux dépôts.

  Assure-toi de gérer correctement le cas où cette information n'est pas disponible.
</Warning>

---

← Previous: [Liste des modèles](./liste-des-modles.md) | [Index](./index.md) | Next: [Aperçu](./aperu.md) →