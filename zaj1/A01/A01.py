import csv
import classes
import array
import random
import calendar
from datetime import datetime, timedelta
import os


NUMBER_OF_INVOICES = 10
DIR = os.path.dirname(__file__)

first_names = ("John", "Andy", "Joe", "Jane", "Mary", "Peter", "Linda")
last_names = ("Johnson", "Smith", "Williams", "Jones", "Brown", "Taylor", "Thomas")


def join_path(filename: str) -> str:
    return os.path.join(DIR, filename)


# put people into a csv
with open(join_path("employee.csv"), "w", newline="") as csvfile:
    fileReader = csv.writer(
        csvfile, delimiter=" ", quotechar="|", quoting=csv.QUOTE_MINIMAL
    )
    for x in range(3):
        fileReader.writerow(
            [
                random.choice(first_names),
                random.choice(last_names),
                random.uniform(1000, 3000),
            ]
        )


def generate_date(x: int) -> datetime.date:
    return datetime(2022, x, 1).date()


# put ReceivedInvoice into a csv
with open(join_path("received.csv"), "w", newline="") as csvfile:
    fileReader = csv.writer(
        csvfile, delimiter=" ", quotechar="|", quoting=csv.QUOTE_MINIMAL
    )
    iter = 2
    for x in range(NUMBER_OF_INVOICES):
        fileReader.writerow(
            [
                generate_date(iter),
                random.uniform(1000, 3000),
            ]
        )
        iter += 1

# put IssuedInvoice into a csv
with open(join_path("issued.csv"), "w", newline="") as csvfile:
    fileReader = csv.writer(
        csvfile, delimiter=" ", quotechar="|", quoting=csv.QUOTE_MINIMAL
    )
    iter = 2
    for x in range(NUMBER_OF_INVOICES):
        fileReader.writerow(
            [
                generate_date(iter),
                random.uniform(7000, 10_000),
            ]
        )
        iter += 1

# read people from a csv
with open(join_path("employee.csv"), newline="") as csvfile:
    fileReader = csv.reader(csvfile, delimiter=" ", quotechar="|")
    people = []
    for row in fileReader:
        people.append(classes.Employee(row[0], row[1], float(row[2])))

# read ReceivedInvoice from a csv
with open(join_path("received.csv"), newline="") as csvfile:
    fileReader = csv.reader(csvfile, delimiter=" ", quotechar="|")
    receivedInvoices = []
    for row in fileReader:
        receivedInvoices.append(
            classes.ReceivedInvoice(
                datetime.strptime(row[0], "%Y-%m-%d"), float(row[1])
            )
        )

# read IssuedInvoice from a csv
with open(join_path("issued.csv"), newline="") as csvfile:
    fileReader = csv.reader(csvfile, delimiter=" ", quotechar="|")
    issuedInvoices = []
    for row in fileReader:
        issuedInvoices.append(
            classes.IssuedInvoice(datetime.strptime(row[0], "%Y-%m-%d"), float(row[1]))
        )


employmentCost = 0

for person in people:
    employmentCost += person.salary


# issued invoice +
# received invoice -
# salary -


budget = []
print("month    ", "income")
for i in range(len(issuedInvoices)):
    budget.append(
        issuedInvoices[i].amount - receivedInvoices[i].amount - employmentCost
    )
    print(calendar.month_name[issuedInvoices[i].date.month - 1], ":", budget[i])
