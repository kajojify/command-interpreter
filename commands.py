import sys


def command_command():
    pass


class CommandsManager:
    def __init__(self, module=None):
        self.module = module or sys.modules[__name__]

    def call(self, cname: str, *args) -> None:
        fname = self.get_fname(cname)
        command = getattr(self.module, fname, None)
        if command is not None and command.__name__ != self.__class__.__name__:
            command(*args)
        else:
            print(f"Wrong command name {cname}")

    @staticmethod
    def get_fname(cname: str) -> str:
        fname = cname.replace("_", "__").replace(".", "_")
        return fname
