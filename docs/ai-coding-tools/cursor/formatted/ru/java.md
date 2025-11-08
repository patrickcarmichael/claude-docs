---
title: "Java"
source: "https://docs.cursor.com/ru/guides/languages/java"
language: "ru"
language_name: "Russian"
---

# Java
Source: https://docs.cursor.com/ru/guides/languages/java

Настрой настройку разработки на Java с JDK, расширениями и инструментами сборки

Этот гайд поможет настроить Cursor для разработки на Java: установить JDK и необходимые расширения, настроить отладку, запуск Java‑приложений и интеграцию инструментов сборки, таких как Maven и Gradle. Также он охватывает возможности рабочего процесса, схожие с IntelliJ или VS Code.

<Note>
  Прежде чем начать, убедись, что у тебя установлен Cursor и он обновлён до
  последней версии.
</Note>

<div id="setting-up-java-for-cursor">
  ## Настройка Java для Cursor
</div>

<div id="java-installation">
  ### Установка Java
</div>

Прежде чем настраивать сам Cursor, тебе нужно установить Java на свой компьютер.

<Warning>
  Cursor не включает компилятор Java, так что установи JDK, если ещё не сделал этого.
</Warning>

<CardGroup cols={1}>
  <Card title="Установка на Windows" icon="windows">
    Скачай и установи JDK (например, OpenJDK, Oracle JDK, Microsoft Build of
    OpenJDK).

    <br />

    Задай переменную JAVA\_HOME и добавь JAVA\_HOME\bin в PATH.
  </Card>

  <Card title="Установка на macOS" icon="apple">
    Установи через Homebrew (`brew install openjdk`) или скачай установщик.

    <br />

    Убедись, что JAVA\_HOME указывает на установленный JDK.
  </Card>

  <Card title="Установка на Linux" icon="linux">
    Используй свой менеджер пакетов (`sudo apt install openjdk-17-jdk` или аналог)
    или установи через SDKMAN.
  </Card>
</CardGroup>

Чтобы проверить установку, запусти:

```bash  theme={null}
java -version
javac -version
```

<Info>
  Если Cursor не видит твой JDK, укажи его вручную в settings.json:
</Info>

```json  theme={null}
{
  "java.jdt.ls.java.home": "/path/to/jdk",
  "java.configuration.runtimes": [
    {
      "name": "JavaSE-17",
      "path": "/path/to/jdk-17",
      "default": true
    }
  ]
}
```

<Warning>Перезапусти Cursor, чтобы применить изменения.</Warning>

<div id="cursor-setup">
  ### Настройка Cursor
</div>

<Info>Cursor поддерживает расширения VS Code. Установи вручную следующие:</Info>

<CardGroup cols={2}>
  <Card title="Extension Pack for Java" icon="java" href="cursor:extension/vscjava.vscode-java-pack">
    Включает поддержку языка Java, отладчик, запуск тестов, поддержку Maven и
    менеджер проектов
  </Card>

  <Card title="Gradle for Java" icon="gears" href="cursor:extension/vscjava.vscode-gradle">
    Нужно для работы с системой сборки Gradle
  </Card>

  <Card title="Spring Boot Extension Pack" icon="leaf" href="cursor:extension/vmware.vscode-boot-dev-pack">
    Нужен для разработки на Spring Boot
  </Card>

  <Card title="Kotlin" icon="window" href="cursor:extension/fwcd.kotlin">
    Нужен для разработки приложений на Kotlin
  </Card>
</CardGroup>

<div id="configure-build-tools">
  ### Настройка инструментов сборки
</div>

<div id="maven">
  #### Maven
</div>

