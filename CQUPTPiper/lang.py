from enum import Enum

class Language(Enum):
    EN = 'en'
    CH = 'ch'

    def __str__(self):
        return self.value

class EN:
    USERNAME = 'Username: '
    PASSWORD = 'Password: '

    ENTER_CAPTCHA = 'Enter captcha: '
    LOGIN_FAILED = 'Login Failed'
    LOGIN_SUCCESSFULLY = 'Login Successfully!'
    RETRYING = 'Retrying ...'

    RECOGNIZING_CAPTCHA = 'Recognizing captcha'

    BEFORE_AUTHORIZATION = 'To start using Piper, we need to know who you are for security.'
    AUTHORIZATION_FAILED = 'Wrong password!'

    SUBCOMMAND_INSTRUCTION = 'You can run "help" to view available commands.'
    EXIT = 'Exit'


class CH:
    USERNAME = '学号: '
    PASSWORD = '密码: '

    ENTER_CAPTCHA = '验证码: '
    LOGIN_FAILED = '登录失败'
    LOGIN_SUCCESSFULLY = '登录成功!'
    RETRYING = '重试 ...'

    RECOGNIZING_CAPTCHA = '正在识别验证码'

    BEFORE_AUTHORIZATION = '第一次使用需验证您的身份.'
    AUTHORIZATION_FAILED = '密码错误!'

    SUBCOMMAND_INSTRUCTION = '输入 help 查看可执行指令'
    EXIT = '已退出'
   