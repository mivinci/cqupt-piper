"""
This package contains all the crawlers that're used in CQUPTPiper.
If jwzx.cqupt.edu.cn changes, those crawlers will be no longer used,
new crawlers must be constructed in time.

So far, crawlers are able to get:
    credit,
    fee of each year,
    gpa and ranks of each year,
    tasks of current semester,
    photo of student by studend ID.

URL for each information are written as comments in each Python file,
but do not write the urls directly in your code, cuz all urls can be called from

    piper.urls

Plus, DO NOT edit any code outside this package.
"""
from CQUPTPiper.subcommand import NameSpace
from .credit import CreditCrawler
from .fee import FeeCrawler
from .gpa import GPACrawler
from .tasks import TasksCrawler
from .photo import PhotoCrawler


CRAWLER_CMD = 'get'
CRAWLER_KEY_OPT = 'option'
CRAWLER_KEY_ARG = 'argument'


class Crawler:
    mapping: dict = {
        'credit': CreditCrawler,
        '-c': CreditCrawler,

        'fee': FeeCrawler,
        '-f': FeeCrawler,

        'gpa': GPACrawler,
        '-g': GPACrawler,

        'tasks': TasksCrawler,
        '-t': TasksCrawler,

        'photo': PhotoCrawler,
        '-p': PhotoCrawler
    }

    @classmethod
    def do(cls, piper, namespace: NameSpace):
        cls.mapping.get(namespace.get(CRAWLER_CMD).get(CRAWLER_KEY_OPT))(piper, namespace.get(CRAWLER_CMD)).fmt_print()
