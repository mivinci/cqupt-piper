from PIL import Image
import pytesseract
import requests

URL_LOGIN = 'http://jwzx.cquptx.cn/login.php'
URL_CAPTCHA = 'http://jwzx.cquptx.cn/createValidationCode.php'
URL_CHECK_LOGIN = 'http://jwzx.cquptx.cn/checkLogin.php'

URL_RANKS = 'http://jwzx.cquptx.cn/student/chengjiPm.php'
URL_STUDENT_PHOTO = 'http://jwzx.cquptx.cn/showstupic.php?xh={stu_id}'

FILENAME_CAPTCHA = 'captcha.png'

s = requests.Session()

s.get(URL_LOGIN)

print(s.cookies)


def crack_captcha():
    with open(FILENAME_CAPTCHA, 'wb') as f:
        f.write(s.get(URL_CAPTCHA).content)
    return pytesseract.image_to_string(Image.open(FILENAME_CAPTCHA))


text = crack_captcha()

while not text or len(text) != 5:
    print(text)
    text = crack_captcha()

print(text)


def crack_check_login():
    return s.post(URL_CHECK_LOGIN,
                  headers={'User-Agent': 'Mozilla/5.0'},
                  data={'name': '2017213056', 'password': 'Iamhungry', 'vCode': text})


resp = eval(crack_check_login().text)['info']

if resp != 'ok！':
    print(resp)
    exit(1)

print(s.cookies)
print(eval(resp.text)['info'])

stu_id = '2017213051'
with open(f"{stu_id}.png", 'wb') as f:
    f.write(s.get(URL_STUDENT_PHOTO.format(stu_id=stu_id)).content)

