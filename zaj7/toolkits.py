import spacy
from spacy.tokens import Token

nlp = spacy.load(name="pl_core_news_lg")

text = "Zmniejsz głośność odtwarzacza muzyki, a potem idź po jedzenie! Pomóż też przy śniadaniu."

doc = nlp(text)

sentence_has_order = False
root = None
for token in doc:
    if token.tag_ == "IMPT" and root is None:
        sentence_has_order = True
        root = token

    print(
        token.text,
        token.pos_,
        token.tag_,
    )
print("\n")

if sentence_has_order:
    print("Zdanie ma rozkaz")
else:
    "KONIEC"
    exit()


assert isinstance(root, Token)


def get_all_children(token: Token) -> list[Token]:
    children = []
    for child in token.children:
        children.append(child)
        children.extend(get_all_children(child))
    return children


children = [root.children.__next__()] + get_all_children(root.children.__next__())


print(f"akcja: {root.text}, obiekt: {' '.join(child.text for child in children)}")
