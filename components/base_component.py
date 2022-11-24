from tkinter import *
class BaseComponent:
    def get_full_width(self, widget, parent, padding=0, column=0, row=0):
        widget.grid(column=column, row=row, sticky=(E, S, W, N))
        parent.rowconfigure(row, weight=1)
        parent.columnconfigure(column, weight=1)
        if padding !=0 :
            widget["padding"] = padding