from bs4 import BeautifulSoup
import requests


html = requests.get(
    'http://jwzx.cqu.pt/student/ksap.php',
    cookies={'PHPSESSID': 'd6l9osc39jphtnqmbeqvfsqdgb'}).text

soup = BeautifulSoup(html, 'html.parser').find('div', {'id': 'stuKsTab-ks'})

trs = soup.find('tbody').findAll('tr')

for tr in trs:
    for td in tr.findAll('td')[5:]:
        print(td.text)
