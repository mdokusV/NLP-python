# polish english dictionary

dictionary = {
    "jabłko": "apple",
    "gruszka": "pear",
    "komputer": "computer",
    "mleko": "milk",
    "jogurt": "yogurt",
    "piwo": "beer",
    "pomidor": "tomato",
    "czekolada": "chocolate",
    "chleb": "bread",
    "jajko": "egg",
    "ser": "cheese",
}

print("Podaj polskie słowo:")
word = input()
print("Odpowiedz:", dictionary.get(word, "nie znaleziono"))