Убедись, что Maven установлен (`mvn -version`). При необходимости установи с [maven.apache.org](https://maven.apache.org/download.cgi):

1. Скачай бинарный архив
2. Распакуй в нужное место
3. Установи переменную окружения MAVEN\_HOME на распакованную папку
4. Добавь %MAVEN\_HOME%\bin (Windows) или \$MAVEN\_HOME/bin (Unix) в PATH

<div id="gradle">
  #### Gradle
</div>

Убедись, что Gradle установлен (`gradle -version`). При необходимости установи с [gradle.org](https://gradle.org/install/):

1. Скачай бинарную дистрибуцию
2. Распакуй в нужное место
3. Установи переменную окружения GRADLE\_HOME на распакованную папку
4. Добавь %GRADLE\_HOME%\bin (Windows) или \$GRADLE\_HOME/bin (Unix) в PATH

Либо используй Gradle Wrapper — он автоматически скачает и применит нужную версию Gradle:

<div id="running-and-debugging">
  ## Запуск и отладка
</div>

Всё готово — пора запускать и отлаживать Java‑код.
В зависимости от задач можешь использовать следующие способы:

<CardGroup cols={2}>
  <Card title="Run" icon="play">
    Нажми ссылку «Run», которая появляется над любым методом main, чтобы быстро
    выполнить программу
  </Card>

  <Card title="Debug" icon="bug">
    Открой боковую панель Run and Debug и нажми кнопку Run, чтобы запустить
    приложение
  </Card>
</CardGroup>

<CardGroup cols={1}>
  <Card title="Terminal" icon="terminal">
    Запусти из командной строки с помощью Maven или Gradle
  </Card>

  <Card title="Spring Boot" icon="leaf">
    Запускай приложения Spring Boot прямо из расширения Spring Boot Dashboard
  </Card>
</CardGroup>

<div id="java-x-cursor-workflow">
  ## Java x Cursor: рабочий процесс
</div>

AI‑возможности Cursor могут серьёзно прокачать твой Java‑воркфлоу. Вот как можно использовать возможности Cursor именно для Java:

<CardGroup cols={2}>
  <Card title="Tab Completion" icon="arrow-right">
    <div className="text-sm">
      Умные автодополнения для методов, сигнатур и типового Java‑кода вроде
      геттеров/сеттеров.
    </div>
  </Card>

  <Card title="Agent Mode" icon="pen-to-square">
    <div className="text-sm">
      Реализуй паттерны проектирования, рефактори код или генерируй классы с корректным
      наследованием.
    </div>
  </Card>

  <Card title="Inline Edit" icon="code">
    <div className="text-sm">
      Быстрые правки прямо в коде: обновляй методы, исправляй ошибки или генерируй unit‑тесты —
      без потери рабочего ритма.
    </div>
  </Card>

  <Card title="Chat" icon="message">
    <div className="text-sm">
      Получай помощь по Java‑концептам, разбирай исключения или изучай возможности фреймворков.
    </div>
  </Card>
</CardGroup>

<div id="example-workflows">
  ### Примеры рабочих процессов
</div>

1. **Генерация типового Java‑кода**\
   Используй [Tab completion](/ru/tab/overview), чтобы быстро сгенерировать конструкторы, геттеры/сеттеры, методы equals/hashCode и другие повторяющиеся Java‑шаблоны.

2. **Отладка сложных Java‑исключений**\
   Когда сталкиваешься с нечитаемым Java stack trace, выдели его и используй [Ask](/ru/chat/overview), чтобы понять первопричину и получить варианты исправления.

3. **Рефакторинг легаси‑кода на Java**\
   Используй [Agent mode](/ru/chat/agent), чтобы модернизировать старый Java‑код: переводи анонимные классы в лямбды, переходи на новые возможности языка Java или внедряй паттерны проектирования.

4. **Разработка с фреймворками**\
   Добавь документацию в контекст Cursor с @docs и генерируй код под конкретный фреймворк прямо в Cursor.

---

← Previous: [Работа с документацией](./section.md) | [Index](./index.md) | Next: [JavaScript & TypeScript](./javascript-typescript.md) →