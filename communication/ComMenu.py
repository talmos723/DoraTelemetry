import tkinter
from tkinter import ttk

from communication import ComModul
from mqtt.MqttMenu import MqttMenu


class ComMenu(tkinter.Menu):
    def __init__(self, root: tkinter.Tk, commod: ComModul, comSys, dataholder):
        tkinter.Menu.__init__(self, root)

        self.commod = commod
        self.comSys = comSys
        self.dataholder = dataholder
        self.root = root

        self.variable = tkinter.StringVar()
        self.win = None
        self.comForms = ['MQTT', 'NONE']

        self.filemenu = None
        self.buildFileMenu()

        self.add_cascade(label="Communication", menu=self.filemenu)

    def donothing(self):
        print("asd")

    def display_selected(self, choice):
        choice = self.variable.get()

    def comModSettings(self):
        self.win = tkinter.Toplevel()
        self.win.wm_title("ComMenu")

        l = tkinter.Label(self.win, text="Choose communication protocol!")
        l.pack()

        self.variable.set(self.comForms[0])

        # creating widget
        dropdown = tkinter.OptionMenu(
            self.win, self.variable, *self.comForms, command=self.display_selected)
        dropdown.pack()

        b = ttk.Button(self.win, text="Okay", command=self.chooseComMod)
        b.pack()

    def chooseComMod(self):
        self.win.destroy()
        if self.variable.get() == self.comForms[0]:  # mqtt
            MqttMenu(self.comSys, self.dataholder).mqttPopup()
            # print("-------COMMOD IS NOW MQTT!-------")

        elif self.variable.get() == self.comForms[1]:  # none
            self.comSys.newCom(None)
            # print("-------COMMOD IS NOW NONE!-------")

    def buildFileMenu(self):
        self.filemenu = tkinter.Menu(self, tearoff=1)
        self.filemenu.add_command(label="Connection Settings", command=self.comModSettings)
        self.filemenu.add_command(label="Start")
        self.filemenu.add_command(label="Stop")
        self.refreshCommodMenus()

        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit", command=self.root.on_closing)

    def refreshCommodMenus(self):
        if self.commod is None:
            self.filemenu.entryconfigure("Start", state=tkinter.DISABLED, command=None)
            self.filemenu.entryconfigure("Stop", state=tkinter.DISABLED, command=None)
        else:
            self.filemenu.entryconfigure("Start", state=tkinter.ACTIVE, command=self.commod.run)
            self.filemenu.entryconfigure("Stop", state=tkinter.ACTIVE, command=self.commod.stop)
