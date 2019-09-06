from os import path

from CQUPTPiper.fr import b64_fwrite, b64_fread

KEY_STUID = 'stuid'
KEY_PASS = 'password'


def isconfig(config: dict) -> bool:
    if config.get('stuid') and config.get('password'):
        return True
    return False


def readconfig(filename: str) -> dict:
    return eval(b64_fread(filename))


def writeconfig(filename: str, config: dict):
    return b64_fwrite(filename, config)


class Auth:
    user = dict()

    @classmethod
    def getuser(cls, config):
        if path.isfile(config.cf_path):
            cls.user = readconfig(config.cf_path)
            if isconfig(cls.user):
                return cls.user
        cls.user[KEY_STUID] = input("Username: ")
        cls.user[KEY_PASS] = input("Password: ")
        writeconfig(config.cf_path, cls.user)
        return cls.user
