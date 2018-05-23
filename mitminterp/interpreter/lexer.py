import re

import ply.lex as lex


tokens = (
    "PLAIN_STR", "QUOTED_STR", "PIPE",
    "COMMAND", "RPAREN", "LPAREN", "RBRACE",
    "LBRACE"
)


special_symbol = re.escape("!@#$%^&*+{}:<>?,;/=-~")
plain_str = r"[\w{}]+".format(special_symbol)

t_PIPE = r"\|"
t_QUOTED_STR = r"\"[\w{0}\s]*\"|\'[\w{0}\s]*\'".format(special_symbol)
t_RPAREN = r"\)"
t_LBRACE = r"\["
t_RBRACE = r"\]"
t_LPAREN = r"\("

t_ignore = " \f\n\r\t\v"

def t_COMMAND(t):
    r"""[&\*]?\w+(\.\w+)+|\.\w+(\.\w+)*"""
    return t


@lex.TOKEN(plain_str)
def t_PLAIN_STR(t):
    return t


def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)


def get_lexer(line: str):
    lexer = lex.lex()
    lexer.input(line)
    return lexer
