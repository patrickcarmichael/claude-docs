---
title: "Python"
source: "https://docs.cursor.com/fr/guides/languages/python"
language: "fr"
language_name: "French"
---

# Python
Source: https://docs.cursor.com/fr/guides/languages/python

Configurer un environnement Python avec des extensions et des outils de linting

<Note>
  Ce guide s’inspire largement de [Jack Fields](https://x.com/OrdinaryInds)
  et de son
  [article](https://medium.com/ordinaryindustries/the-ultimate-vs-code-setup-for-python-538026b34d94)
  sur la configuration de VS Code pour le développement Python. Va lire son article pour
  plus de détails.
</Note>

<div id="prerequisites">
  ## Prérequis
</div>

Avant de commencer, assure-toi d’avoir :

* [Python](https://python.org) installé (3.8 ou version ultérieure recommandée)
* [Git](https://git-scm.com/) pour le contrôle de version
* Cursor installé et à jour avec la dernière version

<div id="essential-extensions">
  ## Extensions essentielles
</div>

Les extensions suivantes configurent Cursor pour offrir un environnement Python complet. Elles te fournissent la coloration syntaxique, le linting, le débogage et les tests unitaires.

<CardGroup cols={2}>
  <Card title="Python" icon="python" href="cursor:extension/ms-python.python">
    Prise en charge principale du langage par Microsoft
  </Card>

  <Card title="Cursor Pyright" icon="bolt" href="cursor:extension/anysphere.cursorpyright">
    Serveur de langage Python ultra-rapide
  </Card>

  <Card title="Python Debugger" icon="bug" href="cursor:extension/ms-python.debugpy">
    Capacités de débogage avancées
  </Card>

  <Card title="Ruff" icon="wand-magic-sparkles" href="cursor:extension/charliermarsh.ruff">
    Linter et formateur pour Python
  </Card>
</CardGroup>

<div id="advanced-python-tooling">
  ### Outils Python avancés
</div>

Même si les extensions ci-dessus ont longtemps été les plus populaires pour le développement Python dans Cursor, on a aussi ajouté d’autres extensions pour t’aider à tirer le maximum de ton workflow Python.

<div id="uv-python-environment-manager">
  #### `uv` - Gestionnaire d’environnements Python
</div>

[uv](https://github.com/astral-sh/uv) est un gestionnaire de paquets Python moderne qui permet de créer et gérer des environnements virtuels, et peut remplacer pip comme gestionnaire de paquets par défaut.

Pour installer uv, exécute la commande suivante dans ton terminal :

```bash  theme={null}
pip install uv
```

<div id="ruff-python-linter-and-formatter">
  #### `ruff` - Linter et formateur Python
</div>

[Ruff](https://docs.astral.sh/ruff/) est un linter et formateur Python moderne qui permet de détecter des erreurs de programmation, d’appliquer les conventions de code et de suggérer des refactorings. Il peut être utilisé avec Black pour le formatage du code.

Pour installer Ruff, exécute la commande suivante dans ton terminal :

```bash  theme={null}
pip install ruff
```

<div id="cursor-configuration">
  ## Configuration de Cursor
</div>

<div id="1-python-interpreter">
  ### 1. Interpréteur Python
</div>

Configure ton interpréteur Python dans Cursor :

1. Ouvre la palette de commandes (Cmd/Ctrl + Shift + P)
2. Cherche « Python: Select Interpreter »
3. Choisis ton interpréteur Python (ou ton environnement virtuel si tu en utilises un)

<div id="2-code-formatting">
  ### 2. Formatage du code
</div>

Mets en place le formatage automatique du code avec Black :

<Note>
  Black est un formateur qui aligne automatiquement ton code sur un
  style cohérent. Il ne nécessite aucune configuration et est largement adopté par la
  communauté Python.
</Note>

Pour installer Black, exécute la commande suivante dans ton terminal :

```bash  theme={null}
pip install black
```

Ensuite, configure Cursor pour utiliser Black pour le formatage du code en ajoutant ce qui suit à ton fichier `settings.json` :

```json  theme={null}
{
  "python.formatting.provider": "black",
  "editor.formatOnSave": true,
  "python.formatting.blackArgs": ["--line-length", "88"]
}
```

<div id="3-linting">
  ### 3. Linting
</div>

On peut utiliser PyLint pour détecter les erreurs de programmation, faire respecter les conventions de code et suggérer des refactorisations.

Pour installer PyLint, exécute la commande suivante dans ton terminal :

```bash  theme={null}
pip install pylint
```

```json  theme={null}
{
  "python.linting.enabled": true,
  "python.linting.pylintEnabled": true,
  "python.linting.lintOnSave": true
}
```

<div id="4-type-checking">
  ### 4. Vérification des types
</div>

En plus du linting, on peut utiliser MyPy pour détecter les erreurs de type.

Pour installer MyPy, exécute la commande suivante dans ton terminal :

```bash  theme={null}
pip install mypy
```

```json  theme={null}
{
  "python.linting.mypyEnabled": true
}
```

<div id="debugging">
  ## Débogage
</div>

Cursor offre de puissantes fonctionnalités de débogage pour Python :

1. Place des points d’arrêt en cliquant dans la gouttière
2. Utilise le panneau Débogage (Cmd/Ctrl + Shift + D)
3. Configure `launch.json` pour des configurations de débogage personnalisées

<div id="recommended-features">
  ## Fonctionnalités recommandées
</div>

<CardGroup cols={3}>
  <Card title="Tab Completion" icon="wand-magic-sparkles" href="/fr/tab/overview">
    Des suggestions de code intelligentes qui comprennent ce que tu fais
  </Card>

  <Card title="Chat" icon="comments" href="/fr/chat/overview">
    Explore et comprends le code grâce à des conversations naturelles
  </Card>

  <Card title="Agent" icon="robot" href="/fr/chat/agent">
    Gère des tâches de développement complexes avec l’aide de l’IA
  </Card>

  <Card title="Context" icon="network-wired" href="/fr/context/model-context-protocol">
    Récupère du contexte depuis des systèmes tiers
  </Card>

  <Card title="Auto-Imports" icon="file-import" href="/fr/tab/auto-import">
    Importe automatiquement les modules pendant que tu codes
  </Card>

  <Card title="AI Review" icon="check-double" href="/fr/tab/overview#quality">
    Cursor passe ton code en revue en continu grâce à l’IA
  </Card>
</CardGroup>

<div id="framework-support">
  ## Prise en charge des frameworks
</div>

Cursor s’intègre parfaitement aux principaux frameworks Python :

* **Frameworks web** : Django, Flask, FastAPI
* **Data science** : Jupyter, NumPy, Pandas
* **Machine learning** : TensorFlow, PyTorch, scikit-learn
* **Tests** : pytest, unittest
* **API** : requests, aiohttp
* **Bases de données** : SQLAlchemy, psycopg2

---

← Previous: [JavaScript & TypeScript](./javascript-typescript.md) | [Index](./index.md) | Next: [iOS & macOS (Swift)](./ios-macos-swift.md) →