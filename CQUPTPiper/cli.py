from sys import argv
from argparse import ArgumentParser
from CQUPTPiper.lang import Language
from CQUPTPiper import __version__


def arg_parser() -> ArgumentParser:
    parser = ArgumentParser(description='CQUPT Piper')
    parser.add_argument('-v', '--version', action='version', version=f'v{__version__}')
    parser.add_argument('-m', '--manual', action='store_true', help='input captcha manually at login')
    parser.add_argument('-l', type=Language, choices=list(Language), help='change language')
    return parser.parse_args()


def noargs():
    return len(argv) == 1


def isquit(cmd: str) -> bool:
    return cmd == 'quit' or cmd == 'exit'


class Argument:
    name: str


class SubCommand:
    def __init__(self):
        self.name: str = None
