from requests import Session

from CQUPTPiper.auth import Auth
from CQUPTPiper.config import Config


class Piper:
    def __init__(self):
        self.session: Session = Session()
        self.config:  Config = Config()
        self.user = None

    def authorize(self):
        Auth.signin(self)

