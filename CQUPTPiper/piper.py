from requests import Session
from argparse import ArgumentParser

from CQUPTPiper.cli import arg_parser, noargs, isquit
from CQUPTPiper.urls import Url
from CQUPTPiper.config import Config
from CQUPTPiper.login import Login, login_execute


class Piper:
    def __init__(self, args: ArgumentParser):
        self.session: Session = Session()
        self.config: Config = Config()
        self.urls: Url = Url()
        self.args: ArgumentParser = args

        self.command = None

    def login(self):
        login = Login(self)
        login_execute(self, login)

    def run(self):
        print(self.config.instruction.SUBCOMMAND_INSTRUCTION)
        while not isquit(self.command):
            self.command = input('> ')
            print(self.command)
        print('Bye!')


def cli():
    args = arg_parser()
    if args.l:
        config = Config()
        config.setlang(str(args.l))

    if noargs() or args.manual:
        piper = Piper(args)
        # piper.login()
        piper.run()
