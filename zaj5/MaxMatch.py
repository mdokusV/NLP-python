import pandas as pd
import subprocess


CHUNKSIZE = 100000


def pd_read_first_column(file_path) -> set[str]:
    print("Start loading words \n")
    bash_wc_command = subprocess.run(
        ["wc", "-l", file_path], stdout=subprocess.PIPE, text=True, check=True
    )
    line_count = int(bash_wc_command.stdout.split()[0])

    words_set = set()
    loaded = 0
    for chunk in pd.read_csv(
        file_path, sep="\t", header=None, usecols=[0], dtype=str, chunksize=CHUNKSIZE
    ):
        loaded += len(chunk[0])
        print(f"Loaded {loaded/line_count * 100}% words")
        for word in chunk[0]:
            words_set.add(word)

    print("Finished loading words \n")
    return words_set


def max_match(sentence, dictionary) -> list[str]:
    words = []
    i = 0
    while i < len(sentence):
        found = False
        for j in range(len(sentence), i, -1):
            current_word = sentence[i:j]
            if current_word in dictionary:
                words.append(current_word)
                i = j
                found = True
                break
        if not found:
            words.append(sentence[i])
            i += 1
    return words


words_set = pd_read_first_column("PoliMorf-0.6.7.tab")

sentence = "matkaradedała"

words = max_match(sentence, words_set)
print(sentence, words)
