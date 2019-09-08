from CQUPTPiper.piper import Piper

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
    def __init__(self, year: int, piper: Piper):
        self.year = year
        self.piper = piper
        """
        You can start coding like
            self.config = self.piper.config
            self.session = self.piper.session
        for your convenience.
        """

    def fmt_print(self): pass
