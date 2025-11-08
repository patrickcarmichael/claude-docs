---
title: "Clés API"
source: "https://docs.cursor.com/fr/settings/api-keys"
language: "fr"
language_name: "French"
---

# Clés API
Source: https://docs.cursor.com/fr/settings/api-keys

Utilise ton propre fournisseur de LLM

Utilise tes propres clés API pour envoyer un nombre illimité de messages IA à tes frais. Une fois configuré, Cursor utilisera tes clés API pour appeler directement les fournisseurs de LLM.

Pour utiliser ta clé API, va dans `Cursor Settings` > `Models` et saisis tes clés API. Clique sur **Verify**. Une fois validée, ta clé API est activée.

<Warning>
  Les clés API personnalisées ne fonctionnent qu’avec les modèles de chat standard. Les fonctionnalités qui nécessitent des modèles spécialisés (comme Tab Completion) continueront d’utiliser les modèles intégrés de Cursor.
</Warning>

<div id="supported-providers">
  ## Fournisseurs pris en charge
</div>

* **OpenAI** - Uniquement des modèles de chat standard, sans raisonnement. Le sélecteur de modèles affichera les modèles OpenAI disponibles.
* **Anthropic** - Tous les modèles Claude disponibles via l’API Anthropic.
* **Google** - Modèles Gemini disponibles via l’API Google AI.
* **Azure OpenAI** - Modèles déployés dans ton instance Azure OpenAI Service.
* **AWS Bedrock** - Utilise des clés d’accès AWS, des clés secrètes ou des rôles IAM. Fonctionne avec les modèles disponibles dans ta configuration Bedrock.

Un ID externe unique est généré après validation de ton rôle IAM Bedrock, que tu peux ajouter à la stratégie d’approbation (trust policy) de ton rôle IAM pour renforcer la sécurité.

<div id="faq">
  ## FAQ
</div>

<AccordionGroup>
  <Accordion title="Est-ce que ma clé API sera stockée ou quittera mon appareil ?">
    Ta clé API n'est pas stockée, mais elle est envoyée à notre serveur à chaque requête. Toutes les requêtes passent par notre backend pour l'assemblage final du prompt.
  </Accordion>
</AccordionGroup>

---

← Previous: [Modèles](./modles.md) | [Index](./index.md) | Next: [Tab](./tab.md) →