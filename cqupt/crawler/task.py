class Task:

    @classmethod
    def handle(cls, request, arg):
        print('task', request)