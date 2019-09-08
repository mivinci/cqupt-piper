class Proxy:
    URL_LOGIN = 'http://jwzx.cqu.pt/login.php'
    URL_CAPTCHA = 'http://jwzx.cqu.pt/createValidationCode.php'
    URL_CHECK_LOGIN = 'http://jwzx.cqu.pt/checkLogin.php'
    
    # 各类数据在 HTML 的标签id:
    # 原始成绩总表: id='cjAllTab-cjzb'
    # 排名和绩点:   id='cjAllTab-zypm'
    # 各类统考成绩: id='ui-id-5'
    URL_GPA = 'http://jwzx.cqu.pt/student/chengjiPm.php'

    # 各类数据在 HTML 的标签id:
    # 学分统计表: id='AxfTjTable'
    URL_CREDIT = 'http://jwzx.cqu.pt/student/xkxfTj.php'
    
    # 各类数据在 HTML 的标签id:
    # 学费: id='ui-id-3'
    URL_FINANCE = 'http://jwzx.cqu.pt/student/zc.php'

    # 考试安排
    URL_TASKS = 'http://jwzx.cqu.pt/student/ksap.php'

    # 学生照片
    URL_STUDENT_PHOTO = 'http://jwzx.cqu.pt/showstupic.php?xh={stu_id}'


class Internal:
    URL_LOGIN = 'http://jwzx.cqupt.edu.cn/login.php'
    URL_CAPTCHA = 'http://jwzx.cqupt.edu.cn/createValidationCode.php'
    URL_CHECK_LOGIN = 'http://jwzx.cqupt.edu.cn/checkLogin.php'
    URL_GPA = 'http://jwzx.cqupt.edu.cn/student/chengjiPm.php'
    URL_FINANCE = 'http://jwzx.cqu.pt/student/zc.php'
    URL_TASKS = 'http://jwzx.cqu.pt/student/ksap.php'
    URL_STUDENT_PHOTO = 'http://jwzx.cqupt.edu.cn/showstupic.php?xh={stu_id}'


class Url:

    def __new__(cls, proxy: bool = True, *args, **kwargs):
        return Proxy if proxy else Internal

