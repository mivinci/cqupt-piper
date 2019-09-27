from cqupt.urls import URL_CREDIT
from cqupt.log import loading
from prettytable import PrettyTable
from bs4 import BeautifulSoup


class Credit:
    credit: dict = {}
    length: int = 0

    @classmethod
    @loading('正在获取学分信息')
    def crawl(cls, request):
        soup = BeautifulSoup(request.get(URL_CREDIT).text, 'html.parser')
        for tr in soup.find('table', {'id': 'AxfTjTable'}).findAll('tr')[1:]:
            tds: list = tr.findAll('td')
            year = tds[1].text
            cls.credit[year] = []
            for td in tds[1:5]:
                cls.credit[year].append(td.text)

    @classmethod
    def handle(cls, request, arg):
        cls.crawl(request)
        table = PrettyTable(['学年', '学分', '二专业学分', '统计时间'])

        if arg == -1:
            for _, v in cls.credit.items():
                table.add_row(v)
                cls.length += 1
        else:
            if len(str(arg)) == 4:
                for year in [f'{arg}1', f'{arg}2']:
                    if year in cls.credit:
                        table.add_row(cls.credit.get(year))
                        cls.length += 1
            else:
                if str(arg) in cls.credit:
                    table.add_row(cls.credit.get(str(arg)))
                    cls.length += 1
        
        if cls.length == 0:
            print('\n无查询结果!')
        else:
            print()
            print(table)


        