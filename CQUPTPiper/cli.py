from argparse import ArgumentParser
from CQUPTPiper import __version__


def ArgParser() -> ArgumentParser:
    parser = ArgumentParser(description='CQUPT Piper')
    parser.add_argument('-v', '--version', action='version', version=__version__)
    parser.add_argument('-m', '--manual', action='store_true', help='manually input captcha at login')
    return parser.parse_args()