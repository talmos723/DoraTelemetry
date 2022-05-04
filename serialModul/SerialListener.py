from communication.ComIn import ComIn
from serialModul.SerialBase import SerialBase


class SerialListener(SerialBase, ComIn):
    def __init__(self):
        pass

    def onMessage(self, message, topic):
        pass

