from tkinter import *


class LabelFr:
    def __init__(self, name, fr, col, row, font, val):
        label_frame = LabelFrame(fr)
        self.entry = Entry(label_frame)
        self.entry.insert(0, val)
        self.entry.grid(column=1, row=0, padx=5)
        self.label = Label(label_frame, text=name, width=15, font=font)
        self.label.grid(column=0, row=0)
        label_frame.grid(column=col, row=row, pady=5, padx=10)

    def get(self):
        return self.entry.get()
