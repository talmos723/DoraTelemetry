import json
import logging
import tkinter

from numpy import byte, int8

from communication import ComSystem


class ControlPanel(tkinter.Frame):
    def __init__(self, parent):
        tkinter.Frame.__init__(self, parent)
        self.parent = parent
        with open("settings/mqtt/Diagnostics.json") as f:
            mqtt_sender_rec = json.load(f)

        self.logger = logging.getLogger('robotlog')

        self.button1 = tkinter.Button(self, text="Print 1 2 3!",
                                      command=lambda: self.sendB(int8(0x00), bytearray([1, 2, 3])))
        self.button2 = tkinter.Button(self, text="Conect to Wifi!",
                                      command=lambda: self.sendB(int8(0x01), bytearray([])))
        self.button3 = tkinter.Button(self, text="Conect to MQTT!",
                                      command=lambda: self.sendB(int8(0x02), bytearray([])))
        self.button4 = tkinter.Button(self, text="Set seven segment display ON!",
                                      command=lambda: self.sendB(int8(0x03), bytearray([])))
        self.button5 = tkinter.Button(self, text="Set seven segment display OFF!",
                                      command=lambda: self.sendB(int8(0x04), bytearray([])))

        self.button1.pack()
        self.button2.pack()
        self.button3.pack()
        self.button4.pack()
        self.button5.pack()

        '''self.serialInst = serialModul.Serial()
        self.serialInst.baudrate = 115200
        self.serialInst.port("/dev/cu.usbserial-0001")
        self.serialInst.open()'''

    def sendB(self, msgType: byte, msgArgs: bytearray):
        msgArgs.insert(0, 0x00)
        msgArgs.insert(1, msgType)
        if ComSystem.ComSystem.getInstance().Sender is None:
            self.logger.warning(f"Unable to send message: {msgArgs}")
        else:
            ComSystem.ComSystem.getInstance().Sender.send(msgArgs)

