from cquptpiper import __version__
from cquptpiper.auth import Auth
from cquptpiper.urls import URL_LOGIN
from cquptpiper.crawler import Crawler
from argparse import ArgumentParser
from requests import Session


class Piper:
    def __init__(self):
        Auth.init()
        self.session: Session = Session()

    def authorize(self):
        user: dict = Auth.load_user()
        cookie: dict = Auth.read_cookie()

        if not user:
            user = Auth.enter_user()

        # print(cookie)
        if cookie is None:
            self.session.get(URL_LOGIN)
            Auth.save_cookie(self.session.cookies.get_dict())
        else:
            self.session.cookies.setdefault(cookie)
        # request the server for captcha recognition

    def drop(self):
        Auth.drop_config()


def construct_args(piper):
    parser = ArgumentParser(prog='cqupt')
    parser.add_argument('-v', '--version', action='version', version=__version__)
    
    group_internal = parser.add_argument_group('内置功能')
    group_internal.add_argument('--drop', action='store_true', help='重新启动')

    group_crawler = parser.add_argument_group('从教务在线获取信息')
    group_crawler.add_argument('--fee', metavar='   学年', type=int, help='获取学年学费')
    group_crawler.add_argument('--gpa', metavar='   学年', type=int, help='获取学年绩点')
    group_crawler.add_argument('--credit', metavar='学年', type=int, help='获取学年学分')
    group_crawler.add_argument('--photo', metavar=' 学号', type=str, help='获取学生照片')
    group_crawler.add_argument('--task', action='store_true', help='获取考试安排')
    group_crawler.set_defaults(handle=Crawler(piper).handle)

    return parser.parse_args()


def cli():
    piper = Piper()
    piper.authorize()
    args = construct_args(piper)

    if args.drop:
        piper.drop()

    if hasattr(args, 'handle'):
        args.handle(args)
    else:
        print('help')
    