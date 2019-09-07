from argparse import ArgumentParser
from CQUPTPiper import __version__


def get_parser() -> ArgumentParser:
    parser = ArgumentParser(description='CQUPT Piper')
    parser.add_argument('-v', '--version', action='version', version=__version__)
    return parser.parse_args()