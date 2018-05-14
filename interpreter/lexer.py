import re

import ply.lex as lex


tokens = (
    "PLAIN_STR", "QUOTED_STR", "PIPE",
    "COMMAND", "RPAREN", "LPAREN", "RBRACE",
    "LBRACE", "WHITESPACE"
)

special_symbol = re.escape("!@#$%^&*()+{}:<>?.,;/][=-~")
PLAIN_STR = r"[\w{}]+".format(special_symbol)

t_WHITESPACE = r"\s+"
t_PIPE = r"\|"
t_QUOTED_STR = r"\"[\w{0}\s]*\"|\'[\w{0}\s]*\'".format(special_symbol)


def t_RPAREN(t):
    r"\)"
    return t


def t_RBRACE(t):
    r"\]"
    return t


def t_LPAREN(t):
    r"\("
    return t


def t_LBRACE(t):
    r"\["
    return t


def t_COMMAND(t):
    r"[&\*]?\w+(\.\w+)+"
    return t


@lex.TOKEN(PLAIN_STR)
def t_PLAIN_STR(t):
    return t


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


def get_lexer(line: str):
    lexer = lex.lex()
    lexer.input(line)
    return lexer
