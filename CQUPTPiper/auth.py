from os import path

from CQUPTPiper.fr import b64_fwrite, b64_fread

KEY_STUID = 'stuid'
KEY_PASS = 'password'
KEY_LANG = 'lang'

VALUE_LANG_SIMPLIFIED_CHINESE = 'ch'
VALUE_LANG_ENGLISH = 'en'


def hasuserconfig(config: dict) -> bool:
    if config.get(KEY_STUID) and config.get(KEY_PASS):
        return True
    return False


def haslangconfig(config: dict) -> dict:
    if config.get(KEY_LANG) in [VALUE_LANG_ENGLISH, VALUE_LANG_SIMPLIFIED_CHINESE]:
        return True
    return False


def readconfig(filename: str) -> dict:
    return eval(b64_fread(filename))


def writeconfig(filename: str, config: dict):
    return b64_fwrite(filename, config)


class Auth:
    config = dict()

    @classmethod
    def getuser(cls, config):
        if path.isfile(config.cf_path):
            cls.config = readconfig(config.cf_path)
            if hasuserconfig(cls.config):
                return cls.config
        print(config.instruction.BEFORE_AUTHORIZATION)
        cls.config[KEY_STUID] = input(config.instruction.USERNAME)
        cls.config[KEY_PASS] = input(config.instruction.PASSWORD)
        writeconfig(config.cf_path, cls.config)
        return cls.config

    @classmethod
    def getlang(cls, config):
        if path.isfile(config.cf_path):
            cls.config = readconfig(config.cf_path)
            if haslangconfig(cls.config):
                return cls.config
        option: str = input("Keep on using English? [y/N]: ")
        cls.config[KEY_LANG] = VALUE_LANG_ENGLISH if option.lower() == 'y' else VALUE_LANG_SIMPLIFIED_CHINESE
        writeconfig(config.cf_path, cls.config)
        return cls.config.get(KEY_LANG)
