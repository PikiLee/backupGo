from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog
from components.file_selector import FileSelector
from components.base_component import BaseComponent
from encrypt import encrypt


class App(BaseComponent):
    def __init__(self, root):
        root.title("backupGo")
        root.geometry("600x400")

        main_frame = Frame(root)
        self.get_full_width(main_frame, root, 10)

        main_notebook = Notebook(main_frame)
        self.get_full_width(main_notebook, main_frame)

        encrypt_frame = Frame(main_notebook)
        self.get_full_width(encrypt_frame, main_notebook, 25)
        encrypt_frame.columnconfigure(56, weight=1)

        decrypt_frame = Frame(main_notebook)
        self.get_full_width(decrypt_frame, main_notebook)

        main_notebook.add(encrypt_frame, text="加密")
        main_notebook.add(decrypt_frame, text="解密")

        self.input_path = StringVar()
        FileSelector(encrypt_frame, self.input_path, "输入", column=55, row=55)

        self.output_path = StringVar()
        FileSelector(encrypt_frame, self.output_path, "输出目录",
                     column=55, row=60, allow_types=["dir"])

        self.error = StringVar(value="good")
        errorLabel = Label(encrypt_frame, text=self.error.get(), textvariable=self.error)
        errorLabel.grid(column=55, row=63, columnspan=3)

        confirmButton = Button(
            encrypt_frame, text="开始加密",  command=self.backup)
        confirmButton.grid(column=56, row=65)

    def backup(self):
        try:
            self.error.set("开始加密备份")
            encrypt(self.input_path.get(), self.output_path.get())
            self.error.set("备份成功")
        except error: 
            self.error.set(error)
        


root = Tk()
App(root)
root.mainloop()
