import csv
import classes
import array
import random


first_names = ("John", "Andy", "Joe")
last_names = ("Johnson", "Smith", "Williams")

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


with open("employee.csv", newline="") as csvfile:
    fileReader = csv.reader(csvfile, delimiter=" ", quotechar="|")
    people = [classes.Employee]
    for row in fileReader:
        people.append(classes.Employee(row[0], row[1], float(row[2])))
        print(row)

    people[1].print()
