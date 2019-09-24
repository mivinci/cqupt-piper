from enum import Enum
from os import path
from CQUPTPiper import PIPER_PATH
from CQUPTPiper.auth import readconfig, KEY_LANG, VALUE_LANG_ENGLISH


class Language(Enum):
    EN = 'en'
    CH = 'ch'

    def __str__(self):
        return self.value

class EN:
    USERNAME = 'Username: '
    PASSWORD = 'Password: '

    LOGIN = 'Sign in ...'
    ENTER_CAPTCHA = 'Enter captcha: '
    LOGIN_FAILED = 'Login Failed'
    LOGIN_SUCCESSFULLY = '\nLogin Successfully!'
    RETRYING = 'Retrying ...'

    RECOGNIZING_CAPTCHA = 'Recognizing captcha'

    BEFORE_AUTHORIZATION = 'To start using Piper, we need to know who you are for security.'
    AUTHORIZATION_FAILED = 'Wrong password!'

    SUBCOMMAND_INSTRUCTION = "You can run 'help' to view available commands."
    EXIT = 'Exit'

    ERROR_UNRECOGNIZED_SUBCOMMAND = 'Unrecognized command'
    ERROR_INVALID_OPTION = 'Invalid option'
    ERROR_INVALID_ARGUMENT = 'Invalid argument'
    ERROR_NO_OPTION = 'Option is required'

    ERROR_NO_NETWORK_CONNECTION = 'No network connection.'
    ERROR_CONNECTION_TIMEOUT = ''


class CH:
    USERNAME = '学号: '
    PASSWORD = '密码: '

    LOGIN = '正在登录 ...'
    ENTER_CAPTCHA = '验证码: '
    LOGIN_FAILED = '登录失败'
    LOGIN_SUCCESSFULLY = '\n登录成功!'
    RETRYING = '重试 ...'

    RECOGNIZING_CAPTCHA = '正在识别验证码'

    BEFORE_AUTHORIZATION = '第一次使用需验证您的身份.'
    AUTHORIZATION_FAILED = '密码错误!'

    SUBCOMMAND_INSTRUCTION = '输入 help 查看可执行命令'
    EXIT = '已退出'

    ERROR_UNRECOGNIZED_SUBCOMMAND = '错误命令'
    ERROR_INVALID_OPTION = '无效选项'
    ERROR_INVALID_ARGUMENT = '无效参数'
    ERROR_NO_OPTION = '需要输入选项'

    ERROR_NO_NETWORK_CONNECTION = '检查您的网络连接.'



if path.isfile(PIPER_PATH):
    Lang: str = readconfig(PIPER_PATH).get(KEY_LANG)
else:
    Lang: str = VALUE_LANG_ENGLISH

Instruction: CH or EN = EN if Lang == VALUE_LANG_ENGLISH else CH
