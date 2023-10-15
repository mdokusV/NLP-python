import csv
import os

DIR = os.path.dirname(__file__)


def join_path(filename: str) -> str:
    return os.path.join(DIR, filename)


with open(join_path("data.csv"), "r", newline="") as file:
    reader = csv.reader(file, delimiter=";")
    for row in reader:
        if len(row) != 3:
            print(False)
            exit()
        if not row[1].isdigit() or not row[2].isdigit():
            print(False)
            exit()
    print(True)
