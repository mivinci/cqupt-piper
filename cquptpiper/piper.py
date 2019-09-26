from cquptpiper import __version__, __description__
from cquptpiper.log import Log
from cquptpiper.auth import Auth
from cquptpiper.urls import URL_LOGIN
from cquptpiper.request import request_login
from cquptpiper.crawler import Crawler
from argparse import ArgumentParser
from requests import Session


class Piper:
    def __init__(self):
        Auth.init()
        self.session: Session = Session()
        self.user: dict = Auth.load_user()
        self.cookie: dict = Auth.read_cookie()

    def authorize(self):
        if not self.user:
            self.user = Auth.enter_user()

        if self.cookie is None:
            self.session.get(URL_LOGIN)
            self.cookie = self.session.cookies.get_dict()
            Auth.save_cookie(self.cookie)
            request_login(self.user, self.cookie)
        else:
            self.session.cookies.update(self.cookie)

    def drop(self):
        Auth.drop_config()
        Log.fatal('已删除配置')


def construct_args():
    parser = ArgumentParser(prog='cqupt', description=__description__)
    parser.add_argument('-v', '--version', action='version', version=__version__)
    
    group_internal = parser.add_argument_group('内置功能')
    group_internal.add_argument('--drop', action='store_true', help='删除配置')

    group_crawler = parser.add_argument_group('从教务在线获取信息')
    group_crawler.add_argument('--fee', metavar='   学年', type=int, help='获取学年学费')
    group_crawler.add_argument('--gpa', metavar='   学年', type=int, help='获取学年绩点')
    group_crawler.add_argument('--credit', metavar='学年', type=int, help='获取学年学分')
    group_crawler.add_argument('--photo', metavar=' 学号', type=str, help='获取学生照片')
    group_crawler.add_argument('--task', action='store_true', help='获取考试安排')
    group_crawler.set_defaults(handle=Crawler().handle)

    return parser.parse_args()


def cli():
    piper = Piper()

    args = construct_args()
    print(args)

    if args.drop:
        piper.drop()

    piper.authorize()

    if hasattr(args, 'handle'):
        args.handle(piper, args)
    else:
        print('help')
    