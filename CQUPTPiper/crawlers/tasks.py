from CQUPTPiper.piper import Piper
from CQUPTPiper.subcommand import NameSpace

"""
Target Url: 'http://jwzx.cqu.pt/student/ksap.php'
            also available at piper.urls.URL_TASKS

Parameter: 'piper' contains attribute that may be needed:
    session: stores all the cookies given by the jwzx server-end
    config:  has the necessary system information and user information
             see at CQUPTPiper.config.Config
    urls:    has the necessary jwzx urls for crawling data

Method: 'fmt_print'
The crawler must have a 'fmt_print' method,
which prints result like
    课程名称 周次 星期 教室 座位号       具体时间        资格
     xxxx   xx   x   xx  xxx   第x-x节 xx:xx-xx:xx   有
     xxxx   xx   x   xx  xxx   第x-x节 xx:xx-xx:xx   无

You DON'T have get the result formatted 100 percent like this.
"""
class PhotoCrawler:
    def __init__(self, piper: Piper, namespace: NameSpace):
        """
        If user input 'get tasks 2018 -s -g'
        namespace will be assigned to a dict:
        {
            'get': {
                'option': 'tasks',
                'argument': '2018',
                'flags': ['-s', '-g'],
            }
        }
        """
        self.namespace = namespace
        self.piper = piper
        """
        You can start coding like
            self.config = self.piper.config
            self.session = self.piper.session
        for your convenience.
        """

    def fmt_print(self): pass