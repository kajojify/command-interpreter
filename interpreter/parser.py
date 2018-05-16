import ply.yacc as yacc

import interpreter.lexer

tokens = interpreter.lexer.tokens


def p_command_line(p):
    """command_line : expression pipes"""
    print(p[1], p[2])


def p_expr_command(p):
    """expression : empty
                  | PLAIN_STR
                  | QUOTED_STR
                  | array
                  | command_call_no_parentheses"""
    p[0] = p[1]


def p_pipes(p):
    """pipes : empty
             | pipe_expression pipes"""
    p[0] = p[1:]


def p_pipe(p):
    """pipe_expression : WHITESPACE PIPE WHITESPACE command_call_no_parentheses"""
    p[0] = p[1:]


def p_array(p):
    """array : LBRACE argument_list RBRACE"""
    p[0] = [p[2]]


def p_command_call_no_parentheses(p):
    """command_call_no_parentheses : COMMAND e_or_ws argument_list"""
    p[0] = p[1:]


def p_argument_list(p):
    """argument_list : argument_expression"""
    p[0] = p[1:]


def p_argument_expression(p):
    """argument_expression : empty
                           | argument argument_sequence"""
    p[0] = p[1:]


def p_argument_sequence(p):
    """argument_sequence : empty
                         | WHITESPACE argument argument_sequence"""
    p[0] = p[1:]


def p_argument(p):
    """argument : PLAIN_STR
                | QUOTED_STR
                | array
                | command_call_with_parentheses"""
    p[0] = p[1]



def p_command_call_with_parentheses(p):
    """command_call_with_parentheses : COMMAND LPAREN argument_list RPAREN"""
    p[0] = p[1:]


def p_optional_whitespace(p):
    """e_or_ws : empty
               | WHITESPACE"""
    p[0] = "empty or whitespace"


def p_empty(p):
    """empty :"""


def p_error(p):
    print("Syntax error at '%s'" % p.value)


def parse(lexer):
    parser = yacc.yacc()
    parser.parse(lexer=lexer)

# command_line = ( plain_str | quoted_str | array | command_call_no_parentheses ), { pipe } ;
#
# pipe = whitespaces, "|", whitespaces, command_call_no_parentheses ;
#
# command_call_with_parentheses = command, { ws }, "(", arguments_list, ")", { ws } ;
# command_call_no_parentheses = command, whitespaces, arguments_list ;
#
# arguments_list = { ws }, [ argument, { whitespaces, argument }, { ws } ] ;
# array = "[", arguments_list, "]" ;
# argument = plain_str | quoted_str | array | command_call_with_parentheses ;