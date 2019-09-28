from os import system
from sys import stdout, platform
from time import sleep
from threading import Thread


class Log:
    prefix = '\ncqupt:'

    @classmethod
    def error(cls, message: str, prog = None):
        if prog is None:
            print(cls.prefix, message)
        else:
            print('\n' + message)

    @classmethod
    def fatal(cls, message: str = '', status: int = 0, prog = None):
        cls.error(message, prog)
        exit(status)


class Loading:
    frames = ['[=   ]', '[ =  ]', '[  = ]', '[   =]']
    curr_i = -1
    done = False

    @classmethod
    def start(cls, msg: str):
        while not cls.done:
            if cls.curr_i < 3:
                cls.curr_i += 1
            else:
                cls.curr_i = 0
            if platform == 'win32':
                print(cls.frames[cls.curr_i], msg, end='\r')
            else:
                print(cls.frames[cls.curr_i], msg)
                stdout.write("\033[F")
            sleep(0.2)


def loading(message: str):
    def loading_wrraper(target):
        def target_wrapper(*args, **kwargs):
            Thread(target=Loading.start, args=(message,)).start()
            resp = target(*args, **kwargs)
            Loading.done = True
            stdout.flush()
            return resp
        return target_wrapper
    return loading_wrraper


