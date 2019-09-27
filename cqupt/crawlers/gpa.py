from cqupt.urls import URL_GPA
from cqupt.log import loading
from prettytable import PrettyTable
from bs4 import BeautifulSoup


class GPA:
    gpa: dict = {}
    length: int = 0

    @classmethod
    @loading('正在获取绩点排名信息')
    def crawl(cls, request):
        soup = BeautifulSoup(request.get(URL_GPA).text, 'html.parser')
        for tr in soup.find('div', {'id': 'cjAllTab-zypm'}).findAll('tr')[1::3]:
            tds: list = tr.findAll('td')
            year = tds[0].text
            cls.gpa[year] = [tds[0].text, tds[2].text, tds[3].text]

    @classmethod
    def handle(cls, request, arg):
        cls.crawl(request)
        table = PrettyTable(['学年', '绩点', '排名'])

        if arg == -1:
            for _, v in cls.gpa.items():
                table.add_row(v)
                cls.length += 1
        else:
            if len(str(arg)) == 4:
                for year in [f'{arg}1', f'{arg}2']:
                    if year in cls.gpa:
                        table.add_row(cls.gpa.get(year))
                        cls.length += 1
        if cls.length == 0:
            print('\n无查询结果!')
        else:
            print(table)