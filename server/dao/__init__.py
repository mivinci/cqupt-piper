from server.dao.captcha import Captcha

class Dao:
    db = None
    cache = None

    @classmethod
    def captcha(cls):
        return Captcha

    @classmethod
    def spy(cls): pass