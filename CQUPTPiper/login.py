from time import sleep

from CQUPTPiper.urls import Url
from CQUPTPiper.fr import flush_print


class Login:
    def __init__(self, piper):
        self.session = piper.session
        self.urls = piper.urls
        self.config = piper.config
        self.args = piper.args

        self.captcha_text = None

    def set_phpsessid(self):
        self.session.get(self.urls.URL_LOGIN)

    def recognize_captcha(self):
        with open(self.config.captcha_path, 'wb') as f:
            f.write(self.session.get(self.urls.URL_CAPTCHA).content)
        from pytesseract import image_to_string
        from PIL import Image
        self.captcha_text = image_to_string(Image.open(self.config.captcha_path)).strip()

    def recognize_captcha_manually(self):
        with open(self.config.captcha_path, 'wb') as f:
            f.write(self.session.get(self.urls.URL_CAPTCHA).content)
        from PIL import Image
        im = Image.open(self.config.captcha_path)
        im.show()
        self.captcha_text = input(self.config.instruction.ENTER_CAPTCHA)

    def strike(self) -> bool:
        resp = self.session.post(self.urls.URL_CHECK_LOGIN,
                                headers={'User-Agent': 'Mozilla/5.0'},
                                data={
                                    'name': self.config.user.get('stuid'),
                                    'password': self.config.user.get('password'),
                                    'vCode': self.captcha_text
                                }).text
        resp = eval(resp)
        if resp['info'] != 'ok！':
            print(f"{self.config.instruction.LOGIN_FAILED}: {resp['info']}")
            print(self.config.instruction.RETRYING)
            return False
        print(self.config.instruction.LOGIN_SUCCESSFULLY)
        return True


def execute_recognize_captcha_manually(piper, login: Login):
    try:
        login.recognize_captcha_manually()
    except Exception:
        raise


def execute_recognize_captcha(piper, login: Login):
    try:
        login.recognize_captcha()
        flush_print(f"{piper.config.instruction.RECOGNIZING_CAPTCHA}: {login.captcha_text}")
        while not login.captcha_text or len(login.captcha_text) != 5 or not login.captcha_text.isdigit():
            login.recognize_captcha()
            flush_print(f"{piper.config.instruction.RECOGNIZING_CAPTCHA}: {login.captcha_text}")
            sleep(0.3)
        print('')
    except Exception:
        raise
    

def login_execute(piper, login: Login):
    def recognize_captcha(piper, login: Login):
        if login.args.manual:
            execute_recognize_captcha_manually(piper, login)
        else:
            execute_recognize_captcha(piper, login)

    try:
        login.set_phpsessid()
        recognize_captcha(piper, login)
        while not login.strike():
            recognize_captcha(piper, login)
    except Exception:
        raise