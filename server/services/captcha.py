from server.services import Service
from PIL import Image


class Captcha(Service):

    @classmethod
    def recognize(cls, data=None):
        return data
