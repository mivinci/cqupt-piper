from requests import Session

from CQUPTPiper.urls import Url
from CQUPTPiper.config import Config
from CQUPTPiper.login import Login


class Piper:
    def __init__(self):
        self.session: Session = Session()
        self.config: Config = Config()
        self.urls: Url = Url()

    def login(self):
        Login(self)

    def run(self):
        pass


if __name__ == '__main__':
    piper = Piper()

    piper.run()

    print("Bye!")

