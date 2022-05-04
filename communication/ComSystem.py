from tkinter import Tk

from communication import ComMenu
from communication.ComOut import ComOut
from communication.ComIn import ComIn

# TODO: additional menus with the commonication moduls (like subscribe to topic with mqttModul)
# TODO: additional menu interfaces
# TODO: communication on serialModul port
# TODO: the communication settings are displayed and managed on an other tab except in menus
from dataholders.initDhs import build_dataholders
from settings.init_settings import plotInit


class ComSystem(object):
    __instance = None

    def __init__(self, root: Tk, sender: ComOut = None, reciever: ComIn = None):

        self._root = root

        if ComSystem.__instance is None:
            ComSystem.__instance = self
        else:
            raise Exception("This is a singleton class!")

        self.Sender: ComOut = sender
        self.Receiver: ComIn = reciever
        self.__commenu = ComMenu.ComMenu(root, self)
        self._root.config(menu=self.__commenu)

        plot_rec = plotInit()
        self.Dataholders = build_dataholders(plot_rec)

        if self.Sender is not None:
            self.Sender.run()
        if self.Receiver is not None:
            self.Receiver.run()

    @staticmethod
    def getInstance():
        if ComSystem.__instance is None:
            raise NotImplemented("Singleton class needs to be initialized!")
        return ComSystem.__instance

    def newSender(self, newSender: ComOut = None):
        if self.Sender is not None:
            self.Sender.stop()
        if newSender is not None:
            newSender.run()

        self.Sender = newSender
        self.__commenu.refreshCommodMenus()

    def newReciever(self, newReciever: ComIn = None):
        if self.Receiver is not None:
            self.Receiver.stop()
        if newReciever is not None:
            newReciever.run()

        self.Receiver = newReciever
        self.__commenu.refreshCommodMenus()
