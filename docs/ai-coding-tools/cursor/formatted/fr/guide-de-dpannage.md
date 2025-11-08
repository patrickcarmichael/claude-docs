---
title: "Guide de dépannage"
source: "https://docs.cursor.com/fr/troubleshooting/troubleshooting-guide"
language: "fr"
language_name: "French"
---

# Guide de dépannage
Source: https://docs.cursor.com/fr/troubleshooting/troubleshooting-guide

Étapes pour résoudre les problèmes et signaler des bugs

Les problèmes de Cursor peuvent venir des extensions, des données de l’app ou du système. Essaie ces étapes de dépannage.

<CardGroup cols={1}>
  <Card horizontal title="Signaler un problème" icon="bug" href="#reporting-an-issue">
    Étapes pour signaler un problème à l’équipe Cursor
  </Card>
</CardGroup>

<div id="troubleshooting">
  ## Dépannage
</div>

<Steps>
  <Step title="Vérifier la connectivité réseau">
    Commence par vérifier si Cursor peut se connecter à ses services.

    **Lance un diagnostic réseau :** Va dans `Cursor Settings` > `Network` et clique sur `Run Diagnostics`. Ça teste ta connexion aux serveurs de Cursor et identifie les problèmes réseau qui affectent les fonctionnalités d’IA, les mises à jour ou d’autres fonctions en ligne.

    Si les diagnostics révèlent des problèmes de connectivité, vérifie les paramètres du pare-feu, la configuration du proxy ou les restrictions réseau qui bloquent l’accès de Cursor.
  </Step>

  <Step title="Effacer les données des extensions">
    Pour les problèmes liés aux extensions :

    **Désactive temporairement toutes les extensions :** Exécute `cursor --disable-extensions` depuis la ligne de commande. Si les problèmes disparaissent, réactive les extensions une par une pour identifier celle qui pose problème.

    **Réinitialiser les données des extensions :** Désinstalle et réinstalle les extensions problématiques pour réinitialiser leurs données stockées. Vérifie les réglages de l’extension qui peuvent persister après réinstallation.
  </Step>

  <Step title="Effacer les données de l’application">
    <Warning>
      Ça supprime les données de ton application, y compris les extensions, thèmes, snippets et les données liées à l’installation. Exporte d’abord ton profil pour conserver ces données.
    </Warning>

    Cursor stocke les données de l’application en dehors de l’app pour permettre la restauration entre les mises à jour et les réinstallations.

    Pour effacer les données de l’app :

    **Windows :** Exécute ces commandes dans l’Invite de commandes :

    ```txt  theme={null}
    rd /s /q "%USERPROFILE%\AppData\Local\Programs\Cursor"
    rd /s /q "%USERPROFILE%\AppData\Local\Cursor"
    rd /s /q "%USERPROFILE%\AppData\Roaming\Cursor"
    del /f /q "%USERPROFILE%\.cursor*"
    rd /s /q "%USERPROFILE%\.cursor"
    ```

    **macOS :** Exécute `sudo rm -rf ~/Library/Application\ Support/Cursor` et `rm -f ~/.cursor.json` dans le Terminal.

    **Linux :** Exécute `rm -rf ~/.cursor ~/.config/Cursor/` dans le Terminal.
  </Step>

  <Step title="Désinstaller Cursor">
    Pour désinstaller Cursor :

    <CardGroup cols={1}>
      <Card horizontal title="Windows" icon="windows">
        Recherche « Add or Remove Programs » dans le menu Démarrer, trouve « Cursor », clique sur « Uninstall ».
      </Card>

      <Card horizontal title="macOS" icon="apple">
        Ouvre le dossier Applications, clique droit sur « Cursor », sélectionne « Move to Trash ».
      </Card>

      <Card horizontal title="Linux" icon="linux">
        **Pour les paquets .deb :** `sudo apt remove cursor`

        **Pour les paquets .rpm :** `sudo dnf remove cursor` ou `sudo yum remove cursor`

        **Pour AppImage :** Supprime le fichier Cursor.appimage à son emplacement.
      </Card>
    </CardGroup>
  </Step>

  <Step title="Réinstaller Cursor">
    Réinstalle depuis la [page de téléchargement](https://www.cursor.com/downloads). Sans effacer les données de l’app, Cursor est restauré à son état précédent. Sinon, tu obtiens une installation neuve.
  </Step>
</Steps>

<div id="reporting-an-issue">
  ## Signaler un problème
</div>

Si ces étapes ne suffisent pas, signale-le sur le [forum](https://forum.cursor.com/).

<Card horizontal title="Forum Cursor" icon="message" href="https://forum.cursor.com/">
  Signale un bug ou un problème sur le forum Cursor
</Card>

Pour une résolution rapide, fournis :

<CardGroup cols={2}>
  <Card title="Capture d’écran du problème" icon="image">
    Prends une capture d’écran et masque les informations sensibles.
  </Card>

  <Card title="Étapes de reproduction" icon="list-check">
    Documente précisément les étapes pour reproduire le problème.
  </Card>

  <Card title="Informations système" icon="computer">
    Récupère les infos système depuis :

    <br />

    `Cursor` > `Help` > `About`
  </Card>

  <Card title="ID de requête" icon="shield-halved" href="/fr/troubleshooting/request-reporting">
    Clique pour voir notre guide sur la collecte des ID de requête
  </Card>

  <Card title="Erreurs de console" icon="bug">
    Vérifie la console de développement : <br />
    `Developer: Toggle Developer Tools`
  </Card>

  <Card title="Journaux" icon="file-lines">
    Accède aux logs : <br />
    `Developer: Open Logs Folder`
  </Card>
</CardGroup>

---

← Previous: [Récupérer un ID de requête](./rcuprer-un-id-de-requte.md) | [Index](./index.md) | Next: [Bienvenue](./bienvenue.md) →