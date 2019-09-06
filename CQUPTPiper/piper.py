from requests import Session

from CQUPTPiper.config import Config


class Piper:
    def __init__(self):
        self.session: Session = Session()
        self.config: Config = Config()

    def authorize(self):
        pass


if __name__ == '__main__':
    piper = Piper()
    print(piper.config.user)
