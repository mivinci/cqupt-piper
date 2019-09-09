from requests import Session
from argparse import ArgumentParser

from CQUPTPiper.cli import arg_parser, noargs, subcommand_parser
from CQUPTPiper.urls import Url
from CQUPTPiper.log import Log
from CQUPTPiper.config import Config
from CQUPTPiper.login import Login, login_execute
from CQUPTPiper.subcommand import isquit


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
        subcommand = subcommand_parser()
        print(self.config.instruction.SUBCOMMAND_INSTRUCTION)
        while not isquit(self.command):
            self.command = input('> ')
            if self.command:
                # I don't wanna write Golang-like code in Python
                # But it works goddamn we!!
                namespace, err = subcommand.parse(self.command)
                if err:
                    Log.error(err)
                if namespace:
                    # Connect to the Crawler.
                    # Connect to the Crawler.
                    # Connect to the Crawler.
                    print(namespace)
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
