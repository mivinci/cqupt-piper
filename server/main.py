from os import path, mkdir
from flask import Flask, request
from internal import SERVER_HOME
from internal.service import Service

app = Flask(__name__)

service = Service()


def init():
    if not path.isdir(SERVER_HOME):
        mkdir(SERVER_HOME)


@app.route('/login', methods=['POST'])
def login_jwzx():
    return service.login_jwzx(request.form)


if __name__ == "__main__":
    init()
    app.run(port=5000)