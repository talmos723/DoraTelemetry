import abc

from communication.ComBase import ComBase


class ComOut(ComBase):
    @abc.abstractmethod
    def send(self, message):
        raise NotImplementedError
