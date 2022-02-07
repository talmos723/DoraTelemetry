import tkinter
import matplotlib
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.animation as animation

import plot.LineDiagram

default = {
  "layout": [1,2],
  "updateperiod": 400,
  "sample_num": 10,
   "plotting":[
     {
       "name": "elso",
       "ylim": [0,10]
     },
     {
       "name": "masodik",
       "ylim": [0,5]
     },
]
}

class PlotsFrame(tkinter.Frame):
    def __init__(self, parent, dataholders, recipe: dict):
        tkinter.Frame.__init__(self, parent)
        self.parent = parent

        if recipe is None:
            self.recipe = default
        else:
            self.recipe = recipe

        self.dataholders = dataholders


        self.fig = Figure(figsize=(10, 8))
        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

        self.lines = []

        layout = self.recipe["layout"]
        rec_num = len(recipe["plotting"])
        for idx in range(layout[0] * layout[1]):
            if idx < rec_num:
                plot_rec = self.recipe["plotting"][idx]
                if plot_rec["type"] == "compass":
                    ax = self.fig.add_subplot(layout[0], layout[1], idx + 1, projection="polar")
                    ax.set_title(plot_rec["name"])
                    ax.set_theta_zero_location("N")
                    ax.set_xticks(np.pi / 180. * np.linspace(-180, 180, 8, endpoint=False))
                    ax.set_thetalim(np.pi, -np.pi)
                    ax.set_theta_direction(-1)
                    ax.set_yticklabels([])
                else:
                    ax = self.fig.add_subplot(layout[0], layout[1], idx+1)
                    line = plot.LineDiagram.LineDiagram(subplot=ax, dataholder=self.dataholders[plot_rec["subtopic"]][plot_rec["name"]], rec=plot_rec)
                    self.lines.append(line)

        self.ani = matplotlib.animation.FuncAnimation(self.fig, self.update_view, interval=self.recipe["updateperiod"], blit=False)
        self.fig.tight_layout()


    def update_view(self, frame):
        for line in self.lines:
            line.update_data()



