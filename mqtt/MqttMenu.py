import os
import tkinter
import tkinter.messagebox
from tkinter import ttk

from mqtt.MqttListener import MqttListener
from settings.init_settings import mqttInit, mqttSave


class MqttMenu:
    def __init__(self, comSys, dataholder):
        self.comDetails = tkinter.StringVar()
        self.win = None
        self.dataFrame = None

        self.comSys = comSys
        self.dataholder = dataholder

        self.saved = []
        files = os.listdir("./settings/mqtt")
        for i in range(len(files)):
            if files[i].find(".json") != -1:
                self.saved.append(files[i].replace(".json", ""))
        self.saved.append("New")

        self.keys = ["broker", "port", "topic", "username", "password"]
        self.entries = None

    def showPsw(self, label: tkinter.Label, psw):
        if label["text"] == psw:
            label["text"] = "****"
        else:
            label["text"] = psw

    def display_selected(self, choice):
        choice = self.comDetails.get()
        for widgets in self.dataFrame.winfo_children():
            widgets.destroy()

        row = 0
        if choice != "New":
            mqttDatas = mqttInit(choice)
        else:
            mqttDatas = None
            self.entries = [tkinter.Entry() for i in range(len(self.keys) + 1)]
            tkinter.Label(self.dataFrame, text="Name").grid(row=row, column=0, sticky=tkinter.E)
            tkinter.Label(self.dataFrame, text=":").grid(row=row, column=1, sticky=tkinter.W)
            self.entries[row] = tkinter.Entry(self.dataFrame)
            self.entries[row].grid(row=row, column=2, sticky=tkinter.W)
            row += 1

        for key in self.keys:
            tkinter.Label(self.dataFrame, text=key).grid(row=row, column=0, sticky=tkinter.E)
            tkinter.Label(self.dataFrame, text=":").grid(row=row, column=1, sticky=tkinter.W)

            if choice == "New":
                self.entries[row] = tkinter.Entry(self.dataFrame)
                self.entries[row].grid(row=row, column=2, sticky=tkinter.W)
            else:
                if key == "password":
                    pswL = tkinter.Label(self.dataFrame, text="****")
                    pswL.grid(row=row, column=2, sticky=tkinter.W)
                    pswL.bind("<Button-1>", lambda e: self.showPsw(pswL, mqttDatas["password"]))
                else:
                    tkinter.Label(self.dataFrame, text=mqttDatas[key]).grid(row=row, column=2, sticky=tkinter.W)

            row += 1

        self.dataFrame.pack()

    def mqttPopup(self):
        self.win = tkinter.Toplevel()
        self.win.wm_title("ComMenu")

        l = tkinter.Label(self.win, text="Choose communication settings!")
        l.pack()

        self.comDetails.set(self.saved[0])

        # creating widget
        dropdown = tkinter.OptionMenu(
            self.win, self.comDetails, *self.saved, command=self.display_selected)
        dropdown.pack()

        self.dataFrame = tkinter.Frame(self.win)
        self.dataFrame.pack()

        b = ttk.Button(self.win, text="Connect", command=self.connect)
        b.pack()

        self.display_selected("")

    def connect(self):
        if self.comDetails.get() == "New":
            newConnection = {}
            for key in range(len(self.keys)):
                newConnection[self.keys[key]] = self.entries[key + 1].get()

            newConnection["port"] = int(newConnection["port"])
            mqttSave(self.entries[0].get(), newConnection)
            self.comDetails.set(self.entries[0].get())

        try:
            self.comSys.newCom(MqttListener(self.dataholder, self.comDetails.get()))
            self.win.destroy()
        except Exception as e:
            tkinter.messagebox.showwarning(
                title="Error",
                message=f"Connection error!\nCaused by:\n{e}")
