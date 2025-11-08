---
title: "Руководство по устранению неполадок"
source: "https://docs.cursor.com/ru/troubleshooting/troubleshooting-guide"
language: "ru"
language_name: "Russian"
---

# Руководство по устранению неполадок
Source: https://docs.cursor.com/ru/troubleshooting/troubleshooting-guide

Шаги по исправлению проблем и отправке отчётов об ошибках

Проблемы в Cursor могут возникать из‑за расширений, данных приложения или системных сбоев. Попробуй эти шаги по устранению неполадок.

<CardGroup cols={1}>
  <Card horizontal title="Сообщить о проблеме" icon="bug" href="#reporting-an-issue">
    Шаги по отправке отчёта о проблеме команде Cursor
  </Card>
</CardGroup>

<div id="troubleshooting">
  ## Диагностика и устранение неполадок
</div>

<Steps>
  <Step title="Проверь сетевое подключение">
    Сначала проверь, может ли Cursor подключаться к своим сервисам.

    **Запусти сетевую диагностику:** Открой `Cursor Settings` > `Network` и нажми `Run Diagnostics`. Это протестирует подключение к серверам Cursor и выявит сетевые проблемы, влияющие на AI-функции, обновления или другие онлайн-возможности.

    Если диагностика покажет проблемы с подключением, проверь настройки брандмауэра, конфигурацию прокси или сетевые ограничения, которые блокируют доступ Cursor.
  </Step>

  <Step title="Очистка данных расширений">
    Если есть проблемы с расширениями:

    **Временно отключи все расширения:** Выполни `cursor --disable-extensions` в командной строке. Если проблема исчезла, включай расширения по одному, чтобы найти проблемное.

    **Сбрось данные расширения:** Удали и заново установи проблемные расширения, чтобы сбросить их сохранённые данные. Проверь настройки на параметры расширения, которые сохраняются после переустановки.
  </Step>

  <Step title="Очистка данных приложения">
    <Warning>
      Это удалит данные приложения, включая расширения, темы, сниппеты и данные, связанные с установкой. Сначала экспортируй свой профиль, чтобы сохранить эти данные.
    </Warning>

    Cursor хранит данные приложения вне самого приложения, чтобы их можно было восстановить между обновлениями и переустановками.

    Чтобы очистить данные приложения:

    **Windows:** Выполни эти команды в Командной строке:

    ```txt  theme={null}
    rd /s /q "%USERPROFILE%\AppData\Local\Programs\Cursor"
    rd /s /q "%USERPROFILE%\AppData\Local\Cursor"
    rd /s /q "%USERPROFILE%\AppData\Roaming\Cursor"
    del /f /q "%USERPROFILE%\.cursor*"
    rd /s /q "%USERPROFILE%\.cursor"
    ```

    **macOS:** Выполни `sudo rm -rf ~/Library/Application\ Support/Cursor` и `rm -f ~/.cursor.json` в Терминале.

    **Linux:** Выполни `rm -rf ~/.cursor ~/.config/Cursor/` в Терминале.
  </Step>

  <Step title="Удаление Cursor">
    Чтобы удалить Cursor:

    <CardGroup cols={1}>
      <Card horizontal title="Windows" icon="windows">
        Найди «Add or Remove Programs» в меню «Пуск», открой, найди «Cursor», нажми «Uninstall».
      </Card>

      <Card horizontal title="macOS" icon="apple">
        Открой папку Applications, кликни правой кнопкой по «Cursor», выбери «Move to Trash».
      </Card>

      <Card horizontal title="Linux" icon="linux">
        **Для .deb-пакетов:** `sudo apt remove cursor`

        **Для .rpm-пакетов:** `sudo dnf remove cursor` или `sudo yum remove cursor`

        **Для AppImage:** Удали файл Cursor.appimage из его расположения.
      </Card>
    </CardGroup>
  </Step>

  <Step title="Переустановка Cursor">
    Переустанови со [страницы загрузок](https://www.cursor.com/downloads). Если данные приложения не очищены, Cursor восстановится в прежнее состояние. Иначе получишь чистую установку.
  </Step>
</Steps>

<div id="reporting-an-issue">
  ## Сообщение о проблеме
</div>

Если эти шаги не помогли, напиши на [форум](https://forum.cursor.com/).

<Card horizontal title="Cursor Forum" icon="message" href="https://forum.cursor.com/">
  Сообщи об ошибке или проблеме на форуме Cursor
</Card>

Чтобы быстрее разобраться, укажи:

<CardGroup cols={2}>
  <Card title="Screenshot of Issue" icon="image">
    Сделай скриншот, замажь конфиденциальные данные.
  </Card>

  <Card title="Steps to Reproduce" icon="list-check">
    Опиши точные шаги для воспроизведения проблемы.
  </Card>

  <Card title="System Information" icon="computer">
    Получи информацию о системе здесь:

    <br />

    `Cursor` > `Help` > `About`
  </Card>

  <Card title="Request IDs" icon="shield-halved" href="/ru/troubleshooting/request-reporting">
    Нажми, чтобы открыть гайд по сбору Request IDs
  </Card>

  <Card title="Console Errors" icon="bug">
    Проверь консоль разработчика: <br />
    `Developer: Toggle Developer Tools`
  </Card>

  <Card title="Logs" icon="file-lines">
    Открой журнал логов: <br />
    `Developer: Open Logs Folder`
  </Card>
</CardGroup>

---

← Previous: [Получение ID запроса](./section-110.md) | [Index](./index.md) | Next: [Welcome](./welcome.md) →