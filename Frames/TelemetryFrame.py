import tkinter
from tkinter import ttk

import plot.PlotsFrame
from settings.init_settings import plotInit


class TelemetryFrame(tkinter.Frame):
    def __init__(self, parent):
        tkinter.Frame.__init__(self, parent)

        ttk.Label(self, text="Telemetry").pack(side=tkinter.TOP)

        recipe = plotInit()
        self.plotframe = plot.PlotsFrame.PlotsFrame(parent=self, recipe=recipe)
        self.plotframe.pack(side=tkinter.TOP)
