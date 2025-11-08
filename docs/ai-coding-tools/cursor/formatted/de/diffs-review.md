---
title: "Diffs & Review"
source: "https://docs.cursor.com/de/agent/review"
language: "de"
language_name: "German"
---

# Diffs & Review
Source: https://docs.cursor.com/de/agent/review

Vom Agent generierte Codeänderungen überprüfen und verwalten

Wenn der Agent Codeänderungen erzeugt, werden sie in einer Review-Oberfläche angezeigt, die Hinzufügungen und Löschungen mit farbcodierten Zeilen darstellt. So kannst du prüfen und steuern, welche Änderungen in deiner Codebasis übernommen werden.

Die Review-Oberfläche zeigt Codeänderungen in einem vertrauten Diff-Format an:

<div id="diffs">
  ## Diffs
</div>

<div className="full-width-table">
  | Typ                     | Bedeutung                     | Beispiel                                                                                              |
  | :---------------------- | :---------------------------- | :---------------------------------------------------------------------------------------------------- |
  | **Hinzugefügte Zeilen** | Neue Codezeilen               | <code className="bg-green-100 text-green-800 px-2 py-1 rounded">+ const newVariable = 'hello';</code> |
  | **Gelöschte Zeilen**    | Entfernte Codezeilen          | <code className="bg-red-100 text-red-800 px-2 py-1 rounded">- const oldVariable = 'goodbye';</code>   |
  | **Kontextzeilen**       | Unveränderter umgebender Code | <code className="bg-gray-100 text-gray-600 px-2 py-1 rounded"> function example() {}</code>           |
</div>

<div id="review">
  ## Review
</div>

Nachdem die Generierung abgeschlossen ist, siehst du eine Aufforderung, alle Änderungen zu überprüfen, bevor es weitergeht. So bekommst du einen Überblick darüber, was geändert wird.

<Frame>
  <img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/review/input-review.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=10633167c76c24c1e69748ef93dc3888" alt="Review-Eingabeoberfläche" data-og-width="2095" width="2095" data-og-height="1178" height="1178" data-path="images/chat/review/input-review.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/review/input-review.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=f462337898ca48f71cd2b570b140d30d 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/review/input-review.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=07c91dfc92110cce444da8bbf3d0b3b5 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/review/input-review.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=492522862dabae6243fa8d33f6fd77f2 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/review/input-review.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=c897e19ce7f508bad4e24fcf8efb2512 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/review/input-review.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=3956c2d2c5c9156181b19e262e301b5b 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/review/input-review.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=907f90b1db432128964a7f4e59523bb6 2500w" />
</Frame>

<div id="file-by-file">
  ### Datei für Datei
</div>

Unten auf deinem Bildschirm erscheint eine schwebende Review-Leiste, mit der du:

* Änderungen für die aktuelle Datei **annehmen** oder **ablehnen** kannst
* Zur **nächsten Datei** mit ausstehenden Änderungen springen kannst
  <Frame>
    <video src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/review/review-bar.mp4?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=5dca0fe7aba3c79e6760cb264821a617" autoPlay loop muted playsInline controls data-path="images/chat/review/review-bar.mp4">
      Dein Browser unterstützt das video-Tag nicht.
    </video>
  </Frame>

<div id="selective-acceptance">
  ### Selektive Annahme
</div>

Für fein abgestimmte Kontrolle:

* Um die meisten Änderungen anzunehmen: unerwünschte Zeilen ablehnen, dann auf **Alle annehmen** klicken
* Um die meisten Änderungen abzulehnen: gewünschte Zeilen annehmen, dann auf **Alle ablehnen** klicken

<div id="review-changes">
  ## Änderungen überprüfen
</div>

Klick am Ende der Agent-Antwort auf **Änderungen überprüfen**, um das vollständige Diff der Änderungen zu sehen.

<Frame>
  <video src="https://www.cursor.com/changelog/049/review-ui.mp4" autoPlay loop muted playsInline controls />
</Frame>

---

← Previous: [Planung](./planung.md) | [Index](./index.md) | Next: [Terminal](./terminal.md) →