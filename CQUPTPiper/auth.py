import json
import getpass


class Auth:

    @classmethod
    def signin(cls, piper):
        username = input("Username: ")
        password = getpass.getpass(prompt="Password: ")
        print(username, password)
