import abc

from communication.ComBase import ComBase


class ComIn(ComBase):
    @abc.abstractmethod
    def onMessage(self, message, topic):
        raise NotImplementedError
