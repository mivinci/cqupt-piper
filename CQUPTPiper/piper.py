from requests import Session

from CQUPTPiper.urls import Url
from CQUPTPiper.config import Config
from CQUPTPiper.login import Login
from CQUPTPiper.cli import get_parser


class Piper:
    def __init__(self):
        self.session: Session = Session()
        self.config: Config = Config()
        self.urls: Url = Url()

    def login(self):
        Login(self)

    def run(self):
        pass


def cli():
    get_parser()


if __name__ == '__main__':
    # piper = Piper()
    # piper.run()

    # print("Bye!")
    cli()

