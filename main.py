from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog
from components.file_selector import FileSelector
from components.base_component import BaseComponent


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

        input_path = StringVar()
        FileSelector(encrypt_frame, input_path, "输入", column=55, row=55)

        output_path = StringVar()
        FileSelector(encrypt_frame, output_path, "输出目录", column=55, row=60, allow_types=["dir"])

        confirmButton = Button(encrypt_frame, text="开始加密")
        confirmButton.grid(column=56, row=65)
    


root = Tk()
App(root)
root.mainloop()
