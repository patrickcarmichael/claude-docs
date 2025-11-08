---
title: "Permissions"
source: "https://docs.cursor.com/ru/cli/reference/permissions"
language: "ru"
language_name: "Russian"
---

# Permissions
Source: https://docs.cursor.com/ru/cli/reference/permissions

Типы разрешений для управления доступом агента к файлам и командам

Настрой, что агенту разрешено делать, используя токены разрешений в конфигурации CLI. Разрешения задаются в `~/.cursor/cli-config.json` (глобально) или `<project>/.cursor/cli.json` (для конкретного проекта).

<div id="permission-types">
  ## Типы разрешений
</div>

<div id="shell-commands">
  ### Команды shell
</div>

**Формат:** `Shell(commandBase)`

Управляет доступом к командам shell. `commandBase` — это первый токен в командной строке.

<div class="full-width-table">
  | Пример       | Описание                                                   |
  | ------------ | ---------------------------------------------------------- |
  | `Shell(ls)`  | Разрешить выполнение команд `ls`                           |
  | `Shell(git)` | Разрешить любые подкоманды `git`                           |
  | `Shell(npm)` | Разрешить команды менеджера пакетов npm                    |
  | `Shell(rm)`  | Запретить разрушительное удаление файлов (обычно в `deny`) |
</div>

<div id="file-reads">
  ### Чтение файлов
</div>

**Формат:** `Read(pathOrGlob)`

Управляет доступом на чтение файлов и каталогов. Поддерживает glob-шаблоны.

<div class="full-width-table">
  | Пример              | Описание                                    |
  | ------------------- | ------------------------------------------- |
  | `Read(src/**/*.ts)` | Разрешить чтение файлов TypeScript в `src`  |
  | `Read(**/*.md)`     | Разрешить чтение файлов Markdown где угодно |
  | `Read(.env*)`       | Запретить чтение файлов окружения           |
  | `Read(/etc/passwd)` | Запретить чтение системных файлов           |
</div>

<div id="file-writes">
  ### Запись файлов
</div>

**Формат:** `Write(pathOrGlob)`

Управляет доступом на запись файлов и каталогов. Поддерживает glob-шаблоны. В режиме печати для записи файлов требуется `--force`.

<div class="full-width-table">
  | Пример                | Описание                                    |
  | --------------------- | ------------------------------------------- |
  | `Write(src/**)`       | Разрешить запись в любые файлы внутри `src` |
  | `Write(package.json)` | Разрешить изменение package.json            |
  | `Write(**/*.key)`     | Запретить запись файлов закрытых ключей     |
  | `Write(**/.env*)`     | Запретить запись файлов окружения           |
</div>

<div id="configuration">
  ## Конфигурация
</div>

Добавь permissions в объект `permissions` в конфигурационном файле CLI:

```json  theme={null}
{
  "permissions": {
    "allow": [
      "Shell(ls)",
      "Shell(git)", 
      "Read(src/**/*.ts)",
      "Write(package.json)"
    ],
    "deny": [
      "Shell(rm)",
      "Read(.env*)",
      "Write(**/*.key)"
    ]
  }
}
```

<div id="pattern-matching">
  ## Сопоставление шаблонов
</div>

* Шаблоны glob используют маски `**`, `*` и `?`
* Относительные пути относятся к текущему рабочему пространству
* Абсолютные пути могут указывать на файлы вне проекта
* Правила deny имеют приоритет над правилами allow

---

← Previous: [Параметры](./section.md) | [Index](./index.md) | Next: [Slash-команды](./slash.md) →