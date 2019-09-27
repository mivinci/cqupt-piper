from cqupt.crawlers.fee import Fee
from cqupt.crawlers.credit import Credit
from cqupt.crawlers.gpa import GPA
from cqupt.crawlers.task import Task
from cqupt.crawlers.photo import Photo


class Crawler:
    def __init__(self): pass

    def handle(self, piper, argument):
        if argument.credit:
            Credit.handle(piper.session, argument.credit)
        if argument.gpa:
            GPA.handle(piper.session, argument.gpa)
        if argument.task:
            Task.handle(piper.session, argument.task)
        if argument.fee:
            Fee.handle(piper.session, argument.fee)
        if argument.photo:
            Photo.handle(piper.session, argument.photo)