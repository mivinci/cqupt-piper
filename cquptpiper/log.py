class Log:
    prefix = 'cqupt:'

    @classmethod
    def error(cls, message: str):
        print(cls.prefix, message)

    @classmethod
    def fatal(cls, message: str, status: int = 0):
        cls.error(message)
        exit(status)
