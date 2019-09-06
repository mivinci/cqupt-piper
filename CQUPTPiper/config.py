import sys
from socket import gethostname, gethostbyname


class Config:
    def __init__(self):
        self.platform = sys.platform
        self.ipv4addr = gethostbyname(gethostname())