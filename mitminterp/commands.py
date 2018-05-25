import sys
import typing

# Commands examples
# underscore(_) means dot(.)
# double underscore(__) means single underscore(_)

# In order to write command like myaddon.command,
# just define function myaddon_command.


def _version(*args):
    return sys.version_info


def a_sum(arg=None) -> int:
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

    def call(self, cname: str, *args):
        fname = self.get_fname(cname)
        command = getattr(self._module, fname, None)
        if command is not None and command.__name__ != self.__class__.__name__:
            try:
                cvalue = command(*args)
            except Exception as e:
                print(e)
            else:
                return cvalue
        else:
            print(f"Wrong command name {cname}")

    @staticmethod
    def get_fname(cname: str) -> str:
        fname = cname.replace("_", "__").replace(".", "_")
        return fname
