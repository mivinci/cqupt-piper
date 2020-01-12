# from PIL import Image
# import pytesseract
# import requests

# URL_LOGIN = 'http://jwzx.cqupt.icu/login.php'
# URL_CAPTCHA = 'http://jwzx.cqupt.icu/createValidationCode.php'
# URL_CHECK_LOGIN = 'http://jwzx.cqupt.icu/checkLogin.php'

# URL_RANKS = 'http://jwzx.cqupt.icu/student/chengjiPm.php'
# URL_STUDENT_PHOTO = 'http://jwzx.cqupt.icu/showstupic.php?xh={stu_id}'

# FILENAME_CAPTCHA = 'captcha.png'

# s = requests.Session()

# s.get(URL_LOGIN)

# print(s.cookies)


# def crack_captcha():
#     with open(FILENAME_CAPTCHA, 'wb') as f:
#         f.write(s.get(URL_CAPTCHA).content)
#     return pytesseract.image_to_string(Image.open(FILENAME_CAPTCHA))


# text = crack_captcha()

# while not text or len(text) != 5:
#     print("破解中", text)
#     text = crack_captcha()

# print(text)


# def crack_check_login():
#     return s.post(URL_CHECK_LOGIN,
#                   headers={'User-Agent': 'Mozilla/5.0'},
#                   data={'name': '2017213056', 'password': 'xxxxx', 'vCode': text})


# resp = eval(crack_check_login().text)['info']

# if resp != 'ok！':
#     print(resp)
#     exit(1)

# print(s.cookies)
# print(eval(resp.text)['info'])

# stu_id = '2017213051'
# with open(f"{stu_id}.png", 'wb') as f:
#     f.write(s.get(URL_STUDENT_PHOTO.format(stu_id=stu_id)).content)

# print("<RequestsCookieJar[<Cookie PHPSESSID=vhbn274hsg9dn2tmbrkpgqkkgo for jwzx.cqupt.icu/>]>")
# print("回合\t尝试次数\t破解结果")
# print("1\t3\t\t93005")
# print("2\t1\t\t48969")
# print("3\t1\t\t23006")
# print("4\t1\t\t90078")
# print("5\t2\t\t98769")
# print("6\t5\t\t16045")
# print("7\t1\t\t86007")
# print("8\t1\t\t10243")
# print("9\t1\t\t50879")
# print("10\t1\t\t40126")
# print("准确率：%.2f" % (10*(1/3+1+1+1+1/2+1/5+1+1+1+1)), "%")
