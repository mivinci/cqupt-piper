from requests import post, ConnectionError
from cquptpiper.log import Log


URL_LOGIN_API = 'http://127.0.0.1:5000/login'


def request_login(user: dict, cookie: dict):
    print(user, cookie)
    user.update(cookie)
    try:
        post(URL_LOGIN_API, data=user).text
    except ConnectionError:
        Log.fatal('服务器走丢啦~')


class Request:

    @staticmethod
    def login(target):
        def target_wrapper(self):
            target(self)
            if self.user and self.cookie:
                print('登录过期, 正在重新请求登录')
                request_login(self.user, self.cookie)
        return target_wrapper