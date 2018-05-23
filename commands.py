import sys


def _version(*args):
    return sys.version_info


def a_sum(arg=None):
    arg = arg or []
    new_args = []
    for a in arg:
        if isinstance(a, list):
            new_args.extend(a)
        else:
            new_args.append(a)
    return sum(int(i) for i in new_args)


class CommandsManager:
    def __init__(self, module=None):
        self._module = module or sys.modules[__name__]

    def call(self, cname: str, *args) -> None:
        fname = self.get_fname(cname)
        command = getattr(self._module, fname, None)
        if command is not None and command.__name__ != self.__class__.__name__:
            return command(*args)
        else:
            print(f"Wrong command name {cname}")

    @staticmethod
    def get_fname(cname: str) -> str:
        fname = cname.replace("_", "__").replace(".", "_")
        return fname
