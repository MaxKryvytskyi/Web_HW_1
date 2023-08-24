
from view import AbstractView

from address_book import AddressBook
from note_book import NoteBook

# from BotAssistant.view import AbstractView
# from BotAssistant.address_book import AddressBook
# from BotAssistant.note_book import NoteBook


from rich.table import Table
from rich.console import Console


class Console_View(AbstractView):
    def show_note_book(self, note_book: NoteBook):
        table = Table(title=f"Note Book")
        table.add_column("Num", justify="center", style="cyan", no_wrap=False)
        table.add_column("Tag", justify="center", style="cyan", no_wrap=False)
        table.add_column("Note", justify="center", style="cyan", no_wrap=False)
  
        for num, record in note_book.data.items():
            table.add_row(f"{note_book.dict_num[str(num)]}", 
                          f"{record.tags}",
                          f"{record.note}")
        return table

    def show_contact_book(self, contact_book: AddressBook):
        if len(contact_book.data) == 0: return None
        table = Table(title=f"Contact Book")
        table.add_column("Name", justify="center", style="cyan", no_wrap=False)
        table.add_column("Phones", justify="center", style="magenta", no_wrap=False)
        table.add_column("Emails", justify="center", style="cyan", no_wrap=False)
        table.add_column("Birthday", justify="center", style="cyan", no_wrap=False)
        table.add_column("Status", justify="center", style="cyan", no_wrap=False)
        table.add_column("Address", justify="center", style="cyan", no_wrap=False)
        table.add_column("Note", justify="center", style="cyan", no_wrap=False)
        for i in contact_book.values():
            table.add_row(f"{i.name.value_of()}", 
                        f"{[el.value_of() for el in i.phones] if [el.value_of() for el in i.phones] != [''] else ''}", 
                        f"{[el.value_of() for el in i.emails] if [el.value_of() for el in i.emails] != [''] else ''}",
                        f"{i.birthday.value_of()}",
                        f"{i.status.value_of()}",
                        f"{i.address.value_of()}",
                        f"{i.note.value_of()}")
        return table

    def show_help_contact_book(self):
        table = Table(title=f"Helper Contact Book")
        table.add_column("Сommand", justify="center", style="cyan", no_wrap=False)
        table.add_column("Description", justify="center", style="magenta", no_wrap=False)
        table.add_column("Example", justify="center", style="magenta", no_wrap=False)
        table.add_row("add", "Додає контакт в книгу контактів", "add | add max")
        table.add_row("add note", "Додає нотатку в книгу контактів", "add note max")
        table.add_row("add phone", "Додає телефон в книгу контактів", "add phone max")
        table.add_row("add email", "Додає емеіл в книгу контактів", "add email max")
        table.add_row("add status", "Додає статус в книгу контактів", "add status max")
        table.add_row("add address", "Додає адрессу в книгу контактів", "add address max")
        table.add_row("add birthday", "Додає дату народження в книгу контактів", "add birthday max")

        table.add_row("change name", "Змінює ім'я контакту", "change name max")
        table.add_row("change note", "Змінює нотатку контакту", "change note max")
        table.add_row("change phone", "Змінює телефон контакту", "change phone max")
        table.add_row("change email", "Змінює емеіл контакту", "change email max")
        table.add_row("change status", "Змінює статус контакту", "change status max")
        table.add_row("change address", "Змінює адресу контакту", "change address max")
        table.add_row("change birthday", "Змінює дату народження контакту", "change birthday max")

        table.add_row("del name", "Видаляє контакт", "del name max")
        table.add_row("del note", "Видаляє нотатку контакту", "del note max")
        table.add_row("del phone", "Видаляє телефон контакту", "del phone max")
        table.add_row("del email", "Видаляє емеіл контакту", "del email max")
        table.add_row("del status", "Видаляє статус контакту", "del status max")
        table.add_row("del address", "Видаляє адресу контакту", "del address max")
        table.add_row("del birthday", "Видаляє дату народження контакту", "del birthday max")

        table.add_row("all birthday", "Виводить в продовж N днів  дні народження", "all birthday 20")
        table.add_row("close | exit | good bye", "Вихід із застосунку", "close | exit | good bye")
        table.add_row("show all", "Виводить всі збережені контакти", "show all")
        table.add_row("search", "Пошук по книгі контактів", "search max")
        table.add_row("hello", "Привітання", "hello")
        table.add_row("birthday", "Виводить кількість днів до дня народження", "birthday max")
        table.add_row("help", "Допомога по командам", "help")
        table.add_row("leave", "Повертаєтся в головне меню", "leave")
        return table

    def show_help_note_book(self):
        table = Table(title=f"Helper Note Book")
        table.add_column("Сommand", justify="center", style="cyan", no_wrap=False)
        table.add_column("Description", justify="center", style="magenta", no_wrap=False)
        table.add_column("Example", justify="center", style="magenta", no_wrap=False)
        table.add_row("add", "Додає нотатки та тег", "add")
        table.add_row("add tag", "Додає додатковий тег", "add tag")
        table.add_row("change note", "Редагує нотатку", "change note")
        table.add_row("change tag", "Редагує тег", "change tag")
        table.add_row("del note", "Видаляє нотатку", "del note")
        table.add_row("del tag", "Видаляє тег", "del tag")
        table.add_row("search", "Пошук по нотаткам та тегам", "search qsd")
        table.add_row("help", "Допомога по командам", "help")
        table.add_row("show all", "Виводить всі збережені нотатки", "show all")
        table.add_row("leave", "Повертаєтся в головне меню", "leave")
        return table