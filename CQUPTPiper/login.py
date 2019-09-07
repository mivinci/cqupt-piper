from CQUPTPiper.urls import Url


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
        self.captcha_text = image_to_string(Image.open(self.config.captcha_path))

    def recognize_captcha_manually(self):
        with open(self.config.captcha_path, 'wb') as f:
            f.write(self.session.get(self.urls.URL_CAPTCHA).content)
        from PIL import Image
        im = Image.open(self.config.captcha_path)
        im.show()
        self.captcha_text = input("Enter captcha: ")

    def strike(self) -> bool:
        resp = self.session.post(self.urls.URL_CHECK_LOGIN,
                                headers={'User-Agent': 'Mozilla/5.0'},
                                data={
                                    'name': self.config.user.get('stuid'),
                                    'password': self.config.user.get('password'),
                                    'vCode': self.captcha_text
                                }).text
        resp = eval(resp)
        if resp['info'] != 'ok!':  # This if expression does not work properly
            print(f"Login Failed: {resp['info']}")
            print('Retrying ...')
            return False
        print('Login Successfully!')
        return True


def execute_recognize_captcha_manually(login: Login):
    try:
        login.recognize_captcha_manually()
    except Exception:
        raise


def execute_recognize_captcha(login: Login):
    try:
        login.recognize_captcha()
        print(f"Recognizing captcha: {login.captcha_text}")
        while not login.captcha_text or len(login.captcha_text) != 5 or not login.captcha_text.isdigit():
            login.recognize_captcha()
            print(f"Recognizing captcha: {login.captcha_text}")
    except Exception:
        raise
    

def login_execute(login: Login):
    try:
        login.set_phpsessid()
        if login.args.manual:
            execute_recognize_captcha_manually(login)
        else:
            execute_recognize_captcha(login)
        login.strike()
    except Exception:
        raise