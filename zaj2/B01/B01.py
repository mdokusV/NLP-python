import re


def main():
    ERROR_RETURN = "Blad: Niepoprawne dane wejsciowe dla pola"

    def get_input(prompt):
        return input(prompt + ": ")

    def validate_title(value):
        return value.istitle()

    def validate_telefon(value):
        return bool(re.match(r"\(\d{2}\) \d{3}-\d{2}-\d{2}$", value))

    def validate_kod_pocztowy(value):
        return bool(re.match(r"\d{2}-\d{3}$", value))

    imie = get_input("Podaj imie")
    nazwisko = get_input("Podaj nazwisko")
    miasto = get_input("Podaj miasto")
    telefon = get_input("Podaj numer telefonu (w formacie (xx) xxx-xx-xx)")
    kod_pocztowy = get_input("Podaj kod pocztowy (w formacie xx-xxx)")

    if (
        not validate_title(imie)
        or not validate_title(nazwisko)
        or not validate_title(miasto)
    ):
        print(ERROR_RETURN + " imie i nazwisko")
        return

    if not validate_telefon(telefon):
        print(ERROR_RETURN + " telefon")
        return

    if not validate_kod_pocztowy(kod_pocztowy):
        print(ERROR_RETURN + " kod pocztowy")
        return

    print("Dane prawidlowe")


if __name__ == "__main__":
    main()
