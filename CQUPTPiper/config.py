import sys
from pathlib import Path
from os import path, mkdir
from socket import gethostname, gethostbyname

from CQUPTPiper.auth import Auth


def makedir(dirpath: str):
    if not path.isdir(dirpath):
        mkdir(dirpath)


class Config:
    def __init__(self):
        self.platform: str = sys.platform
        self.ipv4addr: str = gethostbyname(gethostname())
        self.dirpath:  str = f'{Path.home()}/.piper'
        self.cf_path:  str = f'{self.dirpath}/piper'

        makedir(self.dirpath)
        self.user: dict = Auth.getuser(self)
