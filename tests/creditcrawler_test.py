import requests
from bs4 import BeautifulSoup
from prettytable import PrettyTable

# html = requests.get(
#     'http://jwzx.cqu.pt/student/xkxfTj.php',
#     cookies={'PHPSESSID': 'o2r2fpddrj892dp1ntqddcp2hv'}).text

# soup = BeautifulSoup(html, 'html.parser')

# for tr in soup.find('table', {'id': 'AxfTjTable'}).findAll('tr')[1:]:
#     tds = tr.findAll('td')
#     print(tds[1:5])


table = PrettyTable(['aaa', 'bbb'])

print(table)