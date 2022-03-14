import tkinter
from tkinter import ttk

import plot.PlotsFrame


class TelemetryFrame(tkinter.Frame):
    def __init__(self, parent, dataholders, recipe: dict = None):
        tkinter.Frame.__init__(self, parent)

        ttk.Label(self, text="Telemetry").pack(side=tkinter.TOP)

        self.plotframe = plot.PlotsFrame.PlotsFrame(parent=self, dataholders=dataholders, recipe=recipe)
        self.plotframe.pack(side=tkinter.TOP)
