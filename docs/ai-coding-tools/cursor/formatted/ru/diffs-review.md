---
title: "Diffs & Review"
source: "https://docs.cursor.com/ru/agent/review"
language: "ru"
language_name: "Russian"
---

# Diffs & Review
Source: https://docs.cursor.com/ru/agent/review

Просматривай и управляй изменениями кода, сгенерированными AI-агентом

Когда Agent генерирует изменения в коде, они показываются в интерфейсе ревью с цветовой подсветкой строк добавлений и удалений. Это позволяет просмотреть и выбрать, какие изменения применить к твоей кодовой базе.

Интерфейс ревью отображает изменения кода в знакомом формате diff:

<div id="diffs">
  ## Диффы
</div>

<div className="full-width-table">
  | Тип               | Значение                      | Пример                                                                                                |
  | :---------------- | :---------------------------- | :---------------------------------------------------------------------------------------------------- |
  | **Added lines**   | Добавленные строки кода       | <code className="bg-green-100 text-green-800 px-2 py-1 rounded">+ const newVariable = 'hello';</code> |
  | **Deleted lines** | Удалённые строки кода         | <code className="bg-red-100 text-red-800 px-2 py-1 rounded">- const oldVariable = 'goodbye';</code>   |
  | **Context lines** | Непревращённый окружающий код | <code className="bg-gray-100 text-gray-600 px-2 py-1 rounded"> function example() {}</code>           |
</div>

<div id="review">
  ## Review
</div>

После завершения генерации появится предложение просмотреть все изменения перед продолжением. Это даст тебе общий обзор того, что будет изменено.

<Frame>
  <img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/review/input-review.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=10633167c76c24c1e69748ef93dc3888" alt="Интерфейс просмотра ввода" data-og-width="2095" width="2095" data-og-height="1178" height="1178" data-path="images/chat/review/input-review.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/review/input-review.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=f462337898ca48f71cd2b570b140d30d 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/review/input-review.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=07c91dfc92110cce444da8bbf3d0b3b5 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/review/input-review.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=492522862dabae6243fa8d33f6fd77f2 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/review/input-review.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=c897e19ce7f508bad4e24fcf8efb2512 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/review/input-review.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=3956c2d2c5c9156181b19e262e301b5b 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/review/input-review.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=907f90b1db432128964a7f4e59523bb6 2500w" />
</Frame>

<div id="file-by-file">
  ### По файлам
</div>

Внизу экрана появится плавающая панель обзора, позволяющая:

* **Принять** или **отклонить** изменения для текущего файла
* Перейти к **следующему файлу** с ожидающими изменениями
  <Frame>
    <video src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/review/review-bar.mp4?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=5dca0fe7aba3c79e6760cb264821a617" autoPlay loop muted playsInline controls data-path="images/chat/review/review-bar.mp4">
      Твой браузер не поддерживает тег video.
    </video>
  </Frame>

<div id="selective-acceptance">
  ### Выборочное принятие
</div>

Для более точного контроля:

* Чтобы принять большинство изменений: отклони ненужные строки, затем нажми **Accept all**
* Чтобы отклонить большинство изменений: прими нужные строки, затем нажми **Reject all**

<div id="review-changes">
  ## Просмотр изменений
</div>

В конце ответа агента нажми кнопку **Review changes**, чтобы увидеть полный дифф изменений.

<Frame>
  <video src="https://www.cursor.com/changelog/049/review-ui.mp4" autoPlay loop muted playsInline controls />
</Frame>

---

← Previous: [Планирование](./section.md) | [Index](./index.md) | Next: [Терминал](./section.md) →