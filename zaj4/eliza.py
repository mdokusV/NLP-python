# Import lexer and parser from ply module
import ply.lex as lex
import ply.yacc as yacc

# List of token types.
tokens = ("NUMBER", "OPERATE", "SIZE", "KIND", "COLOR", "MATERIAL")


# Token types may be defined as regular expressions, e.g. r'Buy | Sell'
def t_OPERATE(t):
    r"Buy | Sell"
    return t


def t_MATERIAL(t):
    r"metal | plastic"
    if t.value == "metal":
        t.value = 1
    elif t.value == "plastic":
        t.value = 2
    return t


def t_COLOR(t):
    r"(black | white | red | green | blue)"
    if t.value == "black":
        t.value = 1
    elif t.value == "white":
        t.value = 2
    elif t.value == "red":
        t.value = 3
    elif t.value == "green":
        t.value = 4
    elif t.value == "blue":
        t.value = 5
    return t


def t_SIZE(t):
    r"tiny | small | big | large"
    if t.value == "tiny":
        t.value = 1
    elif t.value == "small":
        t.value = 2
    elif t.value == "big":
        t.value = 3
    elif t.value == "large":
        t.value = 4
    return t


def t_KIND(t):
    r"box(es)? | ring(s)?"
    if t.value[0] == "b":
        t.value = 1
    else:
        t.value = 2
    return t


def t_NUMBER(t):
    r"\d+"
    t.value = int(t.value)
    return t


# Lexer error handling rule (Handle words out of vocabulary)
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


# Ignore white spaces
t_ignore = " \t"


# Main parser rule (command)
def p_command(p):
    "command : OPERATE NUMBER article"
    index = p[3]
    # Buy article
    if p[1] == "Buy":
        tab[index] += p[2]
        print(
            "OK. I am buying "
            + str(p[2])
            + " new articles indexed as "
            + str(index)
            + "."
        )
        print("No of articles in shop: " + str(tab[index]))
    # Sell article
    elif p[1] == "Sell":
        if p[2] > tab[index]:
            print("I do not have as many articles as you want.")
    else:
        tab[index] -= p[2]
    print("OK. I am selling " + str(p[2]) + " articles indexed as " + str(index) + ".")
    print("No of articles in shop: " + str(tab[index]))


# Parser rule (attribute)
def p_attribute_color(p):
    "attribute : COLOR"
    p[0] = p[1]


# Parser rule (attribute)
def p_attribute_material(p):
    "attribute : MATERIAL"
    p[0] = 10 * p[1]


# Parser rule (attribute)
def p_attribute_size(p):
    "attribute : SIZE"
    p[0] = 100 * p[1]


# Parser rule (article - stop)
def p_article_kind(p):
    "article : KIND"
    p[0] = 1000 * p[1]


# Parser rule (article - recursion)
def p_article_attribute(p):
    "article : attribute article"
    p[0] = p[1] + p[2]


# Syntax error handling rule
def p_error(p):
    print("Syntax error in input!")


#######################################
# Main program

# Initialize table of articles (zero articles at the beginning)
tab = []
for index in range(3000):
    tab.append(0)

# Build the lexer
lexer = lex.lex()

# Tokenize (short version)
# for tok in lexer:
#    print(tok)

# Build the parser
parser = yacc.yacc()

# Main loop
while True:
    s = input("What can I do for you? \n")
    if s == "Bye":
        break
    parser.parse(s)
