from CQUPTPiper import PIPER_PATH
from CQUPTPiper.auth import readconfig, KEY_STUID, KEY_PASS
from CQUPTPiper.lang import EN
from CQUPTPiper.log import Log

from getpass import getpass


def authorize(func):
    def func_wrapper(*args, **kwargs):
        config: dict = readconfig(PIPER_PATH)
        if not config.get(KEY_PASS) == getpass(prompt=EN.PASSWORD):
            Log.fatal('Authorization failed!')
    return func_wrapper