from cquptpiper import __version__
from argparse import ArgumentParser


def construct_args():
    parser = ArgumentParser(prog='cqupt')
    parser.add_argument('-v', '--version', action='version', version=__version__)
    group = parser.add_argument_group('从教务在线获取信息')
    group.add_argument('--fee', metavar='   学年', type=int, help='获取学年学费')
    group.add_argument('--gpa', metavar='   学年', type=int, help='获取学年绩点')
    group.add_argument('--credit', metavar='学年', type=int, help='获取学年学分')
    group.add_argument('--photo', metavar=' 学号', type=str, help='获取学生照片')
    group.add_argument('--task', action='store_true', help='获取考试安排')
    return parser.parse_args()

def cli():
    args = construct_args()    

    print(args)