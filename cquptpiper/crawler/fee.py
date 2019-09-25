from cquptpiper.urls import URL_FINANCE
from prettytable import PrettyTable
from bs4 import BeautifulSoup


class Fee:
    fee: dict = {}

    @classmethod
    def crawl(cls, request):
        soup = BeautifulSoup(request.get(URL_FINANCE).text, 'html.parser')
        print(soup)
        # for tr in soup.find('table', {'class', 'pTable'}).findAll('tr')[1:]:
        #     tds = tr.findAll('td')
        #     school_year = tds[0].text.split('-')[0]
        #     cls.fee[school_year] = list()
        #     for td in tds:
        #         cls.fee[school_year].append(td.text)

    @classmethod
    def handle(cls, request, arg):
        cls.crawl(request)
        # row = None
        # table = PrettyTable()
        # table.field_names = ['学年', '应缴', '已缴', '未缴']
        # if arg:
        #     row = cls.fee.get(arg)
        #     if row:
        #         table.add_row(row)
        # else:
        #     for _, v in cls.fee.items():
        #         table.add_row(v)
        # if row:
        #     print(table)
        #     print('(具体明细，请查询财务处集中收费平台)')
        # else:
        #     print('无查询结果')