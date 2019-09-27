from cqupt.urls import URL_TASKS
from cqupt.log import loading
from prettytable import PrettyTable
from bs4 import BeautifulSoup


class Task:
    task: list = []

    @classmethod
    @loading('正在获取考试安排')
    def crawl(cls, request):
        soup = BeautifulSoup(request.get(URL_TASKS).text, 'html.parser')
        for tr in soup.find('tbody').findAll('tr'):
            tds = tr.findAll('td')[5:]
            cls.task.append([
                tds[0].text,  # 课程名称
                tds[4].text,  # 教室号
                tds[5].text,  # 座位号
                tds[1].text,  # 周次
                tds[2].text,  # 星期
                tds[3].text,  # 具体时间
                tds[6].text   # 资格
            ])

    @classmethod
    def handle(cls, request, arg):
        cls.crawl(request)
        row = None
        table = PrettyTable(['课程名称', '教室', '座位', '周次', '星期', '具体时间', '资格'])
        if cls.task:
            for row in cls.task:
                table.add_row(row)
        if cls.task:
            print('\n共', len(cls.task), '项考试')
            print(table)
            print('多喝热水, 及时做好复习准备哦~')
        else:
            print('\n无查询结果!')