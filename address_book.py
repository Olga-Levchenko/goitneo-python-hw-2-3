from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, value):
        super().__init__(value)

class Phone(Field):
    def __init__(self, value):
        super().__init__(value)

    def is_valid(self):
        return self.value.isdigit() and len(self.value) == 10

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
    
    def add_phone(self, number):
        phone = Phone(number)
        if not phone.is_valid():
            raise ValueError
        self.phones.append(phone)

    def find_phone(self, number):
        phones = list(filter(lambda x: x.value == number, self.phones))
        if len(phones) == 0:
            raise KeyError
        return phones[0]

    def delete_phone(self, number):
        phone = self.find_phone(number)
        self.phones.remove(phone)
    
    def edit_phone(self, number, new_number):
        self.delete_phone(number)
        self.add_phone(new_number)

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def __init__(self):
        self.data = {}
    
    def add_record(self, record):
        self.data[record.name.value] = record
    
    def find(self, name):
        records = list(map(lambda x: self.data[x] , filter(lambda x: x == name, self.data)))
        if len(records) == 0:
            raise KeyError
        return records[0]
    
    def delete(self, name):
        record = self.find(name)
        self.data.pop(record.name.value)

 # Створення нової адресної книги
book = AddressBook()

# Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

# Додавання запису John до адресної книги
book.add_record(john_record)

# Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

# Виведення всіх записів у книзі
for name, record in book.data.items():
    print(record)

# Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")

print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

# Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

# Видалення запису Jane
book.delete("Jane")