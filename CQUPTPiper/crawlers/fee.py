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
from CQUPTPiper.subcommand import NameSpace
from CQUPTPiper.decorators import Crawler
from prettytable import PrettyTable
from bs4 import BeautifulSoup

class FeeCrawler:
    def __init__(self, piper, namespace: NameSpace):
        """
        If user input 'get fee 2018 -s -g'
        namespace will be assigned to a dict:
        {
            'get': {
                'option': 'fee',
                'argument': '2018',
                'flags': ['-s', '-g'],
            }
        }
        """
        self.piper = piper
        self.namespace = namespace
        self.year = namespace.get('argument') 
        self.url = self.piper.urls.URL_FINANCE
        self.fee = dict()
        """
        You can start coding like
            self.config = self.piper.config
            self.session = self.piper.session
        for your convenience.
        """

    def crawl(self):
        soup = BeautifulSoup(self.piper.session.get(self.url).text, 'html.parser')
        for tr in soup.find('table', {'class', 'pTable'}).findAll('tr')[1:]:
            tds = tr.findAll('td')
            school_year = tds[0].text.split('-')[0]
            self.fee[school_year] = list()
            for td in tds:
                self.fee[school_year].append(td.text)

    @Crawler.spy
    def fmt_print(self):
        self.crawl()
        row = None
        table = PrettyTable()
        table.field_names = ['学年', '应缴', '已缴', '未缴']
        if self.year:
            row = self.fee.get(self.year)
            if row:
                table.add_row(row)
        else:
            for _, v in self.fee.items():
                table.add_row(v)
        if row:
            print(table)
            print('(具体明细，请查询财务处集中收费平台)')
        else:
            print('无查询结果')
