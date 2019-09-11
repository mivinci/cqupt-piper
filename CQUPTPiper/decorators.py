from CQUPTPiper import PIPER_PATH
from CQUPTPiper.auth import readconfig, KEY_STUID, KEY_PASS, KEY_LANG, VALUE_LANG_ENGLISH
from CQUPTPiper.lang import EN, CH
from CQUPTPiper.log import Log

from getpass import getpass


def authorize(func):
    def func_wrapper(*args, **kwargs):
        config: dict = readconfig(PIPER_PATH)
        instruction = EN if config.get(KEY_LANG) == VALUE_LANG_ENGLISH else CH
        try:
            if not config.get(KEY_PASS) == getpass(prompt=instruction.PASSWORD):
                Log.fatal(instruction.AUTHORIZATION_FAILED)
        except KeyboardInterrupt:
            print('\nBye!')
    return func_wrapper


class Crawler:

    @staticmethod
    def spy(func):
        def func_wrapper(self):
            func(self)
            # print(self.namespace)
            # print(self.piper.config.user)
            # print(func.__name__)
        return func_wrapper