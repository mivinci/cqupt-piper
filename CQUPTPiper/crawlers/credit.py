from CQUPTPiper.piper import Piper
from CQUPTPiper.subcommand import NameSpace

"""
Target Url: 'http://jwzx.cqu.pt/student/xkxfTj.php' with id='AxfTjTable'
            also available at piper.urls.URL_CREDIT

Parameter: 'piper' contains attribute that may be needed:
    session: stores all the cookies given by the jwzx server-end
    config:  has the necessary system information and user information
             see at CQUPTPiper.config.Config
    urls:    has the necessary jwzx urls for crawling data

Method: 'fmt_print'
The crawler must have a 'fmt_print' method,
which prints result like

If year specified:
    学年   | 学分 | 二专业学分 |      统计时间
    20181 | 0.0 |    0.0    | xxxx-xx-xx xx:xx:xx
    20182 | 0.0 |    0.0    | xxxx-xx-xx xx:xx:xx
    总计  | 0.0
If year not specified:
    学年  | 学分 | 二专业学分 | 统计时间
    20181 | 0.0 |    0.0    | xxxx-xx-xx xx:xx:xx
    20182 | 0.0 |    0.0    | xxxx-xx-xx xx:xx:xx
    20191 | 0.0 |    0.0    | xxxx-xx-xx xx:xx:xx
    总计  | 0.0
    还需  | 0.0

You DON'T have get the result formatted 100 percent like this.
"""
class CreditCrawler:
    def __init__(self, namespace: NameSpace, piper: Piper):
        """
        If user input 'get credit 2018 -s -g'
        namespace will be assigned to a dict:
        {
            'get': {
                'option': 'credit',
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
