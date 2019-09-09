from sys import argv
from argparse import ArgumentParser
from CQUPTPiper.lang import Language
from CQUPTPiper.subcommand import SubCommand
from CQUPTPiper import __version__, __description__


def arg_parser() -> ArgumentParser:
    parser = ArgumentParser(description=__description__)
    parser.add_argument('-v', '--version', action='version', version=f'v{__version__}')
    parser.add_argument('-m', '--manual', action='store_true', help='input captcha manually at login')
    parser.add_argument('-l', type=Language, choices=list(Language), help='switch language')
    return parser.parse_args()


def noargs() -> bool:
    return len(argv) == 1



__version__ = '0.0.1'
__author__ = 'XJJ, LCM'
__date__ = '2019.9'
__description__ = f'Crawler v{__version__} @{__author__} {__date__}'

def subcommand_parser():
    subcmd = SubCommand(__description__, __version__)
    group = subcmd.add_group("get")
    group.add_argument("photo", "-p", "获取照片", argname='学号', type=int)
    group.add_argument("credit", "-c", "获取学分", argname='年份', type=int)
    group.add_argument("fee", "-c", "获取学费", argname='年份', type=int)
    group.add_argument("gpa", "-c", "获取绩点和排名", argname='年份', type=int)
    group.add_argument("tasks", "-c", "获取考试安排", argname='年份', type=int)
    return subcmd
