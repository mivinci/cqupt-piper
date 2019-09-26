from requests import post, ConnectionError
from cquptpiper.log import Log, loading
from cquptpiper.auth import Auth


URL_LOGIN_API = 'http://127.0.0.1:5000/login'


class Request:

    @staticmethod
    @loading('登录过期, 正在重新请求登录')
    def login(user: dict, cookie: dict):
        user.update(cookie)
        try:
            post(URL_LOGIN_API, data=user).text
        except ConnectionError:
            Log.fatal('服务器走丢啦~')
        except Exception:
            Auth.clear_config()


def network_required(target):
    def target_wrapper(*args, **kwargs):
        try:
            target()
        except ConnectionError:
            Log.fatal('网络走丢啦~')
    return target_wrapper