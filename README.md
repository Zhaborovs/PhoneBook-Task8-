# Система управления телефонным справочником

Этот простой Python-скрипт предоставляет базовую систему управления телефонным справочником. Пользователи могут выполнять различные операции, такие как добавление новых записей, чтение существующего телефонного справочника, поиск информации и копирование записей из одного файла в другой.

## Использование

1. **Добавление новой записи**
    - Выберите вариант 1 из меню.
    - Введите необходимую информацию по запросу (имя, фамилия, отчество, номер телефона и адрес).

2. **Чтение телефонного справочника**
    - Выберите вариант 2 из меню.
    - Скрипт отобразит весь телефонный справочник.

3. **Поиск информации**
    - Выберите вариант 3 из меню.
    - Введите поисковый запрос по запросу.
    - Скрипт выполнит поиск запроса во всех файлах и отобразит соответствующие записи.

4. **Копирование записи**
    - Выберите вариант 4 из меню.
    - Введите имя исходного файла, имя файла назначения и номер строки для копирования.
    - Скрипт скопирует указанную запись из исходного файла в файл назначения.

5. **Выход**
    - Выберите вариант 5 из меню для завершения программы.

## Требования

- Python 3.x

## Как запустить

1. Сохраните сценарий в файле (например, `phone_book_manager.py`).
2. Откройте терминал и перейдите в каталог с файлом сценария.
3. Запустите сценарий, выполнив команду: `python phone_book_manager.py`

## Примечание

- Записи телефонного справочника сохраняются в файле с именем `phone_book.txt`.
- Каждая запись в файле содержит имя, фамилию, отчество, номер телефона и адрес.
- Скрипт использует модули `os`, `time` и `glob` для различных функциональностей.
- READMI.md был написан при помощи `GPT-3.5`.