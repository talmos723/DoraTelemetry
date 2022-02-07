from tkinter import Tk

from communication.ComModul import ComModul
from communication.ComMenu import ComMenu


class ComSystem:
    def __init__(self, root: Tk, dataholders, commod: ComModul = None):
        self.commod = commod
        self.commenu = ComMenu(root, self.commod, self, dataholders)
        root.config(menu=self.commenu)

        self.root = root
        self.dataholders = dataholders

        if self.commod is not None:
            self.commod.run()

    def newCom(self, newComMod: ComModul):
        if self.commod is not None:
            self.commod.stop()
        if newComMod is not None:
            newComMod.run()

        self.commod = newComMod
        self.commenu.commod = self.commod
        self.commenu.refreshCommodMenus()
