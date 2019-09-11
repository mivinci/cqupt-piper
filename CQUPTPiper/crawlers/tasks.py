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
from CQUPTPiper.subcommand import NameSpace
from prettytable import PrettyTable
from bs4 import BeautifulSoup


class TasksCrawler:
    def __init__(self, piper, namespace: NameSpace):
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
        self.url = self.piper.urls.URL_TASKS
        self.tasks = list()
        """
        You can start coding like
            self.config = self.piper.config
            self.session = self.piper.session
        for your convenience.
        """

    def crawl(self):
        soup = BeautifulSoup(self.piper.session.get(self.url).text, 'html.parser')
        for tr in soup.find('tbody').findAll('tr'):
            tds = tr.findAll('td')[5:]
            self.tasks.append([
                tds[0].text,  # 课程名称
                tds[4].text,  # 教室号
                tds[5].text,  # 座位号
                tds[1].text,  # 周次
                tds[2].text,  # 星期
                tds[3].text,  # 具体时间
                tds[6].text   # 资格
            ])

    def fmt_print(self):
        self.crawl()
        table = PrettyTable()
        table.field_names = ['课程名称', '教室', '座位', '周次', '星期', '具体时间', '资格']
        if self.tasks:
            for row in self.tasks:
                table.add_row(row)
        print(table)
        print('多喝热水, 及时做好复习准备哦!')