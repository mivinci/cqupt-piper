from CQUPTPiper.piper import Piper

"""
Target Url: 'http://jwzx.cqu.pt/student/zc.php' with id='AxfTjTable'
            also available at piper.urls.URL_FINANCE

Parameter: 'piper' contains attribute that may be needed:
    session: stores all the cookies given by the jwzx server-end
    config:  has the necessary system information and user information
             see at CQUPTPiper.config.Config
    urls:    has the necessary jwzx urls for crawling data

Method: 'fmt_print'
The crawler must have a 'fmt_print' method,
which prints result like
       学年   |    应缴   |   已交   | 未缴
    2017-2018 |  xxxx.xx | xxxx.xx | xxxx.xx
    2018-2019 |  xxxx.xx | xxxx.xx | xxxx.xx
       总计   |  xxxx.xx 

You DON'T have get the result formatted 100 percent like this.
"""
class FeeCrawler:
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
