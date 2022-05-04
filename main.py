import multiprocessing
import tkinter
import logging
from tkinter import ttk

from Frames.ControlFrame import ControlFrame
from communication.ComSystem import ComSystem

from mqttModul.MqttSender import testrun, testrun2
from settings.init_settings import *
from Frames.TelemetryFrame import TelemetryFrame
from Frames.PlayerFrame import PlayerFrame


class MyGUI(tkinter.Tk):
    def __init__(self, test_send_process_on = False):
        tkinter.Tk.__init__(self)
        self.title('Dora Telemetry')

        self.logger = None
        self.init_logger()

        self.tabs = None
        self.menubar = None

        comsys = ComSystem(self)

        self.init_gui()

        if test_send_process_on:
            self.testSendProcess = multiprocessing.Process(target=testrun)
            self.testSendProcess.start()
            self.testSendProcess2 = multiprocessing.Process(target=testrun2)
            self.testSendProcess2.start()
        else:
            self.testSendProcess = None
            self.testSendProcess2 = None

        self.logger.info('Program started')
        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.mainloop()

    def init_gui(self):
        self.tabs = ttk.Notebook(self)

        tab1 = ControlFrame(parent=self.tabs)
        self.logger.addHandler(tab1.log.appLogHandler)

        tab2 = PlayerFrame(parent=self.tabs, video_name="./video/baby_dog16.mp4")
        tab3 = TelemetryFrame(parent=self.tabs)
        self.tabs.add(tab1, text='Controls')
        self.tabs.add(tab2, text='Video')
        self.tabs.add(tab3, text='Charts')

        self.tabs.pack(side=tkinter.LEFT, expand=True, fill=tkinter.BOTH)


    def on_closing(self):
        if self.testSendProcess is not None:
            self.testSendProcess.kill()
        if self.testSendProcess2 is not None:
            self.testSendProcess2.kill()

        self.logger.warning('Application closed')
        self.destroy()

    def init_logger(self):
        self.logger = logging.getLogger('robotlog')
        self.logger.setLevel(logging.DEBUG)

        console_handler = logging.StreamHandler()
        file_handler = logging.FileHandler('robot.log', mode='w')
        console_handler.setLevel(logging.DEBUG)
        file_handler.setLevel(logging.DEBUG)

        c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
        f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        console_handler.setFormatter(c_format)
        file_handler.setFormatter(f_format)

        # self.logger.addHandler(console_handler)
        self.logger.addHandler(file_handler)

        self.logger.info('Logging is alive')


if __name__ == '__main__':
    app = MyGUI(True)
