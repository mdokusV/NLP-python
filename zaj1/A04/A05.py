import os
from pydoc import text

DIR = os.path.dirname(__file__)


def join_path(filename: str) -> str:
    return os.path.join(DIR, filename)


with open(join_path("letter.txt"), "r", newline="") as file:
    text = file.read()
    file.seek(0)
    text_lines = file.readlines()

print(text_lines)

new_text = ""
for index, line in enumerate(text_lines):
    if index % 3 == 2:
        text_lines[index] = "*" * len(line) + "\n"

    if "kocham" in line:
        text_lines[index] = "*" * len(line) + "\n"

    new_text += text_lines[index]


with open(join_path("censorship.txt"), "w", newline="") as file:
    file.write(new_text)
