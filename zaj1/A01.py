import csv
import classes
import array
import random
from datetime import datetime, timedelta


NUMBER_OF_INVOICES = 100

first_names = ("John", "Andy", "Joe", "Jane", "Mary", "Peter", "Linda")
last_names = ("Johnson", "Smith", "Williams", "Jones", "Brown", "Taylor", "Thomas")

# put people into a csv
with open("employee.csv", "w", newline="") as csvfile:
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


def random_date():
    start_date = datetime(2022, 1, 1)
    end_date = datetime(2023, 12, 31)
    return start_date + timedelta(days=random.randint(0, (end_date - start_date).days))


# put ReceivedInvoice into a csv
with open("received.csv", "w", newline="") as csvfile:
    fileReader = csv.writer(
        csvfile, delimiter=" ", quotechar="|", quoting=csv.QUOTE_MINIMAL
    )
    for x in range(NUMBER_OF_INVOICES):
        fileReader.writerow(
            [
                random_date(),
                random.uniform(1000, 3000),
            ]
        )

# put IssuedInvoice into a csv
with open("issued.csv", "w", newline="") as csvfile:
    fileReader = csv.writer(
        csvfile, delimiter=" ", quotechar="|", quoting=csv.QUOTE_MINIMAL
    )
    for x in range(NUMBER_OF_INVOICES):
        fileReader.writerow(
            [
                random_date(),
                random.uniform(1000, 3000),
            ]
        )

# read people from a csv
with open("employee.csv", newline="") as csvfile:
    fileReader = csv.reader(csvfile, delimiter=" ", quotechar="|")
    people = []
    for row in fileReader:
        people.append(classes.Employee(row[0], row[1], float(row[2])))

# read ReceivedInvoice from a csv
with open("received.csv", newline="") as csvfile:
    fileReader = csv.reader(csvfile, delimiter=" ", quotechar="|")
    receivedInvoices = []
    for row in fileReader:
        receivedInvoices.append(classes.ReceivedInvoice(row[0], float(row[1])))

# read IssuedInvoice from a csv
with open("issued.csv", newline="") as csvfile:
    fileReader = csv.reader(csvfile, delimiter=" ", quotechar="|")
    issuedInvoices = []
    for row in fileReader:
        issuedInvoices.append(classes.IssuedInvoice(row[0], float(row[1])))


employmentCost = 0

for person in people:
    person.show()
    employmentCost += person.salary

print(employmentCost)
