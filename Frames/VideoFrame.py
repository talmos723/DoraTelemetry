import tkinter
from tkinter import ttk

import imageio as imageio
from PIL import Image, ImageTk


class VideoFrame(tkinter.Frame):
    def __init__(self, parent, root, video_name):
        tkinter.Frame.__init__(self, parent)

        self.root = root

        self.play = True

        self.l1 = ttk.Label(self)
        self.l1.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
        self.video = imageio.get_reader(video_name)
        self.delay = int(1000 / 30)
        self.stream()

    def stream(self):
        try:
            if self.root.index('current') == 1:
                image = self.video.get_next_data()
                w, h = int(self.root.winfo_width()*0.8), int(self.root.winfo_height()*0.8)
                if w*9<h*16:
                    h = int(9*w/16)
                else:
                    w = int(16*h/9)
                frame_image = Image.fromarray(image).resize((w, h), Image.ANTIALIAS)
                frame_image = ImageTk.PhotoImage(frame_image)
                self.l1.config(image=frame_image)
                self.l1.image = frame_image
        except: pass
        if self.play:
            self.l1.after(self.delay, lambda: self.stream())

    def stop(self):
        self.play = False

    def start(self):
        self.play = True
        self.stream()

    def is_running(self):
        return self.play