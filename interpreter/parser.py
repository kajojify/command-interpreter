import ply.yacc as yacc


def parse(lexer):
    parser = yacc.yacc()
    parser.parse(lexer=lexer)
    return parser
