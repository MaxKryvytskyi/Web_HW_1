# Project_Core_group1_ver.1

## CLI - Command Line Interface bot Clane4Code

Вітаємо вас у консольному багатофункціональному помічнику.
Цей додаток виконує багато корисних функцій, таких як:

1. Створення редагування та видалення контакту який має поля: Ім'я, день народження, номер телефону(нів), e-mail, адреса контакту. Також є можливість редагувати ці поля окремо.
2. Також є важлива функція отримання кількості днів до дня народження контакту, а також є дуже корисна можливість виводу контактів у яких буде народження у найближчі дні (кількість днів за які потрібно вивести вказується при введенні команди).
3. Помічник також може зберігатиб, редагувати та видаляти нотатки. Також є можливість додавати "теги" і сортувати нотатки за тегами та просто за окремими словами або датами.
4. Корисна функція сортування файлів допоможе вам навести лад у вказанній папці, наприклад (sort C://testfolder) Також ця функція зберігає "лог файл" з переліком файлів які були відсортовані.

Для початку роботи з цим проектом, потрібно виконати наступні кроки:

1. Спочатку склонуйте цей [https://github.com/Aleksandr-Levchenko/Project_Core_group1_ver.1.git] репозиторій до свого комп'ютера. Також це можна зробити через консоль: git clone [https://github.com/Aleksandr-Levchenko/Project_Core_group1_ver.1.git]
2. Перейдіть до папки проекту: cd "ваш-репозиторій"
3. Запустіть ваш Python віртуальне середовище: напиклад "python3 -m venv venv"
4. Встановіть залежності: "pip install -r requirements.txt"
5. Використання:
   Після встановлення проекту, ви можете використовувати його наступним чином:
   Запустіть головний скрипт:
   python main.py

Команти які можна використовувати в помічнику:

1. cls - очищення екрану від інформації
2. hello - вітання
3. good bye, close, exit - завершення програми
4. load - завантаження інформації про користувачів із файлу
5. save - збереження інформації про користувачів у файл
6. show all - друкування всієї наявної інформації про користувачів
7. show book /N - друкування інформації посторінково, де N - кількість записів на 1 сторінку
8. add - додавання користувача до бази даних.
   > Приклад >> add Mike 02.10.1990 +380504995876
   > Приклад >> add Mike None +380504995876
   > Приклад >> add Mike None None
9. phone - повертає перелік телефонів для особи
   > Приклад >> phone Mike
10. add phone - додавання телефону для користувача
    > Приклад >> add phone Mike +380504995876
11. change phone - зміна номеру телефону для користувача
    > Формат запису телефону: +38ХХХ ХХХ ХХ ХХ
    > Приклад >> change phone Mike +380504995876 +380665554433
12. del phone - видаляє телефон для особи. Дозволяється видаляти одразу декілька телефонів.
    > Приклад >> del phone Mike +380509998877, +380732225566
13. birthday - повертає кількість днів до Дня народження
    > Приклад >> birthday Mike
14. change birthday - змінює/додає Дату народження для особи
    > Приклад >> change birthday Mike 02.03.1990
15. search - виконує пошук інформації по довідковій книзі
    > Приклад >> search Mike
16. sort - виконує сортування файлів у вказаній папці
    > Приклад >> sort C:\\your_folder

Ось приклад коду:

### Функція виконує парсер команд та відповідних параметрів

```
def parcer_commands(cmd_line):
    lst, tmp, cmd, prm  = [[], [], "", ""]

    if cmd_line:
        tmp = cmd_line.split()

        # перевіремо ПОДВІЙНУ команду
        if len(tmp) > 1 and f"{tmp[0]} {tmp[1]}".lower() in COMMANDS: #  add Mike 4589 94508
            cmd = f"{tmp[0]} {tmp[1]}".lower()
            prm = cmd_line.partition(cmd)[2].strip()

        # перевіремо ОДИНАРНУ команду
        elif tmp[0].lower() in COMMANDS:
            cmd = tmp[0].lower()
            prm = cmd_line.partition(" ")[2]
    return cmd, prm


```

## _Додаткова інформація_:

Під час розробки CLI (консольний бот) були розроблені відповідні класи:

> AdressBook, Record, Name, Phone, Birthday, Email, Field, PhoneException, BirthdayException, EmailException

_із викристанням наступних бібліотек_:

> sys, platform, sort_main, re, print, box, Table, Console, UserDict, Iterator, datetime, pickle, Path, uuid, shutil.

- class AddressBook: зберігає функції для роботи з адресною книгою.
- class Record: зберігає записи, що містять ім'я, номери телефонів, дату народження .
- class Name: зберігає записи з іменами контактів.
- class Phone: зберігає записи з номерами телефонів контактів.
- class Birthday: зберігає записи з датами народження контактів.
- class PhoneException, class BirthdayException, class EmailException: зберігають записи з визначеними винятковими ситуаціями, які можуть виникнути при роботі з номерами телефонів, датами народження чи електронною поштою.
- class UserDict: зберігає записи з словників з підтримкою деяких методів. sys: надає доступ до функцій та змінних.
- platform: надає доступ до інформації про операційну систему та обладнання.
- sort_main: пов'язана з сортуванням даних.

- re: надає функціональність регулярних виразів для роботи з текстовими рядками.

- print: вбудована функція для виводу даних на консоль.

- box: включає функції для створення боксів, рамок, рамок навколо тексту.

- Table: для створення таблиць для виведення даних на консоль.

- Console: надає функції для роботи з консоллю.

- Iterator: для створення ітераторів для обходу об'єктів.

- datetime: для роботи з датою та часом.

- pickle: надає можливості серіалізації та десеріалізації об'єктів Python.

- Path: може надавати клас для роботи з файловими шляхами.

- uuid: надає інструменти для генерації унікальних ідентифікаторів.

- shutil: містить функції для роботи з файловою системою, такі як копіювання, переміщення файлів.

Запитання та пропозиції пишіть нашій команді:

- levchenko.aah@gmail.com _Team-Lead_ **Олександр**
- max.krivitskyh@gmail.com _ScrumMaster_ **Максим**
- semnatalis52@gmail.com _Coder_ **Наталія**
- vadim.marenko@gmail.com _Coder_ **Вадим**
- tanichka.chirkova@gmail.com _Coder_ **Таня**
- officedenko@gmail.com _Coder_ **Олег**