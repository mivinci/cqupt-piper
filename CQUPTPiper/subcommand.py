# Customized Argument Parser
from CQUPTPiper.error import Error


KEY_TYPE = 'type'
KEY_HELP = 'help'
KEY_ISFLAG = 'isflag'
KEY_ARGNAME = 'arg_name'
KEY_ALLOW_NOARGS = 'allow_noargs'

KEY_FLAGS = 'flags'
KEY_OPTION = 'option'
KEY_ARGUMENT = 'argument'

INDEX_SUBCOMMAND = 0
INDEX_OPTION = 1
INDEX_ARGUMENT = 2

ERRNO_NONE = 0
ERRNO_UNRECOGNIZED_SUBCOMMAND = 1
ERRNO_INVALID_OPTION = 2
ERRNO_INVALID_ARGUMENT = 3


def isquit(cmd: str) -> bool:
    return cmd == 'quit' or cmd == 'exit'

def ishelp(cmd: str) -> bool:
    return cmd == 'help' or cmd == '-h'

def isversion(cmd: str) -> bool:
    return cmd == 'version' or cmd == '-v'


def hasoption(subcommand: dict, argv: list) -> bool:
    return subcommand.get(argv[INDEX_SUBCOMMAND])


class OptionGroup:
    def __init__(self, subcommand: dict, group_name: str):
        self.name = group_name
        self.subcommand = subcommand

    def add_argument(self, 
                    name: str, 
                    short: str,
                    help: str,
                    type: type = str,
                    argname: str = None,
                    allownoargs: bool = True, 
                    isflag: bool = False):
        self.subcommand[self.name][name] = {
            KEY_ALLOW_NOARGS: allownoargs,
            KEY_ARGNAME: argname,
            KEY_ISFLAG: isflag,
            KEY_HELP: help,
            KEY_TYPE: type
        }
        self.subcommand[self.name][short] = self.subcommand[self.name][name]


class NameSpace(dict):
    def __init__(self, subcommand: dict, cmd: str):
        self.namespace = dict()
        self.subcommand = subcommand
        self.argv: [str] = cmd.strip().split(' ')
        self.argvlen = len(self.argv)

    def parse(self) -> (dict, Error):
        # I don't wanna write Golang-like code in Python
        # But it works goddamn we!!
        err = self.matches()
        if err:
            return None, err
        self.namespace[self.argv[INDEX_SUBCOMMAND]] = {
            KEY_OPTION: self.argv[INDEX_OPTION],
            KEY_ARGUMENT: self.argv[INDEX_ARGUMENT] if self.argvlen >= 3 else None,
            KEY_FLAGS: [*self.argv[3:]] if self.argvlen >= 3 else [*self.argv[2:]]
        }
        return self.namespace, None

    def matches(self) -> Error:
        if not self.command_isvalid():
            return Error.subcommand(self.argv[INDEX_SUBCOMMAND])
        elif not self.hasoption():
            return Error.noption()
        elif not self.option_isvalid():
            return Error.option(self.argv[INDEX_OPTION])
        elif not self.argument_isvalid():
            return Error.argument(self.argv[INDEX_ARGUMENT])
        else:
            return None

    def command_isvalid(self) -> bool:
        return self.argv[INDEX_SUBCOMMAND] in self.subcommand

    def hasoption(self) -> bool:
        return self.argvlen >= 2

    def option_isvalid(self) -> bool:
        return self.hasoption() and self.argv[INDEX_OPTION] in self.subcommand.get(self.argv[INDEX_SUBCOMMAND])

    def argument_isvalid(self) -> bool:
        option: dict = self.subcommand[self.argv[INDEX_SUBCOMMAND]][self.argv[INDEX_OPTION]]
        # Check if the option is a flag that cannot take argument
        if option[KEY_ISFLAG] and self.argvlen != 2:
            return False
        # Check if the option can take non-argument
        if not option[KEY_ALLOW_NOARGS] and self.argvlen != 3:
            return False
        # Check if the needed argument is int-typed
        # But fisrt you need to check if the option needs argument
        if self.argvlen == 3 and issubclass(option[KEY_TYPE], int):
            return self.argv[INDEX_ARGUMENT].isdigit()
        return True

    
class SubCommand:
    def __init__(self, description: str, version: str):
        self.description = description
        self.version = version
        self.commands = dict()

    def add_group(self, name: str, allownoargs: bool = False) -> OptionGroup:
        self.commands[name] = dict()
        return OptionGroup(self.commands, name)

    def parse(self, cmd: str) -> (NameSpace, Error):
        if cmd == 'help':
            self.print_help()
            return None, None
        if cmd == 'version':
            print(f"Piper SubCommand v{self.version}")
            return None, None
        if isquit(cmd):
            return None, None
        return NameSpace(self.commands, cmd).parse()

    def print_help(self):
        # print(self.description)
        print('Usage: command option <argument>\n')
        for kc, vc in self.commands.items():
            for ko, vo in vc.items():
                if ko[0] != '-':
                    print("    \033[1m%s %s\033[0m\t<%s>\t%s" %(kc, ko, vo[KEY_ARGNAME], vo['help']))
            print('\n示例: %s credit 2018' %kc)
