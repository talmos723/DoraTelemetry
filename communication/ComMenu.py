import tkinter
from tkinter import ttk

from communication import ComBase
from communication import ComSystem
from communication import ComDirection
from mqttModul.MqttMenu import MqttMenu
from serialModul.SerialListener import SerialListener
from serialModul.SerialSender import SerialSender


class ComMenu(tkinter.Menu):
    def __init__(self, root: tkinter.Tk, commod: ComBase):
        tkinter.Menu.__init__(self, root)

        self.commod = commod
        self.root = root

        self.win = None
        self.comFormVar = tkinter.StringVar()
        self.comForms = ["MQTT", "SERIAL", "NONE"]
        self.comDirectionVar = tkinter.StringVar()
        self.comDirections = ["Input", "Output"]

        self.filemenu = None
        self.buildFileMenu()

        self.add_cascade(label="Communication", menu=self.filemenu)


    def displaySelectedComForm(self, choice):
        choice = self.comFormVar.get()

    def displaySelectedComDir(self, choice):
        choice = self.comDirectionVar.get()

    def comModSettings(self):
        self.win = tkinter.Toplevel()
        self.win.wm_title("ComMenu")

        l = tkinter.Label(self.win, text="Choose communication protocol adn direction!")
        l.pack()

        self.comFormVar.set(self.comForms[0])
        self.comDirectionVar.set(self.comDirections[0])

        comFormDropdown = tkinter.OptionMenu(
            self.win, self.comFormVar, *self.comForms, command=self.displaySelectedComForm)
        comFormDropdown.pack()


        comDirDropdown = tkinter.OptionMenu(
            self.win, self.comDirectionVar, *self.comDirections, command=self.displaySelectedComDir)
        comDirDropdown.pack()

        b = ttk.Button(self.win, text="Okay", command=self.chooseComMod)
        b.pack()

    def chooseComMod(self):  # TODO: sender, reciever
        self.win.destroy()
        if self.comFormVar.get() == self.comForms[0]:  # mqttModul
            if self.comDirectionVar.get() == self.comDirections[0]:
                MqttMenu(ComDirection.Dir.IN).mqttPopup()
            else:
                MqttMenu(ComDirection.Dir.OUT).mqttPopup()
            # print("-------COMMOD IS NOW MQTT!-------")

        elif self.comFormVar.get() == self.comForms[1]:  # serialModul
            if self.comFormVar.get() == self.comForms[0]:
                ComSystem.ComSystem.getInstance().newReciever(SerialListener())
            else:
                ComSystem.ComSystem.getInstance().newSender(SerialSender())
            # print("-------COMMOD IS NOW SERIAL!-------")

        elif self.comFormVar.get() == self.comForms[1]:  # none
            if self.comFormVar.get() == self.comForms[0]:
                ComSystem.ComSystem.getInstance().newReciever()
            else:
                ComSystem.ComSystem.getInstance().newSender()
            # print("-------COMMOD IS NOW NONE!-------")

    def buildFileMenu(self):
        self.filemenu = tkinter.Menu(self, tearoff=1)
        self.filemenu.add_command(label="Connection Settings", command=self.comModSettings)
        self.filemenu.add_command(label="Start")
        self.filemenu.add_command(label="Stop")
        self.refreshCommodMenus()

        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit", command=self.root.on_closing)

    def refreshCommodMenus(self):  # TODO: sender, reciever : start, stop
        if ComSystem.ComSystem.getInstance().Receiver is None:
            self.filemenu.entryconfigure("Start", state=tkinter.DISABLED, command=None)
            self.filemenu.entryconfigure("Stop", state=tkinter.DISABLED, command=None)
        else:
            self.filemenu.entryconfigure("Start", state=tkinter.ACTIVE, command=ComSystem.ComSystem.getInstance().Receiver.run)
            self.filemenu.entryconfigure("Stop", state=tkinter.ACTIVE, command=ComSystem.ComSystem.getInstance().Receiver.stop)
