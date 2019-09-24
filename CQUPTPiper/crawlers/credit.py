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
from CQUPTPiper.subcommand import NameSpace
from prettytable import PrettyTable
from bs4 import BeautifulSoup


class CreditCrawler:
    def __init__(self, piper, namespace: NameSpace):
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
        self.url = self.piper.urls.URL_CREDIT
        self.school_year: str = namespace.get('argument')
        self.credit: dict = {}

    def crawl(self):
        soup = BeautifulSoup(self.piper.session.get(self.url).text, 'html.parser')
        for tr in soup.find('table', {'id': 'AxfTjTable'}).findAll('tr')[1:]:
            tds: list = tr.findAll('td')
            school_year = tds[1].text
            self.credit[school_year] = []
            for td in tds[1:5]:
                self.credit[school_year].append(td.text)
            


    def fmt_print(self):
        self.crawl()
        row = None
        table = PrettyTable()
        table.field_names = ['学年', '学分', '二专业学分', '统计时间']
        if self.school_year:
            if len(self.school_year) == 4 and self.school_year.isdigit():
                for year in [f'{self.school_year}1', f'{self.school_year}2']:
                    row = self.credit.get(year)
                    if row:
                        table.add_row(row)
            else:
                row = self.credit.get(self.school_year)
                if row:
                    table.add_row(row)
        else:
            for _, v in self.credit.items():
                table.add_row(v)
        if row:
            print(table)
        else:
            print('无查询结果')