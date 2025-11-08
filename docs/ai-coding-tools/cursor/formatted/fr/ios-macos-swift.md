---
title: "iOS & macOS (Swift)"
source: "https://docs.cursor.com/fr/guides/languages/swift"
language: "fr"
language_name: "French"
---

# iOS & macOS (Swift)
Source: https://docs.cursor.com/fr/guides/languages/swift

Intègre Cursor à Xcode pour le développement Swift

Bienvenue dans le développement Swift avec Cursor ! Que tu crées des apps iOS, des applications macOS ou des projets Swift côté serveur, on a ce qu’il te faut. Ce guide t’aidera à configurer ton environnement Swift dans Cursor, en commençant par les bases avant de passer à des fonctionnalités plus avancées.

<div id="basic-workflow">
  ## Flux de travail de base
</div>

La façon la plus simple d'utiliser Cursor avec Swift, c'est d'en faire ton éditeur de code principal tout en t'appuyant sur Xcode pour la compilation et l'exécution de tes apps. Tu profiteras de fonctionnalités au top comme :

* Complétion de code intelligente
* Assistance de codage par IA (essaie [CMD+K](/fr/inline-edit/overview) sur n'importe quelle ligne)
* Accès rapide à la doc avec [@Docs](/fr/context/@-symbols/@-docs)
* Coloration syntaxique
* Navigation de code basique

Quand tu dois builder ou lancer ton app, bascule simplement sur Xcode. Ce flux de travail est parfait si tu veux tirer parti des capacités d'IA de Cursor tout en gardant tes outils Xcode habituels pour le débogage et le déploiement.

<div id="hot-reloading">
  ### Hot Reloading
</div>

Quand tu utilises des workspaces ou des projets Xcode (au lieu d'ouvrir directement un dossier dans Xcode), Xcode peut souvent ignorer les modifications apportées à tes fichiers depuis Cursor, ou plus généralement en dehors de Xcode.

Même si ouvrir le dossier dans Xcode peut régler ça, tu peux avoir besoin d'utiliser un projet pour ton flux de travail Swift.

Une super solution, c'est d'utiliser [Inject](https://github.com/krzysztofzablocki/Inject), une bibliothèque de hot reloading pour Swift qui permet à ton app de “hot reload” et de se mettre à jour en temps réel dès que tu fais des changements. Cette approche n'est pas sujette aux effets de bord liés aux workspaces/projets Xcode et te permet de modifier ton code dans Cursor et de voir les changements reflétés immédiatement dans ton app.

<CardGroup cols={1}>
  <Card title="Inject - Hot Reloading pour Swift" horizontal icon="fire" href="https://github.com/krzysztofzablocki/Inject">
    En savoir plus sur Inject et comment l'utiliser dans tes projets Swift.
  </Card>
</CardGroup>

<div id="advanced-swift-development">
  ## Développement Swift avancé
</div>

<Note>
  Cette section du guide s’inspire largement de [Thomas
  Ricouard](https://x.com/Dimillian) et de son
  [article](https://dimillian.medium.com/how-to-use-cursor-for-ios-development-54b912c23941)
  sur l’utilisation de Cursor pour le développement iOS. Va lire son article pour plus
  de détails et abonne-toi pour plus de contenu Swift.
</Note>

Si tu veux n’avoir qu’un seul éditeur ouvert à la fois et éviter d’alterner entre Xcode et Cursor, tu peux utiliser une extension comme [Sweetpad](https://sweetpad.hyzyla.dev/) pour intégrer Cursor directement au système de build sous-jacent de Xcode.

Sweetpad est une extension puissante qui te permet de compiler, lancer et déboguer tes projets Swift directement dans Cursor, sans rien sacrifier des fonctionnalités de Xcode.

Pour démarrer avec Sweetpad, tu auras quand même besoin d’avoir Xcode installé sur ton Mac — c’est la base du développement Swift. Tu peux télécharger Xcode depuis le [Mac App Store](https://apps.apple.com/us/app/xcode/id497799835). Une fois Xcode configuré, on va améliorer ton expérience de dev dans Cursor avec quelques outils essentiels.

Ouvre ton terminal et exécute :

```bash  theme={null}

---

← Previous: [Python](./python.md) | [Index](./index.md) | Next: [JetBrains](./jetbrains.md) →