import multiprocessing
import tkinter
from tkinter import ttk

from communication.ComSystem import ComSystem
from dataholders.initDhs import build_dataholders

from mqtt.testing.testsender import testrun
from settings.init_settings import *
from telemetry.TelemetryFrame import TelemetryFrame
from video.PlayerFrame import PlayerFrame


class MyGUI(tkinter.Tk):
    def __init__(self, test_send_process_on = False):
        tkinter.Tk.__init__(self)
        self.title('Dora Telemetry')

        self.tabs = None
        self.menubar = None

        self.plot_rec = plotInit()
        self.dataholders = build_dataholders(self.plot_rec)

        self.comsys = ComSystem(self, self.dataholders)

        self.init_gui()

        if test_send_process_on:
            with open("settings/mqtt/mqtt_connect_sender.json") as f:
                mqtt_sender_rec = json.load(f)
            self.testSendProcess = multiprocessing.Process(target=testrun, args=(mqtt_sender_rec, 1, "sender"))
            self.testSendProcess.start()
        else:
            self.testSendProcess = None

        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.mainloop()

    def init_gui(self):
        self.tabs = ttk.Notebook(self)

        tab1 = ttk.Frame()
        tab2 = PlayerFrame(parent=self.tabs, video_name="./video/baby_dog16.mp4")
        tab3 = TelemetryFrame(parent=self.tabs, dataholders=self.dataholders, recipe=self.plot_rec)
        self.tabs.add(tab1, text='Egy')
        self.tabs.add(tab2, text='Video')
        self.tabs.add(tab3, text='Plot')

        ttk.Label(tab1, text="Egy").grid(column=0, row=0, padx=30, pady=30)

        self.tabs.pack(side=tkinter.LEFT, expand=True, fill=tkinter.BOTH)


    def on_closing(self):
        if self.testSendProcess is not None:
            self.testSendProcess.kill()
        self.destroy()


if __name__ == '__main__':
    app = MyGUI()