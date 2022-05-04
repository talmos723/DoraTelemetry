class LineDiagram():
    def __init__(self, subplot, dataholder, rec: dict):
        self.subplot = subplot
        self.dataholder = dataholder
        self.rec = rec
        self.subplot.set_ylim(self.rec["ylim"][0], self.rec["ylim"][1])
        self.subplot.set_xlim(-self.rec["sample_num"] + 1, 0)
        self.subplot.set_title(self.rec["name"])
        self.line, = subplot.plot([i for i in range(-self.rec["sample_num"] + 1, 1)], self.dataholder.getdata())

    def update_data(self):
        if self.dataholder.isnew():
            self.line.set_ydata(self.dataholder.getdata())

