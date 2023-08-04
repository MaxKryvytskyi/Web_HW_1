from abc import ABC, abstractmethod
from typing import Any


# class IPerson(ABC):
#     @abstractmethod
#     def get_phone_number(self):
#         pass


# class IPhone(ABC):
#     @abstractmethod
#     def value_of(self):
#         pass

# class IPersonAddress(ABC):
#     @abstractmethod
#     def value_of(self):
#         pass

# class PhoneNumber(IPhone):
#     def __init__(self, phone:str, code:str) -> None:
#         self.phone = phone
#         self.code = code

#     def value_of(self):
#         return f"+380({self.code}){self.phone}"

# class PersonAddress(IPersonAddress):

#     def __init__(self, zip, city, street) -> None:
#         self.zip = zip
#         self.city = city
#         self.street = street

#     def value_of(self):
#         return f"{self.zip}, {self.city}, {self.street}"

# class Person(IPerson):
#     def __init__(self, name:str, phone: IPhone, address: PersonAddress) -> None:
#         self.name = name
#         self.phone = phone
#         self.address = address

#     def get_phone_number(self):
#         return f"{self.name}: {self.phone.value_of()}"
    
#     def get_address(self):
#         return self.address.value_of()
    



# if __name__ == "__main__":
#     person = Person("Max", PhoneNumber("9991111", "099"), PersonAddress("36007", "Poltava", "european, 28"))
#     print(person.get_phone_number())
#     print(person.get_address()) 



import datetime

class Event:
    _observers = []

    def register(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def unregister(self, observer):
        if observer in self._observers:
            self._observers.remove(observer)

    def notify_all(self, event, data=None):
        for observer in self._observers:
            observer(event, data)


def terminal_logger(event, data):
    print(event, data)



class FileLogger:
    def __init__(self, filename) -> None:
        self.filename = filename

    def __call__(self, event, data) -> Any:
        with open(self.filename, 'a') as fn:
            fn.write(f"{datetime.datetime.now()}: [{event}] - [{data}]\n")

if __name__ == "__main__":
    event = Event()
    event.register(terminal_logger)
    flog = FileLogger('streams.log')
    event.register(flog)


    event.notify_all("tick", 122)
    event.notify_all("tick", 123)
    event.notify_all("tick", 124)
    event.notify_all("tick", 125)
    event.notify_all("mesage", "happens")
    event.unregister(flog)
    event.notify_all("tick", 126)
    event.notify_all("tick", 127)
    event.unregister(terminal_logger)
    event.notify_all("tick", 128)
    event.notify_all("tick", 129)
