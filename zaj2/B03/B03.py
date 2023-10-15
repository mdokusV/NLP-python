import os
import re

DIR = os.path.dirname(__file__)


def join_path(filename: str) -> str:
    return os.path.join(DIR, filename)


with open(join_path("text.txt"), "r", newline="") as file:
    text = file.read()

with open(join_path("vulgarisms.txt"), "r", newline="") as file:
    vulgarisms = file.readlines()
    vulgarisms = [line.strip() for line in vulgarisms]


regex_vulgar = r"\b(" + "|".join(vulgarisms) + r")\b"

censored_text = re.sub(regex_vulgar, "---", text, flags=re.IGNORECASE)

print(censored_text)
