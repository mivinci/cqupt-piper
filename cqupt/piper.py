from cqupt import __version__, __description__
from cqupt.log import Log
from cqupt.auth import Auth
from cqupt.urls import URL_LOGIN
from cqupt.error import Catch
from cqupt.request import Request
from cqupt.crawlers import Crawler
from argparse import ArgumentParser, SUPPRESS
from requests import Session, ConnectionError
from sys import argv


class Piper:
    def __init__(self):
        Auth.init()
        self.session: Session = Session()
        self.user: dict = Auth.load_user()
        self.cookie: dict = Auth.read_cookie()

    def authorize(self):
        if not self.user:
            self.user = Auth.add_user()

        if self.cookie is None:
            try:
                self.session.get(URL_LOGIN)
            except ConnectionError:
                Log.fatal('网络走丢啦~')
            
            self.cookie = self.session.cookies.get_dict()
            Auth.save_cookie(self.cookie)
            Request.handle_login(Request.login(self.user, self.cookie))
        else:
            self.session.cookies.update(self.cookie)

    def handle_args(self, args):
        if args.drop:
            self.drop()
        if args.clear:
            self.clear()
        if args.whoami:
            self.show_config()
        if args.auth:
            Auth.update_user('确定要更改绑定吗?')

    def clear(self):
        Auth.clear_cookie()
        Log.fatal('已清除缓存')

    def drop(self):
        Auth.drop_config()
        Log.fatal('已删除配置')

    def show_config(self):
        config: dict = Auth.load_config()
        if config.get('user'):
            print('学号:', config.get('user').get('userid'))
            print('密码:', config.get('user').get('password'))
        exit(0)


def construct_args():
    parser = ArgumentParser(prog='cqupt', description=__description__, )
    parser.add_argument('-v', '--version', action='version', version=__version__)
    
    group_internal = parser.add_argument_group('设置')
    group_internal.add_argument('--auth', action='store_true', help='绑定学号')
    group_internal.add_argument('--drop', action='store_true', help='删除配置')
    group_internal.add_argument('--clear', action='store_true', help='清除缓存')
    group_internal.add_argument('--whoami', action='store_true', help='显示配置')

    group_crawler = parser.add_argument_group('教务在线查询')
    group_crawler.add_argument('--fee', metavar='学年', type=int, const=-1, nargs='?', help='获取学年学费')
    group_crawler.add_argument('--gpa', metavar='学年', type=int, const=-1, nargs='?', help='获取学年绩点')
    group_crawler.add_argument('--credit', metavar='学年', type=int, const=-1, nargs='?', help='获取学年学分')
    group_crawler.add_argument('--photo', metavar='学号', type=str, const='self', nargs='?', help='获取学生照片')
    group_crawler.add_argument('--task', action='store_true', help='获取考试安排')
    group_crawler.set_defaults(handle=Crawler().handle)

    return parser.parse_args()


@Catch.all
@Catch.keyboard_interrupt
def cli():
    if len(argv) <= 1:
        exit(0)

    piper = Piper()

    args = construct_args()
    # print(args)

    piper.handle_args(args)
   
    piper.authorize()

    if hasattr(args, 'handle'):
        args.handle(piper, args)
    else:
        print('help')
    