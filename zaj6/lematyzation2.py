import pandas as pd
import subprocess


CHUNKSIZE = int(1e5)


def read_dictionary(file_path) -> dict[str, tuple[str, str]]:
    print("Start loading words \n")
    bash_wc_command = subprocess.run(
        ["wc", "-l", file_path], stdout=subprocess.PIPE, text=True, check=True
    )
    line_count = int(bash_wc_command.stdout.split()[0])

    words_dict: dict[str, tuple[str, str]] = {}

    with open(file_path, "r") as file:
        loaded = 0
        for line in file:
            loaded += 1
            if loaded % CHUNKSIZE == 0:
                print(f"Loaded {loaded/line_count * 100:.2f}% words")
            line = line.strip().split("\t")
            if line[0] in words_dict:
                continue
            words_dict[line[0]] = (line[1], line[2].split(":")[0])

    print("Finished loading words \n")
    return words_dict


words_dict = read_dictionary("zaj6/PoliMorf-0.6.7.tab")

input_text = input("Enter word: ")

if input_text in words_dict:
    print(
        f"{input_text} - base form: {words_dict[input_text][0]}, type: {words_dict[input_text][1]}"
    )
else:
    print("Not found")
