from cqupt.log import Log
from cqupt.auth import Auth


class Catch:

    @staticmethod
    def keyboard_interrupt(target):
        def target_wrapper(*args, **kwargs):
            try:
                target(*args, **kwargs)
            except KeyboardInterrupt:
                Log.fatal('Bye!', prog='')
        return target_wrapper

    @staticmethod
    def all(target):
        def target_wrapper(*args, **kwargs):
            try:
                target(*args, **kwargs)
            except Exception:
                Auth.clear_cookie()
        return target_wrapper