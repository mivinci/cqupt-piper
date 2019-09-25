from cquptpiper.crawler.fee import Fee
from cquptpiper.crawler.credit import Credit
from cquptpiper.crawler.gpa import GPA
from cquptpiper.crawler.task import Task
from cquptpiper.crawler.photo import Photo


class Crawler:
    def __init__(self, piper):
        self.piper = piper
        self.request = piper.session

    def handle(self, argument):
        if argument.credit:
            Credit.handle(self.request, argument.credit)
        if argument.gpa:
            GPA.handle(self.request, argument.gpa)
        if argument.task:
            Task.handle(self.request, argument.task)
        if argument.fee:
            Fee.handle(self.request, argument.fee)
        if argument.photo:
            Photo.handle(self.request, argument.photo)