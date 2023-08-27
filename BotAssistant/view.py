from abc import ABC, abstractmethod
from contact_book import AddressBook
from note_book import NoteBook

# from BotAssistant.contact_book import AddressBook
# from BotAssistant.note_book import NoteBook

class AbstractViewTerminal(ABC):

   @abstractmethod
   def show_contact_book(self, contact_book: AddressBook):
      pass

   @abstractmethod
   def show_note_book(self, note_book: NoteBook):
      pass

   @abstractmethod
   def show_help_contact_book(self):
      pass

   @abstractmethod
   def show_help_note_book(self):
      pass