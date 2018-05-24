import ply.yacc as yacc

import mitminterp.interpreter.lexer as lx
from mitminterp import commands


class CommandsLanguageParser:
    tokens = lx.tokens

    def __init__(self, **kwargs):
        self._pipe_value = None
        self.parser = yacc.yacc(module=self, **kwargs)

    def parse(self, lexer):
        self.parser.parse(lexer=lexer)

    def p_command_line(self, p):
        """command_line : empty
                        | expression pipes"""
        if len(p) == 3:
            print(self._pipe_value)
        else:
            print()

    def p_expr_command(self, p):
        """expression : PLAIN_STR
                      | QUOTED_STR
                      | array
                      | command_call"""
        p[0] = p[1]
        self._pipe_value = p[0]

    def p_pipes(self, p):
        """pipes : pipe_expression pipes
           pipes : pipe_expression"""
        if len(p) == 2:
            p[0] = [p[1]]
        else:
            p[0] = [p[1]]
            p[0].append(p[2])

    def p_pipe(self, p):
        """pipe_expression : empty
                           | PIPE command_call"""
        if len(p) == 3:
            p[0] = p[2]
            self._pipe_value = p[0]

    def p_command_call(self, p):
        """command_call : command_call_no_parentheses
                        | command_call_with_parentheses"""
        p[0] = p[1]

    def p_array(self, p):
        """array : LBRACE argument_list RBRACE"""
        p[0] = p[2]

    def p_command_call_no_parentheses(self, p):
        """command_call_no_parentheses : COMMAND argument_list"""
        cm = commands.CommandsManager()
        if self._pipe_value is None:
            p[0] = cm.call(p[1], p[2])
        else:
            first_argument = self._pipe_value
            self._pipe_value = None
            args = [first_argument, *p[2]]
            p[0] = cm.call(p[1], args)

    def p_argument_list(self, p):
        """argument_list : empty
                         | argument_sequence"""
        p[0] = [] if p[1] is None else p[1]

    def p_argument_sequence(self, p):
        """argument_sequence : argument_sequence argument
           argument_sequence : argument"""
        if len(p) == 2:
            if isinstance(p[1], list):
                p[0] = p[1]
            else:
                p[0] = [p[1]]
        else:
            p[0] = p[1]
            p[0].append(p[2])

    def p_argument(self, p):
        """argument : PLAIN_STR
                    | QUOTED_STR
                    | array
                    | command_call_with_parentheses"""
        p[0] = p[1]

    def p_command_call_with_parentheses(self, p):
        """command_call_with_parentheses : COMMAND LPAREN argument_list RPAREN"""
        cm = commands.CommandsManager()
        if self._pipe_value is None:
            p[0] = cm.call(p[1], p[3])
        else:
            first_argument = self._pipe_value
            self._pipe_value = None
            args = [first_argument, *p[3]]
            p[0] = cm.call(p[1], args)


    def p_empty(self, p):
        """empty :"""

    def p_error(self, p):
        if p is None:
            print("Syntax error. p == None!")
        else:
            print(f"Syntax error at '{p.value}'")


def parse(lexer):
    parser = CommandsLanguageParser(debug=False, write_tables=False)
    parser.parse(lexer=lexer)
