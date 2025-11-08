---
title: "Java"
source: "https://docs.cursor.com/fr/guides/languages/java"
language: "fr"
language_name: "French"
---

# Java
Source: https://docs.cursor.com/fr/guides/languages/java

Configurer le développement Java avec le JDK, des extensions et des outils de build

Ce guide t’aide à configurer Cursor pour le développement Java : installer et configurer le JDK, ajouter les extensions nécessaires, déboguer, exécuter des applications Java, et intégrer des outils de build comme Maven et Gradle. Il couvre aussi des fonctionnalités de workflow similaires à IntelliJ ou VS Code.

<Note>
  Avant de commencer, assure-toi d’avoir installé Cursor et de l’avoir mis à jour
  vers la dernière version.
</Note>

<div id="setting-up-java-for-cursor">
  ## Configuration de Java pour Cursor
</div>

<div id="java-installation">
  ### Installation de Java
</div>

Avant de configurer Cursor, tu dois avoir Java installé sur ta machine.

<Warning>
  Cursor n’embarque pas de compilateur Java, donc tu dois installer un JDK si tu
  ne l’as pas déjà fait.
</Warning>

<CardGroup cols={1}>
  <Card title="Installation sur Windows" icon="windows">
    Télécharge et installe un JDK (p. ex. OpenJDK, Oracle JDK, Microsoft Build of
    OpenJDK).

    <br />

    Configure JAVA\_HOME et ajoute JAVA\_HOME\bin à ton PATH.
  </Card>

  <Card title="Installation sur macOS" icon="apple">
    Installe via Homebrew (`brew install openjdk`) ou télécharge un programme d’installation.

    <br />

    Assure-toi que JAVA\_HOME pointe vers le JDK installé.
  </Card>

  <Card title="Installation sur Linux" icon="linux">
    Utilise ton gestionnaire de paquets (`sudo apt install openjdk-17-jdk` ou équivalent)
    ou installe via SDKMAN.
  </Card>
</CardGroup>

Pour vérifier l’installation, exécute :

```bash  theme={null}
java -version
javac -version
```

<Info>
  Si Cursor ne détecte pas ton JDK, configure-le manuellement dans settings.json :
</Info>

```json  theme={null}
{
  "java.jdt.ls.java.home": "/chemin/vers/jdk",
  "java.configuration.runtimes": [
    {
      "name": "JavaSE-17",
      "path": "/chemin/vers/jdk-17",
      "default": true
    }
  ]
}
```

<Warning>Redémarre Cursor pour appliquer les changements.</Warning>

<div id="cursor-setup">
  ### Configuration de Cursor
</div>

<Info>Cursor est compatible avec les extensions VS Code. Installe celles-ci manuellement :</Info>

<CardGroup cols={2}>
  <Card title="Extension Pack for Java" icon="java" href="cursor:extension/vscjava.vscode-java-pack">
    Inclut la prise en charge du langage Java, le débogueur, l’exécution de tests, la prise en charge de Maven et
    le gestionnaire de projets
  </Card>

  <Card title="Gradle for Java" icon="gears" href="cursor:extension/vscjava.vscode-gradle">
    Indispensable pour travailler avec le système de build Gradle
  </Card>

  <Card title="Spring Boot Extension Pack" icon="leaf" href="cursor:extension/vmware.vscode-boot-dev-pack">
    Requis pour le développement Spring Boot
  </Card>

  <Card title="Kotlin" icon="window" href="cursor:extension/fwcd.kotlin">
    Nécessaire pour développer des applications Kotlin
  </Card>
</CardGroup>

<div id="configure-build-tools">
  ### Configurer les outils de build
</div>

<div id="maven">
  #### Maven
</div>

