from server.services import Service


class Spy(Service):

    @classmethod
    def receive(cls, data=None):
        print(cls.dao)