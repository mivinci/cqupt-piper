from flask import Flask
from server.services.captcha import Captcha

app = Flask(__name__)

@app.route("/captcha")
def recognize_captacha():
    return Captcha.recognize()



if __name__ == "__main__":
    app.run()