Assure-toi que Maven est installé (`mvn -version`). Installe-le depuis [maven.apache.org](https://maven.apache.org/download.cgi) si besoin :

1. Télécharge l’archive binaire
2. Extrais-la à l’emplacement souhaité
3. Définis la variable d’environnement MAVEN\_HOME sur le dossier extrait
4. Ajoute %MAVEN\_HOME%\bin (Windows) ou \$MAVEN\_HOME/bin (Unix) au PATH

<div id="gradle">
  #### Gradle
</div>

Assure-toi que Gradle est installé (`gradle -version`). Installe-le depuis [gradle.org](https://gradle.org/install/) si besoin :

1. Télécharge la distribution binaire
2. Extrais-la à l’emplacement souhaité
3. Définis la variable d’environnement GRADLE\_HOME sur le dossier extrait
4. Ajoute %GRADLE\_HOME%\bin (Windows) ou \$GRADLE\_HOME/bin (Unix) au PATH

Sinon, utilise le Gradle Wrapper, qui téléchargera et utilisera automatiquement la bonne version de Gradle :

<div id="running-and-debugging">
  ## Exécution et débogage
</div>

Maintenant que tout est en place, il est temps d’exécuter et de déboguer ton code Java.
Selon tes besoins, tu peux utiliser les méthodes suivantes :

<CardGroup cols={2}>
  <Card title="Run" icon="play">
    Clique sur le lien « Run » qui apparaît au-dessus de n’importe quelle méthode main pour exécuter rapidement
    ton programme
  </Card>

  <Card title="Debug" icon="bug">
    Ouvre le panneau latéral « Run and Debug » et utilise le bouton « Run » pour démarrer ton
    application
  </Card>
</CardGroup>

<CardGroup cols={1}>
  <Card title="Terminal" icon="terminal">
    Exécute depuis la ligne de commande avec des commandes Maven ou Gradle
  </Card>

  <Card title="Spring Boot" icon="leaf">
    Lance des applications Spring Boot directement depuis l’extension « Spring Boot Dashboard »
  </Card>
</CardGroup>

<div id="java-x-cursor-workflow">
  ## Java x Cursor : flux de travail
</div>

Les fonctionnalités IA de Cursor peuvent nettement booster ton flux de travail en Java. Voici quelques façons de tirer parti des capacités de Cursor spécifiquement pour Java :

<CardGroup cols={2}>
  <Card title="Tab Completion" icon="arrow-right">
    <div className="text-sm">
      Des complétions intelligentes pour les méthodes, les signatures et le
      boilerplate Java, comme les getters/setters.
    </div>
  </Card>

  <Card title="Agent Mode" icon="pen-to-square">
    <div className="text-sm">
      Implémente des patrons de conception, refactorise du code ou génère des classes
      avec une bonne hiérarchie d’héritage.
    </div>
  </Card>

  <Card title="Inline Edit" icon="code">
    <div className="text-sm">
      Fais des modifications rapides en ligne sur des méthodes, corrige des erreurs
      ou génère des tests unitaires sans casser ton flux.
    </div>
  </Card>

  <Card title="Chat" icon="message">
    <div className="text-sm">
      Obtiens de l’aide sur des concepts Java, débogue des exceptions ou
      comprends des fonctionnalités de frameworks.
    </div>
  </Card>
</CardGroup>

<div id="example-workflows">
  ### Exemples de flux de travail
</div>

1. **Générer du boilerplate Java**\
   Utilise la [tab completion](/fr/tab/overview) pour générer rapidement des constructeurs, des getters/setters, des méthodes equals/hashCode et d’autres motifs Java répétitifs.

2. **Déboguer des exceptions Java complexes**\
   Face à une stack trace Java cryptique, surligne-la et utilise [Ask](/fr/chat/overview) pour expliquer la cause racine et proposer des correctifs possibles.

3. **Refactoriser du code Java legacy**\
   Utilise le [mode Agent](/fr/chat/agent) pour moderniser du code Java ancien : convertis des classes anonymes en lambdas, migre vers des fonctionnalités plus récentes du langage Java ou implémente des patrons de conception.

4. **Développement avec des frameworks**\
   Ajoute ta doc au contexte de Cursor avec @docs et génère du code spécifique aux frameworks partout dans Cursor.

---

← Previous: [Travailler avec la documentation](./travailler-avec-la-documentation.md) | [Index](./index.md) | Next: [JavaScript & TypeScript](./javascript-typescript.md) →