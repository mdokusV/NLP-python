import datetime


class Employee:
    name = ""
    surname = ""
    salary = 0.0

    def __init__(self, name: str, surname: str, salary: float):
        self.name = name
        self.surname = surname
        self.salary = salary

    def print(self):
        print(self.name, self.surname, self.salary)


class ReceivedInvoice:
    date = datetime.date(2000, 1, 1)
    amount = 0


class IssuedInvoice:
    date = datetime.date(2000, 1, 1)
    amount = 0
