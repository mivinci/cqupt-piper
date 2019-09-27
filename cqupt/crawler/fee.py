from cqupt.urls import URL_FINANCE
from cqupt.log import loading
from prettytable import PrettyTable
from bs4 import BeautifulSoup


class Fee:
    fee: dict = {}
    length: int = 0

    @classmethod
    @loading('正在获取学费信息')
    def crawl(cls, request):
        soup = BeautifulSoup(request.get(URL_FINANCE).text, 'html.parser')
        for tr in soup.find('table', {'class', 'pTable'}).findAll('tr')[1:]:
            tds = tr.findAll('td')
            school_year = tds[0].text.split('-')[0]
            cls.fee[school_year] = list()
            for td in tds:
                cls.fee[school_year].append(td.text)

    @classmethod
    def handle(cls, request, arg):
        cls.crawl(request)
        table = PrettyTable(['学年', '应缴', '已缴', '未缴'])

        if arg == -1:
            for _, v in cls.fee.items():
                table.add_row(v)
                cls.length += 1
        else:
            if str(arg) in cls.fee:
                table.add_row(cls.fee.get(str(arg)))
                cls.length += 1
        
        if cls.length == 0:
            print('\n无查询结果!')
        else:
            print(table)
            print('具体明细，请查询财务处集中收费平台')
