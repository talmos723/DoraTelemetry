import abc


class ComModul(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def connect(self):
        raise NotImplementedError

    @abc.abstractmethod
    def run(self):
        raise NotImplementedError

    @abc.abstractmethod
    def stop(self):
        raise NotImplementedError
