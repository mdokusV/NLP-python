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

word = input("Podaj polskie słowo: ")
print("Odpowiedz:", dictionary.get(word, "nie znaleziono"))
