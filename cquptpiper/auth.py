from cquptpiper import PIPER_HOME
from cquptpiper.fs import b64_fwrite, b64_fread
from time import time
from getpass import getpass
from os import mkdir, path
from shutil import rmtree

PATH_PIPER_COOKIE = f'{PIPER_HOME}/cookie'
PATH_PIPER_USER = f'{PIPER_HOME}/user'

MAX_COOKIE_LIVE = 60 * 15

class Auth:
    @classmethod
    def init(cls):
        if not path.isdir(PIPER_HOME):
            mkdir(PIPER_HOME)
        if not path.isfile(PATH_PIPER_COOKIE):
            b64_fwrite(PATH_PIPER_COOKIE, None)
        if not path.isfile(PATH_PIPER_USER):
            b64_fwrite(PATH_PIPER_USER, None)

    @classmethod
    def drop_config(cls):
        rmtree(PIPER_HOME)

    @classmethod
    def read_cookie(cls) -> dict or None:
        cookie: dict = eval(b64_fread(PATH_PIPER_COOKIE))        
        if cookie and int(time()) - cookie.get('ts') < MAX_COOKIE_LIVE:
            return cookie.get('cookie')
        return None

    @classmethod
    def save_cookie(cls, cookie: dict):
        b64_fwrite(PATH_PIPER_COOKIE, {
            'cookie': cookie,
            'ts': int(time())
        })

    @classmethod
    def load_user(cls) -> dict or None:
        user: dict = eval(b64_fread(PATH_PIPER_USER))
        return user

    @classmethod
    def save_user(cls, user: dict):
        b64_fwrite(PATH_PIPER_USER, user)

    @classmethod
    def enter_user(cls):
        print('为确保本人操作, 第一次登录需输入学号密码')
        user: dict = {}
        user['userid'] = input('学号: ')
        user['password'] = getpass(prompt='密码: ')
        cls.save_user(user)
        return user