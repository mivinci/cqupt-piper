import requests
from bs4 import BeautifulSoup
from prettytable import PrettyTable

session = requests.Session()

session.get('http://jwzx.cqu.pt/login.php')

print(session.cookies.get_dict())

html = session.get('http://jwzx.cqu.pt/student/jfInfo.php', headers={'User-Agent': 'Mozilla/5.0 Chrome/76.0.3809.132 Safari/537.36'}).text


print(html)

# soup = BeautifulSoup(html, 'html.parser')

# fee = dict()

# for tr in soup.find('table', {'class': 'pTable'}).findAll('tr')[1:]:
#     tds = tr.findAll('td')
#     year = tds[0].text.split('-')[0]
#     fee[year] = list()
#     for td in tds:
#         fee[year].append(td.text)

# # print(fee)

# table = PrettyTable()
# table.field_names = ['学年', '应缴', '已缴', '未缴']

# for k, v in fee.items():
#     table.add_row(v)

# print(table)

