from sys import exit

EXIT_FAILURE = 1
EXIT_SUCCESS = 0

class Log:

    __prefix__ = 'Piper: '

    @classmethod
    def error(cls, err: str):
        print(f'{cls.__prefix__}{err}')

    @classmethod
    def fatal(cls, err: str):
        cls.error(err)
        exit(EXIT_FAILURE)
