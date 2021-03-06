from mitminterp.interpreter import parser
from mitminterp.interpreter.lexer import get_lexer


class CommandsExecutor:
    def __init__(self, path=None, command=None, quiet=False, tranquil=False):
        self.path = path
        self.onecommand = command
        self.quiet = quiet
        self.tranquil = tranquil

    def run(self):
        if self.path:
            self.execute_from_file()
        else:
            if self.onecommand is None:
                self.execute_runtime()
            else:
                self.execute(self.onecommand)

    def execute(self, line):
        commands_lexer = get_lexer(line)
        if not self.quiet:
            self.output_tokens_list(commands_lexer)
        if not self.tranquil:
            parser.parse(commands_lexer)

    def execute_from_file(self):
        try:
            with open(self.path) as file:
                for line in file:
                    print(line, end="")
                    self.execute(line)
                    print("=================")
        except IOError as e:
            print(e)

    def execute_runtime(self):
        while True:
            command = input(">>> ").strip()
            self.execute(command)

    @staticmethod
    def output_tokens_list(lexer):
        for token in lexer:
            print(token)
        print()
        lexer.lexpos = 0
