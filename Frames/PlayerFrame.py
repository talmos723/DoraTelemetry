import tkinter
from tkinter import ttk

from Frames.VideoFrame import VideoFrame


class PlayerFrame(tkinter.Frame):
    def __init__(self, parent, video_name):
        tkinter.Frame.__init__(self, parent)

        ttk.Label(self, text=video_name).pack(side=tkinter.TOP)

        self.btn_text = tkinter.StringVar()
        self.btn_text.set("Stop")

        self.video_frame = VideoFrame(parent=self, root=parent, video_name=video_name)
        self.playbutton = tkinter.Button(self, textvariable=self.btn_text, command=lambda: self.start_stop())

        self.video_frame.pack(side=tkinter.TOP)
        self.playbutton.pack(side=tkinter.TOP)

    def start_stop(self):
        if self.video_frame.is_running():
            self.video_frame.stop()
            self.btn_text.set("Start")
        else:
            self.video_frame.start()
            self.btn_text.set("Stop")

