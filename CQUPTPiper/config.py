from pathlib import Path
from os import path, mkdir
from socket import gethostname, gethostbyname

from CQUPTPiper.decorators import authorize
from CQUPTPiper.auth import Auth, writeconfig, KEY_LANG, VALUE_EXPLANATION
from CQUPTPiper.lang import CH, EN
from CQUPTPiper import PIPER_CAPTCHA_PATH, PIPER_DIR, PIPER_PATH

import sys


def makedirifnexists(dirpath: str):
    if not path.isdir(dirpath):
        mkdir(dirpath)


class Config:
    def __init__(self):
        self.platform: str = sys.platform
        self.ipv4addr: str = gethostbyname(gethostname())
        self.dirpath:  str = PIPER_DIR
        self.cf_path:  str = PIPER_PATH
        self.captcha_path: str = PIPER_CAPTCHA_PATH

        makedirifnexists(self.dirpath)

        self.lang: str = Auth.getlang(self)
        self.instruction = CH if self.lang == 'ch' else EN
        self.user: dict = Auth.getuser(self)

        self.config: dict = Auth.getconfig(self)

    def setlang(self, lang: str):
        self.config.update(lang=lang)
        writeconfig(self.cf_path, self.config)
        print(f'Switched to {VALUE_EXPLANATION.get(self.config.get(KEY_LANG))}')

    @authorize
    def setuser(self): pass
        
