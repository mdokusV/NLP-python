import collections
from typing import Any


def generate_vocabulary_1_letter(text):
    vocabulary = collections.Counter(text[i : i + 1] for i in range(len(text) - 1))
    return vocabulary


def get_most_popular_2_letter_appearances(text):
    appearances = collections.Counter(text[i : i + 2] for i in range(len(text) - 1))
    return appearances


def remove_punctuation(text):
    return (
        text.replace(".", "")
        .replace(",", "")
        .replace("?", "")
        .replace("!", "")
        .replace(":", "")
    )


def add_new_words_to_vocabulary(
    vocabulary: collections.Counter,
    new_words: collections.Counter,
    max_length: int,
) -> collections.Counter:
    free_space = max_length - len(vocabulary)
    if free_space < 0:
        print("Too many words!")
        return vocabulary

    new_words_list = new_words.most_common(free_space)
    new_words = collections.Counter(dict(new_words_list))

    vocabulary.update(new_words)

    return vocabulary


def print_vocabulary(vocabulary: collections.Counter):
    print_list = []
    for key, value in vocabulary.items():
        key = key.replace(" ", "<w>")
        print_list.append((key, value))
    print(print_list)


TEXT = "Politycznych konszachtów, intryg, dotknął końcami bokach cztery rękojeści przy bardzo niskiej Śmiga mówi coś dotknął końcami palców i pomknął bezgłośnie dalej coś w jego stronę palców po rurze, wystarczyć na miesiące? Żywność żalu do Smigi on już raz jeden tylko a za resztę pograłby zwiedzający wnętrze bez przerwy krążyła, było: pewien. Można powiedzieć, się wkuwanie do końcowych egzaminów! Naprzód poleciał wzdłuż rury, zimno gładkiej powierzchni to horyzont epoka wysokich sporów?"
NUMBER_OF_SUB_WORDS = 2**6

text = remove_punctuation(TEXT)


vocabulary = generate_vocabulary_1_letter(text)

vocabulary = add_new_words_to_vocabulary(
    vocabulary, get_most_popular_2_letter_appearances(text), NUMBER_OF_SUB_WORDS
)

print_vocabulary(vocabulary)
