from internal import SERVER_HOME
from pytesseract import image_to_string
from requests import get, post
from PIL import Image
from time import time


URL_CAPTCHA = 'http://jwzx.cqu.pt/createValidationCode.php'
URL_CAPTCHA_CHECK = 'http://jwzx.cqu.pt/checkLogin.php'


class Captcha:
    def __init__(self, param: dict):
        self.params: dict = param
        self.userid: str = self.params.get('userid')
        self.password: str = self.params.get('password')
        self.phpsessid: str = self.params.get('PHPSESSID')
        self.cookie: dict = {'PHPSESSID': self.phpsessid}
        self.captcha_path: str = f"{SERVER_HOME}/captcha_{self.userid}_{int(time())}.jpg"
        self.captcha_text: str = ''

    def fetchnew(self):
        with open(self.captcha_path, 'wb') as f:
            f.write(get(URL_CAPTCHA, cookies=self.cookie).content)

    def crack(self):
        captcha = Image.open(self.captcha_path)
        text: str = image_to_string(captcha).strip()
        count: int = 0
        while not text or len(text) != 5 or not text.isdigit():
            if count > 9:
                break
            text: str = image_to_string(captcha).strip()
            count += 1
        self.captcha_text = text

    def request(self) -> dict:
        return eval(post(URL_CAPTCHA_CHECK, 
                    cookies=self.cookie,
                    data={
                        'name': self.userid,
                        'password': self.password,
                        'vCode': self.captcha_text
                    }).text)


class Service:
    def __init__(self):
        self.dao = None

    def login_jwzx(self, params: dict):
        captcha = Captcha(params)
        captcha.fetchnew()
        captcha.crack()
        resp: dict = captcha.request()
        while resp.get('code') != 0:
            if resp.get('info') == '密码错误!':
                return "wrong password"
            if resp.get('info') == '验证码错误':
                captcha.fetchnew()
                captcha.crack()
                resp = captcha.request()
            else:
                return "Server Error"
        return "success"
