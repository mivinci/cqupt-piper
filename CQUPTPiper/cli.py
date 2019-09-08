from sys import argv
from argparse import ArgumentParser
from CQUPTPiper import __version__


def arg_parser() -> ArgumentParser:
    parser = ArgumentParser(description='CQUPT Piper')
    parser.add_argument('-v', '--version', action='version', version=f'v{__version__}')
    parser.add_argument('-m', '--manual', action='store_true', help='manually input captcha at login')
    return parser.parse_args()


def noargs():
    return len(argv) == 1


def isquit(cmd: str) -> bool:
    return cmd == 'quit' or cmd == 'exit'
