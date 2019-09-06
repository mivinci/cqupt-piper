class Proxy:
    URL_LOGIN = 'http://jwzx.cqu.pt/login.php'
    URL_CAPTCHA = 'http://jwzx.cqu.pt/createValidationCode.php'
    URL_CHECK_LOGIN = 'http://jwzx.cqu.pt/checkLogin.php'

    URL_RANKS = 'http://jwzx.cqu.pt/student/chengjiPm.php'
    URL_STUDENT_PHOTO = 'http://jwzx.cqu.pt/showstupic.php?xh={stu_id}'


class Internal:
    URL_LOGIN = 'http://jwzx.cqupt.edu.cn/login.php'
    URL_CAPTCHA = 'http://jwzx.cqupt.edu.cn/createValidationCode.php'
    URL_CHECK_LOGIN = 'http://jwzx.cqupt.edu.cn/checkLogin.php'

    URL_RANKS = 'http://jwzx.cqupt.edu.cn/student/chengjiPm.php'
    URL_STUDENT_PHOTO = 'http://jwzx.cqupt.edu.cn/showstupic.php?xh={stu_id}'


class Url:

    def __new__(cls, proxy: bool = True, *args, **kwargs):
        return Proxy if proxy else Internal

