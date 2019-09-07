from requests import Session
from argparse import ArgumentParser

from CQUPTPiper.urls import Url
from CQUPTPiper.config import Config
from CQUPTPiper.login import Login, login_execute
from CQUPTPiper.cli import ArgParser


class Piper:
    def __init__(self):
        self.session: Session = Session()
        self.config: Config = Config()
        self.urls: Url = Url()
        self.args: ArgumentParser = ArgParser()

    def login(self):
        login = Login(self)
        login_execute(login)

    def run(self):
        pass


def cli():
    piper = Piper()
    piper.login()
    if piper.args.manual:
        print("manual")

    print("Bye!")


if __name__ == '__main__':
    cli()
