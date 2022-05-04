import tkinter

from Frames.ControlPanel import ControlPanel
from Frames.ScreenLogger import ScreenLogger


class ControlFrame(tkinter.Frame):
    def __init__(self, parent):
        tkinter.Frame.__init__(self, parent)

        self.map_log = tkinter.Frame(self)
        self.map_log.place(relheight=1, relwidth=0.8)

        self.map = tkinter.Frame(self.map_log)
        self.map.place(relheight=0.8, relwidth=1)

        self.log = ScreenLogger(self.map_log)
        self.log.place(relheight=0.2, rely=0.8, relwidth=1)

        self.controls = ControlPanel(self)
        self.controls.place(relheight=1, relwidth=0.2, relx=0.8)
