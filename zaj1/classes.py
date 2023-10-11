import datetime


class Employee:
    name = ""
    surname = ""
    salary = 0.0

    def __init__(self, name: str, surname: str, salary: float):
        self.name = name
        self.surname = surname
        self.salary = salary

    def show(self):
        print(self.name, self.surname, self.salary)


class ReceivedInvoice:
    date = datetime.date(2000, 1, 1)
    amount = 0

    def __init__(self, date: datetime.date, amount: float):
        self.date = date
        self.amount = amount

    def show(self):
        print(self.date, self.amount)


class IssuedInvoice:
    date = datetime.date(2000, 1, 1)
    amount = 0

    def __init__(self, date: datetime.date, amount: float):
        self.date = date
        self.amount = amount

    def show(self):
        print(self.date, self.amount)
