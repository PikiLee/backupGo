from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog
from components.file_selector import FileSelector
from components.base_component import BaseComponent
from encrypt import encrypt
from utils import readEncryptionPaths, saveEncryptionPaths


class App(BaseComponent):
    def __init__(self, root):
        root.title("backupGo")
        root.geometry("600x200")

        main_frame = Frame(root)
        self.get_full_width(main_frame, root, 10)

        main_notebook = Notebook(main_frame)
        self.get_full_width(main_notebook, main_frame)

        encrypt_frame = Frame(main_notebook)
        self.get_full_width(encrypt_frame, main_notebook, 25)
        encrypt_frame.columnconfigure(56, weight=1)

        decrypt_frame = Frame(main_notebook)
        self.get_full_width(decrypt_frame, main_notebook)

        main_notebook.add(encrypt_frame, text="备份")
        main_notebook.add(decrypt_frame, text="解密")

        res = readEncryptionPaths()
        if res:
            self.input_path = StringVar(value=res[0])
            self.output_path = StringVar(value=res[1])
        else:
            self.input_path = StringVar()
            self.output_path = StringVar()

        FileSelector(encrypt_frame, self.input_path, "输入", column=55, row=55)
        FileSelector(encrypt_frame, self.output_path, "输出目录",
                     column=55, row=60, allow_types=["dir"])

        self.error = StringVar()
        errorLabel = Label(encrypt_frame, text=self.error.get(), textvariable=self.error)
        errorLabel.grid(column=55, row=63, columnspan=3, rowspan=3)

        confirmButton = Button(
            encrypt_frame, text="开始加密备份",  command=self.backup)
        confirmButton.grid(column=56, row=70, columnspan=2)

    def backup(self):
        try:
            self.error.set("")
            self.error.set("开始加密备份")
            saveEncryptionPaths(self.input_path.get(), self.output_path.get())
            encrypt(self.input_path.get(), self.output_path.get())
            self.error.set("备份成功")
        except Exception as error: 
            self.error.set(error)
        


root = Tk()
App(root)
root.mainloop()
