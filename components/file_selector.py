from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog
from .base_component import BaseComponent


class FileSelector(BaseComponent):
    def __init__(self, parent, textVariable, label, column=0, row=0, allow_types=["dir", "file"]):
        self.textVariable = textVariable
        label = Label(parent, text=label)
        label.grid(column=column, row=row, sticky=W)
        column += 1

        entry = Entry(parent, textvariable=textVariable)
        entry.grid(column=column, row=row, sticky=(W, E))
        column += 1

        if "dir" in allow_types:
            button1 = Button(parent, text="打开目录", command=self.open_dir_dialog)
            button1.grid(column=column, row=row)
            column += 1
        
        if "file" in allow_types:
            button2 = Button(parent, text="打开文件", command=self.open_file_dialog)
            button2.grid(column=column, row=row)
            column += 1

    def open_dir_dialog(self):
        path = filedialog.askdirectory()
        self.textVariable.set(path)

    def open_file_dialog(self):
        path = filedialog.askopenfilename()
        self.textVariable.set(path) 
